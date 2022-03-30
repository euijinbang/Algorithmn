### if문 - 6221번

> Game 리스트를 만들고, 비길 경우와 그렇지 않은 경우를 나눈다. 이길 경우의 수 3가지와 그렇지 않은 경우 (질 경우) 3가지로 나뉜다.

- 가위, 바위
- Result : Man1 Win!

```python
Man1 = input()
Man2 = input()
Game = ["가위", "바위", "보"]

if Man1 == Man2:
    print("Draw!")
    
if (Man1 == Game[0] and Man2 == Game[2]) or (Man1 == Game[1] and Man2 == Game[0]) or (Man1 == Game[2] and Man2 == Game[1]):
    print("Result : Man1 Win!")
else:
    print("Man2 Win!")
```



### if문 - 6222번

> 알파벳인지 확인한다.
>
> 알파벳이고 대문자라면 소문자로 변환, 알파벳이고 소문자라면 대문자로 변환한다.
>
> ord 함수를 이용하여 알파벳을 숫자로 바꾼다. (아스키코드)

- 아스키 코드 관련 내장함수 : ord(), char()

- c(ASCII: 99) => C(ASCII: 67)

```python
char = input()

if char.isalpha == False:
    print(char)

else:
    if char.isupper == True:
        charN = char.lower()
    else:
        charN = char.upper()

print("{}(ASCII: {}) => {}(ASCII: {})".format(char, ord(char), charN, ord(charN)))
```



### if문 - 6226번

> 1부터 200까지 수 중, 7의 배수이면서 5의 배수가 아닌 것을 고르는 문제다.
>
> 받은 Int형 자료를 string 형으로 바꾼 후 append 함수를 이용하여 빈 리스트에 넣어준다.
>
> 이후 join 함수로 '문자열 str로 구성된 리스트 내부 요소들을 문자열로 합쳐 반환한다.
>
> *** 빈 문자열을 사용하면, 리스트를 쓰지 않고도 바로 문자열 반환이 가능하다.

- 리스트에 항목을 추가하는 append 메서드 사용하기
- 문자열을 더하는 join 메서드 사용하기

```python
# 방법 1. 빈 리스트에 문자열로 변환하여 하나하나 담고, 조인 함수로 하나의 문자열로 반환한다.
tempL = []

for i in range(1, 201) :
    if i % 7 == 0 and i % 5 != 0 :
        tempL.append(str(i)) 
        
# ['7', '14', '21', '28', '42', '49', '56', '63', '77', '84', '91', '98', '112', '119', '126', '133', '147', '154', '161', '168', '182', '189', '196']
        
result = ','.join(tempL)

print(result)

# 방법 2. 빈 문자열에 문자를 하나하나 더해준다.

tempC = ''

for i in range(1, 201):
  if (i % 7 == 0) and (i % 5 != 0) :
    a += str(i) + ','

print(tempC[:-1]) # (,) 가 맨 뒤에 출력되기 때문에 슬라이싱으로 맨 뒷자리 하나(,)를 빼준다.
```



### if문 - 6227번

> 100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.

- 200,202,204,206,208,220,222,224,226,228,240,242,244,246,248,260,262,264,266,268,280,282,284,286,288
- 방법 1. 숫자형을 문자열로 순회 가능하도록 변환 후 for 문 돌려 찾고, 다시 숫자로 변환하여 조건확인, 다시문자열로 바꾸고 그것을 다시 join으로 묶는다.
- 방법 2. %10, //10 활용하기

