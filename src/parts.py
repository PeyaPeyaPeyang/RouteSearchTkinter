
COLORS = {
    "NORMAL": "#FFFFFF",  # white
    "WALL": "#000000",  # black
    "START": "#FF00FF",  # magenta
    "GOAL": "#00FF00",  # green
    "OPEN": "#FF0000",  # red
    "CLOSE": "#0000FF",  # blue
    "BT": "#FFFF00"  # yellow
}


class Panel:

    def __init__(self, canvas, w_x, h_z, pixel):
        self.abs_x = w_x
        self.abs_z = h_z
        self.pos_x = w_x * pixel + pixel // 2
        self.pos_z = h_z * pixel + pixel // 2

        self.pixel = pixel
        self.canvas = canvas
        self.type = "NORMAL"
        self.root = None
        self.parents = []

        self.n = self.m = self.s = 0 # extend for a*

    def bind(self):
        pixel = self.pixel
        self.canvas.create_rectangle(self.abs_x * pixel,
                                     self.abs_z * pixel,
                                     self.abs_x * pixel + pixel,
                                     self.abs_z * pixel + pixel,
                                     fill=COLORS[self.type])

    def search_parents(self, tree, size_x, size_z):
        if self.abs_x < size_x - 1:  # search mid
            self.parents.append(tree[self.abs_x + 1][self.abs_z])
            if self.abs_z > 0:  # left
                self.parents.append(tree[self.abs_x + 1][self.abs_z - 1])
            if self.abs_z < size_z - 1:
                self.parents.append(tree[self.abs_x + 1][self.abs_z + 1])
        if self.abs_x > 0:
            self.parents.append(tree[self.abs_x - 1][self.abs_z])
            if self.abs_z > 0:  # left
                self.parents.append(tree[self.abs_x - 1][self.abs_z - 1])
            if self.abs_z < size_z - 1:
                self.parents.append(tree[self.abs_x - 1][self.abs_z + 1])
        if self.abs_z < size_z - 1:
            self.parents.append(tree[self.abs_x][self.abs_z + 1])
        if size_z > 0:
            self.parents.append(tree[self.abs_x][self.abs_z - 1])

        return self.parents

    def on_search(self):
        if not self.root:
            return
        self.canvas.create_line(self.root.pos_x, self.root.pos_z,  # start
                                self.pos_x, self.pos_z,  # end
                                width=5,
                                fill="green"
                                )
