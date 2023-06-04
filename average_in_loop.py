count = 0
sum = 0
print('Before', count, sum)
for value in [9,12,6,4,8,36,14] :
    count = count +1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)