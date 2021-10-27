from OpenGL.GL import *
from OpenGL.GLUT import *



def midPoint(x1, y1,x2, y2):

    # Setup initial conditions

    points = []

    if x1 == x2:
        for i in range(y1, y2 + 1):
            z = (x1, i)
            points.append(z)


        return points
    if y1 == y2:
        for i in range(x1, x2 + 1):
            z = (i, y1)
            points.append(z)


        return points
    dx = x2 - x1
    dy = y2 - y1

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1

    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points

def drawid():
    glPointSize(3)
    glBegin(GL_POINTS)

    lst = midPoint(200, 250, 200, 300)

    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1


#___________________________________________________#
    lst1 = midPoint(150, 300, 200, 300)
    i = 0
    while i < len(lst1):
        glVertex2f(lst1[i][0], lst1[i][1])
        i = i + 1


# #_______________________________________________+
    lst = midPoint(150, 250, 200, 250)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1


# #======================================================
    lst = midPoint(200, 200, 200, 250)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1
#
#
#     # ======================================================
    lst = midPoint(150, 200, 200, 200)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1

# #
#
#     # ======================================================
    lst = midPoint(280, 200, 280, 300)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1
#
#
#     # ======================================================
    lst = midPoint(230, 250, 280, 300)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1
#
#
#     # ======================================================
    lst = midPoint(240, 200, 310, 200)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1
    glEnd()


def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 0.0)
    drawid()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 2 Task 1")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
