input_raw = '112356'
INPUT = [i for i in input_raw]
result = True

for i in INPUT:
    INPUT.remove(str(i))
    if i in INPUT:
        result = False
        break
INPUT