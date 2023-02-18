# 从摄像头读取
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("index_camera",help="the camera ID", type=int)
args = parser.parse_args()
# 视频捕获
##
##capture = cv2.VideoCapture(args.index_camera)
## [ WARN:0@2.521] global D:\a\opencv-python\opencv-python\opencv\modules\videoio\src\cap_msmf.cpp (539) `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback
##
# 方法二：（仅适用于Windows操作系统）

# 打开cmd并输入：

# setx OPENCV_VIDEOIO_PRIORITY_MSMF 0 
## 这两个方法并不好使
capture = cv2.VideoCapture(0, args.index_camera)
# 帧的宽度
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
# 帧的高度
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
# 每秒的帧数
fps = capture.get(cv2.CAP_PROP_FPS)
print("frame width:{}".format(frame_width))
print("frame height:{}".format(frame_height))
print("frames per second:{}".format(fps))

if capture.isOpened() is False:
    print("Error Camera !")


# 读取视频直到关闭

while capture.isOpened():
    # 通过摄像头,一帧一帧捕获
    ret, frame = capture.read()
    if  ret is True:
        # 显示捕获的帧
        cv2.imshow("frame", frame)
        # 将捕获的帧转化为灰度帧
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 显示灰度帧
        cv2.imshow("gray frame", gray_frame)
        # 键盘输入q, 退出视频捕获
        # if cv2.waitKey(20) & 0xFF == ord("q"):
        #     break
        # if cv2.waitKey(20) & 0xFF == ord("q"):
        #     break
        key_pressed = cv2.waitKey(100)
        print('单机窗口，输入按键，电脑按键为',key_pressed,'按esc键结束')
        if key_pressed == 27:
            break

    else:
        break
# 释放
capture.release()
cv2.destroyAllWindows()