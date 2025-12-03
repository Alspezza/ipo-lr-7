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


rect1 = [(1,1),(4,7)]
rect2 = [(2,3),(4,5)]

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
    [(r1x1, r1y1), (r1x2, r1y2)] = rect1 
    [(r2x1, r2y1), (r2x2, r2y2)] = rect2 
    if isCollisionRect(rect1,rect2) == False:
        return 0 
    elif isCollisionRect(rect1, rect2) == RectCorrectError:
        raise ValueError('В функцию передан некорректный прямоугольник')
    else:
         x_left = max(x1_left, x2_left)
    x_right = min(x1_right, x2_right)
    
    # Пересечение по оси Y
    y_bottom = max(y1_bottom, y2_bottom)
    y_top = min(y1_top, y2_top)
    
    # Вычисляем ширину и высоту пересечения
    width = x_right - x_left
    height = y_top - y_bottom


print(isCollisionRect(rect1, rect2))
        
