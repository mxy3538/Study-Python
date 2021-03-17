TempStr = input()
result = 0
if TempStr[0:1] == "C":
    result = eval(TempStr[1:]) * 1.8 + 32
    print("F%.2f"%result)
elif TempStr[0:1] == "F":
    result = (eval(TempStr[1:]) - 32) / 1.8
    print("C%.2f"%result)
