# Minha primeira Pipeline de CI/CD

Oi! Este repositório foi criado para uma atividade prática onde explorei o **GitHub Actions**. A ideia aqui não é só guardar o código, mas mostrar como automatizar processos que acontecem toda vez que eu mando uma atualização para o GitHub.

### O que o meu projeto faz automaticamente?
Criei um fluxo dividido em 3 partes principais para garantir que o código esteja bom:

1.  **Check de Qualidade (Linting):** O GitHub olha se o meu código Python está escrito direitinho, sem bagunça ou erros bobos de digitação.
2.  **Varredura de Segurança:** Ele faz um "scan" para ver se não deixei nenhuma falha de segurança ou bobeira no código que possa ser perigosa.
3.  **Simulação de Deploy:** Se passar em tudo, ele empacota o projeto num arquivo `.zip` e simula o envio para um servidor.

---
### Como ver isso funcionando?
É só clicar ali na aba **[Actions](https://github.com/SEU-USUARIO/SEU-REPO/actions)**. Lá dá para ver cada um desses 3 passos ficando verdinhos conforme o GitHub termina de processar.
