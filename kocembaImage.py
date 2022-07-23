import kociemba
import cv2
from graphics import *
from pynput import mouse
from pynput.mouse import Button
import time
import math

color = []
speed = 2000 #less no more speed
wtc = 1
coordinateMap=[(195,198),(278,198),(362,198),(195,282),(278,282),(362,282),(195,365),(278,365),(362,365)]


def calibrateColors(facee,name):
    temp =[0,0,0]
    cnt =0
    for i in range(198,282):
        for j in range(278,362):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b5=temp
    color.append(b5)
    print(name+" : "+str(b5))
    cv2.putText(facee,name,(280,275),cv2.FONT_HERSHEY_COMPLEX,0.6,(0))
    cv2.imshow(name,facee)
    cv2.waitKey(100)

face = -1

def getcnt():
    return face

def setcnt(a):
    global face
    face =a

def on_move(x, y):
    pass

test_cnt =-1
def on_click(x, y, button, pressed):
    cnt = getcnt()
    if cnt ==-1 and button== Button.right:
        cnt=0
    elif cnt == 0 and button==Button.right:
        cnt =1
    elif cnt == 1 and button==Button.right:
        cnt =2
    elif cnt == 2 and  button==Button.right:
        cnt =3
    elif cnt == 3 and  button==Button.right:
        cnt =4
    elif cnt == 4 and  button==Button.right:
        cnt =5
    elif cnt == 5 and  button==Button.right:
        cnt =6
    elif cnt == 6 and  button==Button.right:
        cnt =7
    else:
        pass
    global test_cnt
    if cnt ==7 and button==Button.right and test_cnt<4:
        test_cnt+=1
    if test_cnt ==4:
        pass
    if cnt<7 and button==Button.right:
        print(cnt)
    elif cnt>=7 and button==Button.right:
        print(test_cnt)
    
    setcnt(cnt)
    time.sleep(1)

def on_scroll(x, y, dx, dy):
    pass

def getcamera():
    win = GraphWin("Select Camera",500,250)
    win.setBackground(color_rgb(255,255,255))
    info = Text(Point(250,20),"press 0 for laptop camera")
    info1 = Text(Point(250, 80), "press 1 for usb or wifi connected camera")
    info2 = Text(Point(250, 140), "or enter ip address of camera manually")
    info.draw(win)
    info1.draw(win)
    info2.draw(win)

    responseBox = Entry(Point(250,200),25)
    responseBox.draw(win)

    win.getMouse()
    response = responseBox.getText()
    win.close()

    if(response=='0' or response=='1'):
        return int(response)
    return response



listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()


def calculateColor(c):
    colorList = ["White", "Orange","Green","Red","Blue","Yellow"]
    colorDist = [1000,1000,1000,1000,1000,1000]
    for i in range(6):
        temp =0
        for j in range(3):
            temp+=pow(abs(color[i][j]-c[j]),2)
        colorDist[i] = pow(temp,0.5)

    minn = 1000
    minI = -1
    for i in range(6):
        if colorDist[i]<minn:
            minn = colorDist[i]
            minI = i
    return colorList[minI][0]



def findColors(facee,name):
    temp =[0,0,0]
    cnt =0
    for i in range(115,198):
        for j in range(195,278):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b1=temp
    # print(b1)
    temp =[0,0,0]
    cnt =0
    for i in range(115,198):
        for j in range(278,362):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b2=temp
    # print(b2)
    temp =[0,0,0]
    cnt =0
    for i in range(115,198):
        for j in range(362,445):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b3=temp
    # print(b3)
    temp =[0,0,0]
    cnt =0
    for i in range(198,282):
        for j in range(195,278):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b4=temp
    # print(b4)
    temp =[0,0,0]
    cnt =0
    for i in range(198,282):
        for j in range(278,362):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b5=temp
    # print(b5)
    temp =[0,0,0]
    cnt =0
    for i in range(198,282):
        for j in range(362,445):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b6=temp
    # print(b6)
    temp =[0,0,0]
    cnt =0
    for i in range(282,365):
        for j in range(195,278):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b7=temp
    # print(b7)
    temp =[0,0,0]
    cnt =0
    for i in range(282,365):
        for j in range(278,362):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b8=temp
    # print(b8)
    temp =[0,0,0]
    cnt =0
    for i in range(282,365):
        for j in range(362,445):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b9=temp
    # print(b9)
    ColorCode = calculateColor(b1)+calculateColor(b2)+calculateColor(b3)+calculateColor(b4)+calculateColor(b5)+calculateColor(b6)+calculateColor(b7)+calculateColor(b8)+calculateColor(b9)
    print(ColorCode)
    if wtc ==1:
        for i in range(9):
            cv2.putText(facee,ColorCode[i],coordinateMap[i],cv2.FONT_HERSHEY_PLAIN,2,(0))
        cv2.imshow("check "+name,facee)
        cv2.waitKey(1000)
        if int(input("is it correct(0 or 1) : "))==0:
            ColorCode = input("enter color code manually : ")
        cv2.destroyAllWindows()
    return ColorCode


