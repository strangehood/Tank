from graph import *
import math
from sys import platform
def Abs(a):
    if a<0:
        return -a
    return a
def GenerateWall():
    global walls, wallCoords,deltaSize
    walls = []
    size = 4
    color = randColor()
    wallCoord = ((0,0),(0+deltaSize,0),(0,0+deltaSize),(0,0+2*deltaSize))
    penColor(color)
    brushColor(color)
    for i in range(size):
        w = rectangle(wallCoord[i][0],wallCoord[i][1],wallCoord[i][0]+deltaSize,wallCoord[i][1]+deltaSize)
        walls.append(w)
def CheckWallCollision(bullet):
    global deltasize
    mark = False
    for w in walls:
        wX = coords(w)[0]+deltaSize/2
        wY = coords(w)[1]+deltaSize/2
        bX = coords(bullet)[0]
        bY = coords(bullet)[1]
        print(wX,wY,bX,bY)
        if (Abs(wX -bX)< deltaSize/2 and Abs(wY-bY)< deltaSize/2):
            moveObjectTo(w,600,600)
            mark = True
    return  mark



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
	if platform == "win32" or platform == "cygwin":
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
			shooting()
		elif event.keycode == VK_ESCAPE:
			close()
	elif platform == "linux":
		if event.keycode == VK_INSERT:  # Q
			gun_draw(angle + 5)
		elif event.keycode == VK_DELETE:  # E
			gun_draw(angle - 5)
		elif event.keycode == VK_UP:  # W
			dy = -5
		elif event.keycode ==  VK_DOWN:  # S
			dy = 5
		elif event.keycode == VK_LEFT:  # A
			dx = -5
		elif event.keycode == VK_RIGHT:  # D
			dx = 5
		elif (event.keycode == VK_SPACE) and (bulletbool is True):
			shooting()
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
	global bulletbool
	bulletbool=True

def shooting():
    global bulletbool, bulletFlybool
    moveObjectTo(bullet, x0, y0)
    bulletbool = False
    bulletFlybool=True

def bulletFly():
    global bulletbool, bulletFlybool, t, bullet

    if CheckWallCollision(bullet)==True:
        bulletFlybool = False
    if bulletFlybool==True:
        aRad = angle * math.pi / 180
        moveObjectBy(bullet, int( L * math.cos(aRad))//10, - int(L * math.sin(aRad))//10)
        t=t+1
    if t>100:
        t=0
        bulletFlybool=False
        moveObjectTo(bullet, -5, -5)

global walls, wallCoords,deltaSize
deltaSize = 50
GenerateWall()

windowSize(400, 400)
canvasSize(400, 400)
gun = None
t=0 # время полета пули
penColor('green')
brushColor('green')
hull = rectangle(110, 110, 170, 170)
bulletbool = False
bulletFlybool=False
x1 = 100
y1 = 100
x0 = 140
y0 = 140
penColor('red')
brushColor('red')
bullet = circle(-5, -5, 3)
dx = dy = 1
penSize(9)
L = math.sqrt((x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0))
gun_draw(0)
onKey(keyPressed)
onTimer(shooting_check, 1000)
onTimer(movement, 50)
onTimer(bulletFly, 10)
run()

