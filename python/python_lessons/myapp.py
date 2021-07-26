# モジュール

# import user
# from user import AdminUser
# from user import AdminUser, User

# # bob = user.AdminUser("bob", 23)
# bob = AdminUser("bob", 23)

# tom = User("bob", 23)

# print(bob.name)
# bob.say_hi()
# bob.say_hello()

# 例外処理

class MyException(Exception):
    pass

def div(a, b):
    try:
        if (b < 0):
            raise MyException("not minus")
        print(a / b)
    except ZeroDivisionError:
        print("not by zero!")
    except MyException as e:
        print(e)
    else:
        print("no exception!")
    finally:
        print("-- end --")

div(10, -3)
# div(10, 3)
# div(10, 0)