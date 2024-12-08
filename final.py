import pandas
file_path = "D:/Python/100 days Python Challenge/Intermediate/day 26/nato_phonetic_alphabet.csv"

file = pandas.read_csv(file_path)
nato_dic = {row.letter:row.code for (index, row) in file.iterrows()}

# solution
user_name = "Tillo"
result =[nato_dic[letter.upper()] for letter in user_name]
print(result)
