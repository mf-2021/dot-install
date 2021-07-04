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


# クラス

class User:
    # クラス変数
    count = 0
    def __init__(self, name):
        User.count += 1
        self.name = name

print(User.count) # 0
tom = User("tom")
bob = User("bob")
print(User.count) # 2

print(tom.count)