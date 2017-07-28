import numpy as np
import Braille_DB as BDB
import cv2
import pyttsx

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')
img1 = cv2.imread('image1.png')
img2 = cv2.imread('image2.png')
img1=cv2.flip(img1,1)
# img2=cv2.flip(img2,1)
cv2.imshow('imagen1',img1)
cv2.imshow('imagen2',img2)
diff_total=100
while(1):
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hsv = cv2.GaussianBlur(hsv, (5, 5), 0)
    hsv = cv2.medianBlur(hsv, 5)

    lower_mask = np.array([29, 136, 179])
    upper_mask = np.array([42, 255, 255])

    mask = cv2.inRange(hsv, lower_mask, upper_mask)

    kernel = np.ones((6, 6), np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    blur = cv2.GaussianBlur(res, (5, 5), 0)

    ret, thresh = cv2.threshold(res, 127, 255, 0)

    diff_total1 = cv2.absdiff(blur,img1)
    diff_total2 = cv2.absdiff(blur,img2)

    imagen_gris1 = cv2.cvtColor(diff_total1, cv2.COLOR_BGR2GRAY)
    imagen_gris2 = cv2.cvtColor(diff_total2, cv2.COLOR_BGR2GRAY)
    print  diff_total1.sum()
    if(diff_total1.sum()<3000000):
        pdef = {
            1: BDB.letterb[3],
            2: BDB.letterb[1],
            3: BDB.letterb[19],
            4: BDB.letterb[1]
        }
        break
    print  diff_total2.sum()
    if (diff_total2.sum() < 3000000):
        pdef = {
            1: BDB.letterb[18],
            2: BDB.letterb[15],
            3: BDB.letterb[2],
            4: BDB.letterb[15],
            5: BDB.letterb[20]
        }
        break
    cv2.imshow('blur', blur)
    cv2.imshow('diff1', imagen_gris1)
    cv2.imshow('diff2', imagen_gris2)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        # cv2.imwrite('image2.png', blur)
        break
cap.release()
cv2.destroyAllWindows()

long= pdef.__len__()
p=""
for q in range(1,long+1):
    # data = letterb[np.random.randint(1,27)]
    data=pdef[q]
    print data
    index=0
    print("START")
    for j in range(1,27):
        print('Etapa ',repr(j))
        test=BDB.letterb[j]
        res=test==data
        for k in range(0,6):
            l=True
            if(res.item(k)==False):
                l=False
                break
        if(l):
            index=j
            print test
            break
    p += BDB.letter[index]
    print p
print ("DONE")

engine = pyttsx.init()
engine.setProperty('rate', 100)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

engine.say(p)

engine.runAndWait()