hex_number = "0x555555556013"
decimal_number = int(hex_number, 16)
print("Le nombre décimal correspondant est :", decimal_number)
resultat=bytes.fromhex("0040202018").decode("utf-8")
print(resultat)
hex_string ="e"
hex_string1 = "2dc6"  # Remplacez cela par votre chaîne hexadécimale
hex_string2 = "1fbc"  # Remplacez cela par votre chaîne hexadécimale

decimal_number = int(hex_string, 16)
decimal_number1 = int(hex_string1, 16)
decimal_number2 = int(hex_string2, 16)
print(decimal_number)
print(decimal_number1-decimal_number2)