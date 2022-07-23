```
1.
a =int(input())

for i in range(1, a+1):
if a % i == 0:
print(i, end=' ')
```

```
2.
def recursive(numbers):
    print("===================")
    print('receive :', numbers)
    if len(numbers) < 2:
        print('end!!')
        return numbers.pop()
    else:
        pop_num = numbers.pop()
        print('pop num is : ',pop_num)
        print('rest list is : ',numbers)
        sum = pop+num + recursive(numbers)
        print('sum is : ', sum)
        return sum