```bash
# 100 ~ 300
# 방법 1. 숫자형을 이터러블한 문자열 리스트로 바꿔서 for문으로 돌려가며 인덱스를 확인한다.
charL = []
for i in range(100, 301):
  charL.append(str(i)) 

tempL = []
for j in charL: # ['100', '101, '102' ,...]
    if (int(j[0]) % 2 == 0) and (int(j[1]) % 2 == 0) and (int(j[2]) % 2 == 0):
        # 숫자를 한번 더 문자열로 바꿔서 리스트에 넣는다.
        tempL.append(str(j))
        # 그 문자열을 다시, join으로 묶는다.
        result = ','.join(tempL)
print(result)



# 방법 2. 나눗셈과 나머지를 활용하여 각 자리의 숫자를 그대로 출력한다.
# 10으로 나눈 나머지, 10으로 나눈 몫

tempStr = '' # 빈 문자열을 만든다.
for i in range(100, 301): 
    if (i % 2 == 0) and (i // 10 % 2 == 0) and (i // 100 % 2 == 0):
        j = str(i) # 숫자를 문자열로 변환한다.
        tempStr += j + ',' # 문자열에 쉼표와 함께 넣어준다. (join 함수도 가능하다.)
        
print (tempStr[:-1])  # 마지막 쉼표는 제외하고 출력한다.



# TIP. 각 자릿수 출력하기(정식) n을 10으로 나눈 몫이 0보다 클 동안 반복한다.
digit = []
n = 325
while n > 0 :
    digit.append(n % 10) # 1의자리, 10의자리, 100의자리 출력
    n = n // 10
print(digit[::-1]) # [5, 2, 3] => [3, 2, 5] 거꾸로 출력
```



### 반복문 - 6230 번

> 다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,
>
> 60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오

```python
# 내가 한 방법  : 따로 변수를 설정해서 하나씩 더한다.
scores = [88, 30, 61, 55, 95]
i = 0  # 학생 순번을 나타내기 위한 변수
for score in scores:
    i = i + 1
    if score >= 60:
        print("{}번 학생은 {}점으로 합격입니다.".format(i, score))
    else:
        print("{}번 학생은 {}점으로 불합격입니다.".format(i, score))

# 모범답변 : 전체 스코어 길이만큼의 범위로 인덱스를 돌린다.
scores = [88, 30, 61, 55, 95]
for i in range(len(scores)):
    if scores[i] >= 60:
        print("{}번 학생은 {}점으로 합격입니다.".format(i+1, scores[i]))
    else:
        print("{}번 학생은 {}점으로 불합격입니다.".format(i+1, scores[i]))
```



### 반복문 - 6242번

> 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
>
> ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
>
> for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

- 딕셔너리 선언하기

```python
T = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
a = 0
b = 0
ab = 0
o = 0

for i in range(len(T)):
    if T[i] == 'A':
        a += 1
    if T[i] == 'B':
        b += 1
    if T[i] == 'O':
        o += 1
    if T[i] == 'AB':
        ab += 1

result = dict(A = a, O = o, B = b,  AB = ab) # 주의 : 딕셔너리 선언!! 키값에 텍스트여도 ''넣지않는다.
print(result)

# => {'A': 3, 'O': 3, 'B': 2, 'AB': 2}
```



### 반복문 - 6247번

```python
'''
*******
 *****
  ***
   *
'''

i  = 7
count = 0  # 홀수가 몇 번 돌았는지를 세는 변수
while i > 0 :
    if i % 2 :
        print(" " * ((i - (i - 2 * count)) // 2) + "*" * i + " " * ((i - (i - 2 * count)) // 2))
        i -= 1
        count += 1
    else:
        i -= 1
```



### 반복문 - 6249번

- 11 

- 0 1 2 3 4 5 6 7 8 9

  0 2 0 0 0 0 0 0 0 0

-  list 함수를 이용하여 숫자를 스트링 리스트로 바꾸기

- **리스트 괄호 없애기!!!!**

  - **방법 1. 리스트 언패킹 print(*list[::]) **으로 리스트의 [ ] 괄호를 없앤다.
  - **방법 2. map 과 join 함수 이용하기** map함수로 str로 변환 후 join으로 결합시킨다.

```python
n = list(input()) #  11 => ['1', '1'] 숫자를 스트링 리스트로 변환
countBoard = [0] * 10 # [0, 0, 0, 0, 0, 0, 0, 0, 0] 카운트보드 생성

# 문제요구사항 0 1 2 3 4 5 6 7 8 9 출력
answer1 = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(*answer1[::])     
# 리스트 언패킹!!!!!!!

b = " ".join(map(str, answer1)) 
# map으로 스트링 리스트 ["0", "1", ... , "9" ] 로 바꾼 후 join으로 결합!!! 


for i in n:
    countBoard[int(i)] += 1 # str 형식을 다시 int로 변환하여 보드의 해당 인덱스값에 1 추가
                            # [0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
print(*countBoard[::])			# 리스트 언패킹 => 0 2 0 0 0 0 0 0 0 0
```



