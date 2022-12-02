from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

w = 1000
h = 550
xmainchar, ymainchar = 50, 60
xmonster1, ymonster1 = 555, 440
arah_monster = False
coll = False

def gerak():
    global ymonster1, xmonster1, arah_monster

    if ymonster1 <= 460 and arah_monster == False:
        ymonster1 -= 2.5
        if ymonster1 <= 60:
            arah_monster =True
    if ymonster1 >= 60 and arah_monster == True:
        ymonster1 += 2.5
        if ymonster1 >= 460:
            arah_monster = False

xkotak, ykotak = 60, 350
xKondisi, yKondisi = False, False
def kotak():
    global xkotak, ykotak, xKondisi, yKondisi
    glPushMatrix()
    if xkotak >= 40 and xKondisi == False:
        xkotak += 1
        if xkotak >= 970:
            xKondisi = True
    
    if xkotak <= 970 and xKondisi == True:
        xkotak -= 1
        if xkotak <= 40:
            xKondisi = False

    if ykotak >= 30 and yKondisi == False:
        ykotak += 2.5
        if ykotak >= 460:
            yKondisi = True
    
    if ykotak <= 460 and yKondisi == True:
        ykotak -= 2.5
        if ykotak <= 30:
            yKondisi = False
    glTranslated(xkotak, ykotak, 0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3d(255, 0, 0)
    glVertex2f(0, 0)
    glEnd()
    glPopMatrix()


xsquare, ysquare = 100, 250
xcondition, ycondition = False, False
def square():
    global xsquare, ysquare, xcondition, ycondition
    glPushMatrix()
    if xsquare >= 40 and xcondition == False:
        xsquare += 2
        if xsquare >= 970:
            xcondition = True
    
    if xsquare <= 970 and xcondition == True:
        xsquare -= 2
        if xsquare <= 40:
            xcondition = False

    if ysquare >= 30 and ycondition == False:
        ysquare += 2.5
        if ysquare >= 460:
            ycondition = True
    
    if ysquare <= 460 and ycondition == True:
        ysquare -= 2.5
        if ysquare <= 30:
            ycondition = False
    glTranslated(xsquare, ysquare, 0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3d(255, 0, 0)
    glVertex2f(0, 0)
    glEnd()
    glPopMatrix()


def tembok():

    glBegin(GL_POLYGON)
    glColor3d(0, 0, 256)
    glVertex2f(0, 0)
    glVertex2f(0, 500)
    glVertex2f(30, 500)
    glVertex2f(30, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(0, 0, 256)
    glVertex2f(0, 500)
    glVertex2f(1000, 500)
    glVertex2f(1000, 470)
    glVertex2f(0, 470)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(0, 0, 256)
    glVertex2f(1000, 500)
    glVertex2f(1000, 0)
    glVertex2f(970, 0)
    glVertex2f(970, 500)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(0, 0, 256)
    glVertex2f(1000, 0)
    glVertex2f(0, 0)
    glVertex2f(0, 30)
    glVertex2f(1000, 30)
    glEnd()


def mainchar():

    glPushMatrix()
    glTranslated(xmainchar, ymainchar, 0)

    if xmainchar in range(int(xmonster1) - 45, int(xmonster1) + 50) and ymainchar in range(int(ymonster1) - 75, int(ymonster1) + 45):
        print("kena")

    # Rambut ==========================================================
    glBegin(GL_POLYGON)
    glColor3ub(77, 60, 56)
    glVertex2f(-20, 0)
    glVertex2f(-20, 23)
    glVertex2f(-16, 23)
    glVertex2f(-16, 30)
    glVertex2f(16, 30)
    glVertex2f(16, 23)
    glVertex2f(20, 23)
    glVertex2f(20, 10)
    glVertex2f(0, 10)
    glVertex2f(0, 0)
    glEnd()

    # Kepala ===========================================================
    glBegin(GL_POLYGON)
    glColor3ub(255, 200, 170)
    glVertex2f(-12, -4)
    glVertex2f(16, -4)
    glVertex2f(16, 14)
    glVertex2f(-6, 14)
    glVertex2f(-6, 6)
    glVertex2f(-12, 6)
    glEnd()

    # Mata ==============================================================
    glBegin(GL_POLYGON)
    glColor3d(0, 0, 0)
    glVertex2f(15, 2)
    glVertex2f(15, 10)
    glVertex2f(10, 10)
    glVertex2f(10, 2)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(0, 0, 0)
    glVertex2f(4, 2)
    glVertex2f(4, 10)
    glVertex2f(-1, 10)
    glVertex2f(-1, 2)
    glEnd()

    # Badan ===============================================================
    glBegin(GL_POLYGON)
    glColor3ub(200, 0, 0)
    glVertex2f(-10, -4)
    glVertex2f(10, -4)
    glVertex2f(10, -16)
    glVertex2f(-10, -16)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(200, 150, 35)
    glVertex2f(-2, -16)
    glVertex2f(-2, -10)
    glVertex2f(4, -10)
    glVertex2f(4, -16)
    glEnd()

    # Tangan ================================================================
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 200)
    glVertex2f(-12, -8)
    glVertex2f(-6, -8)
    glVertex2f(-6, -4)
    glVertex2f(-12, -4)
    glVertex2f(-12, -8)
    glVertex2f(-16, -8)
    glVertex2f(-16, -12)
    glVertex2f(-12, -12)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255, 200, 170)
    glVertex2f(-20, -12)
    glVertex2f(-12, -12)
    glVertex2f(-12, -20)
    glVertex2f(-20, -20)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 200)
    glVertex2f(10, -8)
    glVertex2f(14, -8)
    glVertex2f(14, -12)
    glVertex2f(10, -12)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255, 200, 170)
    glVertex2f(10, -12)
    glVertex2f(18, -12)
    glVertex2f(18, -20)
    glVertex2f(10, -20)
    glEnd()

    # Kaki =====================================================================
    glBegin(GL_POLYGON)
    glColor3ub(102, 51, 0)
    glVertex2f(-10, -16)
    glVertex2f(10, -16)
    glVertex2f(10, -26)
    glVertex2f(4, -26)
    glVertex2f(4, -20)
    glVertex2f(-4, -26)
    glVertex2f(-10, -26)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(204, 102, 0)
    glVertex2f(-10, -26)
    glVertex2f(-4, -26)
    glVertex2f(-4, -30)
    glVertex2f(-10, -30)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(204, 102, 0)
    glVertex2f(4, -26)
    glVertex2f(10, -26)
    glVertex2f(10, -30)
    glVertex2f(4, -30)
    glEnd()
    glPopMatrix()


