print("name =", __name__)

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("greet.py: файл загружен")
    print(greet("Dmitriy"))