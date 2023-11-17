class Vec3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "[{}, {}, {}]".format(self.x, self.y, self.z)

    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

a = [(8.76, 4.45, 4.21), (9.32, 8.38, 2.43), (0.98, 2.23, 0.61), (2.23, 6.53, 2.53), (7.65, 2.23, 7.65)]

Vec3D_list = [Vec3D(x, y, z) for x, y, z in a]

sorted_Vec3D_list = sorted(Vec3D_list, key = lambda vec: vec.length())

print(sorted_Vec3D_list)