# クラス
# - アクセス制限

# user_name = "taguchi"
# user_score = 10

# class User:
#     pass

# tom = User() # インスタンス
# tom.name = "tom"
# tom.score = 20

# bob = User()
# bob.name = "bob"
# bob.level = 5
# python

# クラス

# class User:
#     # クラス変数
#     count = 0
#     def __init__(self, name):
#         User.count += 1
#         self._name = name
#     # インスタンスメソッド
#     def say_hi(self):
#         print("hi {0}".format(self._name))
#     # クラスメソッド
#     @classmethod
#     def show_info(cls):
#         print("{0} instances".format(cls.count))

# tom = User("tom")
# print(tom._name)
# tom.say_hi()

# クラスの継承
# User -> AdminUser

class User:
    def __init__(self, name):
        self.name = name
    # インスタンスメソッド
    def say_hi(self):
        print("hi {0}".format(self.name))

class AdminUser(user):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def say_hello(self):
        print("hello {0} ({1})".format(self.name, self.age))

bob = AdminUser("bob", 23)
print(bob.name)
bob.say_hi()
bob.say_hello()