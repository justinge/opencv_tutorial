# 1 导入库
import cv2
import matplotlib.pyplot as plt
import numpy as np


# 2 方法：显示图片
def show_image(image, title, pos):
    img_RGB = image[:, :, ::-1] # BGR to RGB
    plt.title(title)
    plt.subplot(2, 2, pos)
    plt.imshow(img_RGB)

# 3 方法：显示灰度直方图
def show_histogram(hist, title, pos, color):
    plt.subplot(2, 2, pos)
    plt.title(title)
    plt.xlim([0, 256])
    plt.plot(hist, color=color)

# 4 主函数
def main():
    # 5 创建画布
    plt.figure(figsize=(12, 7))
    plt.suptitle("Gray Image and Histogram with mask", fontsize=4, fontweight="bold")

    # 6 读取图片并灰度转换，计算直方图，显示
    img_gray = cv2.imread("../images/children.jpg", cv2.COLOR_BGR2GRAY) # 读取并进行灰度转换
    img_gray_hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256]) # 计算直方图
    show_image(img_gray, "image gray", 1)
    show_histogram(img_gray_hist, "image gray histogram", 2, "m")

    # 7 创建mask，计算位图，直方图
    mask = np.zeros(img_gray.shape[:2], np.uint8)
    mask[130:500, 600:1400] = 255 # 获取mask，并赋予颜色
    img_mask_hist = cv2.calcHist([img_gray], [0], mask, [256], [0, 256]) # 计算mask的直方图

    # 8 通过位运算（与预算）计算带有mask的灰度图片
    mask_img = cv2.bitwise_and(img_gray, img_gray, mask = mask)

    # 9 显示带有mask的图片和直方图
    show_image(mask_img, "gray image with mask", 3)
    show_histogram(img_mask_hist, "histogram with masked gray image", 4, "m")

    plt.show()
if __name__ == '__main__':
    main()