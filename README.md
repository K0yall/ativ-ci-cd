# Projeto de Exploração de CI/CD (GitHub Actions)

Este repositório demonstra um fluxo de CI/CD automatizado com 3 estágios:

1.  **Linter (Quality Check):** Uso do `flake8` para garantir que o código segue os padrões PEP8.
2.  **Security Scan:** Uso do `bandit` para verificar vulnerabilidades de segurança no código Python.
3.  **Deploy Simulation:** Simulação de empacotamento (`zip`) e deploy em ambiente de homologação.
