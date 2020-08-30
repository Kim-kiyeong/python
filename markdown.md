### 1. Github 사용법
***
1. Github ? : `Github는 소프트웨어 개발 프로젝트를 위한 소스코드 관리 서비스`

2. 사전지식
    > - 가장 중요한 2가지
    >   1. commit : 파일을 추가하거나 변경 내용을 저장소에 저장하는 작업
    >   2. push : 파일을 추가하거나 변경 내용을 원격 저장소에 업로드하는 작업
    > 
    > - 로컬 저장소와 원격 저장소 : `로컬에서 작업 > 원격에 저장`
    >   1. 로컬 저장소 : 자신의 컴퓨터에 있는 저장소
    >   2. 원격 저장소 : 서버 등 네트워크에 있는 저장소
    >
    > - 브랜치(Branch)
    
3. Github 사용법
    > 1. Github에 저장소 작성(git init) 또는 복제(git clone)
    > 2. 파일의 작성, 편집
    > 3. 파일의 생성/변경/삭제를 git 인덱스에 추가(git add)
    > 4. 변경 결과를 로컬 저장소에 커밋(git commit)
    > 5. 로컬 저장소를 푸쉬해 원격 저장소에 반영(git push)
    > 6. [https://gbsb.tistory.com/10](https://gbsb.tistory.com/10)

<br>
<br>

### 2. Linux Command
***
##### 1) File and Directory 관련

1. ls : `List imformation about file`
    > 1. ls -a : hidden file도 다 보여줌
    > 2. ls -l : 파일 정보를 리스트로 보여줌
2. cd : `Change a directory`
    > 1. cd : 홈 디렉토리
    > 2. cd . : 현재 디렉토리
    > 3. cd .. : 상위 디렉토리
3. mkdir [name] : `Make a new directory`
4. rmdir [name] : `Remove a directory, but directory file or sub-directory cna not be delete`
5. rm  : `Remove files or directories`
6. mv : `Move files or directories`
7. clear : `Delete all contents of terminal`
8. grep : `조건 설정 및 검색 시 좋음`
9. du : `모든 디렉토리`
10. passwd : `Change password`
11. tar : `압축`

<br>
<br>

### 3. 올바르게 코드를 작성하는 방법
***
##### 1) Camel Case
    > 첫 단어의 첫 글자만 소문자로 하고, 다음 단어부터 첫 글자는 대문자로
        ex ) markDown, camelCase

<br>

##### 2) Pascal Case
    > 첫 단어의 첫 글자부터 대문자
        ex ) MarkDown, PascalCase
    
<br>

##### 3) Snake Case
    > 단어 사이에 언더바( _ )로 나누는 방식
        ex ) mark_down, snake_case
    > python은 주로 이거 사용한답니다 ^__^


<br>
<br>

### 4. SRP : Single Responsibility Principle
***
- 객체지향 설계의 5원칙 (SOLID) : SRP, OCP, LSP, ISP, DIP
    > 응집도는 높이고, 결합도는 낮추자는 고전 원칙을 객체 지향의 관점에서 재정립

- SRP : 단일 책임 원칙
    - 한 클래스는 하나의 책임만 가져야 한다.
    - 어떤 클래스를 변경해야 하는 이유는 오직 하나 뿐이어야 한다.
        > SRP가 안지켜진 사례
        >   - 변수 레벨
        >       - 하나의 속성이 여러 의미를 갖는 경우
        >       - 어떤 곳에는 쓰고, 어떤 곳에선 안쓰는 속성이 있는 경우
        >   - 메소드 레벨
        >       - 분기처리를 위한 if문이 많을 경우


<br>
<br>

### 5. HTTP response status code
***
##### 1) 성공 응답

1. 200 OK : `요청이 성공적으로 되었습니다. 성공의 의미는 HTTP 메소드에 따라 달라집니다.`
    > - GET : 리소스를 불러와서 메세지 바디에 전송되었습니다.
    > - HEAD : 개체 해더가 메세지 바디에 있습니다.
    > - PUT 또는 POST : 수행 결과에 대한 리소스가 메세지 바디에 전송되었습니다.
    > - TRACE : 메세지 바디는 서버에서 수신한 요청 메세지를 포함하고 있습니다.

