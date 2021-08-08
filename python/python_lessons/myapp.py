# リスト型とタプル
# 集合型
# 辞書型

# リスト型

# scores = [40, 50]
# # print(scores[0]) # 40
# # scores[0] = 45
# # print(len(scores)) # 2
# # scores.append(100)
# # print(scores)

# # for score in scores:
# #     print(score)

# for i, score in enumerate(scores):
#     print("{0}: {1}".format(i, score))


# タプル

# items = (50, "apple", 32.5)
# print(items[1])
# items[1] = "pen"

# print(list((1, 3, 5)))
# print(tuple([1, 3, 5]))

# スライス
# scores = [40, 50, 70, 90, 60]
# print(scores[1:4]) # 50, 70, 90
# print(scores[:2]) # 40, 50
# print(scores[3:]) # 90, 60
# print(scores[-3:]) # 70, 90, 60

# s = "hello"
# print(s[1:4])

# セット
# a = set([5, 4, 8, 5])
# a = {5, 3, 8, 5}
# print(a)
# print(5 in a) # True
# a.add(2)
# a.remove(3)
# print(a)
# print(len(a))

# a = {1, 3, 5, 8}
# b = {3, 5, 8, 9}
# print(a | b)
# print(a & b)
# print(a - b)

# 辞書型
# sales = {"taguchi": 200, "fkoji": 400}
# # print(sales["taguchi"])
# # sales["taguchi"] = 300
# # sales["dotinstall"] = 500
# # del(sales["fkoji"])
# # print(sales)

# for key, value in sales.items():
#     print("{0}: {1}".format(key, value))

# イテレータ

# scores = [40, 50, 70, 90, 60]
# it = iter(scores)
# print(next(it))
# print(next(it))
# print("hello")
# print(next(it))

# for score in scores:
#     print(score)

# def get_infinite(): #ジェネレータ
#     i = 0
#     while True:
#         yield i * 2
#         i += 1

# g = get_infinite()
# print(next(g))
# print(next(g))
# print(next(g))

# map（関数、イテレータ）
# def triple(n):
#     return n * 3

# print(list(map(triple, [1, 2, 3])))

# lambda 引数：　処理
print(list(map(lambda n: n * 3, [1, 2, 3])))