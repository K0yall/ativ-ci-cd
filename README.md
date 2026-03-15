# 🚀 Projeto de Exploração de CI/CD com GitHub Actions

Este repositório foi criado para a atividade de exploração de recursos de **Integração Contínua e Entrega Contínua (CI/CD)**.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Automação:** GitHub Actions
* **Qualidade:** Flake8 (Linter)
* **Segurança:** Bandit (Security Scan)

## 🔄 Fluxo do Pipeline (Pipeline Stages)
O arquivo de workflow está configurado com 3 estágios sequenciais:

1.  **Quality Check (Linting):** Analisa o código em busca de erros de sintaxe e padrões de estilo (PEP8) usando o `flake8`.
2.  **Security Scan:** Realiza uma varredura de segurança com o `bandit` para encontrar vulnerabilidades comuns.
3.  **Artifact & Deploy Simulation:** Gera um artefato compactado (`.zip`) do código e simula o envio para um ambiente de produção/homologação.

## 📊 Status do Pipeline
Você pode conferir a execução dos estágios na aba [Actions](./actions) deste repositório.