def monster1():

    glPushMatrix()

    glTranslated(xmonster1, ymonster1, 0)

    # Kepala ====================================================================
    glBegin(GL_QUADS)
    glColor3ub(255, 200, 0)
    glVertex2f(-25, -25)
    glVertex2f(-25, 10)
    glVertex2f(25, 10)
    glVertex2f(25, -25)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(255, 140, 0)
    glVertex2f(-15, -25)
    glVertex2f(15, -25)
    glVertex2f(15, -40)
    glVertex2f(-15, -40)
    glEnd()

    # Garis Mata Kiri ===================================================================
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(-11, 5)
    glVertex2f(-11, -15)
    glEnd()

    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(-20, -5)
    glVertex2f(-2, -5)
    glEnd()

    # Garis Mata Kanan ===========================================================================
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(12, 5)
    glVertex2f(12, -15)
    glEnd()

    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(2, -5)
    glVertex2f(20, -5)
    glEnd()

    # Mata =============================================================================
    def mata(cx, cy, r, sisi):
        glBegin(GL_POLYGON)
        glColor3f(0.5, 0.1, 0.1)
        for i in range(sisi):
            theta = 2 * 3.1415926 * i / sisi
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f(x + cx, y + cy)
        glEnd()
    mata(-11,-5,4.5,1000)
    mata(11.5,-5,4.5,1000)

    # Hidung ========================================================================
    glBegin(GL_POLYGON)
    glColor3d(0, 0, 0)
    glVertex2f(-5, -14)
    glVertex2f(5, -14)
    glVertex2f(0, -23)
    glEnd()

    # Gigi ==============================================================================
    glLineWidth(2)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(-9, -27)
    glVertex2f(-9, -38)
    glEnd()

    glLineWidth(2)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(-3, -27)
    glVertex2f(-3, -38)
    glEnd()

    glLineWidth(2)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(3, -27)
    glVertex2f(3, -38)
    glEnd()

    glLineWidth(2)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(9, -27)
    glVertex2f(9, -38)
    glEnd()

    glPopMatrix()


