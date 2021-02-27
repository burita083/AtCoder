def solv_quadratic_equation(a, b, c):
    """ 2次方程式を解く  """
    D = (b**2 - 4*a*c) ** (1/2)
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)

    return x_1, x_2

S, P = map(int, input().split())
S *= -1

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

m1, m2 = solv_quadratic_equation(1, S, P)
n1 = -1
n2 = -1
S *= -1
if is_integer_num(m1) and m1 >= 1:
  n1= S-m1

if is_integer_num(m2) and m2 >= 1:
  n2= S-m2


if n1 == -1 and n2 == -1:
  print("No")
  exit()

if n1 <= 0 and n2 <= 0:
  print("No")
  exit()

print("Yes")

