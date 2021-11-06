# coding: utf-8

import PIL as plt
import os
import tkinter
import tkinter.filedialog
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

from treelib import Tree, Node

global a
a = []
def FileChoose():
    root = tkinter.Tk()    # 创建一个Tkinter.Tk()实例
    root.withdraw()       # 将Tkinter.Tk()实例隐藏
    default_dir = r"文件路径"
    file_path = tkinter.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
    image = Image.open(file_path)
    
    #plt.imshow(image)
    #plt.show()
    return file_path

def getfilepath(file_path_):
    global img
    img = cv2.imread(file_path_)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    cv2.imshow("image", img)
    cv2.waitKey(0)

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a.append(xy)
        print(xy)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness = -1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0,0,0), thickness = 1)
        cv2.imshow("image", img)
        


if __name__ == "__main__":
    
    tree = Tree()
    path = FileChoose()
    getfilepath(path)
    print(a)
    


