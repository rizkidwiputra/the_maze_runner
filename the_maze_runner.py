from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

xmainchar, ymainchar = 50, 60
xmonster1, ymonster1 = 555, 440
xmonster2, ymonster2 = 635, 440
xmonster3, ymonster3 = 715, 440
xdiamond, ydiamond = 940, 440
arah_monster1 = False
arah_monster2 = False
arah_monster3 = False
xkotak1, ykotak1 = 60, 350
xKondisi1, yKondisi1 = False, False
xkotak2, ykotak2 = 100, 250
xkondisi2, ykondisi2 = False, False
xkotak3, ykotak3 = 400, 250
xkondisi3, ykondisi3 = False, False
coll = False
play = True
lose = False
win = False

# Gerak Monster 1 =====================================================================

def gerak1():
    global ymonster1, xmonster1, arah_monster1

    if ymonster1 <= 460 and arah_monster1 == False:
        ymonster1 -= 2.5
        if ymonster1 <= 70:
            arah_monster1 =True
    if ymonster1 >= 70 and arah_monster1 == True:
        ymonster1 += 2.5
        if ymonster1 >= 460:
            arah_monster1 = False


# Gerak Monster 2 =====================================================================
def gerak2():
    global ymonster2, xmonster2, arah_monster2

    if ymonster2 <= 460 and arah_monster2 == False:
        ymonster2 -= 10
        if ymonster2 <= 70:
            arah_monster2 =True
    if ymonster2 >= 70 and arah_monster2 == True:
        ymonster2 += 10
        if ymonster2 >= 460:
            arah_monster2 = False


# Gerak Monster 3 =====================================================================
def gerak3():
    global ymonster3, xmonster3, arah_monster3

    if ymonster3 <= 460 and arah_monster3 == False:
        ymonster3 -= 5
        if ymonster3 <= 70:
            arah_monster3 =True
    if ymonster3 >= 70 and arah_monster3 == True:
        ymonster3 += 5
        if ymonster3 >= 460:
            arah_monster3 = False


# Laser 1 =============================================================================
def kotak1(cx, cy, r, sisi):
    global xkotak1, ykotak1, xKondisi1, yKondisi1
    glPushMatrix()
    if xkotak1 >= 40 and xKondisi1 == False:
        xkotak1 += 2.5
        if xkotak1 >= 960:
            xKondisi1 = True
    
    if xkotak1 <= 960 and xKondisi1 == True:
        xkotak1 -= 2.5
        if xkotak1 <= 40:
            xKondisi1 = False

    if ykotak1 >= 40 and yKondisi1 == False:
        ykotak1 += 2
        if ykotak1 >= 460:
            yKondisi1 = True
    
    if ykotak1 <= 460 and yKondisi1 == True:
        ykotak1 -= 2
        if ykotak1 <= 40:
            yKondisi1 = False
    glTranslated(xkotak1, ykotak1, 0)
    glBegin(GL_POLYGON)
    glColor3d(255, 0, 0)
    for i in range(sisi):
        theta = 2 * 3.1415926 * i / sisi
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()
    glPopMatrix()


# Laser 2 =============================================================================
def kotak2(cx, cy, r, sisi):
    global xkotak2, ykotak2, xkondisi2, ykondisi2
    glPushMatrix()
    if xkotak2 >= 40 and xkondisi2 == False:
        xkotak2 += 4
        if xkotak2 >= 960:
            xkondisi2 = True
    
    if xkotak2 <= 960 and xkondisi2 == True:
        xkotak2 -= 4
        if xkotak2 <= 40:
            xkondisi2 = False

    if ykotak2 >= 40 and ykondisi2 == False:
        ykotak2 += 2
        if ykotak2 >= 460:
            ykondisi2 = True
    
    if ykotak2 <= 460 and ykondisi2 == True:
        ykotak2 -= 2
        if ykotak2 <= 40:
            ykondisi2 = False
    glTranslated(xkotak2, ykotak2, 0)
    glBegin(GL_POLYGON)
    glColor3d(255, 0, 0)
    for i in range(sisi):
        theta = 2 * 3.1415926 * i / sisi
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()
    glPopMatrix()


