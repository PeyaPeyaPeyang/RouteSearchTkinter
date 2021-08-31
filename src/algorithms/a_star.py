import math

from utils import *


class AStar:
    def __init__(self, start_panel, goal_panel, tree):
        self.goal = goal_panel
        self.last_search = self.current = start_panel
        self.mark_open = [start_panel]
        self.tree = tree
        self.mark_close = []

    def on_bt(self):
        t = self.current
        route = [t]
        while t.root:
            route.append(t.root)
            t = t.root
        [panel.on_search() for panel in route]

    def on_step(self):
        for panel in self.mark_open:
            type_as(panel, "OPEN")
        for panel in self.mark_close:
            type_as(panel, "CLOSE")

        if len(self.mark_open) == 0:
            print("No solution has found.")
            return True

        solve = 0
        for i in range(1, len(self.mark_open)):
            if self.mark_open[i].n < self.mark_open[solve].n:
                solve = i

            if (self.mark_open[i].n == self.mark_open[solve].n) \
                and self.mark_open[i].m > self.mark_open[solve].m:
                solve = i

        current = self.current = self.last_search = self.mark_open[solve]

        if current == self.goal:
            print("Solved.")
            return True

        if current in self.mark_open:
            self.mark_open.remove(current)

        self.mark_close.append(current)

        parents = self.current.parents

        if len(parents) == 0:
            parents = current.search_parents(self.tree, len(self.tree), len(self.tree[0]))

        for parent in parents:
            if parent not in self.mark_close:
                if parent.type == "WALL":
                    continue
                tmp_m = current.m + math.sqrt((parent.pos_x - current.pos_x) ** 2 + (parent.pos_z - current.pos_z) ** 2)

                if parent not in self.mark_open:
                    self.mark_open.append(parent)
                elif tmp_m >= parent.m:
                    continue

                parent.m = tmp_m
                parent.s = math.sqrt((parent.pos_x - self.goal.pos_x) ** 2 + (parent.pos_z - self.goal.pos_z) ** 2)
                parent.n = parent.m + parent.s
                parent.root = current

        return False
