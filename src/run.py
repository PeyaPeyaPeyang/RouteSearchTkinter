import tkinter

import parts
from utils import *
from algorithms import a_star


config = {
    "width": 500,
    "height": 500,
    "pixel": 25,
    "algo": a_star.AStar
}


class Main:
    def __init__(self):

        # ⇣Magic
        tk = tkinter.Tk()
        self.tk = tk

        w = config["width"]
        h = config["height"]

        tk.title("Python RouteSearch")
        tk.geometry(f"{w}x{h}")
        canvas = tkinter.Canvas(tk, bg="#ffffff", width=w, height=h)

        canvas.grid(row=0, column=0, sticky=tkinter.NSEW)
        canvas.bind("<ButtonPress>", self.bt_prs)
        canvas.bind("<ButtonPress-1>", self.change_start)
        canvas.bind("<ButtonPress-2>", self.change_goal)
        canvas.bind("<ButtonPress-3>", self.change_wall)
        canvas.bind("<ButtonRelease>", self.bt_rel)
        canvas.bind("<Motion>", self.cursor)
        canvas.pack()
        tk.canvas = canvas
        # ↑Magic

        self.panels = []
        self.start = None
        self.goal = None

        self.init_panels()

    def init_panels(self):
        self.panels = []
        for x in range(config["width"] // config["pixel"]):
            s = []
            for z in range(config["height"] // config["pixel"]):
                p = parts.Panel(self.tk.canvas, x, z, config["pixel"])
                s.append(p)
                p.bind()
            self.panels.append(s)

    def bt_rel(self, e):
        print("onRelease: " + str(e))
        pass

    def bt_prs(self, e):
        print("onPress: " + str(e))

    def change_goal(self, e):
        print("on_changeGoal: " + str(e))
        panel = self.get_pos_at(e.x, e.y)

        if panel is None:
            return
        panel: parts.Panel

        if panel.type == "WALL":
            return

        self.goal = self.b(e.x, e.y, "GOAL", self.goal)
        if self.start is not None:
            self.start_solve()

    def change_start(self, e):
        print("on_changeStart: " + str(e))
        panel = self.get_pos_at(e.x, e.y)

        if panel is None:
            return
        panel: parts.Panel

        if panel.type == "WALL":
            return

        self.start = self.b(e.x, e.y, "START", self.start)

        if self.goal is not None:
            self.start_solve()

    def change_wall(self, e):
        print("on_ChangeWall: " + str(e))

        self.b(e.x, e.y, "WALL")
        pass

    def b(self, x, z, type, unique=None):
        panel = self.get_pos_at(x, z)

        if panel is None:
            return

        if unique:
            type_as(self.get_pos_at_raw(unique[0], unique[1]), "NORMAL")

        type_as(panel, a("NORMAL", type, panel.type == type))

        return calc_at(x, z, config["pixel"])

    def get_pos_at_raw(self, x, z):
        if len(self.panels) < x - 1:
            return None
        if len(self.panels[x]) < z - 1:
            return None
        return self.panels[x][z]

    def get_pos_at(self, x, z):
        pixel = config["pixel"]
        pos = calc_at(x, z, pixel)
        x = pos[0]
        z = pos[1]

        return self.get_pos_at_raw(x, z)

    def cursor(self, e):
        #print("onCursor: " + str(e))
        pass

    def start_solve(self):
        if self.start is None or self.goal is None:
            return

        algo = config["algo"](self.get_pos_at_raw(*self.start),
                              self.get_pos_at_raw(*self.goal),
                              self.panels)
        i = 0

        while True:
            solved = algo.on_step()
            algo.on_bt()
            if solved:
                self.tk.update()
                print("Solved in " + str(i) + " steps")
                break

            i += 1

            if i % 10 == 0:
                self.tk.update()

    def main(self):
        self.tk.mainloop()


if __name__ == '__main__':
    main = Main()
    main.main()
