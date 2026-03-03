
from api_client import get_bitcoin_prices
from normalizacao import normalize
from analytics import calculate_returns
from reconciliador import simulate_second_source, reconcile
from database import save_to_db

def main():
  # 1. Buscar dados
  df = get_bitcoin_prices(30)

  # 2. Normalizar
  df = normalize(df)

  # 3. Calcular retorno
  df = calculate_returns(df)

  # 4. Simular segunda fonte
  df2 = simulate_second_source(df)

  # 5. Reconciliar
  result = reconcile(df, df2)

  # 6. Salvar CSV
  result.to_csv("resultado_final.csv", index=False)

  # 7. Salvar no banco
  save_to_db(result)

  print("Executado com sucesso")

if __name__ == "__main__":
  main()
