# 1 加入库
import cv2
import dlib

# 定义方法：显示信息
def show_info(frame, tracking_state):
    pos1 = (10, 20)
    pos2 = (10, 40)
    pos3 = (10, 60)

    info1 = "put left button, select an area, starct tracking"
    info2 = " '1' : starct tracking ,  '2' : stop tacking , 'q' : exit "
    cv2.putText(frame, info1, pos1, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
    cv2.putText(frame, info2, pos2, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
    if tracking_state:
        cv2.putText(frame, "tracking now ...", pos3, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
    else:
        cv2.putText(frame, "stop tracking ...", pos3, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0))

# 存放鼠标事件的坐标点
points = []

# 定义方法：鼠标点击的事件
def mouse_event_handler(event, x, y, flags, parms):
    global points # 全局调用
    if event == cv2.EVENT_LBUTTONDOWN: # 鼠标左键按下
        points = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP: #  鼠标左键松开
        points.append((x,y))

# 2 打开摄像头
capture = cv2.VideoCapture(0)

# 3 设定窗口名称
nameWindow = "Ojbect Tracking"

# 4 将鼠标事件绑定到窗口上去
cv2.namedWindow(nameWindow)
cv2.setMouseCallback(nameWindow, mouse_event_handler)

# 5 启动跟踪器 dlib.correlation_tracker()
tracker = dlib.correlation_tracker()

# 6 假设跟踪状态
tracking_state = False

# 7 循环读取视频流
while True:
    # 8 获取每一帧
    ret, frame = capture.read()
    # 9 显示提示信息：调用方法
    show_info(frame, tracking_state)
    # 10 如果获取到的坐标点为2个，那么就绘制出矩形框，以及也要让dlib的rectangle()知道坐标点在哪里
    if len(points) == 2 :
        cv2.rectangle(frame, points[0], points[1], (0,255,0), 3) # points[0] : (x,y), points[1] : (x,y)
        dlib_rect = dlib.rectangle(points[0][0], points[0][1], points[1][0], points[1][1])
    # 11 判断：如果跟踪状态为True, 那么，更新跟踪，获取位置，绘制矩形框
    if tracking_state is True:
        tracker.update(frame) # 更新画面
        pos = tracker.get_position() # 获取位置的坐标
        cv2.rectangle(frame, (int(pos.left()),int(pos.top())), (int(pos.right()), int(pos.bottom())), (255, 0, 0), 3)

    # 12 事件判断，根据按键：'1', '2', 'q'
    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        if len(points) == 2:
            tracker.start_track(frame, dlib_rect)
            tracking_state = True
            points = []

    if key == ord('2'):
        points = []
        tracking_state = False

    if key == ord('q'):
        break

    # 13 显示整体效果
    cv2.imshow(nameWindow, frame)

capture.release()
cv2.destroyAllWindows()


