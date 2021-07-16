from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *




def drwahouse():
    glBegin(GL_LINES)
    glVertex2f(100, 250)
    glVertex2f(500, 250)

    glVertex2f(100, 250)
    glVertex2f(300, 350)

    glVertex2f(500, 250)
    glVertex2f(300, 350)

    glVertex2f(100, 250)
    glVertex2f(100, 20)

    glVertex2f(500, 250)
    glVertex2f(500, 20)

    glVertex2f(100, 20)
    glVertex2f(500, 20)








    glVertex2f(130, 210)
    glVertex2f(200, 210)

    glVertex2f(130, 210)
    glVertex2f(130, 150)

    glVertex2f(130, 150)
    glVertex2f(200, 150)

    glVertex2f(200, 210)
    glVertex2f(200, 150)

    #____________________________

    glVertex2f(470, 210)
    glVertex2f(400, 210)

    glVertex2f(470, 210)
    glVertex2f(470, 150)

    glVertex2f(400, 150)
    glVertex2f(470, 150)

    glVertex2f(400, 210)
    glVertex2f(400, 150)

    # ____________________________

    glVertex2f(250, 120)
    glVertex2f(350, 120)

    glVertex2f(250, 120)
    glVertex2f(350, 120)


    glVertex2f(250, 120)
    glVertex2f(250, 20)

    glVertex2f(350, 120)
    glVertex2f(350, 20)

    glEnd()
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(330, 100)


    glEnd()


def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()




def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 0.0)


    # Task 2

    drwahouse()




    glutSwapBuffers()




glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 1 Task 2")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()