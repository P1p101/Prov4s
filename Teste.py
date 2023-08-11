import pandas as pd
import pyautogui

baseDeDados = pd.read_excel(r"C:\trabalhos\BaseTeste.xlsx", engine='openpyxl')
print(baseDeDados)

totalGasto = baseDeDados["ValorFinal"].sum()
qtdadeComprada = baseDeDados["Quantidade"].sum()
precoMedio = totalGasto / qtdadeComprada

print("Total gasto:", totalGasto)
print("Quantidade comprada:", qtdadeComprada)
print(f"Preço médio dos produtos: {precoMedio:.2f}")