2. 201 Created : `요청이 성공적이었으며, 그 결과로 새로운 리소스가 생성되었습니다.
이 응답은 일반적으로 POST 요청 또는 일부 PUT 요청 이후에 따라옵니다.`

<br>

##### 2) 클라이언트 에러 응답

1. 400 Bad Request : `이 응답은 잘못된 문법으로 인하여 서버가 요청을 이해할 수 없음을 의미합니다.`

2. 401 Unauthorized : `비록 HTTP 표준에서는 "미승인(Unauthorized)"을 명확히 하고 있지만,
의미상 이 응답은 "비인증(Unauthenticated)"을 의미합니다. 클라이언트는 요청한 응답을 받기 위해서는 반드시
스스로 인증해야 합니다.`

3. 404 Not Found : `서버는 요청받은 리소스를 찾을 수 없습니다. 브라우저에서는 알려지지 않은
URL을 의미합니다. 이것은 API에서 종점은 적절하지만, 리소스 자체는 존재하지 않음을 의미할 수도 있습니다.
서버들은 인증받지 않은 클라이언트로부터 리소스를 숨기기 위하여 이 응답을 403(Forbidden) 대신에 전송할 수도 있습니다.`

<br>

##### 3) 서버 에러 응답

1. 500 Internal Server Error : `서버가 처리 방법을 모르는 상황이 발생했습니다. 서버는 아직 처리 방법을 알 수 없습니다.`


<br>
<br>

### 4. Python
***
* 20.08.31 피드백 : 함수명에는 return을 쓰지 말 것

##### 1) 모듈

1. Module : `A file containing a set of functions you want to include in your application.`

2. 사용 법 : `확장자 .py로 만든 후 import로 불러와서 사용하면 됨`
    - import [module]
        - module.py에 담긴 모든 모듈을 사용
        - 대신 module.method 형태로 사용해야함
        - method 말고도 class나 변수도 가져올 수 있음
    - from [module] import [method1], [method2] ...
        - module.py 안의 특정 메소드만 가져와서 사용
        - method 이름만 단독 사용 가능
    - from [module] import *
        - 전체 메소드 사용 가능

3. module.py에 출력이 있는 경우 import 하는 순간 module의 결과값이 출력됨.
    - 이 때 module.py 파일 안의 출력문에 if `__name__` == "`__main__`" : 사용
        - 직접 .py을 실행할 경우엔 if문이 참이 되어 출력문이 실행
            - `__name__` 안에 `__main__` 값이 저장 
        - import를 한 경우엔 거짓이 되어 출력문이 실행되지 않음
            - `__name__` 안에 모듈 이름 값 저장
    - `__name__` 변수 : `파이썬 내부적으로 사용하는 메서드`
    
4. 환경변수 PYTHONPATH : `디렉토리 이동 및 설정 시`
    
##### 2) 패키지

1. Package : `패키지(Packages)는 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다.
예를 들어 모듈 이름이 A.B인 경우에 A는 패키지 이름이 되고 B는 A 패키지의 B모듈이 된다.`
    > - 파이썬의 패키지는 디렉토리와 파이썬 모듈로 이루어진다.
    
    > 예시 1 ) import game.sound.echo
       : game.sound.echo.echo_test()                    
    > 
    > 예시 2 ) from game.sound import echo
       : echo.echo_test()
    >
    > 예시 3 ) from game.sound.echo import echo_test()
       : echo_test()
    >
    > - import를 하기 위해선 모듈이 있는 디렉토리로 접근해줘야함
    > - from이 아닌 import만 사용 시 마지막 항목은 반드시 모듈 또는 패키지여야 함.
 
2. `__init__.py`의 용도 : `해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.`

3. relative 패키지 : `한 모듈에서 다른 디렉토리의 모듈을 사용하고 싶을 때, import 해서 사용하면,
전체 경로를 입력하지 않아도 편히 사용 가능`