### 10진수를 2진수로 변환하기 - 6253번

- 몫과 나머지 활용하기
- 문자열 슬라이싱[::-1] 으로 거꾸로 출력하기

```python
n = int(input())                     # 정수 숫자 n 입력
str_board = ''                       # 빈 문자열 생성
while n > 0:                
    remainder = n % 2                # 나머지 변수
    n = n // 2                       # 몫
    str_board += str(remainder)      # (거꾸로 출력을 위한) 문자열 슬라이싱을 위해 문자열에 추가한다.

print(str_board[::-1])               # 문자열 슬라이싱을 활용하여 결과물을 거꾸로 출력한다.
```



### 함수의 기초 1 - 6319번

- 문자열 인덱스를 거꾸로 출력하기 range(a, b, -1)

```python
# eye
word = input() 
reversed_word = ''  # 거꾸로 캐릭터를 넣을 빈 문자열을 생성합니다.
for i in range(len(word)-1, -1, -1):    # 인덱스번호 거꾸로 출력합니다. 2, 1, 0
    reversed_word += word[i]    # 빈 문자열에 거꾸로 입력합니다.

if word == reversed_word:
    print("{}\n입력하신 단어는 회문(Palindrome)입니다.".format(word))
```



### 함수의 기초 2 - 가위바위보 - 6320번

- 가위바위보 함수 만들기

```python
man1 = input()
man2 = input()
man1g = input()
man2g = input()

Game = ["가위", "바위", "보"]  # 가위바위보를 리스트 내용으로 갖는 게임 리스트를 정의합니다.

def RSP(m1, m2):
    if m1 == m2:	# 비겼을 경우입니다.
        print("draw")
    if (m1 == Game[0] and m2 == Game[1]) or (m1 == Game[1] and m2 == Game[0]):
        print("바위가 이겼습니다!")
    if (m1 == Game[0] and m2 == Game[2]) or (m1 == Game[2] and m2 == Game[0]):
        print("가위가 이겼습니다!")
    if (m1 == Game[1] and m2 == Game[2]) or (m1 == Game[2] and m2 == Game[1]):
        print("보가 이겼습니다!")
    
result = RSP(man1g, man2g)	# 함수를 호출합니다.
```



### 함수의 기초 3 - 소수 검사 - 6321번

- 해당 자연수의 약수가 2개이면 소수이다. (ex. 3, 13, ...)

```python
num = int(input())
dividers = []	# 약수를 모두 담을 리스트 변수를 생성합니다.

def isPrimenum(num):	# 소수(prime number) 를 검사하는 함수를 정의합니다.
    for i in range(1, num + 1):	# 1부터 해당 정수까지 반복합니다.
        if num % i == 0:
            dividers.append(i)	# 매개변수를 나눈 나머지가 0 인 수(약수)를 리스트에 저장합니다.
    
    if len(dividers) == 2:	# 약수의 갯수가 2개이면 "소수입니다" 를 출력합니다.
        print("소수입니다.")

result = isPrimenum(num)	# 함수를 호출합니다.
```



### 함수의 기초 4 - 피보나치 수열 - 6323번

- 파이써닉하게 피보나치 수열 구현하기
- 초기값 설정 (0, 1) 과 while문 활용, 파이써닉 => a, b = b , a+b
- 문제별 초기값 및 while문의 범위를 주의해야 합니다.

```python
def fib(n):     # 피보나치 수열 함수를 정의합니다.
    a, b = 1, 1 # 피보나치 처음 두 숫자(1, 1 : 문제마다 다를수있음)를 지역변수로 설정합니다.
    fibL = []   
    while len(fibL) < n:   # 길이가 9일때 까지만 while문이 실행되게 합니다.
        fibL.append(a)
        a, b = b, a+b   # 피보나치 수열의 핵심부분을 파이써닉하게 구현합니다.
    return fibL

result = fib(10)    # 함수를 호출합니다.
print(result)
```



### 함수의 기초 5 - 중복제거 - 6324번

- set 세트로 중복 제거하기

