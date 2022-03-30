# Iterations



1. 반복문으로 팩토리얼을 만들어보자. 시작은 어떻게 설정할까? 범위는 어떻게 정할까?

2. 삼각별을 찍어보자. row 별로 무엇이 프린트 되어야 하는지 생각해보자.

3. 거꾸로된 삼각형을 생각해보자. step(start, stop, step) 을 활용하자.

4. 구체적인 범위를 모른다면 while 문을 활용하자. 자연수가 몇 자리수인지 구해보자.

5. 자연수 n 보다 작은 모든 피보나치 수열을 나열해보자. 첫 두 개의 수는 정해져 있다. n 이하인 동안 반복문을 돌려보자.


6. range를 사용하여 범위를 표현해보자.


7. Dictionary 형태로 key와 value를 출력해보자.




### 짚고가는 지역변수와 전역변수
#### Error
UnboundLocalError: local variable 'a' referenced before assignment

#### Reason

함수 내에서 변수를 할당하면 ( a = 10 ) 변수 a가 함수 내에서만 쓰일 수 있게 된다. 정확히 말하면 함수 밖에 같은 이름을 가진 변수는 가려버린다. 만약 a = 5 처럼 함수 밖에서 a 가 언급되고 있다면 `UnboundLocalError`가 발생한다.

로컬 변수가 할당되기도 전에 사용되었어요!! 라는 것이다.

함수를 실행하면 함수 내부를 먼저 확인하고 로컬 변수가 할당되면 함수 밖은 shadow 된다는 것을 잊지 말자.


#### Solution
그러면 이 에러를 어떻게 해결할까?


##### 1. global variable 사용

함수 안에서 `global` a  라고 선언하면, a라는 변수는 함수 외부에서도 사용할 수 있게 된다. 정확히 이야기하면 파이썬 인터프리터가 동작하고 함수 모듈을 실행할 때 `global` 임을 확인하면 변수 a 를 함수 밖에서부터 찾기 시작한다. 외부 변수를 함수 내부에서 조작할 수도 있게 된다.

![](https://images.velog.io/images/lluna/post/50e4fe5f-2d5a-42df-a1cf-c623a3806c9b/image.png)


##### 2. parameter 사용
글로벌 사용시 변수 충돌이 날 수 있어 이것을 더 권장한다. 
함수 안에 파라미터로 a를 넣어 사용한다.

![](https://images.velog.io/images/lluna/post/1a0fc6a1-ade4-4300-8fc2-8cd256a2342d/image.png)





출처
https://app.codility.com/programmers/lessons/1-iterations/