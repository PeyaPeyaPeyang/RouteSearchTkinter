
COLORS = {
    "NORMAL": "#FFFFFF",
    "WALL": "#000000",
    "START": "#FF00FF",
    "GOAL": "#00FF00"
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

    def bind(self):
        pixel = self.pixel
        self.canvas.create_rectangle(self.abs_x * pixel,
                                     self.abs_z * pixel,
                                     self.abs_x * pixel + pixel,
                                     self.abs_z * pixel + pixel,
                                     fill=COLORS[self.type])

    def search_parents(self, tree, size_x, size_z):
        self.parents = []
        if self.abs_x < size_x - 1:  # search mid
            self.parents.append(tree[self.abs_x + 1][self.abs_z])
            if self.abs_x > 0:  # left
                self.parents.append(tree[self.abs_x + 1][self.abs_z - 1])
            if self.abs_z < size_z - 1:
                self.parents.append(tree[self.abs_x + 1][self.abs_z + 1])
        if self.abs_x > 0:
            self.parents.append(tree[self.abs_x - 1][self.abs_z])
            if self.abs_x > 0:  # left
                self.parents.append(tree[self.abs_x - 1][self.abs_z - 1])
            if self.abs_z < size_z - 1:
                self.parents.append(tree[self.abs_x - 1][self.abs_z + 1])
        if self.abs_z < size_z - 1:
            self.parents.append(tree[self.abs_x][self.abs_z + 1])
        if size_z > 0:
            self.parents.append(tree[self.abs_x][self.abs_z + 1])

    def on_search(self):
        if not self.root:
            raise ValueError("Root panel is not defined.")
        self.canvas.create_line(self.root.pos_x, self.root.pos_y,  # start
                                self.pos_x, self.pos_z,  # end
                                )
