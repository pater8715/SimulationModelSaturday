palab = input("Introduce una palabra: ")
reversed_palab = palab
palab = list(palab)
reversed_palab = list(reversed_palab)
reversed_palab.reverse()
if palab == reversed_palab:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")