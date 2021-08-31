def calc_at(x, z, pixel):
    return x // pixel, z // pixel


def a(y, n, b):
    return y if b else n


def type_as(panel, type):
    if panel is None:
        return
    panel.type = type

    panel.bind()
