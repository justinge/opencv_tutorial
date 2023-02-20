# 1 加入库
import cv2
import dlib

# 增加功能二：信息提示
def show_info(frame, tracking_state):
    pos1 = (20, 40)
    pos2 = (20, 80)
    cv2.putText(frame, "'1' : reset ", pos1, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
    # 根据状态，显示不同的信息
    if tracking_state is True:
        cv2.putText(frame, "tracking now ...", pos2, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
    else:
        cv2.putText(frame, "no tracking ...", pos2, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))

# 2 主函数
def main():
    # 3 打开摄像头
    capture = cv2.VideoCapture(0)

    # 4 基于dlib库获取人脸检测器
    detector = dlib.get_frontal_face_detector()

    # 5 基于dlib库实时跟踪
    tractor = dlib.correlation_tracker()

    # 6 跟踪状态
    tracking_state = False

    # 增加功能一：保存视频
    frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    frame_fps = capture.get(cv2.CAP_PROP_FPS)
    # 设置视频格式
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # 设置输出格式
    output = cv2.VideoWriter("record.avi", fourcc, int(frame_fps), (int(frame_width), int(frame_height)), True)

    # 7 循环读取每一帧
    while True:
        ret, frame = capture.read()

        # 显示提示信息
        show_info(frame, tracking_state)

        # 8 如果没有跟踪， 启动跟踪器
        if tracking_state is False:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            dets = detector(gray, 1) # 返回检测到的人脸
            if len(dets) > 0:
                tractor.start_track(frame, dets[0])
                tracking_state = True

        # 9 正在跟踪，实时获取人脸的位置，显示
        if tracking_state is True:
            tractor.update(frame) # 跟新画面
            position = tractor.get_position() # 获取人脸的坐标
            cv2.rectangle(frame,(int(position.left()), int(position.top())), (int(position.right()), int(position.bottom())), (0,255,0), 3)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

        if key == ord('1'):
            tracking_state = False

        cv2.imshow("face tracking", frame)
        # 保存视频
        output.write(frame)

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()