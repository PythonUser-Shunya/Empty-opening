import cv2

img_path = "kaikuudo.jpg"
img = cv2.imread(img_path, 0)


def onTrackbar(position):
    global threshold
    threshold = position


cv2.namedWindow("img")
threshold = 100
cv2.createTrackbar("track", "img", threshold, 255, onTrackbar)


while True:
    ret, img_th = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    whole_area = img_th.size
    # 白部分の画素数
    white_area = cv2.countNonZero(img_th)
    # 黒部分の画素数
    black_area = whole_area-white_area
    # 第五引数である3 * 3の中で閾値を作っていく。これなら影があっても大丈夫
    cv2.imshow("img", img_th)
    cv2.imshow("src", img)
    if cv2.waitKey(10) == ord("s"):
        # それぞれの割合を表示
        print('White_Area = '+str(white_area / whole_area * 100) + '%')
        print('Black_Area = '+str(black_area / whole_area * 100) + '%')
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
