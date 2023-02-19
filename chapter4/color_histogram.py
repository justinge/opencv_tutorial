# 1 导入库
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 2 方法：显示图片
def show_image(image, title, pos):
    plt.subplot(3, 2, pos)
    plt.title(title)
    image_RGB = image[:, :, ::-1] # BGR to RGB
    plt.imshow(image_RGB)
    plt.axis("off")

# 3 方法：显示彩色直方图 b, g, r
def show_histogram(hist, title, pos, color):
    plt.subplot(3, 2, pos)
    plt.title(title)
    plt.xlim([0, 256])
    for h, c in zip(hist, color): # color: ('b', 'g', 'r')
        plt.plot(h, color=c)


# 4 方法：计算直方图
def calc_color_hist(image):
    # b, g, r
    hist = []
    hist.append( cv2.calcHist([image], [0], None, [256], [0, 256]))
    hist.append( cv2.calcHist([image], [1], None, [256], [0, 256]))
    hist.append( cv2.calcHist([image], [2], None, [256], [0, 256]))
    return hist

# 5 主函数
def main():
    # 5.1 创建画布
    plt.figure(figsize=(12, 8))
    plt.suptitle("Color Histogram", fontsize=4, fontweight="bold")

    # 5.2 读取原图片
    img = cv2.imread("../images/children.jpg")

    # 5.3 计算直方图
    img_hist = calc_color_hist(img)

    # 5.4 显示图片和直方图
    show_image(img, "RGB Image", 1)
    show_histogram(img_hist, "RGB Image Hist", 2, ('b', 'g', 'r'))

    # 5.5 原始图片中的每个像素增加50个像素值
    M = np.ones(img.shape, dtype="uint8") * 50

    added_image = cv2.add(img, M) # 像素一一对应相加
    added_image_hist = calc_color_hist(added_image)
    show_image(added_image, 'added image', 3)
    show_histogram(added_image_hist, 'added image hist', 4, ('b', 'g', 'r'))


    # 5.6 原始图片中的每个像素减去50个像素值
    subtracted_image = cv2.subtract(img, M)
    subtracted_image_hist = calc_color_hist(subtracted_image)
    show_image(subtracted_image, 'subtracted image', 5)
    show_histogram(subtracted_image_hist, 'subtracted image hist', 6, ('b', 'g', 'r'))

    plt.show()
if __name__ == '__main__':
    main()