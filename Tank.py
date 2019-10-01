from graph import *
import math


def gun_draw(new_angle):
    global tower, L, angle, gun, x1, y1, x0, y0
    angle = new_angle
    penColor('black')
    aRad = angle * math.pi / 180
    x1 = x0 + L * math.cos(aRad)
    y1 = y0 - L * math.sin(aRad)
    if gun == None:
        gun = line(x0, y0, x1, y1)
        penColor('grey')
        brushColor('grey')
        tower = circle(140, 140, 16)
    else:
        changeCoords(gun, [(x0, y0), (x1, y1)])


def movement():
    global hull, gun, tower, angle, dx, dy, x1, x0, y1, y0
    if (wall_check(1) is True) or (wall_check(2) is True):
        dx = 0
    elif (wall_check(3) is True) or (wall_check(4) is True):
        dy = 0
    x0 += dx
    x1 += dx
    y0 += dy
    y1 += dy
    moveObjectBy(hull, dx, dy)
    gun_draw(angle)
    moveObjectBy(tower, dx, dy)
    dx = dy = 0


def keyPressed(event):
    global dx, dy, bulletbool
    if event.keycode == 0x51:  # Q
        gun_draw(angle + 5)
    elif event.keycode == 0x45:  # E
        gun_draw(angle - 5)
    elif event.keycode == 0x57:  # W
        dy = -5
    elif event.keycode == 0x53:  # S
        dy = 5
    elif event.keycode == 0x41:  # A
        dx = -5
    elif event.keycode == 0x44:  # D
        dx = 5
    elif (event.keycode == VK_SPACE) and (bulletbool is True):
        pass
    elif event.keycode == VK_ESCAPE:
        close()


def wall_check(side_number):  # 1 - left ; 2 - right; 3 - up; 4 - down;
    wall_bool = False
    if (x0 < 35) and (dx < 0) and (side_number == 1):
        wall_bool = True
    elif (x0 > 365) and (dx > 0) and (side_number == 2):
        wall_bool = True
    elif (y0 < 35) and (dy < 0) and (side_number == 3):
        wall_bool = True
    elif (y0 > 365) and (dy > 0) and (side_number == 4):
        wall_bool = True
    return wall_bool


def shooting_check():
    bullet_bool = True
    return bullet_bool


def shooting():
    global  bulletbool
    moveObjectTo(bullet, x0, y0)
    bulletbool = False


windowSize(400, 400)
canvasSize(400, 400)
gun = None

penColor('green')
brushColor('green')
hull = rectangle(110, 110, 170, 170)
bulletbool = True
x1 = 100
y1 = 100
x0 = 140
y0 = 140
penColor('red')
brushColor('red')
bullet = circle(-5, -5, 3)
dx = dy = 1
penSize(7)
L = math.sqrt((x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0))
gun_draw(0)
onKey(keyPressed)
onTimer(shooting_check, 1000)
onTimer(movement, 50)
run()