# Laser 3 =============================================================================
def kotak3(cx, cy, r ,sisi):
    global xkotak3, ykotak3, xkondisi3, ykondisi3
    glPushMatrix()
    if xkotak3 >= 40 and xkondisi3 == False:
        xkotak3 += 4
        if xkotak3 >= 960:
            xkondisi3 = True
    
    if xkotak3 <= 960 and xkondisi3 == True:
        xkotak3 -= 4
        if xkotak3 <= 40:
            xkondisi3 = False

    if ykotak3 >= 40 and ykondisi3 == False:
        ykotak3 += 3
        if ykotak3 >= 460:
            ykondisi3 = True
    
    if ykotak3 <= 460 and ykondisi3 == True:
        ykotak3 -= 3
        if ykotak3 <= 40:
            ykondisi3 = False
    glTranslated(xkotak3, ykotak3, 0)
    glBegin(GL_POLYGON)
    glColor3d(255, 0, 0)
    for i in range(sisi):
        theta = 2 * 3.1415926 * i / sisi
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()
    glPopMatrix()


# Pembatas ============================================================================
def tembok():
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 153)
    glVertex2f(0, 0)
    glVertex2f(0, 500)
    glVertex2f(30, 500)
    glVertex2f(30, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 153)
    glVertex2f(0, 500)
    glVertex2f(1000, 500)
    glVertex2f(1000, 470)
    glVertex2f(0, 470)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 153)
    glVertex2f(1000, 500)
    glVertex2f(1000, 0)
    glVertex2f(970, 0)
    glVertex2f(970, 500)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 153)
    glVertex2f(1000, 0)
    glVertex2f(0, 0)
    glVertex2f(0, 30)
    glVertex2f(1000, 30)
    glEnd()


# Main Character ======================================================================
def mainchar():
    global coll, play, lose, win
    if coll == False and play == True and lose == False:
        glPushMatrix()
        glTranslated(xmainchar, ymainchar, 0)

        if xmainchar in range(int(xmonster1) - 45, int(xmonster1) + 50) and ymainchar in range(int(ymonster1) - 75, int(ymonster1) + 45):
            print("kena")
            coll = True
            lose = True
            play = False
        elif xmainchar in range(int(xmonster2) - 45, int(xmonster2) + 50) and ymainchar in range(int(ymonster2) - 75, int(ymonster2) + 45):
            print("kena")
            coll = True
            lose = True
            play = False
        elif xmainchar in range(int(xmonster3) - 45, int(xmonster3) + 50) and ymainchar in range(int(ymonster3) - 75, int(ymonster3) + 45):
            print("kena")
            coll = True
            lose = True
            play = False
        elif xmainchar in range(int(xkotak1)-30, int(xkotak1)+40) and ymainchar in range(int(ykotak1)-40, int(ykotak1)+50):
            print("kena")
            coll = True
            lose = True
            play = False
        elif xmainchar in range(int(xkotak2)-30, int(xkotak2)+40) and ymainchar in range(int(ykotak2)-40, int(ykotak2)+50):
            print("kena")
            coll = True
            lose = True
            play = False
        elif xmainchar in range(int(xkotak3)-30, int(xkotak3)+40) and ymainchar in range(int(ykotak3)-40, int(ykotak3)+50):
            print("kena")
            coll = True
            lose = True
            play = False
        if xmainchar in range(int(xdiamond)-40, int(xdiamond)+50) and ymainchar in range(int(ydiamond)-50, int(ydiamond)+60):
            print("kena")
            win = True
            play = False

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


