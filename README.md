# Pipeline de Dados: Integração Postgres com Airflow e Docker

Este projeto foi desenvolvido como parte do desafio técnico da Lighthouse. O objetivo foi criar um fluxo automático (ETL) para migrar dados de clientes entre dois bancos de dados PostgreSQL, garantindo que o processo seja seguro e organizado.

## 🛠️ Tecnologias Utilizadas
* **Orquestração:** Apache Airflow (Astro CLI)
* **Ambiente:** Docker e Docker Compose
* **Bancos de Dados:** PostgreSQL (Instâncias Source e Target)
* **Ferramenta de Query:** DBeaver
* **Linguagem:** Python (Pandas)

## ⚙️ Como o projeto funciona
O pipeline foi estruturado em três etapas principais dentro de uma DAG:

1. **Extração:** O sistema conecta no banco de origem e captura a tabela de clientes.
2. **Staging:** Para garantir a segurança, os dados são salvos primeiro em um arquivo CSV local. Isso serve como um backup antes da carga final.
3. **Carga:** O Airflow lê esse arquivo CSV e insere as informações no banco de destino.

## 🚀 Desafios e Aprendizados
Durante o desenvolvimento, precisei lidar com situações reais que acontecem no dia a dia de quem trabalha com dados:

* **Conexão de Rede no Docker:** Configurei a comunicação entre os containers usando portas específicas (5433 e 5434). Também precisei ajustar os hosts conforme o IP da rede local mudava para manter o fluxo ativo.
* **Integridade dos Dados:** Gerenciei erros de chaves duplicadas (Primary Key) para garantir que o banco de destino não ficasse com registros repetidos.
* **Manutenção com DBeaver:** Usei a ferramenta para validar se as tabelas estavam corretas e para limpar o banco (Truncate/Delete) durante os testes de carga.

## 📊 Resultado Final
O pipeline foi testado e validado, completando todas as etapas com sucesso conforme a imagem abaixo:
<img width="1900" height="898" alt="Captura de tela 2026-03-12 162835" src="https://github.com/user-attachments/assets/12079b04-4f10-4e7f-ad01-6bffadc12646" />



---
**Projeto desenvolvido por Agatha Luiza**
