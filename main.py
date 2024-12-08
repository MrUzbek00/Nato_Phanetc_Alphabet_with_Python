# Simple List comprehension      new_list_veriable = [item for item in iterable_type] 
# List comprehenion with condition new_list_veriable = [item for item in iterable_type if condition]
# Dictionary comprehension 
    # new_dic_veriable = {new_ky:new_value for item in the list}
    # new_dic_veriable = {new_ky:new_value for (key,value) in existing_dic.items()}
    # new_dic_veriable = {new_ky:new_value for (key,value) in existing_dic.items() if condition}

import random
import pandas
number_list = [1,2,3]
new_list = [num +1 for num in number_list]
#print(new_list)
name = "Tillo"
new_name  = [letter for letter in name]
#print(new_name)
ran_list = [num*2 for num in range(1,5)]
print(ran_list)

names_list = ["Tillo", "Bekmirza","John", "Javohir", "Holiddin", "Bek", "Tom"]

new_names =[name.upper() for name in names_list if len(name) <= 5 ]
# print(new_names)

def test():
        
    with open("D:/Python/100 days Python Challenge/Intermediate/day 26/file1.txt", "r") as file1:
        num_list1 = file1.readlines()
        print(num_list1)
        num_list1 = [num.strip() for num in num_list1]
        print(num_list1)
        num_list1 = [int(num) for num in num_list1 if num != ""]
        print(num_list1)


    with open("file2.txt", "r") as file2:
        num_list2 = file2.read()
        
    result = [common_num for common_num in num_list1 if common_num in num_list2] 

names_list = ["Tillo", "Bekmirza","John", "Javohir", "Holiddin", "Bek", "Tom"]

name_score = {key_name:random.randint(1,100) for key_name in names_list}
passed_names ={key_name:value for (key_name, value) in name_score.items() if value > 70}
#Simple looping in dictionary 
# for key, value in passed_names.items():
#     #print(value) 
#         pass

simple_dict_frame= {
     "students": ["Tillo", "Bekmirza","John", "Javohir", "Holiddin", "Bek", "Tom"],
     "score" : [98, 48, 56, 70, 80, 85, 45] 
} 

pandas_df = pandas.DataFrame(simple_dict_frame)

#looping through simply data_frame

#for k, v in pandas_df.items():
    #print(k)
    #result
    # students
    #score
#     print(v)
#     0       Tillo
# 1    Bekmirza
# 2        John
# 3     Javohir
# 4    Holiddin
# 5         Bek
# 6         Tom
# Name: students, dtype: object
# 0    98
# 1    48
# 2    56
# 3    70
# 4    80
# 5    85
# 6    45
# Name: score, dtype: int64
    # Lopping through rows in data frame

for index, row in pandas_df.iterrows():
    #print(row)
    #print(index)
    if row.students == "Tillo": #row data type is pandas object with access to its "methods"
        print(row.score)
