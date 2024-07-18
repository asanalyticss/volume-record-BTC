import requests
import sqlite3
import time
from datetime import datetime

# Função para obter o volume do BTC/USDT da Binance
def get_btc_usdt_volume():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    params = {"symbol": "BTCUSDT"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return float(data["volume"])
    else:
        return None

# Função para criar uma tabela no banco de dados SQLite se ela não existir
def create_table_if_not_exists(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS btc_volume (
            timestamp INTEGER PRIMARY KEY,
            volume REAL,
            data DATE,
            hora TIME
        )
    """)
    conn.commit()

# Função para inserir dados no banco de dados SQLite
def insert_data(conn, timestamp, volume, data, hora):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO btc_volume (timestamp, volume, data, hora) VALUES (?, ?, ?, ?)", (timestamp, volume, data, hora))
    conn.commit()

# Loop principal
if __name__ == "__main__":
    conn = sqlite3.connect("btc_volume.db")
    create_table_if_not_exists(conn)

    while True:
        timestamp = int(time.time())
        volume = get_btc_usdt_volume()
        data_hora_atual = datetime.now()
        data = data_hora_atual.strftime("%Y-%m-%d")
        hora = data_hora_atual.strftime("%H:%M:%S")

        if volume is not None:
            insert_data(conn, timestamp, volume, data, hora)
            print(f"Registrado em Data: {data} Hora: {hora}, Volume do BTC/USDT: {volume:.2f}")

        time.sleep(600)  # Aguarda 10 minutos (600 segundos)
