from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def bangun_bawahkanan():
    glBegin(GL_QUADS)
    glColor3d(255, 255, 0)
    glVertex2f(55, 10)
    glVertex2f(95, 10)
    glVertex2f(95, 50)
    glVertex2f(55, 50)
    glEnd()

def bangun_bawahkiri():
    glBegin(GL_QUADS)
    glColor3d(0, 0, 255)
    glVertex2f(10, 10)
    glVertex2f(50, 10)
    glVertex2f(50, 50)
    glVertex2f(10, 50)
    glEnd()

def bangun_ataskanan():
    glBegin(GL_QUADS)
    glColor3d(0, 255, 0)
    glVertex2f(55, 55)
    glVertex2f(95, 55)
    glVertex2f(95, 95)
    glVertex2f(55, 95)
    glEnd()

def bangun_ataskiri():
    glBegin(GL_QUADS)
    glColor3d(255, 0, 0)
    glVertex2f(10, 55)
    glVertex2f(50, 55)
    glVertex2f(50, 95)
    glVertex2f(10, 95)
    glEnd()

def iterate():
    glViewport(0, 0, 2500, 2500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255,255,255,1)
    glLoadIdentity()
    iterate()
    bangun_bawahkiri()
    bangun_bawahkanan()
    bangun_ataskanan()
    bangun_ataskiri()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(530, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()