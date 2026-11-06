    # Maak een boodschappenlijst
shopping_list = ["Brood", "Melk", "Eieren", "Kaas", "Appels"]

# Voeg twee producten toe
shopping_list.append("Bananen")
shopping_list.append("Yoghurt")

# Verwijder een product
shopping_list.remove("Kaas")

# Print het aantal producten
print("Aantal producten:", len(shopping_list))

# Print de boodschappenlijst
print("Boodschappenlijst:", shopping_list)

# Bonus: controleer of melk aanwezig is
if "Melk" in shopping_list:
    print("Melk staat op de boodschappenlijst!")