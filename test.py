# #1
def sum(a,b):
    return a+b
a=int(input("정수1: "))
b=int(input("정수2: "))
print("합은:",sum(a,b),"입니다.")

# #2
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# a=int(input("정수1: "))
# b=int(input("정수2: "))
# print(f"add:{add(a,b)}")
# print(f"sub:{sub(a,b)}")
# print(f"mul:{mul(a,b)}")
# print(f"div:{div(a,b):.1f}")

#3
def gogodan():
    for i in range(2,10):
        for j in range(1,10):
            print(f'{i}*{j}={i*j}',end='\t')
        print()

#4
# import random

# def num4():
#     print("당신의 이름은 ?")
#     name = input()

#     print(f"안녕하세요 {name}님 1에서 20까지 숫자중 하나를 생각합니다.")
#     secretNumber = random.randint(1,20)
#     for count in range(1, 7):
#         guess = int(input("맞춰보세요 \n"))
#         if (secretNumber>guess):
#             print('그 숫자보다 큰수')
#         elif (secretNumber<guess):
#             print('그 숫자보다 작은수')
#         else:
#             break
#     if guess == secretNumber:
#         print(f'잘 맞췄어요 {name}님 {count} 번만에 맞췄어요 !')
#     else:
#         print(f'틀렸네요. 정답은 {secretNumber} 입니다.')
# num4()
# 5
# def easy_unpack(elements):
#     return (elements[0],elements[2],elements[-2])  # 튜플로 리턴

# if __name__ == '__main__':
#     print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

#     #다음과 같이 리턴결과가 나와야 한다.
#     assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
#     assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
#     assert easy_unpack((6, 3, 7)) == (6, 7, 3)

#6
# def is_acceptable_password(password):
#     return len(password)>6
    
# if __name__ == '__main__':
#     print(is_acceptable_password('ashort'))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('muchlonger') == True
#     assert is_acceptable_password('ashort') == False

#7
# def number_length(a):
#     return len(str(a))

# if __name__ == '__main__':
#     print(number_length(10))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert number_length(10) == 2
#     assert number_length(0) == 1
#     assert number_length(4) == 1
#     assert number_length(44) == 2

#8?
# def remove_all_before(items, i):
#     #코드 작성
#     if i in items:
#         return items[items.index(i)::]
#     else:
#         return items[::]
    
    
# if __name__ == '__main__':
#     print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
    
#     #다음과 같이 리턴결과가 나와야 한다.
#     assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
#     assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
#     assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
#     assert list(remove_all_before([], 0)) == []

#9
# def replace_first(items):
#     #코드작성
#     if(items):
#         x=items.pop(0)
#         items.append(x)
#         return items
#     else:
#         return items
   

# if __name__ == '__main__':
#     print(list(replace_first([1, 2, 3, 4])))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
#     assert list(replace_first([1])) == [1]
#     assert list(replace_first([])) == []
