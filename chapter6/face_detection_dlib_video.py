# 1 导入库
import cv2
import dlib

# 2 方法：绘制人脸矩形框
def plot_rectangle(image, faces):
    for face in faces:
        cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (255,0,0), 4)
    return image

def main():
    # 3 打开摄像头，读取视频
    capture = cv2.VideoCapture(0)
    # 4 判断摄像头是否正常工作
    if capture.isOpened() is False:
        print("Camera Error !")
    # 5 摄像头正常打开：循环读取每一帧
    while True:
        ret, frame = capture.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # BGR to GRAY

            # 6 调用dlib库中的检测器
            detector = dlib.get_frontal_face_detector()
            det_result = detector(gray, 1)
            # 7 绘制检测结果
            dets_image = plot_rectangle(frame, det_result)

            # 8 实时显示最终的检测效果
            cv2.imshow("face detection with dlib", dets_image)

            # 9 按键"ESC"，退出，关闭摄像头
            if cv2.waitKey(1) == 27:
                break

    # 10 释放所有的资源
    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()