def add(a,b):
  print(a-b)
  



def dec(func):
  def inner(a,b):
    if a<b:
      a,b=b,a
    return func(a,b)
  return inner

dec=dec(add)
dec(4,3)