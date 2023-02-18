# 1.导入库
import cv2
import argparse

# 2. 获取参数
parser = argparse.ArgumentParser()

# 3. 参加参数
parser.add_argument("img_input",help="read one image")
parser.add_argument("img_output",help="save the processed image")

# 4. 解析参数, 以字典形式保存参数和值
args = vars(parser.parse_args())

print(args)
# exit("=" * 100)
# 5. 加载图片
img = cv2.imread(args["img_input"])

# 6.处理: 灰度处理
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 7 保存图片
cv2.imwrite(args["img_output"],img_gray)

# 8 显示图片
cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", img_gray)

# 9 等待
cv2.waitKey(0)

# 10 关闭窗口
cv2.destroyAllWindows()