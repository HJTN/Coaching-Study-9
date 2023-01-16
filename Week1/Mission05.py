inputs = "cat32dog16cow5"

def find_string(inputs: str):
    nums = "1234567890"
    for num in nums:
        inputs = inputs.replace(num,' ')
    return inputs.split()

string_list = find_string(inputs)
print(string_list)