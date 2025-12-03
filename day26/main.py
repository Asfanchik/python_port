# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict())
#TODO 1. Create a dictionary in this format:
phanetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(phanetic_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter u name: ").upper()
output_list = [phanetic_dict[letter] for letter in word]
print(output_list)
