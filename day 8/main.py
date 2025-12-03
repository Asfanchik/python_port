# def gree():
#     print("Hello James ")
#     print("How are you ??")
#     print("How do you do")
# greet()
#
# def greet_whith_name(name):
#     print(f"HEllo {name}")
#     print(f"How are you{name}?")
# greet_whith_name("Jacob")
# def greet_with(name, location):
#     print(f"Hello {name}")#
#     print(f"What is the like in {location} ?")
# name1 = input("Enter name - ")
# loc1 = input("Enter adress - ")
# greet_with(name1, loc1)
# import math
# def paint_calc(height, width, cover):
#     area = height * width
#     num_of_calc = math.ceil(area / cover)
#     print(f"You need - {num_of_calc}")


# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)\



# Programa dlya proverki chisal chot ili ne chot
# def prime_checker(number):
#     chot = True
#     for i in range(2, number):
#        if number % i ==0:
#            chot = False
#     if chot :
#         print("it's prime number")
#     else:
#         print("Not prime number")
#
#
#
# n = int(input("Check this number"))# vvod chisla
# prime_checker(number=n)# ssilka na kod proverki chisla
# alphabet = ['a', 'b', 'c', 'd', 'e', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#             'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#             'u', 'v', 'w', 'x', 'y', 'z']
#
# direct = input("Type 'encode' to encript, type 'decode' to decript:\n")
# text = input("Type your massage:\n").lower() #vvod texta
# shift = int(input("Type the shift number ")) # na skolko strochek delat otstup
#
# def encript(plain_text, shift_amount):
#     cipher_text = "" #prosto est
#     for letter in plain_text:
#          position = alphabet.index(letter)
#          new_position = position + shift_amount
#          new_letter = alphabet[new_position]
#          cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
# encript(plain_text=text, shift_amount=shift)
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#             'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#             'u', 'v', 'w', 'x', 'y', 'z']
#
# direct = input("Type 'encode' to encript, type 'decode' to decript:\n")
# text = input("Type your massage:\n").lower() #vvod texta
# shift = int(input("Type the shift number ")) # na skolko strochek delat otstup
#
# def encript(plain_text, shift_amount): # za kodir
#     cipher_text = "" #prosto est
#     for letter in plain_text:
#          position = alphabet.index(letter)
#          new_position = position + shift_amount
#          new_letter = alphabet[new_position]
#          cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
# def decript(cipher_text, shift_amount): # raz kodir
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text} ")
#
# if direct == "encode":
#     encript(plain_text=text, shift_amount=shift)# naprovitel
# elif direct == "decode":
#     decript(cipher_text=text, shift_amount=shift)
# uproshenaya versiya previdushego
# alphabet = ['a', 'b', 'c', 'd', 'e', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#             'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#             'u', 'v', 'w', 'x', 'y', 'z']
#
# direct = input("Type 'encode' to encript, type 'decode' to decript:\n")
# text = input("Type your massage:\n").lower() #vvod texta
# shift = int(input("Type the shift number ")) # na skolko strochek delat otstup
#
# def caesar(inp_text, shift_amount, cipher_direct):
#     end_text = ""
#     if cipher_direct == "decode":
#         shift_amount *= -1 # shift_amount = shift_amaunt * -1
#     for letter in inp_text: #dlya kajdoy bukvi v vvedenom texte
#         position = alphabet.index(letter) # nayti v texte
#         new_position = position + shift_amount #kodirovka
#         end_text += alphabet[new_position] #za / razkodirovaniy text
#     print(f"Here is the {direct}d result: {end_text} - ")
#
# caesar(inp_text=text, shift_amount=shift, cipher_direct=direct) #ssilki na input


alphabet = ['a', 'b', 'c', 'd', 'e', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


# decoder
def caesar(start_text, shift_amount, cipher_direct):
    end_text = ""
    if cipher_direct == "decode":
        shift_amount *= -1
    for chr in start_text:
        if chr in alphabet:
            position = alphabet.index(chr)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += chr
    print(f"Here is the {cipher_direct}d result: {end_text}")
 # repeat or no
should_continue = True
while should_continue:
    direct = input("Type 'encode' to encript, type 'decode' to decript:\n")
    text = input("Type your massage:\n").lower() #vvod texta
    shift = int(input("Type the shift number ")) # na skolko strochek delat otstup

    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direct=direct)

    result = input("If you want again type 'yes', if not type 'no'.\n ")
    if result == "no":
        should_continue = False
        print("GOOD BYE")
