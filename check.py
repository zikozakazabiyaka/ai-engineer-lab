import sys

def f():
    return 1, 2

print(type(f))
print(type(f()))
print(type(sys.argv))
print(type(sys.argv[0]), sys.argv[0])
print(type(sys.argv[1]), sys.argv[1])
print(int(sys.argv[1]) + 1)
print(sys.argv[1] + 1)