import os
import cv2


def input(dataset, curpath, flag):
    filelist = os.listdir(curpath)

    for file in filelist:
        img = cv2.imread(curpath + '/' + file, -1)
        dataset.append((img, flag))


def loadImages(dataPath):
    """
    load all Images in the folder and transfer a list of tuples. The first
    element is the numpy array of shape (m, n) representing the image.
    The second element is its classification (1 or 0)
      Parameters:
        dataPath: The folder path.
      Returns:
        dataset: The list of tuples.
    """
    # Begin your code (Part 1)
    '''
    Since variable "dataPath" couldn't reach pictures, I extended the folder path with "/face" and "/non-face" to 
    arrive at the destination that pictures stayed.

    And, I utilized my function "input()" to read pictures with instruction "cv2.imread()" in package cv2.
    Form a numpy array of a picture and its label as a small list, and append different small lists into big list "dataset"
    
    Meanwhile, I labeled the pictures "1" when they came from folder "face", and "0" when they came from folder "non-face".
    
    Function code "input()" shows in the next screenshot.
    '''

    dataset = []

    curpath = dataPath + '/' + 'face'
    input(dataset, curpath, 1)

    curpath = dataPath + '/' + 'non-face'
    input(dataset, curpath, 0)

    # raise NotImplementedError("To be implemented")

    # End your code (Part 1)
    return dataset
