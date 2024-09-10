def contar_letra_a(texto):
    return texto.lower().count('a')

# Exemplo de uso
texto = input("Digite uma string para contar a ocorrência da letra 'a': ")
quantidade = contar_letra_a(texto)
print(f"A letra 'a' ocorre {quantidade} vezes.")