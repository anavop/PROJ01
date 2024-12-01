import os
import secrets


def generate_secure_verification_code():
    # Gera números aleatórios seguros
    potencia = secrets.randbelow(100) + 1  # Entre 1 e 100
    numero = secrets.randbelow(100) + 1   # Entre 1 e 100
    modulo = secrets.randbelow(9) + 1     # Entre 1 e 9

    # Calcula os dígitos usando operações seguras
    digt1 = numero % modulo
    digt2 = potencia % modulo
    digt3 = modulo
    digt4 = pow(potencia, numero, modulo)  # Usa pow com módulo diretamente

    # Calcula o dígito final
    digt5 = (digt1 * 1 + digt2 * 2 + digt3 * 3 + digt4 * 4) % modulo

    # Retorna o código como uma string única
    return f"{digt1}{digt2}{digt3}{digt4}{digt5}"

# Gera e exibe o código de verificação seguro
verification_code = generate_secure_verification_code()
print("Código de Verificação Seguro:", verification_code)
