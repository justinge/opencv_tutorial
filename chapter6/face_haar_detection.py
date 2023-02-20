# 1.导入库
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 2.方法：显示图片
def show_image(image,title,pos):
    #BRG to RGB
    img_RGB = image[:,:,::-1]
    plt.subplot(2,2,pos)
    plt.title(title)
    plt.imshow(img_RGB)
    plt.axis("off")

# 3 方法：绘制图片中检测到的人脸
def plot_rectangle(image, faces):
    # 拿到检测到的人脸数据，返回4个值：坐标(x,y), 宽高width, height
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 3)
    return image

# 4 主函数
def main():
    # 5 读取一张图片
    image = cv2.imread("../images/family.jpg")
    # 6 转成灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # 7 通过OpenCV自带的方法cv2.CascadeClassifier()加载级联分类器
    face_alt2 = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

    # 8 通过第7步，对图像中的人脸进行检测
    face_alt2_detect = face_alt2.detectMultiScale(gray)

    # 9 绘制图片中检测到的人脸
    face_alt2_result = plot_rectangle(image.copy(), face_alt2_detect)

    # 10 创建画布
    plt.figure(figsize=(9, 6))
    plt.suptitle("Face detection with Haar Cascade", fontsize=14, fontweight="bold")

    # 11 最终显示整个检测效果
    show_image(face_alt2_result, "face_alt2", 1)

    plt.show()

# 12 主程序入口
if __name__ == '__main__':
    main()