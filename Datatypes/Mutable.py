def f(m):
    m.append(3)
x = [1, 2]
f(x);

print(x ==[1 , 2]);
print(x is [1, 2]);   # Checks the x wheather is value is true: -> output: False
                      # because x is modified
print(x);

const = list([1, 2, 3, 4])
const = len(const)
print(const)

mutable_array = [4, 3, 2, 1]
mutable_array[0] = 5
print(mutable_array);

mutable_array.sort();
print(mutable_array)
