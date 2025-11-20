import random
import string

chars = " " + string.punctuation + string.ascii_letters + string.digits

chars = list(chars)
keys = chars.copy()
random.shuffle(keys)




plain_texts = input("Enter the text you want to encrypt:  ")

return_texts = ""

for letter in plain_texts: 

    index_number = chars.index(letter)

    return_texts = return_texts + keys[index_number]

print(f"original message : {plain_texts}")    
print(f"Encrypted message: {return_texts}")