cap = cv2.VideoCapture(getcamera())
cnt =0
white,orange,green,red,blue,yellow = None,None,None,None,None,None
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,480))

    cv2.line(frame,(195,115),(445,115),(0))
    cv2.line(frame,(195,115),(195,365),(0))
    cv2.line(frame,(445,115),(445,365),(0))
    cv2.line(frame,(195,365),(445,365),(0))
    cv2.line(frame,(278,115),(278,365),(0))
    cv2.line(frame,(362,115),(362,365),(0))
    cv2.line(frame,(195,198),(445,198),(0))
    cv2.line(frame,(195,282),(445,282),(0))

    
    if(face == 0):
        cv2.putText(frame,"right click , when focused on white face",(20,20),cv2.FONT_HERSHEY_PLAIN,1.5,(0))
    if( face ==1 ):
        if cnt ==0:
            white = frame
            cnt =1
        cv2.putText(frame,"right click , when focused on orange face",(20,20),cv2.FONT_HERSHEY_PLAIN,1.5,(0))
    elif face ==2:
        if cnt ==1:
            orange = frame
            cnt =2
        cv2.putText(frame,"click , when focused on green face",(20,20),cv2.FONT_HERSHEY_PLAIN,1.5,(0))
    elif face == 3:
        if cnt == 2:
            green = frame
            cnt =3
        cv2.putText(frame,"click , when focused on red face",(20,20),cv2.FONT_HERSHEY_PLAIN,1.5,(0))
    elif face ==4:
        if cnt ==3:
            red = frame
            cnt =4
        cv2.putText(frame,"click , when focused on blue face",(20,20),cv2.FONT_HERSHEY_PLAIN,1.5,(0))
    elif face ==5:
        if cnt ==4:
            blue = frame
            cnt =5
        cv2.putText(frame,"click , when focused on yellow face",(20,20),cv2.FONT_HERSHEY_PLAIN,1.5,(0))
    elif cnt ==5 and face ==6:
        cnt =6
        yellow= frame
        
    if face == 7:
        break

    cv2.imshow('live',frame)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
    # frame=cv2.flip(frame,1)


calibrateColors(white,"white")
calibrateColors(orange,"orange")
calibrateColors(green,"green")
calibrateColors(red,"red")
calibrateColors(blue,"blue")
calibrateColors(yellow,"yellow")

cv2.waitKey(10)
cv2.destroyAllWindows()

colorCode = findColors(white,"white")+findColors(red,"red")+findColors(green,"green")+findColors(yellow,"yellow")+findColors(orange,"orange")+findColors(blue,"blue")

listener.stop()
directionCode = colorCode.replace('W','U')
directionCode = directionCode.replace('G','F')
directionCode = directionCode.replace('O','L')
directionCode = directionCode.replace('Y','D')

algo = kociemba.solve(directionCode)
algo = algo.replace('\'','i')
print("algo is : "+algo)
algo = algo.split()

direct = 'images/'


print("place your cube in position")
time.sleep(5)
for step in algo:
    photo = cv2.imread(direct+step+'.png')
    cv2.imshow("step",photo)
    cv2.waitKey(speed)
cv2.destroyAllWindows()

print("yay!!!")
input()
#UP RIGHT FRONT DOWN LEFT BACK
#white = U
#green = F
#red = R
#orange = L
#blue = B
#yellow = D