# Diamond =============================================================================
def diamond():
    glPushMatrix()
    glTranslated(xdiamond, ydiamond, 0)

    glBegin(GL_POLYGON)
    glColor3ub(40, 255, 210)
    glVertex2f(0, -20)
    glVertex2f(-20, 5)
    glVertex2f(-10, 20)
    glVertex2f(10, 20)
    glVertex2f(20, 5)
    glVertex2f(20, 5)
    glEnd()

    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glColor3ub(40, 195, 210)
    glVertex2f(0, -20)
    glVertex2f(-20, 5)
    glVertex2f(-10, 20)
    glVertex2f(10, 20)
    glVertex2f(20, 5)
    glVertex2f(20, 5)
    glEnd()

    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glColor3ub(40, 195, 210)
    glVertex2f(-20, 5)
    glVertex2f(-10, 20)
    glVertex2f(-5, 13)
    glVertex2f(5, 13)
    glVertex2f(10, 20)
    glVertex2f(20, 5)
    glVertex2f(10, 3)
    glVertex2f(5, 13)
    glVertex2f(-5, 13)
    glVertex2f(-10, 3)
    glVertex2f(10, 3)
    glVertex2f(0, -20)
    glVertex2f(-10, 3)
    glEnd()

    glPopMatrix()


# Monster 1 ===========================================================================
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


# Monster 2 ===========================================================================
def monster2():

    glPushMatrix()
    glTranslated(xmonster2, ymonster2, 0)

    # Kepala ====================================================================
    glBegin(GL_QUADS)
    glColor3ub(255, 200, 0)
    glVertex2f(-25, -25)
    glVertex2f(-25, 10)
    glVertex2f(25, 10)
    glVertex2f(25, -25)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(80, 100, 0)
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


# Monster 3 ===========================================================================
def monster3():

    glPushMatrix()
    glTranslated(xmonster3, ymonster3, 0)

    # Kepala ====================================================================
    glBegin(GL_QUADS)
    glColor3ub(255, 200, 0)
    glVertex2f(-25, -25)
    glVertex2f(-25, 10)
    glVertex2f(25, 10)
    glVertex2f(25, -25)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(165, 0, 90)
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
    glColor3ub(0, 0, 153)
    glVertex2d(120, 30)
    glVertex2d(120, 400)
    glVertex2d(180, 400)
    glVertex2d(180, 30)
    glEnd()
    glPopMatrix()


def objek2():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 153)
    glVertex2d(250, 470)
    glVertex2d(250, 100)
    glVertex2d(280, 100)
    glVertex2d(280, 470)
    glEnd()
    glPopMatrix()


def objek3():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 153)
    glVertex2d(350, 30)
    glVertex2d(350, 400)
    glVertex2d(380, 400)
    glVertex2d(380, 30)
    glEnd()
    glPopMatrix()


def objek4():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 153)
    glVertex2d(450, 470)
    glVertex2d(450, 100)
    glVertex2d(500, 100)
    glVertex2d(500, 470)
    glEnd()
    glPopMatrix()


def objek5():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 153)
    glVertex2d(800, 30)
    glVertex2d(800, 400)
    glVertex2d(830, 400)
    glVertex2d(830, 30)
    glEnd()
    glPopMatrix()


def objek6():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 153)
    glVertex2d(880, 470)
    glVertex2d(880, 100)
    glVertex2d(910, 100)
    glVertex2d(910, 470)
    glEnd()
    glPopMatrix()
    

