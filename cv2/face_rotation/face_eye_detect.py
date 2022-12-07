import cv2
import numpy as np

face_casacade = cv2.CascadeClassifier('Python/4일차/haarcascade_frontalface_default.xml')
eye_casacade = cv2.CascadeClassifier('Python/4일차/haarcascade_eye.xml')

face_img = cv2.imread('Python/4일차/face.png')
face_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

faces = face_casacade.detectMultiScale(face_gray, 1.1, 4)


for (x, y, w, h) in faces:
    cv2.rectangle(face_img, (x, y), (x+w, y+h), (0, 255, 0), 3)

    roi_img = face_img[y:(y+h), x:(x+w)]
    roi_gray = face_gray[y:(y+h), x:(x+w)]
    # cv2.imshow('face', face_img)
    # cv2.waitKey(0)


eyes = eye_casacade.detectMultiScale(roi_gray, 1.1, 4)
# print(eyes)
for (x, y, w, h) in eyes:
    cv2.rectangle(roi_img, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # cv2.imshow('face box', face_img)
    # cv2.waitKey(0)

for i , (x, y, w, h) in enumerate(eyes):
    if i == 0 :
        eye1 = (x, y, w, h)
    elif i == 1 :
        eye2 = (x, y, w, h)
if eye1[0] < eye2[0] :
    left_eye = eye1
    right_eye = eye2
else :
    left_eye = eye2
    right_eye = eye1

### 두 눈의 중심점 사이에 선 긋기
left_eye_center = (int(left_eye[0] + (left_eye[2]/2)), int(left_eye[1] + (left_eye[3]/2)))
left_eye_x = left_eye_center[0]
left_eye_y = left_eye_center[1]

right_eye_center = (int(right_eye[0] + (right_eye[2]/2)), int(right_eye[1] + (right_eye[3]/2)))
right_eye_x = right_eye_center[0]
right_eye_y = right_eye_center[1]

### 삼각형 그리기

# cv2.circle(roi_img, left_eye_center, 5,(0, 0, 255), -1)
# cv2.circle(roi_img, right_eye_center, 5,(0, 0, 255), -1)
# cv2.line(roi_img, right_eye_center, left_eye_center, (0, 200, 200), 3)

# cv2.imshow('face', face_img)
# cv2.waitKey(0)


# if left_eye_y > right_eye_y:
#     A = (right_eye_x, left_eye_y)
#     direction = -1
# else:
#     A = (left_eye_x, right_eye_y)
#     direction = -1

# cv2.circle(roi_img, A, 5, (0, 0, 255), -1)
# cv2.line(roi_img, left_eye_center, A, (0, 200, 200), 3)
# cv2.line(roi_img, right_eye_center, A, (0, 200, 200), 3)

# cv2.imshow('face', face_img)
# cv2.waitKey(0)

# 각도 구하기
delta_x = right_eye_x - left_eye_x
delta_y = right_eye_y - left_eye_y
angle = np.arctan(delta_y/delta_x)
angle = (angle * 180)/np.pi

# 회전시키기
h, w = face_img.shape[:2]
center = (h // 2, w // 2)

M = cv2.getRotationMatrix2D(center, (angle), 1.0)
rotated_img = cv2.warpAffine(face_img, M, (w, h))
cv2.imshow('face', rotated_img)
cv2.waitKey(0)

cv2.imwrite('PYTHON/rotated_woman.png', rotated_img)