```python
numbers = [1, 2, 3, 4, 3, 2, 1]

def soleNum(n):	# 중복이 제거된 리스트를 출력하는 함수를 정의합니다.
    return list(set(n))	# 리스트를 세트로 만들어 중복제거 후, 다시 리스트로 반환합니다.

result = soleNum(numbers)	# 함수를 호출합니다.

print(numbers)
print(result)
```



### 함수의 기초 6 - 6325번

- random 함수로 임의의 수 뽑기, random 모듈 집어넣어야!
- random.randrange(a , b) => a부터 b-1 까지 임의의 정수 출력

```python
import random

>>> random.random()		# random float : 0.0 <= x < 1.0
0.3728991874

>>> int(random.random()*n)		# random integer (n = 10 or...)
4

>>> random.randrange(10)		# integer from 0 to 9 inclusive
7

>>> random.randrange(0, 101, 2)	# even integer from 0 to 100 inclusive
26

>>> random.randint(3, 5)		# integer from 3 to 5 inclusive (3 <= N <= 5)
5
```

```python
# 풀이
numbers = [2, 4, 6, 8, 10]

def isnumincluded(num):
    if num in numbers:
        print("{} ==> True".format(num))
    else:
        print("{} ==> False".format(num))

isnumincluded(5)
isnumincluded(10)
```

```python
# 완전 랜덤 인풋을 위한 랜덤 모듈 추가시 (문제와 약간 다름) 1 ~ 10 까지 가능
import random

numbers = [2, 4, 6, 8, 10]

def isnumincluded():
    random_number = random.randrange(1, 11) # random integer from 0 to 10 included
    if random_number in numbers:
        print("{} => True".format(random_number))
    else:
        print("{} => False".format(random_number))

isnumincluded()
isnumincluded()
```



### 함수의 기초 7 - 재귀함수 팩토리얼 - 6326번

- 재귀함수를 이용한 팩토리얼 구현

```python
n = int(input())

def factorial(n):		
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
        
print(factorial(n))
```



### 함수의 기초 8 - 6327번

- input에 한 번에 두 개의 값 입력받기

```python
변수1, 변수2 = input().split()
변수1, 변수2 = input().split(기준문자)
변수1, 변수2 = input(문자열).split()
변수1, 변수2 = input(문자열).split(기준문자)
```

- 3, 5 처럼 콤마로 구분되어 들어오는 문자열을 처리하는 법 => input.split(',')

```python
a, b = map(int, input().split(',')) # 3,5 콤마를 기준으로 split 함수로 문자열을 나누고 map 함수를 이용하여 int로 각각 변환합니다.
# print(type(a)) # => int
# print(a) # => 3
# print(b) # => 5

def square(n):
    return "square({}) => {}".format(n, n**2)
        
print(square(a))
print(square(b))
```



### 함수의 기초 9 - 6328번

- ', ' 콤마 공백을 기준으로 한 번에 두 개의 값 입력받기

```python
a, b = input().split(', ')

def whichisLonger(a, b):
    if len(a) > len(b):
        return a
    else:
        return b

print(whichisLonger(a, b))
```



### 함수의 기초 10 - 6329번

- 거꾸로 숫자 나열하기 -> range의 step을 -1 로 주어 조정하였다.

- 발생한 문제점 : 해당 숫자 출력 마지막에 None이 추가로 출력되었다.
  - 원인 : 함수 내에 print를 사용했으므로 함수 호출만 해도 프린트가 된다. 함수호출을 프린트하면 2번 프린트가 되어 중복이 발생하고 None이 추가로 출력된다.
  - 해결 : 함수를 호출만 하고 프린트하지 않는다.

```python
def countDown(num):
    if num <= 0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    else:
        for i in range(num, 0, -1):
            print(i)
            
# print(countDown(0)) => None 출력

countDown(0)
countDown(10)                
```



### 자료구조 - 리스트, 튜플 - 6273번

- 튜플을 항목으로 갖는 리스트 객체 활용
- 튜플 언패킹 tuple unpacking
  - Packing and Unpacking
    In packing, we place value into a new tuple while in unpacking we extract those values back into variables.

```python
# tuple unpacking

x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(company)
print(emp)
print(profile)
```

- code

