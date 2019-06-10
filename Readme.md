## Django (디장고)

* **DJango의 구조**
  * **M (Model):** Database 관리 / 테이블을 정의하는 모델
  * **T (Templates):** 사용자가 보게 될 화면의 모습을 정의
  * **V (View):** 앱의 제어 흐름 및 처리 로직을 정의

---



* **Django 설정방법**

  **1) 설치명령어**

  ```python
  pip install django
  ```

  **2) 장고 intro 설정**

  ```python
  django-admin startproject intro
  ```

  **3) 서버 시작하기**

  ```python
  python manage.py runserver
  ```

  **4) 새로운 페이지 만들기**

  ```python
  python manage.py startapp '페이지 이름'
  ```

---



* **Django 페이지 구조**

  * **admin.py:** 전체 관리 페이지를 만드는 페이지
  * **urls.py** (flask의 app.route와 동일한 역할): 문지가 같은 역할

  ```python
  from django.contrib import admin
  from django.urls import path
  
  # pages에서 views를 불러오기
  from pages import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('index/', views.index),
      path('hola/', views.hola),
  ]
  ```

  * **views.py** (flask의 app.route 하단의 def와 동일한 역할): 중간 관리자 페이지를 만드는 페이지

---



* **페이지 관리 (settings.py에서 설정)**

  * settings.py에서 **'INSTALLED_APPS'**에 만든 페이지 이름을 등록한다.

    ```python
    INSTALLED_APPS = [
        'pages',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```

  * 언어 설정 및 시간 설정

    ```python
    LANGUAGE_CODE = 'ko-kr'
    TIME_ZONE = 'Asia/Seoul'
    ```

---

## **Django의 template_language**

```html
<h3>1. 반복문</h3>
{% for menu in menus %}
    <p>{{ menu }}</p>
{% endfor %}
<hr>

{% for menu in menus %}
    <p>{{ forloop.counter }}, {{ menu }}</p>
{% endfor %}
<hr>

{% for user in empty_list %}
    <p>{{ user }}</p>
{% empty %}
    <p>현재 가입한 유저가 없습니다.</p>
{% endfor %}
<hr>

<h3>2. 조건문</h3>
{% if '짜장면' in menus %}
    <p>짜장면에는 고추가루지!!</p>
{% endif %}
<hr>

{% for menu in menus %}
    {{ forloop.counter }}번째 도는중...
    {% if forloop.first %}
        <p>짜장면 + 고추가루</p>
    {% else %}
        <p>{{ menu }}</p>
    {% endif %}
{% endfor %}
<hr>

<h3>3. length filter 활용</h3>
{% for message in messages %}
    {% if message|length > 5 %}
        <p>글씨가 너무 길어요...</p>
    {% else %}
        <p>{{ message }}, {{ message|length }}</p>
    {% endif %}
{% endfor %}
<hr>

<h3>4. lorem</h3>
{% lorem %}
<hr>

{% lorem 3 w %}
<hr>

{% lorem 4 w random %}
<hr>

{% lorem 3 p %}
<hr>

<h3>5. 글자수 제한(truncate)</h3>
<p>{{ my_sentence|truncatewords:3 }}</p>
<p>{{ my_sentence|truncatechars:3 }}</p>
<p>{{ my_sentence|truncatechars:10 }}</p>
<hr>

<h3>6. 글자 관련 필터</h3>
<p>{{ 'abc' | length }}</p>
<p>{{ 'ABC' | lower }}</p>
<p>{{ my_sentence | title }}</p>
<p>{{ menus | random }}</p>
<hr>

<h3>7. 연산</h3>
<p>{{ 4 | add:6 }}</p>
<hr>

<h3>8. 날짜표현</h3>
{{ datetimenow }}<br>
{% now 'DATETIME_FORMAT' %}<br>
{% now 'SHORT_DATETIME_FORMAT' %}<br>
{% now 'DATE_FORMAT' %}<br>
{% now 'SHORT_DATE_FORMAT'%}<br>
<hr>

{% now 'Y년 m월 d일 (D)' %}
<hr>

{% now 'Y' as current_year %}
Copyright {{ current_year }}
<hr>

{{ datetimenow | date:'SHORT_DATE_FORMAT' }}
<hr>

<h3>9. 기타</h3>
{{ 'google.com' | urlize }}
<hr>
```

---

## **form 구문**

* **Django에서 서버로 요청을 보낼 때 필요한 구문**
  * get: 원하는 자료를 요청하는 것 (주로 html 문서를 요청함)
  * post: DB를 통해서 원하는 자료를 요청하는 것
  
  ---

## **1. Class (클래스)**

```python
class Person:
    name = '사람의 고유한 속성'
    age = '충생 이후부터 삶을 마감할 때까지의 시간'

    def greeting(self):
        print(f'{self.name}이 인사합니다. 안녕하세요')

    def eating(self):
        print(f'{self.name}은 밥을 먹고 있습니다.')

    def aging(self):
        print(f'{self.name}은 현재 {self.age}살이고, 현재 노화가 진행중입니다.')

kyd = Person()
print(kyd.name)
print(kyd.age)

kyd.name = 'KYD'
kyd.age = 17

print(kyd.name)
print(kyd.age)

kyd.greeting()
kyd.eating()
kyd.aging()
```





**1-1.  Board(게시판) Class (클래스) 만들기**

