import pandas as pd

url = 'https://raw.githubusercontent.com/ClarityCoders/CodingChallenge1/master/spam.csv'
df = pd.read_csv(url,  encoding="ISO-8859-1")

#print(df['v2'])

characters = {}

for row in df['v2']:
    # print(row)
    for letter in row:
        letter = letter.lower()
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1

sort_characters = sorted((value, key) for (key, value) in characters.items() )
# print(sort_characters)

index = -1
for i in range(5):
    print(f'{i+1} - {sort_characters[index][1]}')
    index -= 1

