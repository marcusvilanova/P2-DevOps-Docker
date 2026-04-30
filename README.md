# 🚀 DimDim - Checkpoint 2 DevOps & Cloud Computing

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)

Este projeto apresenta a migração de uma aplicação legada para uma arquitetura moderna baseada em containers na nuvem **Microsoft Azure**, utilizando o conceito de **Docker One**.

---

## 👥 Integrantes do Grupo (2TDSR - FIAP)
*   **HEBERT LOPES** - RM: 563192
*   **MARCUS VILA NOVA** - RM: 558771
*   **NICOLAS RAMIRO** - RM: 562380

---

## 📺 Demonstração
*   **Vídeo do Projeto:** [Assista aqui no YouTube](https://youtu.be/9I4pvTSLmTk?si=wmFIUZhmPoKtZXxR)
*   **IP Público da VM (Azure):** `20.63.36.109`

---

## 🏗️ Arquitetura do Projeto
A stack tecnológica foi orquestrada via **Docker Compose**, garantindo isolamento e persistência:

*   **Frontend/Backend:** Python Flask rodando em container.
*   **Banco de Dados:** MySQL 8.0 com persistência via **Named Volumes**.
*   **Infraestrutura:** VM Azure (Ubuntu 24.04 LTS) com configuração de **SWAP** para estabilidade.

---

## 🛠️ Como Rodar o Projeto

### Pré-requisitos
*   Docker instalado
*   Docker Compose instalado

### Passo a Passo
1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/marcusvilanova/P2-DevOps-Docker.git
    cd P2-DevOps-Docker
    ```

2.  **Suba os containers:**
    ```bash
    sudo docker-compose up -d --build
    ```

3.  **Acesse a aplicação:**
    Abra o navegador em `http://localhost:80` (ou o IP da máquina: http://20.63.36.109:80).

---

## 🧪 Funcionalidades Testadas (CRUD)
- [x] **Create:** Adição de novos usuários ao banco MySQL.
- [x] **Read:** Listagem em tempo real dos registros.
- [x] **Update:** Edição de dados existentes.
- [x] **Delete:** Remoção de registros.
- [x] **Persistência:** Os dados sobrevivem ao comando `docker-compose down`.

---

## 📄 Licença
Este projeto foi desenvolvido para fins acadêmicos na **FIAP**.
