num_list = [1,2,1,5,6,10]
unique = []

for number in num_list:
    if number not in unique:
        unique.append(number)
        print(unique)