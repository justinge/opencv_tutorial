# 1 加入库
import face_recognition
import cv2
import matplotlib.pyplot as plt

# 2 方法：显示图片
def show_image(image, title):
    plt.title(title)
    plt.imshow(image)
    plt.axis("off")

# 3 方法：绘制Landmars关键点
def show_landmarks(image, landmarks):
    for landmarks_dict in landmarks:
        for landmarks_key in landmarks_dict.keys():
            for point in landmarks_dict[landmarks_key]:
                cv2.circle(image, point, 2, (0,0,255), -1)
    return image
# 4 主函数
def main():
    # 5 读取图片
    image = cv2.imread("Tom.jpeg")
    # 6 图片灰度转换
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 7 调用face_recognition库中的方法：face_landmarks()
    face_marks = face_recognition.face_landmarks(gray, None, "large")
    print(face_marks)
    # 8 绘制关键点
    img_result = show_landmarks(image.copy(), face_marks)
    # 9 创建画布
    plt.figure(figsize=(9,6))
    plt.suptitle("Face Landmarks with face_recognition", fontsize=14, fontweight="bold")
    # 10 显示整体效果
    show_image(img_result, "landmarks")

    plt.show()

if __name__ == '__main__':
    main()