```python
from django.db import models

# 게시판 만들기
class Board(models.Model):
    # 제목
    # CharField -> max_length: 글자수 제한 설정
    title = models.CharField(max_length=10)

    # 내용
    content = models.TextField()

    # 게시글 작성시간
    # DateTimeField -> auto_now_add: 최초작성 시간 (불변)
    created_at = models.DateTimeField(auto_now_add=True)

    # 게시글 수정시간
    # DateTimeField -> auto_now: 수정 시간 (가변)
    updated_at = models.DateTimeField(auto_now=True)
```



**1-2.  명령어**

* **아래는 장고 Shell을 호출하는 명령어이다.**
* **장고 명령어는 python 기본 interpreter와 같은 역할을 하지만, 장고 안에서 DB도 조작할 수 있는 기능도 가지고 있다.**

```python
python manage.py shell
```

* **Board 클래스를 호출하는 명령어**



* **Object 관리 명령어**

```python
Board.objects.all()
```

---

## **CRUD (CREATE, READ, UPDATE, DELETE)**

## **1. CREATE: DB에 데이터 추가하기**

```python
# 1. 개별로 만들기
board = Board()
board.title = 'first'
board.content = 'django!'
board.save() # save() 필수!!!!!!


# 2. 한줄로 만들기
board = Board(title = 'second', content = 'django!')
board.save() # save() 필수!!!!!!


# 3. save() 명령어 없이 바로 DB에 반영하기
Board.objects.create(title='third', content='django!')


```

## **2. READ: DB 데이터  읽어오기**

```python
Board.objects.all()

# <QuerySet [<Board: Board object (1)>, <Board: Board object (2)>, <Board: Board object (3)>]>
```

```python
board.title = 'asdfasdfasdf'
board.full_clean()

# Board Class에 제목 글자수를 10자로 제한하여 발생한 오류
'''
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\multicampus\TIL\venv\lib\site-packages\django\db\models\base.py", line 1203, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'title': ['이 값이 최대 10 개의 글자인지 확인하세요(입력값 12 자).'], '
content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
'''
```



* **저장한 DB를 text형태 (string)로 불러오는 함수**

```python
# <QuerySet [<Board: Board object (1)>, <Board: Board object (2)>, <Board: Board object (3)>]>

from django.db import models

# 게시판 만들기
    # <QuerySet [<Board: Board object (1)>, <Board: Board object (2)>]>
    # 이처럼 뜨는 DB 내용을 str 타입으로 보여주기 위한 함수
    # 함수 앞에 __(text)__ : magic method라고 불리며 특수한 기능을 가지고 있음
    def __str__(self):
        return f'{self.id}번글 - {self.title} : {self.content}'
```

* **저장한 DB를 text형태로 불러오기**
  * **.filter():** 다수의 값을 가져올 때 사용
  * **.get():** 유일한 값 1개를 가져올 때 사용

```python
## title이 first인 DB만 가져오기
boards = Board.objects.filter(title = 'first')

# <QuerySet [<Board: 1번글 - first : django!>, <Board: 5번글 - first : hahaha>]>

## title이 first인 DB 1개 앞에서 가져오기
# SELECT * FROM boards WHERE title = 'first' LIMIT 1;
Board.objects.filter(title = 'first').first()

## title이 first인 DB 1개 뒤에서 가져오기
Board.objects.filter(title = 'first').last()

## Primary Key(PK)가 1번인 DB 가져오기
# SELECT * FROM boards WHERE id = 1
Board.objects.get(pk=1)

## get() 명령어는 유일한 값 1개만 호출할 수 있다.
Board.objects.get(title='first')
# boards.models.Board.MultipleObjectsReturned: get() returned more than one Board -- it returned 2!
Board.objects.get(pk=1)
# <Board: 1번글 - first : django!>

## order_by('title'): 오름차순으로 가져오기
# order_by('-title'): 내림차순으로 가져오기
# SELECT * FROM boards ORDER BY title ASC;
Board.objects.order_by('title').all() # 오름차순
Board.objects.order_by('-title').all() # 내림차순

## DB 데이터를 슬라이스하기
Board.objects.all()[2]
Board.objects.all()[1:3]

```

## **3. UPDATE: DB 데이터  수정하기**

```python
# UPDATE boards SET title='byebye' WHERE id = 1
# 1.
board = Board.objects.get(pk=1)
# <Board: 1번글 - first : django!>

# 2.
board.title = 'byebye'
board.save()
# <Board: 1번글 - byebye : django!>
```

---

## **4. DELETE: DB 데이터 삭제하기**

```python
## DB 내용 삭제하기
board = Board.objects.get(pk=1)
board.delete()
# (1, {'boards.Board': 1})
```



### **POST 방식으로 바꾸기**

![image](https://user-images.githubusercontent.com/42408554/59167181-e79b0000-8b6a-11e9-9601-218ea15bfe3b.png)



![image](https://user-images.githubusercontent.com/42408554/59167233-33e64000-8b6b-11e9-9262-0db7e6bb3dea.png)



---

## **5. redirect 함수**

* **redirect 함수를 사용하지 않으면, '글쓰기' 페이지로 다시 이동하기가 어렵다. 따라서 게시글을 작성한 후, 바로 메인 페이지로 이동할 수 있도록 redirect 함수를 사용한다.**

![image](https://user-images.githubusercontent.com/42408554/59167270-55dfc280-8b6b-11e9-9e90-9edd4daa9b15.png)