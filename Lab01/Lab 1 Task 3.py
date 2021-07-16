from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def drawp_y_points():
    glPointSize(3)


    y = 30
    x = 10
    for j in range(50):
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        y = y+ 10
        glEnd()
def draw_x_points():
    #Task 1
    glPointSize(3)
    x= 10
    y = 20
    for i in range(700):
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
        x = x + 10






def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def DDA(x1, y1, x2, y2):
    glPointSize(3)
    # m = (y1-y2)/(x1-x2)

    if y1 == y2:

        glBegin(GL_POINTS)

        while x1 < x2:
            x1 = x1 + 1
            glVertex2f(x1, round(y1))

        glEnd()

    elif x1 == x2:
        glBegin(GL_POINTS)

        while y1 < y2:
            y1 = y1 + 1
            glVertex2f(x1, y1)

        glEnd()


    else:
        m = (y2 - y1) / (x2 - x1)
        if -1 < m and m > 1:
            glBegin(GL_POINTS)

            while x1 < x2:
                x1 = x1 + 1
                y1 = y1 + m
                glVertex2f(x1, round(y1))

            glEnd()
        else:
            glBegin(GL_POINTS)

            while y1 < y2:
                x1 = x1 + m
                y1 = y1 + 1
                glVertex2f(round(x1), y1)

            glEnd()
def DDA_Dotted(x1, y1, x2, y2):
    glPointSize(2)
    # m = (y1-y2)/(x1-x2)
    u = 0

    if y1 == y2:

        glBegin(GL_POINTS)

        while x1 < x2:
            x1 = x1 + 1
            if u%2==0:
                glVertex2f(x1, round(y1))

            u = u + 1
        glEnd()

    elif x1 == x2:
        glBegin(GL_POINTS)

        while y1 < y2:
            y1 = y1 + 1
            if u % 4 ==0:
                glVertex2f(x1, round(y1))
            u = u + 1
        glEnd()


    else:
        m = (y2 - y1) / (x2 - x1)
        if -1 < m and m > 1:
            glBegin(GL_POINTS)

            while x1 < x2:
                x1 = x1 + 1
                y1 = y1 + m
                if u % 2==0:
                    glVertex2f(x1, round(y1))

                u = u + 1
            glEnd()
        else:
            glBegin(GL_POINTS)

            while y1 < y2:
                x1 = x1 + m
                y1 = y1 + 1

                if u % 2 == 0:
                    glVertex2f(round(x1), y1)

                u = u + 1



            glEnd()
def Tails_draw():
    DDA(200, 50, 200, 250)
    DDA_Dotted(100, 250, 300, 250)

def Heads_draw():
    DDA_Dotted(100, 100, 100, 400)
    DDA(100,250, 300, 250)
    DDA(300, 100, 300, 400)

def Toss(x):
    if int(x[-1])%2==0:
        Tails_draw()

    else:
        Heads_draw()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 0.0)

    # x = input(" Please Provide s Student Id")
    Toss('19101331')





    glutSwapBuffers()




glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 1 Task 3")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()