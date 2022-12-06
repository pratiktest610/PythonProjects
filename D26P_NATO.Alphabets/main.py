import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
on = True
while on:
    word = input("Enter a Word: ")
    if word == "exit now":
        on = False
    else:
        letters = [letter.upper() for letter in word]
        code = [nato_dict[letter] for letter in letters]
        print(code)
        print(" ")

