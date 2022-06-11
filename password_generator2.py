#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print("Password includes: 8 letters, 4 symbols, 4 numbers")
nr_letters= 8
nr_symbols = 4
nr_numbers = 4

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
num = ""
for i in range(1,nr_letters+1):
    num = (random.choice(letters)) + num
let = num
#print(let)

num = ""
for i in range(1,nr_symbols+1):
    num = (random.choice(symbols)) + num
sym = num
#print(sym)

num = ""
for i in range(1,nr_numbers+1):
    num = (random.choice(numbers)) + num
nome = num
#print(nome)

last = let + sym + nome

last_l = list(last)
random.shuffle(last_l)
new_word = ''.join(last_l)

print("")
print(f"The password is:\n {new_word}")




