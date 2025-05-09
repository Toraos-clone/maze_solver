from point import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.draw(200, 50, 250, 100)

    c1.draw_move(c2)

    #c = Cell(win)
    #c.has_left_wall = False
    #c.draw(50, 50, 100, 100)

    #c = Cell(win)
    #c.has_right_wall = False
    #c.draw(125, 125, 200, 200)

    #c = Cell(win)
    #c.has_bottom_wall = False
    #c.draw(225, 225, 250, 250)

    #c = Cell(win)
    #c.has_top_wall = False
    #c.draw(300, 300, 500, 500)

    win.wait_for_close()


main()