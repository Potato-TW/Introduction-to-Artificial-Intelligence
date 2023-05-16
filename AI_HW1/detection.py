import os
import cv2
import matplotlib.pyplot as plt
import numpy as np


def cut(arg):
    return [arg[0], arg[1]], [arg[0], arg[1] + arg[2]], [arg[0] + arg[2], arg[1]], [arg[0] + arg[2], arg[1] + arg[2]]


def detect(dataPath, clf):
    """
    Please read detectData.txt to understand the format. Load the image and get
    the face images. Transfer the face images to 19 x 19 and grayscale images.
    Use clf.classify() function to detect faces. Show face detection results.
    If the result is True, draw the green box on the image. Otherwise, draw
    the red box on the image.
      Parameters:
        dataPath: the path of detectData.txt
      Returns:
        No returns.
    """
    # Begin your code (Part 4)
    '''
    First, read the file in "dataPath", analyze the text. We knew it said file's name, the number of rectangles, left-top 
    coordinate of rectangle, its width, and its height.

    Utilize "cv2.imread" to get numpy array of pictures, and turn them into gray scale. 
    Meanwhile, I also saved non-gray-scaled pictures, that is colorful, inorder to show out red and green rectangles later.

    Then I defined function "cut()" to locate rectangles' four vertices that helped me calling function "cv2.resize()".
    
    After I knew where the rectangles were, I resized them in 19*19, then called function "clf.classify()" with numpy array
    of 19*19 pictures as parameter. If the function returned true, paint rectangles green in colorful pictures on the rim 
    meaning it was a face. On the other hand, if it returned false, paint them red meaning it was not a face.
    '''
    with open(dataPath, 'r') as f:
        text = f.read().split()

    img = []
    rec = []
    ans = []

    while len(text) > 0:
        tmp = cv2.imread('./data/detect/' + text[0], cv2.IMREAD_GRAYSCALE)
        ans.append(cv2.imread('./data/detect/' + text[0], cv2.IMREAD_COLOR))
        del text[0]

        n = int(text[0])
        del text[0]
        smallrec = []
        for i in range(n):
            rr = []
            for j in range(4):
                rr.append(int(text[0]))
                del text[0]
            smallrec.append(rr)
        img.append(tmp)
        rec.append(smallrec)

    for i in range(len(img)):
        for j in range(len(rec[i])):
            lt, ld, rt, rd = cut(rec[i][j])
            resizedimg = cv2.resize(
                img[i][lt[1]: ld[1], lt[0]: rt[0]], (19, 19), interpolation = cv2.INTER_AREA)
            if clf.classify(resizedimg) == 1:
                cv2.rectangle(ans[i], lt, rd, (0, 255, 0), 2)
            else:
                cv2.rectangle(ans[i], lt, rd, (0, 0, 255), 2)

    for i in ans:
        cv2.imshow('result', i)
        cv2.waitKey(0)

    # raise NotImplementedError("To be implemented")
    # End your code (Part 4)
