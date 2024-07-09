def f(m):
    m.append(3)
x = [1, 2]
f(x);

print(x ==[1 , 2]);
print(x is [1, 2]);   # Checks the x wheather is value is true: -> output: False
                      # because x is modified
print(x);

