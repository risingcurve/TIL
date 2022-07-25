def get_dict_avg(grades):
    return sum(grades.values()) / len(grades)


grades = {'python' : 80, 
          'web' : 83,
          'algorithm' : 90,
          'django' : 89}

print(get_dict_avg(grades))