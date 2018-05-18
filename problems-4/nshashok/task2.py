# Game of Life

import re
import time
from tkinter import Frame
from tkinter import Button
from tkinter import Canvas
from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Scale, HORIZONTAL
from tkinter import W, N


class RLEConfigures:

    def __init__(self):
        self.comment = ''
        self.name = ''
        self.origin = ''
        self.born = [2, 3]
        self.survive = [3, 3]
        self.alive = 'o'
        self.dead = 'b'
        self.end_line = '$'
        self.end_file = '!'
        self.width = 30
        self.height = 30
        self.field = set()

    def read_config(self, filename: str):
        self.comment = ''
        self.name = ''
        self.origin = ''
        self.born = [2, 3]
        self.survive = [3]
        self.alive = 'o'
        self.dead = 'b'
        self.end_line = '$'
        self.end_file = '!'
        mode = '#'
        with open(filename, "r") as file:
            line = ' '
            field = ''
            while line is not None and len(line) != 0:
                line = file.readline()
                if line.startswith("#") and mode == '#':
                    if line[1] == 'C' or line[1] == 'c':
                        self.comment += line[3:]
                    elif line[1] == 'N':
                        self.name = line[3:]
                    elif line[1] == 'O':
                        self.origin = line[3:]
                    elif line[1] == 'P' or line[1] == 'R':
                        pass
                    elif line[1] == 'r':
                        rules = line[3:].split('/')
                        self.born = [int(b) for b in rules[0]]
                        self.survive = [int(s) for s in rules[1]]
                    # do rules
                elif line.startswith("#"):
                    raise ValueError("Comments should be at the beginning of the config file")
                else:
                    mode = '!'
                    field += line
        self._adjust_field(field)
        if len(self.born) == 1:
            self.born.append(self.born[0])
        if len(self.survive) == 1:
            self.survive.append(self.survive[0])

    def print(self):
        for i in range (0, self.height):
            for j in range (0, self.width):
                if (i, j) in self.field:
                    print("o",end='')
                else:
                    print("*",end='')
            print()
        print()

    def _adjust_field(self, field: str):
        lines = field.split("\n")
        rules = [x.split(" = ") for x in lines[0].split(", ")]
        for rule in rules:
            if rule[0] == 'x':
                self.width = int(rule[1])
            elif rule[0] == 'y':
                self.height = int(rule[1])
            elif rule[0] == 'rule':
                born_survive = rule[1].split('/')
                for b_s in born_survive:
                    if b_s[0] == 'B':
                        self.born = [int(b) for b in b_s[1:]]
                    elif b_s[0] == 'S':
                        self.survive = [int(s) for s in b_s[1:]]
                    else:
                        raise ValueError("Unknown rule:", b_s[0])
        lines = ("".join(lines[1:]).split("!"))[0].split("$")
        regex = re.compile(r"(\d*[a-z])")
        self.field = set()
        for line in enumerate(lines):
            a = 0
            splitted = regex.findall(line[1])
            for part in splitted:
                if part[:len(part) - 1] == '':
                    parts = [1, part[len(part) - 1]]
                else:
                    parts = [int(part[:len(part) - 1]), part[len(part) - 1]]
                if parts[1] == self.alive:
                    for i in range(0, parts[0]):
                        self.field.add((line[0], a + i))
                    a += parts[0]
                else:
                    a += parts[0]
        pass

    def is_dead(self, row: int, col: int):
        if 0 > row >= self.height:
            return True
        if 0 > col >= self.width:
            return True
        if (row, col) not in self.field:
            return True
        return False

    def is_alive(self, row: int, col: int):
        if 0 > row >= self.height:
            return False
        if 0 > col >= self.width:
            return False
        if (row, col) in self.field:
            return True
        return False

    def set_alive(self, row: int, col: int, field):
        if 0 > row >= self.height:
            return
        if 0 > col >= self.width:
            return
        if (row, col) not in field:
            field.add((row, col))

    def set_dead(self, row: int, col: int, field: set):
        if 0 < row >= self.height:
            return
        if 0 < col >= self.width:
            return
        if (row, col) in field:
            field.remove((row, col))

    def switch_status(self, row: int, col: int, field: set):
        if 0 < row >= self.height:
            return
        if 0 < col >= self.width:
            return
        if (row, col) in field:
            field.remove((row, col))
        else:
            field.add((row, col))

    def clear(self):
        self.field = set()

    def do_step(self):
        field = set()

        for i in range(0, self.height):
            for j in range(0, self.width):
                tos = 0

                if ((i - 1 + self.height) % self.height,
                    (j - 1 + self.width) % self.width) in self.field:
                    tos += 1
                if ((i - 1 + self.height) % self.height,
                    (j + 1) % self.width) in self.field:
                    tos += 1
                if ((i - 1 + self.height) % self.height,
                    j) in self.field:
                    tos += 1
                if ((i + 1 + self.height) % self.height,
                    (j - 1 + self.width) % self.width) in self.field:
                    tos += 1
                if ((i + 1 + self.height) % self.height,
                    (j + 1) % self.width) in self.field:
                    tos += 1
                if ((i + 1 + self.height) % self.height,
                    (j) % self.width) in self.field:
                    tos += 1
                if ((i),
                    (j - 1 + self.width) % self.width) in self.field:
                    tos += 1
                if ((i),
                    (j + 1) % self.width) in self.field:
                    tos += 1
                if self.is_dead(i, j) and self.born[0] <= tos <= self.born[1]:
                    self.set_alive(i, j, field)
                elif self.is_alive(i, j) and self.survive[0] <= tos <= self.survive[1]:
                    self.set_alive(i, j, field)
                else:
                    self.set_dead(i, j, field)
        self.field = field