def game_over():
    global play, lose
    if play == False and lose == True:
        glPushMatrix()
        glTranslated(500, 250, 0)
        
        # Kotak Dasar ==============================================================================
        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 255)
        glVertex2f(-300, -150)
        glVertex2f(-300, 150)
        glVertex2f(300, 150)
        glVertex2f(300, -150)
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor3ub(64, 64, 64)
        glVertex2f(-300, 100)
        glVertex2f(-300, 150)
        glVertex2f(300, 150)
        glVertex2f(300, 100)
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor3ub(190, 0, 0)
        glVertex2f(150, 100)
        glVertex2f(200, 150)
        glVertex2f(250, 150)
        glVertex2f(200, 100)
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor3ub(0, 0, 204)
        glVertex2f(200, 100)
        glVertex2f(250, 150)
        glVertex2f(300, 150)
        glVertex2f(250, 100)
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor3ub(190, 0, 0)
        glVertex2f(250, 100)
        glVertex2f(300, 150)
        glVertex2f(300, 100)
        glEnd()
        
        # Tulisan ====================================================================================
        # G
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-160, 45)
        glVertex2f(-185, 45)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-185, 45)
        glVertex2f(-200, 20)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-200, 20)
        glVertex2f(-190, 5)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-190, 5)
        glVertex2f(-165, 5)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-165, 5)
        glVertex2f(-165, 20)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-165, 20)
        glVertex2f(-180, 20)
        glEnd()

        # A
        glLineWidth(10)
        glBegin(GL_LINE_LOOP)
        glColor3d(255, 0, 0)
        glVertex2f(-142, 20)
        glVertex2f(-130, 50)
        glVertex2f(-118, 20)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-150, 0)
        glVertex2f(-142, 20)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-110, 0)
        glVertex2f(-118, 20)
        glEnd()

        # M
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-100, 0)
        glVertex2f(-100, 50)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-100, 50)
        glVertex2f(-80, 25)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-80, 25)
        glVertex2f(-60, 50)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-60, 50)
        glVertex2f(-60, 0)
        glEnd()

        # E
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-40, 0)
        glVertex2f(-40, 50)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-40, 45)
        glVertex2f(-10, 45)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-40, 25)
        glVertex2f(-10, 25)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-40, 5)
        glVertex2f(-10, 5)
        glEnd()

        # O
        glLineWidth(10)
        glBegin(GL_LINE_LOOP)
        glColor3d(255, 0, 0)
        glVertex2f(25, 25)
        glVertex2f(45, 50)
        glVertex2f(65, 25)
        glVertex2f(45, 0)
        glEnd()

        # V
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(70, 50)
        glVertex2f(90, 0)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(90, 0)
        glVertex2f(110, 50)
        glEnd()

        # E
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(120, 0)
        glVertex2f(120, 50)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(120, 45)
        glVertex2f(150, 45)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(120, 25)
        glVertex2f(150, 25)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(120, 5)
        glVertex2f(150, 5)
        glEnd()

        # R
        glLineWidth(8)
        glBegin(GL_LINE_LOOP)
        glColor3d(255, 0, 0)
        glVertex2f(160, 30)
        glVertex2f(160, 45)
        glVertex2f(180, 45)
        glVertex2f(200, 40)
        glVertex2f(180, 30)
        glEnd()
        glLineWidth(8)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(160, 0)
        glVertex2f(160, 30)
        glEnd()
        glLineWidth(8)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(160, 30)
        glVertex2f(200, 0)
        glEnd()

        # Button ==================================================================================
        glBegin(GL_POLYGON)
        glColor3d(255, 0, 0)
        glVertex2f(-100, -50)
        glVertex2f(100, -50)
        glVertex2f(100, -100)
        glVertex2f(-100, -100)
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor3d(255, 255, 255)
        glVertex2f(-20, -90)
        glVertex2f(-20, -60)
        glVertex2f(20, -75)
        glEnd()
        glPopMatrix()


