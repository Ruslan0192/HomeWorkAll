# Создайте матрицу (картинку) при помощи NumPy в виде квадрата произвольного размера.
# Отрисуйте картинку используя примитивы circle, ellipse, line и др.
# Цвета должны совпадать с картинкой или хотя бы быть того же оттенка
# Приветствуются дополнительные элементы, так вы лучше отточите навык определения координат.
#
# Доп. задание:
# Попробуйте сделать фон - градиент (можно цветной):

import numpy as np
import cv2

screen_width = 800
screen_height = 800

def get_gradient(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype='uint8')
    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        if is_horizontal:
            result[:, :, i] = np.tile(np.linspace(start, stop, width), (height, 1))
        else:
            result[:, :, i] = np.tile(np.linspace(start, stop, height), (width, 1)).T
    return result

screen = get_gradient(screen_width, screen_height, (0, 0, 0), (255, 255, 255), (True, True, True))
# screen = get_gradient(screen_width, screen_height, (0, 0, 0), (255, 255, 255), (False, False, False))
# screen = get_gradient(screen_width, screen_height, (0, 0, 0), (255, 255, 255), (True, False, False))

center_x = screen.shape[1]//2-100
center_y = screen.shape[0]//2-100
cv2.circle(screen, (center_x, center_y), 250, (255,255,255), thickness=3)
# cv2.circle(screen, (center_x, center_y-25), 125, (255,255,255), thickness=3)

cv2.ellipse(screen, (center_x, center_y), (100,100), 0, 180, 0, (0,255,0), thickness=3)
cv2.ellipse(screen, (center_x, center_y), (50,50), 0, 180, 0, (0,255,0), thickness=3)

cv2.line(screen, (center_x+50, center_y), (center_x+50, center_y-100), (255,0,0), thickness=3)
cv2.line(screen, (center_x-50, center_y), (center_x-50, center_y-100), (255,0,0), thickness=3)
cv2.line(screen, (center_x+100, center_y), (center_x+100, center_y-100), (255,0,0), thickness=3)
cv2.line(screen, (center_x-100, center_y), (center_x-100, center_y-100), (255,0,0), thickness=3)
cv2.line(screen, (center_x-50, center_y-100), (center_x-100, center_y-100), (0,0,255), thickness=3)
cv2.line(screen, (center_x+50, center_y-100), (center_x+100, center_y-100), (0,0,255), thickness=3)

cv2.imshow('logo', screen)
cv2.waitKey(0)