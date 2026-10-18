import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados da temporada 2024/25

url = "https://www.football-data.co.uk/mmz4281/2425/E0.csv"

# 2. Selecionar e renomear colunas

jogos = pd.read_csv(url)

jogos = jogos[["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"]]

jogos = jogos.rename(columns={
    "Date": "data",
    "HomeTeam": "mandante",
    "AwayTeam": "visitante",
    "FTHG": "gols_casa",
    "FTAG": "gols_fora",
    "FTR": "resultado",
})

# 3. Converter a coluna de data

jogos["data"] = pd.to_datetime(jogos["data"], dayfirst=True)

# 4. Calcular o percentual de cada resultado

contagem = jogos["resultado"].value_counts()

percentual = jogos["resultado"].value_counts(normalize=True) * 100

percentual = percentual.rename({"H": "Mandante", "D": "Empate", "A": "Visitante"})

percentual = percentual.reindex(["Mandante", "Empate", "Visitante"])

# 5. Gerar e salvar o gráfico

plt.figure(figsize=(8, 5))
sns.barplot(x=percentual.index, y=percentual.values)
plt.title("Resultados da Premier League 2024/25 (%)")
plt.ylabel("% dos jogos")
plt.xlabel("")
plt.savefig("imagens/resultados.png")
plt.show()