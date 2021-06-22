def square(w,h):
    area = w * h
    return area

def triangle(w,h):
    area = (w * h) / 2
    return area

print('사각혐의 면적 : {}'.format(square(5,4)))
print('삼각혐의 면적 : {}'.format(int(triangle(4,7))))

