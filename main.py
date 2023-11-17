from plot import Plot
from polygon_offset import Polygon, Point


if __name__ == '__main__':
    try:
        input_figure_1 = input("Enter coordinates in format '(x,y) (x,y) ...': ")
        input_offset = input("Enter offset in format '(segment_index,offset)': ")

        coordinates = input_figure_1.split(', ')

        figure_1 = []
        for coord in coordinates:
            x, y = map(float, coord.strip('()').split(','))
            figure_1.append((x, y))

        segment_index, offset = map(float, input_offset.strip('()').split(','))

        points = [Point(*p) for p in figure_1]
        polygon = Polygon(points)
        polygon.offset_segment(int(segment_index), offset)

        figure_2 = []
        for i in polygon.points:
            figure_2.append((i.x, i.y))
        print(figure_2)

        Plot(figure_1, figure_2).run()
    except Exception as e:
        print(e)
