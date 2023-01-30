import csv

file_path = "./data.csv"

class ReadCSV(object):
    def __init__(self, file_path):
        self._file_path = file_path
        self._data_list = list()
        self._merge_list = list()
        
    def read_file(self):
        try:
            with open(self._file_path,"r") as data_file:
                csv_data = csv.reader(data_file)
                for row in csv_data:
                    self._data_list.append(list(map(int,row)))
        except FileNotFoundError:
            print("Check your file path!")
        
        return self._data_list
    
    def merge_list(self):
        for data in self._data_list:
            self._merge_list.append(sum(data))
        
        return self._merge_list

read_csv = ReadCSV(file_path)
print(read_csv.read_file(),'\n')
print(read_csv.merge_list())