dict_first = {'사과':30, '배':15, '감':10, '포도':10}
dict_second = {'사과': 5, '감':25, '배':15, '귤':25}

def merge_dict(dict_first: dict, dict_second: dict):
    for key in dict_second.keys():
        if key in dict_first.keys():
            dict_first[key] += dict_second[key]
        else:
            dict_first[key] = dict_second[key]
    
    return dict_first

result = merge_dict(dict_first, dict_second)
print(sorted(result.items()))