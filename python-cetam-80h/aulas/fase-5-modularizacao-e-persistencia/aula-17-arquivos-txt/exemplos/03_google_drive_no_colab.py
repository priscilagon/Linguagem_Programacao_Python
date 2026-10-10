# Aula 17 | Somente no Colab: montar o Google Drive (não executa fora do Colab).

# Somente no Google Colab: salvar arquivos no seu Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Depois use caminhos como:
# '/content/drive/MyDrive/agencia_tur/clientes.txt'
