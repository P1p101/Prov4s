import statistics


def calcular_media(p_valores):
    p_media = statistics.mean(p_valores)
    return p_media


def calcular_mediana(p_valores):
    p_mediana = statistics.median(p_valores)
    return p_mediana


def calcular_desvio_padrao(p_valores):
    p_desvio_padrao = statistics.stdev(p_valores)
    return p_desvio_padrao


valores = []
qtde_valores = int(input('Digite a quantidade de valores: '))
for i in range(qtde_valores):
    valor = float(input('Digite um valor: '))
    valores.append(valor)

media = calcular_media(valores)
mediana = calcular_mediana(valores)
desvio_padrao = calcular_desvio_padrao(valores)

print('A média é:', media), print('A mediana é:', mediana), print('O desvio padrão é:', desvio_padrao)
