from name_function import *

print("Entrez q à tout moment pour quitter")
while True:
    first = input("\n Entrez votre nom de famille :")
    if first == 'q':
        break
    last = input("\n Entrez votre prénom :")
    if last == 'q':
        break

    formatted_name = get_formated_name(first, last)
    print(f"\t Nom complet : {formatted_name}.")
