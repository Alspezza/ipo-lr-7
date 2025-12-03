class RectCorrectError (Exception):
    pass
def isCorrectRect(m,n):
    if x[0] < y[0] and x[1] < y[1]:
        return True
    else:
        return False
m = (1,3)
n = (2,4)
#print(isCorrectRect(m,n))


rect1 = [(1,1),(5,5)]
rect2 = [(2,3),(6,8)]

def isCollisionRect(rect1, rect2):
    if rect1[0][0] < rect1[1][0] and rect1[0][1] < rect1[1][1]:
        r1 = True
    else: 
        r2 = False
        raise RectCorrectError ("1 прямоугольник не существует")
    if rect2[0][0] < rect2[1][0] and rect2[0][1] < rect2[1][1]:
        r2 = True
    else:
        r2 = False
        raise RectCorrectError ("2 прямоугольник не существует")
    if r1 == r2 == False:
        return 0
    
    if rect2[0][0] > rect1[1][0] or rect2[1][0] < rect1[0][0] or rect2[0][1] > rect1[1][1] or rect2[1][1] < rect1[0][1]:
        return False
    else:
        return True
#print(isCollisionRect(rect1, rect2))


def intersectionAreaRect(rect1,rect2):
    try:
        [(r1x1, r1y1), (r1x2, r1y2)] = rect1 
        [(r2x1, r2y1), (r2x2, r2y2)] = rect2 
        if isCollisionRect(rect1,rect2) == False:
            return 0 
        else:
            x_left = max(r1x1, r2x1)
            x_right = min(r1x2, r2x2)
        # Пересечение по оси Y
            y_bottom = max(r1y1, r2y1)
            y_top = min(r1y2, r2y2)
        # Вычисляем ширину и высоту пересечения
            width = x_right - x_left
            height = y_top - y_bottom
            S = width * height
            return S
    except RectCorrectError as e:
        raise ValueError(f"В функцию был передан некорректный прямоугольник: {e}")
print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))
   
