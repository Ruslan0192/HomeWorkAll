
import cv2

cap = cv2.VideoCapture('mixkit-young-woman-having-a-job-interview-online-46900-hd-ready.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
last_coord_eyes = [] # последнее значение координат прямоугольника для глаз

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eye = cv2.CascadeClassifier('haarcascade_eye.xml')
    # eye = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    results = eye.detectMultiScale(gray, scaleFactor=2, minNeighbors=7)
    coord_eyes = []
    for (x, y, w, h) in results:
        coord_eye = [x,y,w,h]
        coord_eyes.append(coord_eye)
        # eye = cv2.rectangle(frame,(x,y), (x+w, y+h), (0,0,255), thickness=1)

    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    if len(coord_eyes) == 2:
        for i in range(len(coord_eyes)):  #определение минимального и максимального значения координат по x и y
            coord_eye = coord_eyes[i]
            if min_x > coord_eye[0] or min_x == 0:
                min_x = coord_eye[0]
            if max_x < coord_eye[0]:
                max_x = coord_eye[0]
            if min_y > coord_eye[1] or min_y == 0:
                min_y = coord_eye[1]
            if max_y < coord_eye[1]:
                max_y = coord_eye[1]
    if max_x == 0 or max_y == 0:
        min_x, max_x, min_y, max_y = last_coord_eyes  # если значения не определены берем предыдущие
    else:
        last_coord_eyes = [ min_x, max_x, min_y, max_y]

    #координаты для ROI
    delta = 5 # разница для увеличения границ прямоугольника
    x1 = min_x-delta-10
    y1 = min_y-delta
    x2 = max_x+w+delta
    y2 = max_y+h

    #определяем ROI, замылевание и инверсия цвета
    roi = frame[y1:y2,x1:x2]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi,(21, 21), 11, 9,21)
    inverted_roi = 255 - gray_roi
    frame[y1:y2,x1:x2]  = cv2.cvtColor(inverted_roi, cv2.COLOR_GRAY2BGR)

    out.write(frame)
    cv2.imshow('video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


