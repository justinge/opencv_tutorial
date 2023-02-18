# 1. 记载库
import cv2
import argparse

# 2 获取参数
parser = argparse.ArgumentParser()

# 3 添加参数
parser.add_argument("video_path", help="the path to the video file")

# 4 解析参数
args = parser.parse_args()

# 5 加载视频文件
capture = cv2.VideoCapture(args.video_path)



# 6 读取视频
ret, frame = capture.read() # ret 是否读取到了帧（图片）

while ret:
    cv2.imshow("video", frame)
    ret, frame = capture.read() # 继续读取帧
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows() # 关闭