class GameOfLife:

    def __init__(self, master):
        self.reader = RLEConfigures()
        self.master = master
        self.frame = Frame(self.master, width = 1000, height = 1000)
        self.buttons = Frame(self.frame)
        self.cell_size = 20
        self.alive_color = "green"
        self.dead_color = "white"
        self.rectangles = []
        self.canvas = Canvas(self.frame, width = self.cell_size * (self.reader.width + 2),
                             height = self.cell_size * (self.reader.height + 2))

        self.btn = Button(self.buttons, text="Шаг", command=self.do_step)
        self.btn_g = Button(self.buttons, text="Играть", command=self.do_step_overtime)
        self.btn_s = Button(self.buttons, text="Остановить", command=self.stop_game)
        self.btn_с = Button(self.buttons, text="Очистить", command=self.clear)
        self.btn_o = Button(self.buttons, text="Открыть конфиг", command=self.open_file)
        self.btn_cmnt = Button(self.buttons, text="Комментарий", command=self.show_comment)
        self.btn_n = Button(self.buttons, text="Название", command=self.show_name)
        self.btn_orig = Button(self.buttons, text="Origin", command=self.show_origin)
        self.scale = Scale(self.buttons, orient=HORIZONTAL, length=300, from_=0.05, to=1, tickinterval=0.1,
                           resolution=0.05)
        self._g = None

        self.canvas.grid(row=0, column=0, padx=20, sticky=N)
        self.buttons.grid(row=0, column=1, padx=20, pady=20, sticky=N)
        self.btn.grid(row=0, column=0, padx=20, sticky=W+N)
        self.btn_g.grid(row=1, column=0, padx=20, sticky=W+N)
        self.btn_s.grid(row=2, column=0, padx=20, sticky=W+N)
        self.btn_с.grid(row=3, column=0, padx=20, sticky=W+N)
        self.btn_o.grid(row=4, column=0, padx=20, sticky=W+N)

        self.btn_n.grid(row=7, column=0, padx=20, sticky=W+N)
        self.btn_orig.grid(row=8, column=0, padx=20, sticky=W+N)
        self.btn_cmnt.grid(row=9, column=0, padx=20, sticky=W+N)

        self.scale.grid(row=5, column=0, padx=20, sticky=W+N)
        self.canvas.bind("<Button-1>", self.change_color)
        self.create_field()
        self.frame.pack()
        # self.read_config_file("config.rle")

    def read_config_file(self, filename: str):
        self.reader.read_config(filename)
        self.create_field()

    def create_field(self):
        self.canvas.delete("all")
        self.rectangles = []
        #self.canvas.setvar("height", self.cell_size * (self.reader.height + 2))
        #self.canvas.setvar("width", self.cell_size * (self.reader.width + 2))
        self.canvas.config(width=self.cell_size * (self.reader.width + 2),
                           height=self.cell_size * (self.reader.height + 2))
        #self.canvas = Canvas(self.frame, width=self.cell_size * (self.reader.width + 2),
        #                     height=self.cell_size * (self.reader.height + 2))
        #self.canvas.grid(row=0, column=0, padx=20, sticky=N)
        #self.canvas.bind("<Button-1>", self.change_color)
        for j in range(self.reader.width):
            self.rectangles.append([])
            for i in range(self.reader.height):
                if self.reader.is_alive(i, j):
                    color = self.alive_color
                else:
                    color = self.dead_color
                rect = self.canvas.create_rectangle(self.cell_size * (j + 1),
                                                   self.cell_size * (i + 1),
                                                   self.cell_size * (j + 2),
                                                   self.cell_size * (i + 2), fill=color)
                self.rectangles[j].append(rect)

    def find_rect_coords(self, x, y):
        return x - x % self.cell_size, y - y % self.cell_size

    def change_color(self, event):
        x, y = self.find_rect_coords(event.x, event.y)
        try:
            ix = int(x / self.cell_size - 1)
            iy = int(y / self.cell_size - 1)
            self.reader.switch_status(iy, ix, self.reader.field)
            if self.reader.is_alive(iy, ix):
                color = self.alive_color
            else:
                color = self.dead_color
            self.canvas.itemconfig(self.rectangles[ix][iy], fill=color)
        except IndexError as e:
            print(e)
            return

    def do_step(self):
        old_field = self.reader.field
        self.reader.do_step()
        new_field = self.reader.field
        for elem in old_field:
            self.canvas.itemconfig(self.rectangles[elem[1]][elem[0]], fill=self.dead_color)
        for elem in new_field:
            self.canvas.itemconfig(self.rectangles[elem[1]][elem[0]], fill=self.alive_color)


    def do_step_overtime(self):
        self.do_step()
        time.sleep(self.scale.get())
        self._g = self.master.after(10, self.do_step_overtime)

    def stop_game(self):
        if self._g is not None:
            self.master.after_cancel(self._g)
            self._g = None

    def clear(self):
        old_field = self.reader.field
        self.reader.clear()
        for elem in old_field:
            self.canvas.itemconfig(self.rectangles[elem[1]][elem[0]], fill=self.dead_color)

    def open_file(self):
        filename = filedialog.askopenfilename(filetypes=(("RLE config", "*.rle"),
                                                         ("All files", "*.*")))
        if filename:
            try:
                self.read_config_file(filename)
            except:
                messagebox.showerror("Ошибка", "Не получилось открыть файл: %s\n"%filename)

    def show_origin(self):
        messagebox.showinfo("Origin", self.reader.origin)

    def show_comment(self):
        messagebox.showinfo("Комментарий", self.reader.comment)

    def show_name(self):
        messagebox.showinfo("Имя", self.reader.name)


if __name__ == "__main__":
    root = Tk()
    root.title("Convay's Game of Life")
    app = GameOfLife(root)
    root.mainloop()