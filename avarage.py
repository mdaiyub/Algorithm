def Find_average(num):
    sum_num = 0
    for i in num:
        sum_num = sum_num + i           

    avg = sum_num / len(num)
    return avg
num = list(map(int, input(). split()))
print("The average is", Find_average(num))