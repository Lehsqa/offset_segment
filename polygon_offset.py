import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point


class Polygon:
    def __init__(self, points):
        self.points = points

    def offset_segment(self, segment_index, offset):
        if segment_index < 0 or segment_index >= len(self.points) - 1:
            raise ValueError("Incorrect segment index")

        start_point = self.points[segment_index]
        end_point = self.points[segment_index + 1]

        dx = end_point.x - start_point.x
        dy = end_point.y - start_point.y
        length = math.sqrt(dx ** 2 + dy ** 2)
        ux = dx / length
        uy = dy / length

        new_start_x = start_point.x + offset * uy
        new_start_y = start_point.y - offset * ux
        new_end_x = end_point.x + offset * uy
        new_end_y = end_point.y - offset * ux

        self.points[segment_index] = Point(new_start_x, new_start_y)
        self.points[segment_index + 1] = Point(new_end_x, new_end_y)
