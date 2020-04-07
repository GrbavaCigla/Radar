from graphics import *
from screeninfo import get_monitors
from math import *
from time import sleep
import serial


def main(thickness=3, barheight=-100):
    try:
        s = get_monitors()[0]
        height = s.height
        width = s.width

        win = GraphWin('Radar', width, height)
        win.setBackground('black')

        textti = Text(Point(width/2, height/2-30), 'Speed (default 0.08):')
        textti.setOutline('Green')
        textti.draw(win)

        entry2 = Entry(Point(width/2, height/2), 20)
        entry2.draw(win)

        win.getMouse()
        times = entry2.getText()

        if not times:
            times = 0.08
        else:
            times = float(times)
        entry2.undraw()
        textti.undraw()

        textse = Text(Point(width/2, height/2-30), 'Serial port:')
        textse.setOutline('Green')
        textse.draw(win)

        entry = Entry(Point(width/2, height/2), 20)
        entry.draw(win)
        win.getMouse()
        port = entry.getText()
        print(port)
        if not port:
            pass
        else:
            ser = serial.Serial(port)
            print(ser.name)
        entry.undraw()
        textse.undraw()
        height = s.height+barheight

        circle = Circle(Point(width/2, height), width/2)
        circle.setOutline('green')
        circle.setFill('green')
        circle.draw(win)
        circle2 = Circle(Point(width/2, height), width/2-thickness)
        circle2.setOutline('green')
        circle2.setFill('black')
        circle2.draw(win)

        circles1 = Circle(Point(width/2, height), width/3)
        circles1.setOutline('green')
        circles1.draw(win)

        circles2 = Circle(Point(width/2, height), width/4)
        circles2.setOutline('green')
        circles2.draw(win)

        circles3 = Circle(Point(width/2, height), (width/2+width/3)/2)
        circles3.setOutline('green')
        circles3.draw(win)

        circles4 = Circle(Point(width/2, height), width/6)
        circles4.setOutline('green')
        circles4.draw(win)

        linenorm = Line(Point(width/2, height), Point(width/2, height-width/2))
        linenorm.setOutline('green')
        linenorm.draw(win)

        y = height-(sqrt(2)/2)*(width/2)
        x = width/2-(sqrt(2)/2)*(width/2)

        line45 = Line(Point(width/2, height), Point(x, y))
        line45.setOutline('green')
        line45.draw(win)

        y = height-((sqrt(2)/2)*(width/2))
        x = (width/2)+((sqrt(2)/2)*(width/2))
        line135 = Line(Point(width/2, height), Point(x, y))
        line135.setOutline('green')
        line135.draw(win)

        rect = Rectangle(Point(-1, height-barheight*10), Point(width, height))
        rect.setOutline('green')
        rect.setFill('black')
        rect.draw(win)

        textnorm = Text(Point(width/2, height-width/2-10), "0")
        textnorm.setOutline('Green')
        textnorm.draw(win)

        textcm = Text(Point(width/4*3, width/2+35), '20cm')
        textcm.setOutline('Green')
        textcm.draw(win)

        textcm2 = Text(Point(width/6*4, width/2+35), '10cm')
        textcm2.setOutline('Green')
        textcm2.draw(win)

        textcm3 = Text(Point(width-20, width/2+35), '50cm')
        textcm3.setOutline('Green')
        textcm3.draw(win)

        textcm4 = Text(Point((width/2+width/3)*1, width/2+35), '30cm')
        textcm4.setOutline('Green')
        textcm4.draw(win)

        textcm5 = Text(Point((width+width/3)/1.455, width/2+35), '40cm')
        textcm5.setOutline('Green')
        textcm5.draw(win)

        while True:

            rect2 = Rectangle(Point(width-200, 10),
                              Point(width-5, height-(height-80)))
            rect2.setOutline('Green')
            rect2.draw(win)
            text3 = Text(Point(width-100, 20), 'r={}'.format(width/2))
            text3.setOutline('Green')
            text3.draw(win)
            for i in range(1, 180):
                if port:
                    data = ser.readline()

                g = i
                y3 = height-(sin(radians(g))*(width/2))
                x3 = (width/2)+(cos(radians(g))*(width/2))
                lines = Line(Point(width/2, height), Point(x3, y3))
                lines.setOutline('red')
                lines.draw(win)
                textangle = Text(Point(width/4, width/2+35),
                                 'Angle:{}°'.format(g))
                textangle.setOutline('Green')
                textangle.draw(win)

                trigfunctext = Text(Point(width-100, 40),
                                    'x=sin{}°*r≈{}'.format(g, round(x3, 5)))
                trigfunctext.setOutline('Green')
                trigfunctext.draw(win)
                trigfunctext2 = Text(Point(width-100, 60),
                                     'y=cos{}°*r≈{}'.format(g, round(y3, 5)))
                trigfunctext2.setOutline('Green')
                trigfunctext2.draw(win)
                sleep(times)
                textangle.undraw()
                lines.undraw()
                trigfunctext.undraw()
                trigfunctext2.undraw()

            for i in range(1, -180, -1):
                if port:
                    data = ser.readline()

                g = abs(i)
                y3 = height-(sin(radians(g))*(width/2))
                x3 = (width/2)-(cos(radians(g))*(width/2))
                lines = Line(Point(width/2, height), Point(x3, y3))
                lines.setOutline('red')
                lines.draw(win)
                textangle = Text(Point(width/4, width/2+35),
                                 'Angle:{}°'.format(g))
                textangle.setOutline('Green')
                textangle.draw(win)

                trigfunctext = Text(Point(width-100, 40),
                                    'x=sin{}°*r≈{}'.format(180-g, round(x3, 5)))
                trigfunctext.setOutline('Green')
                trigfunctext.draw(win)
                trigfunctext2 = Text(
                    Point(width-100, 60), 'y=cos{}°*r≈{}'.format(180-g, round(y3, 5)))
                trigfunctext2.setOutline('Green')
                trigfunctext2.draw(win)
                sleep(times)
                lines.undraw()
                trigfunctext.undraw()
                trigfunctext2.undraw()
                textangle.undraw()

            # p=win.getMouse()
            # print(p.x,p.y)
    except GraphicsError:
        win.close()


main()
