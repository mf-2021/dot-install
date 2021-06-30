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


class User:
    """
    コンストラクタ（Rubyでいう"def initialize"）
    # ここで設計図（クラス）を作っているが、
    上の例では"pass"で空のクラスを作っている
    """
    def __init__(self, name):
        # インスタンス変数
        self.name = name

tom = User("tom")
bob = User("bob")


print(tom.name)
print(bob.name)