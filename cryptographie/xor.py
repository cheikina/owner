def xor_hex_strings(hex_str1, hex_str2):
    # Convertir les chaînes hexadécimales en entiers
    int1 = int(hex_str1, 16)
    int2 = int(hex_str2, 16)

    # Appliquer l'opération XOR sur les entiers
    result_int = int1 ^ int2

    # Convertir le résultat en chaîne hexadécimale
    result_hex = format(result_int, 'x')

    return result_hex


# Exemple d'utilisation
cipher_text1 = "0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d"
cipher_text2 = "684854016c4b0f006d190151555f513e495d0444694b50076f4105097019691c"
cipher_text3 = "4000036a1a005c6b1904531d3941055d"

result1 = xor_hex_strings(cipher_text1, cipher_text2)
result = xor_hex_strings(result1, cipher_text3)

print(f"ciphertext1 XOR ciphertext2 = {result}")
