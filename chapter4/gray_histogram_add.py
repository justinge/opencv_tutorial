# 1 导入库
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 2 方法：显示图片
def show_image(image, title, pos):
    #  顺序转换：BGR TO RGB
    image_RGB = image[:, :, ::-1] # shape : (height, width, channel)
    # 显示标题
    plt.title(title)
    plt.subplot(2, 3, pos) # 定位
    plt.imshow(image_RGB)

# 3 方法：显示图片的灰度直方图
def show_histogram(hist, title, pos, color):
    # 显示标题
    plt.title(title)
    plt.subplot(2, 3, pos) # 定位图片
    plt.xlabel("Bins") # 横轴信息
    plt.ylabel("Pixels") # 纵轴信息
    plt.xlim([0, 256]) # 范围
    plt.plot(hist, color=color) # 绘制直方图

# 4 主函数 main()
def main():
    # 5 创建画布
    plt.figure(figsize=(15, 6)) # 画布大小
    plt.suptitle("Gray Image Histogram", fontsize=14, fontweight="bold") # 设置标题形式

    # 6 加载图片
    img = cv2.imread("../images/children.jpg")

    # 7 灰度转换
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 8 计算灰度图的直方图
    hist_img = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

    # 9 展示灰度直方图
    # 灰度图转换成BGR格式图片
    img_BGR = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    show_image(img_BGR, "BGR image", 1)
    show_histogram(hist_img, "gray image histogram", 4, "m")

    # 10 对图片中的每个像素值增加50个像素
    M = np.ones(img_gray.shape, np.uint8) * 50 # 构建矩阵

    added_img = cv2.add(img_gray, M)
    add_img_hist = cv2.calcHist([added_img], [0], None, [256], [0, 256]) # 计算直方图
    added_img_BGR = cv2.cvtColor(added_img, cv2.COLOR_GRAY2BGR)
    show_image(added_img_BGR, "added image", 2)
    show_histogram(add_img_hist, "added image hist", 5, "m")

    # 11 对图片中的每个像素值减去50个像素
    subtract_img = cv2.subtract(img_gray, M)
    subtract_img_hist = cv2.calcHist([subtract_img], [0], None, [256], [0, 256]) # 计算直方图
    subtract_img_BGR = cv2.cvtColor(subtract_img, cv2.COLOR_GRAY2BGR)
    show_image(subtract_img_BGR, "subtracted image", 3)
    show_histogram(subtract_img_hist, "subtracted image hist", 6, "m")

    plt.show()


if __name__ == '__main__':
    main()