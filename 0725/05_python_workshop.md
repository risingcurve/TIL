```
1.
def get_dict_avg(grades):
    return sum(grades.values()) / len(grades)

grades = {'python' : 80, 
          'web' : 83,
          'algorithm' : 90,
          'django' : 89}

print(get_dict_avg(grades))
```

```
2.
def count_blood(blood_list):

    return {'A' : blood_list.count('A'), 
            'B' : blood_list.count('B'), 
            'O' : blood_list.count('O'), 
            'AB' : blood_list.count('AB')}


blood_list = ['A', 'B', 'A', 'O', 'AB', 'AB', 
              'O', 'A', 'B', 'O', 'B', 'AB']

print(count_blood(blood_list))
```