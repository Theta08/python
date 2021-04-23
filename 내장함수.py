# dir 객체가 자체적으로 가진 변수나 함수를 보여준다.
# dir(__builtins__) #내장함수를 보여준다.
# 터미널 클리어 : cls


# rang(n,m,a) : n~m까지 +a증가 시킴
# a=list(range(1,101,2)) #홀수
# print(a)

# 함수 정의
def hello():
    print('hi')
    print('hi2')
    print('hi3')


def hello2(name,name2):
    print(name)
    print(name2)

# retrue
def add(n):
    return n+10

def ho(n):
    if(n%2==0):
        print("홀")
    else:
        print("짝")
#*:매개변수 제안x
def ho1(*arg):
    return sum(arg)/len(arg)



# 실행
# ho(1)
# print(ho1(1,3))

# =================================================
def div10(num):
  try:
    return 10/num
  except ZeroDivisionError:
    print('에러: 0으로 나눌수 없음.')
  

print(div10(2))
print(div10(0))
print(div10(5))