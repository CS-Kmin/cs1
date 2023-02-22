# Hàm = Function

# Định nghĩa hàm = Definition
def xinChao():
    print("Hello ")
    print("Hello ")
    print("Hello ")

def tamBiet(a):
    print("Bye " + a)
    print("Bye " + a)


def hello(fn, ln):
    print("Hello " + fn + " " + ln)

# Viết hàm in ra màn hình lời chào
# Hàm có 2 tham số: firstName, lastName
def main():
    a = input("Nhap ten: ")
    b = input("Nhap ho: ")
    hello(a, b) # Hello, Bao Vu

main()