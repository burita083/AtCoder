Sx, Sy, Gx, Gy = map(int, input().split())

a = (-Gy-Sy)/(Gx-Sx)
b =(Gx*Sy-Sx*Gy)/(Gx-Sx)

#y=%fx+%f' % (a, b) )

#a*x+b = 0
def calc_slope_intersept(x1, y1, x2, y2):
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1
    return (a, b)

(a, b) = calc_slope_intersept(Sx, Sy, Gx, -Gy)

print(-b/a)