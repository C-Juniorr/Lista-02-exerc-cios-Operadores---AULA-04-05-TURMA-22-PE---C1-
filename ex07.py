
idade_motorista = int(input("Qual a sua idade? "))
tem_carteira_str = input("Você tem carteira de motorista? (True/False ou Sim/Nao) ")
tem_carteira = parse_bool(tem_carteira_str)

pode_dirigir = (idade_motorista >= 18) and tem_carteira
print(f"Pode dirigir? {pode_dirigir}")