```python
def getScore(sub1, sub2):
    total = sub1 + sub2
    avg = (sub1 + sub2) / 2

    return total, avg

score = [(80, 90), (85, 75), (90,100)]

for i in range(3):
    # tuple unpacking
    (sub1, sub2) = score[i]
    result = getScore(sub1, sub2) # (170, 85.0)

    # # tuple unpacking
    (total, avg) = result

    print("{}번 학생의 총점은 {}점이고, 평균은 {}입니다.".format(i+1, total, avg))
```



### 자료구조 - 리스트, 튜플 - 6275번

- in, not in 등 리스트 내포기능 사용
- join으로 묶어서 출력

```python
chars = list('Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.')

vowels = ['a','e','i','o','u']
new_chars = []

for i in range(len(chars)):
    if chars[i] not in vowels:
        new_chars.append(chars[i])
    if i in vowels:
        pass
      
ans = ''.join(new_chars)

print(ans)
```



### 자료구조- 리스트, 튜플 - 6276번

- 리스트가 분리되는 지점 (반복문 분기점) 잘 보기

```python
# 구구단 만들기
result = []
for i in range(2, 10):
    dan = []
    for j in range(1, 10):
      	# 3의 배수와 7의 배수를 제외하고 gugu 에 삽입
        if (i % 3 and i % 7 != 0) and (j % 3 and j % 7 != 0):
            dan.append(i * j)     
    result.append(dan)          # result에 각 단마다 리스트를 만들어 삽입

print(result)
```



### 자료구조- 리스트, 튜플 - 6277번

- list.append() 사용하기

```python
arr = []
for i in range(5):
    arr.append(int(input()))

aver = sum(arr) / len(arr)
print("입력된 값{0}의 평균은 {1}입니다.".format(arr,aver))
```



### 자료구조- 리스트, 튜플 - 6280번

- N (정수) 의 약수 구하기 - append 사용하기

```python
# 12
N = int(input())
arr = []

for i in range(1, N+1):
    if N % i == 0:
        arr.append(i)

print(arr)
# [1, 2, 3, 4, 6, 12]
```



### 자료구조- 리스트, 튜플 - 6282번

- 리스트에서 짝수만 뽑기 - append 사용하기

```python
arr = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
even_arr=[]
for i in arr:
    if i % 2 == 0:
        even_arr.append(i)

print(even_arr)
```



### 자료구조- 리스트, 튜플 - 6286번

- 재귀함수 구현하기 => 3가지 방법(<피보나치수열 구현 3가지 방법> 참조)

```python
def fibo(n):                                                
    if n < 2:                                               
        return n                                            
    arr = [0, 1]                                            
    for i in range(2, n + 1):                               
        arr.append(arr[i - 2] + arr[i - 1])                 
    arr.pop(0)                                              
    return arr

print(fibo(10))

# >>> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```



### 자료구조- 리스트, 튜플 - 6286번

```python
list = []
for i in range(1, 21):
  if (i % 3 != 0) or (i % 5 != 0):
    list.append(i ** 2)
print(list)
```



### 자료구조- 리스트, 튜플 - 6289번

- 문자열 텍스트를 숫자형 리스트로 반환하기

```python
text = '12345'
arr = list(map(int, list(text)))
# [1, 2, 3, 4, 5]

total = 0
for i in range(len(arr)):
    total += arr[i]

print(total)
```



### 자료구조- 리스트, 튜플 - 6290번

- `list comprehension`과 for문 비교
- 가나다.. 한글 자모는 대소로 비교가 가능하다.

```python
dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
 

inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다', '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그',
'자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']

# 정규 표현식
[[word for word in inputWord if (word >= base [0]) is (word <= base[1])] for base in dicBase]

# for문
arr = []
for base in dicBase:
    word_arr = []
    for word in inputWord:
        if word >= base[0] and word <= base[1]:
            word_arr.append(word)
    arr.append(word_arr)

#>>> [['계시다', '가지다', '그', '개'], ['놀이'], ['들다', '다', '뒤', '듣다', '데리다'], [], ['막', '무척', '마리'], ['부모님', '비용', '비행기', '보이다'], ['싶다', '수출'], ['원래', '아이', '옳다'], ['좀', '자르다', '정도'], ['처리', '최초'], [], [], [], ['함께']]
```



- list comprehension

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```

