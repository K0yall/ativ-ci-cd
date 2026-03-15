def saudacao(nome):
    """Função simples de saudação."""
    return f"Olá, {nome}! Pipeline funcionando."


if __name__ == "__main__":
    # Uma mensagem simples para o log do GitHub Actions
    print(saudacao("DevOps Student"))
