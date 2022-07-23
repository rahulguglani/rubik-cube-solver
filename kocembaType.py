import kociemba
import cv2
import time

def showAlgo(algo):
    direct = 'images/'
    print("place your cube in position")
    time.sleep(5)
    for step in algo:
        photo = cv2.imread(direct+step+'.png')
        cv2.imshow("step",photo)
        cv2.waitKey(speed)
    cv2.destroyAllWindows()
    print("yay!!!")



up = input("enter up face (white) : ")
front = input("enter front face (green) : ")
left = input("enter left face (orange) : ")
right = input("enter right face (red) : ")
back = input("enter back face (blue) : ")
down = input("enter down face (yellow) : ")


speed = 1500
colorCode = up+ right + front + down + left + back
colorCode = colorCode.upper()
directionCode = colorCode.replace('W','U')
directionCode = directionCode.replace('G','F')
directionCode = directionCode.replace('O','L')
directionCode = directionCode.replace('Y','D')

algo = kociemba.solve(directionCode)
algo = algo.replace('\'','i')
print("algo is : "+algo)
algo = algo.split()

showAlgo(algo)

cmd = input()
while cmd !='exit':
    if cmd == 'again':
        showAlgo(algo)
    cmd = input()

#UP RIGHT FRONT DOWN LEFT BACK
#white = U
#green = F
#red = R
#orange = L
#blue = B
#yellow = D
