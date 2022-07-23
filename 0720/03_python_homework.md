1.

```
builtin_f = ['abs()', 'all()', 'id()', 'open()', 'print()']
```


2.
```
odd = range(1,51)

list_odd = list(odd)

print(list_odd[0:49:2])
```


3.
```
n = 5
m = 9

for i in range(m):
for j in range(n):
print('*', end='')
print()
```


4.
```
temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실 가능')
```


5.
```
def get_middle_char(str):
return str[(len(str)-1)//2:len(str)//2+1]
```
