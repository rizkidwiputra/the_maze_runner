from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

w = 1000
h = 560
xmonster = 10
ymonster = 10
xScale = 3
yScale = 3 

def transformation():
    glScale(4, 4, 0)
    glTranslate(10, 10, 0)
    glBegin(GL_POLYGON)
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


def monster():
    glTranslated(xmonster, ymonster, 0)
    glScaled(xScale,yScale,0)

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

def mySpecialKeyboard(key, x, y):
    global xmonster
    global ymonster
    global xScale
    global yScale
    if key == GLUT_KEY_LEFT:
        if xmonster > 10:
            xmonster -= 10
        else:
            xmonster =- 0
    elif key == GLUT_KEY_RIGHT:
        if xmonster < 910:
            xmonster += 10
        else:
            xmonster +- 0
    elif key == GLUT_KEY_UP:
        if ymonster < 480:
            ymonster += 10
        else:
            ymonster += 0
    elif key == GLUT_KEY_DOWN:
        if ymonster > 10:
            ymonster -= 10
        else:
            ymonster -= 0

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
    # transformation()
    monster()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(mySpecialKeyboard)
glutMainLoop()