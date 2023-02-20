# 1 导入库
import cv2
import dlib
import numpy as np
import matplotlib.pyplot as plt

# 2 方法：显示图片
def show_image(image, title):
    img_RGB = image[:, :, ::-1] # BGR to RGB
    plt.title(title)
    plt.imshow(img_RGB)
    plt.axis("off")

# 3 方法：绘制人脸矩形框
def plot_rectangle(image, faces):
    for face in faces:
        cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (255,0,0), 4)
    return image

def main():
    # 4 读取一张图片
    img = cv2.imread("family.jpg")

    # 5 灰度转换
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 6 调用dlib库中的检测器
    detector = dlib.get_frontal_face_detector()
    dets_result = detector(gray, 1) # 1 ：代表将图片放大一倍
    # 7 给检测出的人脸绘制矩形框
    img_result = plot_rectangle(img.copy(), dets_result)

    # 8 创建画布
    plt.figure(figsize=(9, 6))
    plt.suptitle("face detection with dlib", fontsize=14, fontweight="bold")

    # 9 显示最终的检测效果
    show_image(img_result, "face detection")

    plt.show()

if __name__ == '__main__':
    main()