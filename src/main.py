from graphics import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(50, 50, 100, 100)

    win.wait_for_close()


main()
