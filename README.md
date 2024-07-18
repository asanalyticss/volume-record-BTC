# volume-record-BTC
Este projeto registra o volume de negociação do par BTC/USDT na corretora Binance a cada 10 minutos e armazena os dados em um banco de dados SQLite.

Requisitos
Python 3.7 ou superior
Bibliotecas Python:
requests
sqlite3
time
datetime

git clone https://github.com/seu-usuario/btc-volume-tracker.git
cd btc-volume-tracker

Estrutura do Banco de Dados
A tabela btc_volume tem os seguintes campos:

timestamp: Marca temporal do registro (INTEGER)
volume: Volume de negociação do BTC/USDT (REAL)
data: Data do registro (DATE)
hora: Hora do registro (TIME)


OBS: O ideal é subir para um servidor na nuvem para deixar o código rodando 24hrs e também manter armazenamento na nuvem do registro de cotação a cada 10min para futuramente tirar uma média dessas cotações com desvio padrão

Objetivo é ter um indicador de aumento de volume correlacionado com os movimento futuro dos preços 
