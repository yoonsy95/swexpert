```python
import base64

case=int(input())

for i in range(case):
    s1=input()
    d = base64.b64decode(s1)
    s2 = d.decode("UTF-8")
    print(f'#{i+1} {s2}')
```

