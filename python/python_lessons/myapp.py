# クラス

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

class User:
    # クラス変数
    count = 0
    def __init__(self, name):
        User.count += 1
        self.name = name
    # インスタンスメソッド
    def say_hi(self):
        print("hi {0}".format(self.name))
    # クラスメソッド
    @classmethod
    def show_info(cls):
        print("{0} instances".format(cls.count))

tom = User("tom")
bob = User("bob")

User.show_info()
User.show_info()

# tom.say_hi()
# bob.say_hi()