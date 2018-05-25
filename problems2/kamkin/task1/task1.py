import sys

def numberReader():
    while True:
        try:
            buf = sys.stdin.read(1)
            int(buf)
            return
        except EOFError:
            return
        except ValueError:
            continue
        except KeyboardInterrupt:
            return


numberReader()
