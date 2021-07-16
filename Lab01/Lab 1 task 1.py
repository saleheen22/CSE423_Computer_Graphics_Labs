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






def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 0.0)




    # # Task 1
    draw_x_points()  # x coordinate
    drawp_y_points() # y coordinate


    # Task 2

    # drwalines()




    glutSwapBuffers()




glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 1 Task 1")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()