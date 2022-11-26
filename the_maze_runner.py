from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

w = 1000
h = 560
xmonster1 = 10
ymonster1 = 10
xmonster2 = 100
ymonster2 = 100
xScale1 = 3
yScale1 = 3 

def transformation():
    glBegin(GL_POLYGON)
    glScale(3, 3, 0)
    glTranslate(10, 10, 0)
    glEnd()


def tembok():
    glBegin(GL_POLYGON)
    glColor3d(0, 0, 256)
    glVertex2f(0, 0)
    glVertex2f(0, 560)
    glVertex2f(30, 560)
    glVertex2f(30, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(0, 0, 256)
    glVertex2f(0, 560)
    glVertex2f(1000, 560)
    glVertex2f(1000, 530)
    glVertex2f(0, 530)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(0, 0, 256)
    glVertex2f(1000, 560)
    glVertex2f(1000, 0)
    glVertex2f(970, 0)
    glVertex2f(970, 560)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(0, 0, 256)
    glVertex2f(1000, 0)
    glVertex2f(0, 0)
    glVertex2f(0, 30)
    glVertex2f(1000, 30)
    glEnd()


def monster1():
    global xmonster1
    global ymonster1
    glTranslated(xmonster1, ymonster1, 0)
    glScaled(xScale1,yScale1,0)

    # Kepala--------------------
    glBegin(GL_POLYGON)
    glColor3d(255, 255, 0)
    glVertex2f(10, 10)
    glVertex2f(10, 17)
    glVertex2f(20, 17)
    glVertex2f(20, 10)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(255, 255, 0)
    glVertex2f(12, 10)
    glVertex2f(18, 10)
    glVertex2f(18, 7)
    glVertex2f(12, 7)
    glEnd()

    # Garis Mata-------------
    glLineWidth(4)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(13, 15.5)
    glVertex2f(13, 12.5)
    glEnd()

    glLineWidth(4)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(11.5, 14)
    glVertex2f(14.5, 14)
    glEnd()

    glLineWidth(4)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(17, 15.5)
    glVertex2f(17, 12.5)
    glEnd()

    glLineWidth(4)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(15.5, 14)
    glVertex2f(18.5, 14)
    glEnd()

    # Mata-----------------
    def mata(cx, cy, r, sisi):
        glBegin(GL_POLYGON)
        glColor3f(0.5, 0.1, 0.1)
        for i in range(sisi):
            theta = 2 * 3.1415926 * i / sisi
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f(x + cx, y + cy)
        glEnd()
    mata(13,14,0.85,100)
    mata(17,14,0.85,100)

    # Hidung----------------
    glBegin(GL_POLYGON)
    glColor3d(0, 0, 0)
    glVertex2f(14, 11)
    glVertex2f(16, 11)
    glVertex2f(15, 12)
    glEnd()

    # Gigi---------------
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(13.5, 10)
    glVertex2f(13.5, 7.5)
    glEnd()

    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(15, 10)
    glVertex2f(15, 7.5)
    glEnd()

    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(16.5, 10)
    glVertex2f(16.5, 7.5)
    glEnd()


def monster2():
    glBegin(GL_POLYGON)
    glColor3d(255,0,0)
    glVertex2d(30, 30)
    glVertex2d(30, 70)
    glVertex2d(70, 70)
    glVertex2d(70, 30)
    glEnd()



def mySpecialKeyboard1(key, x, y):
    global xmonster1
    global ymonster1
    if key == GLUT_KEY_LEFT:
        if xmonster1 > 10:
            xmonster1 -= 10
        else:
            xmonster1 =- 0
    elif key == GLUT_KEY_RIGHT:
        if xmonster1 < 910:
            xmonster1 += 10
        else:
            xmonster1 +- 0
    elif key == GLUT_KEY_UP:
        if ymonster1 < 480:
            ymonster1 += 10
        else:
            ymonster1 += 0
    elif key == GLUT_KEY_DOWN:
        if ymonster1 > 10:
            ymonster1 -= 10
        else:
            ymonster1 -= 0

def myMouse(button, state, xmouse, ymouse):
    global xmonster2, ymonster2
    if button == GLUT_LEFT_BUTTON & state == GLUT_DOWN:
        xmonster2 = xmouse - w/2
        xmonster2 = h/2 - ymouse
        # print(pos_x_box)
        # print(xmouse)
        # print(pos_y_box)
        # print(ymouse)



def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,1)
    glLoadIdentity()
    iterate()
    tembok()
    monster1()
    monster2()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(mySpecialKeyboard1)
glutMouseFunc(myMouse)
glutMainLoop()