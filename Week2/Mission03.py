import csv

file_path = "./data.csv"

def read_file(file_path):
    data_list = list()

    with open(file_path,"r") as data_file:
        csv_data = csv.reader(data_file)
        for row in csv_data:
            data_list.append(list(map(int,row)))
    
    return data_list

print(read_file(file_path))