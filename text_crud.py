

FILE = "students.txt"

open(FILE, "a").close()

def add():

    
    code = input("کد ملی: ")
    name = input("نام: ")
    lname = input("نام خانوادگی: ")
    major = input("رشته: ")
    city = input("شهر: ")

    with open(FILE, "a") as file:
        file.write(f"{code},{name},{lname},{major},{city}\n")

    print("اضافه شد!")


def show():
    with open(FILE, "r") as file:
        for student in file:
            print(student.strip())


def search():
    code = input("کد ملی: ")

    with open(FILE, "r") as file:
        for student in file:
            if student.startswith(code + ","):
                print(student)
                return

    print("پیدا نشد!")


def delete():
    code = input("کد ملی: ")

    with open(FILE, "r") as file:
        students = file.readlines()

    with open(FILE, "w") as file:
        for student in students:
            if code != student.startswith(code + ","):
                file.write(student)

    print("عملیات حذف انجام شد!")

while True:

    print("""
1 => اضافه کردن
2 => نمایش
3 => جست و جو
4 => حذف
5 => خروج
""")

    m = input(">>> ")

    if m == "1":
        add()

    elif m == "2":
        show()

    elif m == "3":
        search()

    elif m == "4":
        delete()

    elif m == "5":
        print("خروج از برنامه")
        break

    else:
        print("منو اشتباه است!")
