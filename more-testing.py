def calcular_ranque(vitorias, derrotas):
    # Calcula o saldo de rankeadas
    saldo = vitorias - derrotas

    # Determina a classificação com base nas vitórias
    if vitorias < 10:
        rank = "Ferro"
    elif 11 <= vitorias <= 20:
        rank = "Bronze"
    elif 21 <= vitorias <= 50:
        rank = "Prata"
    elif 51 <= vitorias <= 80:
        rank = "Ouro"
    elif 81 <= vitorias <= 90:
        rank = "Diamante"
    elif 91 <= vitorias <= 100:
        rank = "Lendário"
    else:
        rank = "Imortal"
    
    return saldo, rank

# Exemplo de uso:
vitorias = 705
derrotas = 3
saldo, rank = calcular_ranque(vitorias, derrotas)
print(f"O Herói tem de saldo de **{saldo}** está no nível de **{rank}**")
