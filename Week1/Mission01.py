num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list):
    return [num for num in num_list if num % 2 == 1]

print(get_odd_num(num_list))