def winner():
    global play, win
    if play == False and win == True:
        glPushMatrix()
        glTranslated(500, 250, 0)
        
        # Kotak Dasar ==============================================================================
        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 255)
        glVertex2f(-300, -150)
        glVertex2f(-300, 150)
        glVertex2f(300, 150)
        glVertex2f(300, -150)
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor3ub(64, 64, 64)
        glVertex2f(-300, 100)
        glVertex2f(-300, 150)
        glVertex2f(300, 150)
        glVertex2f(300, 100)
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor3ub(0, 0, 204)
        glVertex2f(150, 100)
        glVertex2f(200, 150)
        glVertex2f(250, 150)
        glVertex2f(200, 100)
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor3ub(190, 0, 0)
        glVertex2f(200, 100)
        glVertex2f(250, 150)
        glVertex2f(300, 150)
        glVertex2f(250, 100)
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor3ub(0, 0, 204)
        glVertex2f(250, 100)
        glVertex2f(300, 150)
        glVertex2f(300, 100)
        glEnd()
        
        # Tulisan ====================================================================================
        # W
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-130, 0)
        glVertex2f(-130, 40)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-130, 0)
        glVertex2f(-110, 20)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-110, 20)
        glVertex2f(-90, 0)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-90, 0)
        glVertex2f(-90, 40)
        glEnd()

        # I
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-70, 0)
        glVertex2f(-70, 40)
        glEnd()

        # N
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-50, 40)
        glVertex2f(-50, 0)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-50, 0)
        glVertex2f(-10, 40)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(-10, 40)
        glVertex2f(-10, 0)
        glEnd()

        # N
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(10, 0)
        glVertex2f(10, 40)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(10, 40)
        glVertex2f(50, 0)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(50, 0)
        glVertex2f(50, 40)
        glEnd()
        
        # E
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(65, 0)
        glVertex2f(65, 40)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(65, 35)
        glVertex2f(90, 35)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(65, 20)
        glVertex2f(90, 20)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(65, 5)
        glVertex2f(90, 5)
        glEnd()
        
        # R
        glLineWidth(10)
        glBegin(GL_LINE_LOOP)
        glColor3d(255, 0, 0)
        glVertex2f(105, 20)
        glVertex2f(105, 40)
        glVertex2f(125, 35)
        glVertex2f(135, 30)
        glVertex2f(125, 20)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(105, 0)
        glVertex2f(105, 20)
        glEnd()
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3d(255, 0, 0)
        glVertex2f(105, 20)
        glVertex2f(135, 0)
        glEnd()

        # Button ==================================================================================
        glBegin(GL_POLYGON)
        glColor3d(255, 0, 0)
        glVertex2f(-100, -50)
        glVertex2f(100, -50)
        glVertex2f(100, -100)
        glVertex2f(-100, -100)
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor3d(255, 255, 255)
        glVertex2f(-20, -90)
        glVertex2f(-20, -60)
        glVertex2f(20, -75)
        glEnd()
        glPopMatrix()


def myMouse(button, state, x, y):
    global coll, play, lose, win, xmainchar, ymainchar
    if play == False:
        if lose == True or win == True:
            if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
                # print(f"{x}, {y}")
                if ((400 <= x <= 600) and (300 <= y <= 350)):
                    coll = False
                    lose = False
                    win = False
                    play = True
                    xmainchar, ymainchar = 50, 60
                    

def mySpecialKeyboard(key, x, y):
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
        elif xmainchar == 780 and ymainchar < 430:
            xmainchar+=0
        elif xmainchar == 860 and ymainchar > 70:
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
        elif xmainchar == 850 and ymainchar < 430:
            xmainchar -= 0
        elif xmainchar == 930 and ymainchar > 70:
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
        elif ymainchar == 70 and 860 < xmainchar < 930:
            ymainchar+=0
        elif ymainchar == 390 and 900 < xmainchar < 980:
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
        elif ymainchar == 430 and 780 < xmainchar < 850:
            ymainchar-=0
        elif ymainchar <= 60:
            ymainchar-= 0
        else:
            ymainchar-=10
        
    # print(f"{xmainchar}, {ymainchar}")

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
    objek5()
    objek6()
    diamond()
    monster1()
    gerak1()
    monster2()
    gerak2()
    monster3()
    gerak3()
    mainchar()
    kotak1(0, 0, 10, 20)
    kotak2(0, 0, 10, 20)
    kotak3(0, 0, 10, 20)
    game_over()
    winner()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("===>> Maze Runner <<===")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(mySpecialKeyboard)
glutMouseFunc(myMouse)
glutMainLoop()


