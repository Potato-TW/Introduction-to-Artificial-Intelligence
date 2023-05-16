import cv2
import numpy as np


def cut(arg):
    return [arg[0], arg[1]], [arg[0], arg[1]+arg[2]], [arg[0]+arg[2], arg[1]], [arg[0]+arg[2], arg[1]+arg[2]]

'''
with open("C:\\Users\\user\\Desktop\\Python\\AI_HW1\\data\\detect\\yourOwnImages.txt", 'r') as f:
    text = f.read().split()

img = []
rec = []

tmp = cv2.imread('./data/detect/'+text[0], cv2.IMREAD_GRAYSCALE)
del text[0]
# tmp = cv2.resize(tmp, (19, 19), interpolation=cv2.INTER_AREA)

n = int(text[0])
del text[0]
for i in range(n):
    rr = []
    for j in range(4):
        rr.append(int(text[0]))
        del text[0]
    rec.append(rr)
img.append(tmp)

for i in rec:
    lt, ld, rt, rd = cut(i)
    cv2.rectangle(img[0], lt, rd, [0, 255, 0], 2)

cv2.imshow('r', img[0])
cv2.waitKey(0)
'''

# img=cv2.imread("C:\\Users\\user\\Desktop\\Python\\AI_HW1\\data\\detect\\avadar.jpg", cv2.IMREAD_GRAYSCALE)

dataPath = "C:\\Users\\user\\Desktop\\Python\\AI_HW1\\data\\detect\\detectData.txt"
with open(dataPath, 'r') as f:
    text = f.read().split()

img = []
rec = []

while len(text) > 0:
    tmp = cv2.imread('./data/detect/'+text[0], cv2.IMREAD_GRAYSCALE)
    del text[0]

    n = int(text[0])
    del text[0]
    smallrec=[]
    for i in range(n):
        rr = []
        for j in range(4):
            rr.append(int(text[0]))
            del text[0]
        smallrec.append(rr)
    img.append(tmp)
    rec.append(smallrec)

ans = []
for i in range(len(img)):
    ans.append(cv2.cvtColor(img[i], cv2.COLOR_GRAY2BGR))
    # img[0] = cv2.resize(img[0], (19, 19), interpolation=cv2.INTER_AREA)

    for j in range(len(rec[i])):
        lt, ld, rt, rd = cut(rec[i][j])
        if 1:
            cv2.rectangle(ans[i], lt, rd, (0, 255, 0), 2)
        else:
            cv2.rectangle(ans[i], lt, rd, (0, 0, 255), 2)

for i in ans:
    cv2.imshow('result', i)
    cv2.waitKey(0)

# allimg = []
# for i in ans:
#     allimg.append(i)

# show=np.hstack(allimg)
# cv2.imshow('result', show)
# cv2.waitKey(0)