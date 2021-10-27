from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def drawPoint(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def circlePoints(x, y, x_centre, y_centre):
    zone_change(x, y, x_centre, y_centre)


def zone_change(x, y, x_centre, y_centre):
    new_x = x + x_centre
    new_y = y + y_centre
    drawPoint(new_x, new_y)


    new_x = y + x_centre
    new_y = x + y_centre
    drawPoint(new_x, new_y)


    new_x = -1 * y + x_centre
    new_y = x + y_centre
    drawPoint(new_x, new_y)


    new_x = -1 * x + x_centre
    new_y = y + y_centre
    drawPoint(new_x, new_y)


    new_x = -1 * x + x_centre
    new_y = -1 * y + y_centre
    drawPoint(new_x, new_y)


    new_x = -1 * y + x_centre
    new_y = -1 * x + y_centre
    drawPoint(new_x, new_y)


    new_x = y + x_centre
    new_y = -1 * x + y_centre
    drawPoint(new_x, new_y)


    new_x = x + x_centre
    new_y = -1 * y + y_centre
    drawPoint(new_x, new_y)


def midPointCircle(x_centre, y_centre, r):
    d = 1 - r
    x = 0
    y = r
    circlePoints(x, y, x_centre, y_centre)
    while x < y:
        if d < 0:

            d = d + 2 * x + 3
            x = x + 1
        else:

            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1

        circlePoints(x, y, x_centre, y_centre)


def drawCircle():
    midPointCircle(300, 100, 30)
    midPointCircle(300, 150, 30)
    midPointCircle(300, 200, 30)
    midPointCircle(300, 250, 30)
    midPointCircle(300, 300, 30)
    midPointCircle(300, 350, 30)
    midPointCircle(300, 400, 30)
    midPointCircle(300, 450, 30)
    midPointCircle(300, 500, 30)

    midPointCircle(260, 480, 30)
    midPointCircle(220, 450, 30)
    midPointCircle(180, 415, 30)
    midPointCircle(150, 385, 30)
    midPointCircle(110, 350, 30)

    midPointCircle(200, 100, 30)
    midPointCircle(250, 100, 30)
    midPointCircle(300, 100, 30)
    midPointCircle(350, 100, 30)
    midPointCircle(400, 100, 30)


def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)

    drawCircle()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Id-19101331 print 1")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
