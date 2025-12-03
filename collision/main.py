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


print(isCollisionRect(rect1, rect2))
        
