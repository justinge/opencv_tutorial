# 1.导入库
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 方法：显示图片
def show_image(image,title,pos):
    # 顺序转换：BGR TO RGB
    img_RGB = image[:,::-1] # shape : (height, width, channel)
    # 显示标题
    plt.title(title)
    plt.subplot(2,3,pos) # 定位
    plt.imshow(img_RGB)


# 3 方法：显示
def show_histogram(hist, title, pos, color):
    plt.title(title) # 显示标题
    plt.subplot(2,3,pos) # 定位图片
    plt.xlabel("Bins") # 横轴信息
    plt.ylabel("Pixels") # 纵轴信息
    plt.xlim([0,256]) # 范围
    plt.plot(hist, color=color) # 绘制直方图

# 4 主函数 main()
def main():
    # 5. 创建画布
    # 画布大小
    plt.figure(figsize=(15,6)) 
    # 设置标题形式
    plt.suptitle("Gray Image Histogram", fontsize=14, fontweight="bold")
    # 6 加载图片
    img = cv2.imread("../images/children.jpg")
    # 7 灰度转换
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # 8 计算灰度图的直方图
    hist_img = cv2.calcHist([img_gray],[0],None,[256],[0, 256])
    # 9 展示灰度直方图
    # 灰度图转换成BGR格式图片
    img_BGR = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    show_image(img_BGR, "BGR image", 1)
    show_histogram(hist_img, "gray image histogram", 4, "m")
    plt.show()

if __name__ == '__main__':
    main()