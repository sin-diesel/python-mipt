#!/usr/bin/python3

from math import sqrt
import code

class Point3D:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.coordinates = [self.x, self.y, self.z]

    def distance_to(self, point) -> float:
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2 + 
                    (self.z - point.z) ** 2)

class Segment3D:
    def __init__(self, point_1: Point3D, point_2: Point3D) -> None:
        self.point_1 = point_1
        self.point_2 = point_2
        self.x = point_1.x - point_2.x
        self.y = point_1.y - point_2.y
        self.z = point_1.z - point_2.z

    def length(self) -> float:
        return self.point_1.distance_to(self.point_2)

    def middle(self) -> Point3D:
        return Point3D((self.point_1.x + self.point_2.x) / 2,
                       (self.point_1.y + self.point_2.y) / 2,
                       (self.point_1.z + self.point_2.z) / 2)

    def dot(self, segment) -> float:
        return self.x * segment.x + self.y * segment.y + self.z * segment.z

    def cos_to(self, segment) -> float:
        return abs(self.dot(segment) / (self.length() * segment.length()))

s1 = Segment3D(Point3D(0, 0, 0), Point3D(1, 2, 3))
s2 = Segment3D(Point3D(0, 0, 0), Point3D(1, 0, 0))
code.interact(local={**locals(), **globals()})