def objek1():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3d(0,0,256)
    glVertex2d(120, 30)
    glVertex2d(120, 400)
    glVertex2d(180, 400)
    glVertex2d(180, 30)
    glEnd()
    glPopMatrix()


def objek2():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3d(0,0,256)
    glVertex2d(250, 470)
    glVertex2d(250, 100)
    glVertex2d(280, 100)
    glVertex2d(280, 470)
    glEnd()
    glPopMatrix()


def objek3():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3d(0,0,256)
    glVertex2d(350, 30)
    glVertex2d(350, 400)
    glVertex2d(380, 400)
    glVertex2d(380, 30)
    glEnd()
    glPopMatrix()


def objek4():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3d(0,0,256)
    glVertex2d(450, 470)
    glVertex2d(450, 100)
    glVertex2d(500, 100)
    glVertex2d(500, 470)
    glEnd()
    glPopMatrix()


def mySpecialKeyboard1(key, x, y):
    global xmainchar, ymainchar, xmonster1, ymonster1

    if key == GLUT_KEY_RIGHT:
        if xmainchar == 100 and ymainchar < 430:
            xmainchar+=0
        elif xmainchar == 230 and ymainchar > 70:
            xmainchar+=0
        elif xmainchar == 330 and ymainchar < 430:
            xmainchar+=0
        elif xmainchar == 430 and ymainchar > 70:
            xmainchar+=0
        elif xmainchar >= 950:
            xmainchar += 0
        else:
            xmainchar+=10

    if key == GLUT_KEY_LEFT:
        if xmainchar == 200 and ymainchar < 430:
            xmainchar-=0
        elif xmainchar == 300 and ymainchar > 70:
            xmainchar -= 0
        elif xmainchar == 400 and ymainchar < 430:
            xmainchar -= 0
        elif xmainchar == 520 and ymainchar > 70:
            xmainchar -= 0
        elif xmainchar <= 50:
            xmainchar -= 0
        else:
            xmainchar-=10

    if key == GLUT_KEY_UP:
        if ymainchar == 70 and 230 < xmainchar < 300:
            ymainchar+=0
        elif ymainchar == 70 and 430 < xmainchar < 520:
            ymainchar+=0
        elif ymainchar >= 440:
            ymainchar+= 0
        else:
            ymainchar+=10

    if key == GLUT_KEY_DOWN:
        if ymainchar == 430 and 100 < xmainchar < 200:
            ymainchar-=0
        elif ymainchar == 430 and 330 < xmainchar < 400:
            ymainchar-=0
        elif ymainchar <= 60:
            ymainchar-= 0
        else:
            ymainchar-=10
        
    print(f"{xmainchar}, {ymainchar}")


   
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,1)
    glLoadIdentity()
    glViewport(0, 0, 1000, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 1000, 0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    tembok()
    objek1()
    objek2()
    objek3()
    objek4()
    monster1()
    gerak()
    mainchar()
    kotak()
    square()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutSpecialFunc(mySpecialKeyboard1)
glutIdleFunc(showScreen)
glutMainLoop()