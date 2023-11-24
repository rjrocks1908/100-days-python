import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

alpha_name_dic = {row["letter"]: row["code"] for index, row in df.iterrows()}

while True:
    try:
        name = input("Enter a word: ").upper()
        code_list = [alpha_name_dic[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        break

print(code_list)
