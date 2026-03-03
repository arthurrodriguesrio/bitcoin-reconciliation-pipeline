# Bitcoin Reconciliation Pipeline

End-to-end Bitcoin market data reconciliation pipeline built with Python.

## Overview

This project implements a modular data pipeline that:

- Ingests Bitcoin market data from an API
- Normalizes and validates the data
- Performs reconciliation logic
- Stores processed data
- Generates analytical outputs

The architecture follows a clean and modular structure inside the `src/` directory.

---

## Project Structure


bitcoin-reconciliation-pipeline/
│
├── data/ # Generated datasets
├── notebooks/ # Exploratory analysis
├── src/ # Core pipeline modules
│ ├── api_client.py
│ ├── normalizacao.py
│ ├── reconciliador.py
│ ├── database.py
│ ├── analytics.py
│ └── main.py
│
├── requirements.txt
└── README.md


---

## Technologies Used

- Python
- Pandas
- SQLite
- REST API integration

---

## How to Run

1. Install dependencies:


pip install -r requirements.txt


2. Run the pipeline:


python src/main.py


---

## Output

The pipeline generates reconciled Bitcoin market data stored in the `data/` directory.


## 🇧🇷 Versão em Português

### Visão Geral

Este projeto implementa um pipeline modular de dados que:

- Coleta dados de mercado de Bitcoin via API
- Normaliza e valida os dados
- Executa lógica de reconciliação
- Armazena os dados processados
- Gera análises

A arquitetura segue uma estrutura limpa e modular dentro do diretório `src/`.

---

### Como Executar

1. Instale as dependências:


pip install -r requirements.txt


2. Execute o pipeline:


python src/main.py


---

### Resultado

O pipeline gera dados reconciliados de mercado de Bitcoin armazenados no diretório `data/`.