import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet1.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
on = True
while on:
    word = input("Enter a Word: ")
    if word == "exit now":
        on = False
    else:
        letters = [letter.upper() for letter in word]
        try:
            code = [nato_dict[letter] for letter in letters]
        except KeyError:
            print("Please only enter alphabets in your word.")
        else:
            print(code)
        finally:
            print(" ")
