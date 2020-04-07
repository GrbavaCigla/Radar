from graphics import *
import gi
from math import *
from screeninfo import get_monitors


def main(thickness=3, barheight=-100):
    try:
        s = get_monitors()[0]

        height = s.height
        width = s.width

        win = GraphWin('Radar', width, height)
        win.setBackground('white')

        circle = Circle(Point(width/2, height), width/2)
        circle.setOutline('black')
        circle.draw(win)

        linenorm = Line(Point(width/2, height), Point(width/2, height-width/2))
        linenorm.setOutline('black')
        linenorm.draw(win)

        y = height-(sqrt(2)/2)*(width/2)
        x = width/2-(sqrt(2)/2)*(width/2)

        line45 = Line(Point(width/2, height), Point(x, y))
        line45.setOutline('black')
        line45.draw(win)

        y2 = height-((sqrt(2)/2)*(width/2))
        x2 = (width/2)+((sqrt(2)/2)*(width/2))

        line135 = Line(Point(width/2, height), Point(x2, y2))
        line135.setOutline('black')
        line135.draw(win)

        for i in range(1, 90):
            g = i
            y3 = height-(sin(radians(g))*(width/2))
            x3 = (width/2)-(cos(radians(g))*(width/2))
            lines = Line(Point(width/2, height), Point(x3, y3))
            lines.setOutline('red')
            lines.draw(win)
        for i in range(1, 90):
            g = i
            y3 = height-(sin(radians(g))*(width/2))
            x3 = (width/2)+(cos(radians(g))*(width/2))
            lines = Line(Point(width/2, height), Point(x3, y3))
            lines.setOutline('red')
            lines.draw(win)

        while True:
            p = win.getMouse()
            print(p.x, p.y)
    except GraphicsError:
        win.close()
        pass


main()
