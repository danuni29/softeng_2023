### 응소 week 2

_______

예외처리
```python

while True:
    try:
        x = int(input("값을 입력하세요"))
        break
    except ValueError:
        print("숫자만 입력해주세요")

```

rich

 터미널에서 풍부한(rich) 텍스트와 아름다운 서식을 지원하기 위한 파이썬 라이브러리