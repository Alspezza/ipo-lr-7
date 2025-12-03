def isCorrectRect(x,y):
    if x[0] < y[0] and x[1] < y[1]:
        return True
    else:
        return False

m = (1,3)
n = (2,4)

print(isCorrectRect(m,n))
