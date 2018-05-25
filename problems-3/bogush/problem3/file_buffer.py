from typing import IO


def file_buffer(fp: IO, buff_size: int=512):
    """
    Returns generator object that reads the specified file fp
    in portions of size ≤ buff_size and yields each read byte
    or char (depends on fp.mode).

    :param fp: file object to read from
    :param buff_size: maximum size of portions
    """
    while True:
        units = fp.read(buff_size)
        if len(units) == 0:
            return
        for unit in units:
            yield unit
