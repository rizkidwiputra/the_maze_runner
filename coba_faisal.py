from math import atan2
import random as rd
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import os
del os.environ['DISPLAY']


w, h = 1000, 800
pos_x_arrow = -400
pos_y_arrow = 0
pos_x_box = 300
pos_y_box = 0
collision = False
pos_x_meteor = 1000
pos_y_meteor = rd.randint(0,800)
tes = ['faisal']


def timer_laser(value):
    global pos_x_arrow, pos_y_arrow
    pos_x_arrow += 6
    print(pos_x_arrow)
    glutTimerFunc(10, timer_laser, 0)

def gerak_meteor():
    global pos_x_meteor, pos_y_meteor
    if pos_x_meteor != pos_x_arrow and pos_y_meteor != pos_y_arrow:
        pos_x_meteor -= 1
        pos_y_meteor -= 1
    glutTimerFunc(10,gerak_meteor, 0)

def meteor():
    glPushMatrix()
    glScaled(100,100,1)
    glTranslated(pos_x_meteor, pos_y_meteor, 0)
    glBegin(GL_POLYGON)
    glVertex2f(1.5,1.5)
    glVertex2f(1.2295140197694,1.9797922412113)
    glVertex2f(0.9658978770376,2.192149689523)
    glVertex2f(0.7242497462002,2.3166350902575)
    glVertex2f(0.2263081432624,2.3898617965718)
    glVertex2f(-0.2936014715696,2.3898617965718)
    glVertex2f(-0.4766682373555,2.3898617965718)
    glVertex2f(-0.8794151220846,2.3019897489946)
    glVertex2f(-1.0917725703963,2.2653763958374)
    glVertex2f(-1.304130018708,2.023728265)
    glVertex2f(-1.3846793956538,1.840661499214)
    glVertex2f(-1.3846793956538,1.5697226858508)
    glVertex2f(-1.4139700781795,1.437914614485)
    glVertex2f(-1.3114526893394,1.2109118249104)
    glVertex2f(-1.186967288605,1.0937490948074)
    glVertex2f(-1.0917725703963,0.9180049996529)
    glVertex2f(-1.0478365466077,0.7935195989185)
    glVertex2f(-1.0405138759762,0.5958074918697)
    glVertex2f(-1.1137405822906,0.4786447617667)
    glVertex2f(-1.2601939949193,0.3395140197694)
    glVertex2f(-1.2528713242879,0.2296739602978)
    glVertex2f(-1,0)
    glVertex2f(-0.7329617094559,-0.0632328649597)
    glVertex2f(-0.5865082968271,-0.1803955950627)
    glVertex2f(-0.0519533407322,-0.3341716783229)
    glVertex2f(0.4313429209427,-0.3634623608486)
    glVertex2f(0.6144096867286,-0.2389769601142)
    glVertex2f(0.9073165119861,-0.0192968411711)
    glVertex2f(1.1416419721921,0.3980953848209)
    glVertex2f(1.2880953848209,0.6324208450269)
    glVertex2f(1.3100633967152,0.9106823290215)
    glVertex2f(1.5150981743954,1.3353972256449)
    glEnd()
    glPopMatrix()

def arrow():
    global collision
    if collision == False:
        glPushMatrix()
        glTranslated(pos_x_arrow, pos_y_arrow, 0)
        if pos_x_arrow in range(int(pos_x_box)-100, int(pos_x_box)+100) and pos_y_arrow in range(int(pos_y_box)-100, int(pos_y_box)+100):
                collision = True
        glBegin(GL_LINE_LOOP)
        glVertex2f(-10, 10)
        glVertex2f(10, 10)
        glVertex2f(10, -10)
        glVertex2f(-10, -10)
        glEnd()
        glutPostRedisplay()
        glPopMatrix()


def box():
    if collision == False:
        glPushMatrix()
        glTranslated(pos_x_box, pos_y_box, 0)
        glBegin(GL_POLYGON)
        glVertex2f(-100, 100)
        glVertex2f(100, 100)
        glVertex2f(100, -100)
        glVertex2f(-100, -100)
        glEnd()
        glPopMatrix()

def background():
    glScaled(100, 100, 1)
    glPushMatrix()
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(-10, 10)
    glVertex2f(10, 10)
    glVertex2f(10, -10)
    glVertex2f(-10, -10)
    glEnd()
    glPopMatrix()

def myKeyboard(key, x, y):
    global collision, pos_x_arrow, pos_y_arrow
    if key == b' ': 
        timer_laser(0)  
    if key == b'a':
        pos_x_arrow -= 10
    if key == b'w':
        pos_y_arrow += 10
    if key == b's':
        pos_y_arrow -= 10
    if key == b'd':
        pos_x_arrow += 10
    if key == b'r':
        collision = False
        

def myMouse(button, state, xmouse, ymouse):
    global pos_x_box, pos_y_box
    if button == GLUT_LEFT_BUTTON & state == GLUT_DOWN:
        pos_x_box = xmouse - w/2
        pos_y_box = h/2 - ymouse
        print(pos_x_box)
        print(xmouse)
        print(pos_y_box)
        print(ymouse)

def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-w/2, w/2, -h/2, h/2, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    if collision == False:
        arrow()
        box()
    # meteor()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
window = glutCreateWindow("glTransform")
glutDisplayFunc(showScreen)
glutKeyboardFunc(myKeyboard)
glutMouseFunc(myMouse)
glutIdleFunc(showScreen)
glutMainLoop()
