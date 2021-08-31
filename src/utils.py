import json

import parts


def calc_at(x, z, pixel):
    return x // pixel, z // pixel


def a(y, n, b):
    return y if b else n


def type_as(panel, type):
    if panel is None:
        return
    panel.type = type

    panel.bind()


def edge_save(panels, width, height, pixel):
    obj = {
        "sx": width,
        "sz": height,
        "px": pixel,
        "ob": []
    }
    for x in range(width // pixel):
        o = []
        for z in range(height // pixel):
            typ = panels[x][z].type
            if typ != "NORMAL" and typ != "WALL":
                typ = "NORMAL"
            o.append(typ)
        obj["ob"].append(o)
    with open("edge.json", "w") as w:
        w.write(json.dumps(obj))


def load_edge(filename, canvas, config):
    dat = []
    with open(filename, "r") as w:
        obj = json.loads(w.read())
        if obj["sx"] != config["height"] or \
            obj["sz"] != config["width"] or \
            obj["px"] != config["pixel"]:
            raise ValueError("Metadata mismatch.")
        for x in range(config["width"] // config["pixel"]):
            s = []
            for z in range(config["height"] // config["pixel"]):
                p = parts.Panel(canvas, x, z, config["pixel"], obj["ob"][x][z])
                s.append(p)
                p.bind()
            dat.append(s)
    return dat
