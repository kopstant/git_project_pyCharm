def add(a,b):
  return a+b

def minus(a,b):
  return a-b


a = int(input())
b = int(input())
how_many_plus = add(a,b)
how_many_minus = minus(a,b)
print (f"Результат сложения {how_many_plus}")
print (f"Результат вычитания {how_many_minus}")
