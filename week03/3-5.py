# from unittest import result


# print(people)

# print(fruits[3])

# fruits.append('가능')

# print(fruits)

# ------------------------
# from unittest import result


# def aa(num1,num2):
#     print("안녕")
#     return num1+num2

# result = aa(2,54)

# print(result)
    
# ------------------------
# age = 25

# if age > 20:
#     print("성인")
# else:
#     print("청소년")

# ------------------------
# def is_age(age):
#     if age > 20:
#         print("성인")
#     else:
#         print('청소년')

# is_age(50)
# is_age(15)

# ------------------------
# from itertools import count


# fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

# count = 0
# for aa in fruits:
#     if aa == '수박':
#         count += 1
# print(count)

# ------------------------

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    # print(person['name'],person['age'])
    if person['age'] < 20:
        print(person)