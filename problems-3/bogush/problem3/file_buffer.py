from typing import IO


def file_buffer(fp: IO, buff_size: int=5):
    while True:
        units = fp.read(buff_size)
        if len(units) == 0:
            return
        for unit in units:
            yield unit
