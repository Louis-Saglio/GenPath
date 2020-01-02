from __future__ import annotations

from random import randint, choice


class Point:

    def __init__(self, x, y):
        self.coord = self.x, self.y = x, y

    def __eq__(self, other: Point):
        return self.coord == other.coord

    def __hash__(self):
        return hash(self.coord)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Path:

    def __init__(self, points=None):
        self.points = points or []

    def total_length(self):
        total = 0
        old_point = self.points[0]
        for point in self.points[1:]:
            total += Path.distance_between(old_point, point)
            old_point = point
        return total

    @staticmethod
    def distance_between(a: Point, b: Point):
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** (1 / 2)

    @staticmethod
    def merge(a: Path, b: Path) -> Path:
        points = []
        for p1, p2 in zip(a.points, b.points):
            point = choice((p1, p2))
            if point not in points:
                points.append(point)
        path = Path(points)
        print(Path.similarity(a, path), Path.similarity(b, path))
        return path

    @staticmethod
    def similarity(p1: Path, p2: Path) -> int:
        total = 0
        for point1, point2 in zip(p1.points, p2.points):
            if point1 == point2:
                total += 1
        return total / len(p1.points)

    def __repr__(self):
        return f"size: {len(self.points)}, length: {self.total_length()}"


def get_random_point_list(nbr=30000, mini=0, maxi=10) -> list:
    return [Point(randint(mini, maxi), randint(mini, maxi)) for _ in range(nbr)]


P1 = Path(list(get_random_point_list()))
P2 = Path(list(get_random_point_list()))
P3 = Path.merge(P1, P2)
