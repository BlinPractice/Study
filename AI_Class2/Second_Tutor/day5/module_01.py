class calculator():
    def __init__(self):
        self.result = 0.0

    def add(self, value):
        self.result += value
        return self.result

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

name = "Goblin"

if __name__ == "__main__":
    print(add(3, 6))
    print(mul(2.4, 5))
    print(type(calculator()))