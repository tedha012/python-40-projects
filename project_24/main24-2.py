import numpy as np
import cv2

ff = np.fromfile(r"./maple-leaves.jpg", np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(
    img,
    dsize=(0, 0),
    fx=0.4,
    fy=0.4,
    interpolation=cv2.INTER_LINEAR,
)


def onChange(pos):
    pass


cv2.namedWindow("Trackbar Windows")  # 트랙 윈도우 생성
cv2.createTrackbar(
    "sigma_s",
    "Trackbar Windows",
    0,
    200,
    onChange,
)  # 트랙 sigma_s 최소 최대값 설정
cv2.createTrackbar(
    "sigma_r",
    "Trackbar Windows",
    0,
    100,
    onChange,
)  # 트랙 sigma_r 최소 최대값 설정

cv2.setTrackbarPos("sigma_s", "Trackbar Windows", 100)  # 트랙 sigma_s 기본값 설정
cv2.setTrackbarPos("sigma_r", "Trackbar Windows", 10)  # 트랙 sigma_r 기본값 설정

while True:

    if cv2.waitKey(100) == ord("q"):
        break

    sigma_s_value = cv2.getTrackbarPos("sigma_s", "Trackbar Windows")
    sigma_r_value = cv2.getTrackbarPos("sigma_r", "Trackbar Windows") / 100.0

    cartoon_img = cv2.stylization(
        img,
        sigma_s=sigma_s_value,
        sigma_r=sigma_r_value,
    )
    cv2.imshow("cartoon view", cartoon_img)

cv2.destroyAllWindows()  # OpenCV 모든창 종료
