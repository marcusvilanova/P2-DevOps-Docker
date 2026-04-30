🚀 DimDim - Checkpoint 2 DevOps & Cloud Computing


Este projeto apresenta a migração de uma aplicação legada para uma arquitetura moderna baseada em containers na nuvem Microsoft Azure, utilizando o conceito de Docker One.


👥 Integrantes do Grupo (2TDSR - FIAP)

• HEBERT LOPES - RM: 563192

• MARCUS VILA NOVA - RM: 558771

• NICOLAS RAMIRO - RM: 562380



📺 Demonstração

• Vídeo do Projeto: https://youtu.be/9I4pvTSLmTk

• IP Público da VM (Azure): 20.63.36.109




🏗️ Arquitetura do Projeto

A stack tecnológica foi orquestrada via Docker Compose, garantindo isolamento e persistência:

• Frontend/Backend: Python Flask rodando em container.

• Banco de Dados: MySQL 8.0 com persistência via Named Volumes.

• Infraestrutura: VM Azure (Ubuntu 24.04 LTS) com configuração de SWAP para estabilidade.




🛠️ Como Rodar o Projeto

Pré-requisitos

• Docker instalado

• Docker Compose instalado

Passo a Passo

1. Clone o repositório:

Bash


git clone https://github.com/marcusvilanova/P2-DevOps-Docker.git
cd P2-DevOps-Docker



2. Suba os containers:

Bash

sudo docker-compose up -d --build



3.Acesso: Abrir o navegador em http://localhost:80 (ou o IP da máquina: http://20.63.36.109:80 ).


