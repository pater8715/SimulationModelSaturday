word = input(" Introduce una palabra: ")
reversed_word = word 
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palindromo")
else:
    print("No es un palindromo")