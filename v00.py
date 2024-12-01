import secrets
import matplotlib.pyplot as plt
from collections import Counter

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

# Gera 1000 códigos
codes = [generate_secure_verification_code() for _ in range(1000)]

# Conta a frequência de cada código
frequency = Counter(codes)

# Plota o histograma
plt.figure(figsize=(12, 6))
plt.bar(frequency.keys(), frequency.values(), color='skyblue')
plt.xlabel('Código de Verificação')
plt.ylabel('Frequência')
plt.title('Distribuição de Códigos de Verificação Gerados')
plt.xticks(rotation=90, fontsize=8)  # Rotaciona os rótulos para caberem no gráfico
plt.tight_layout()
plt.show()
