# Jogo da Forca
# Projeto — Python


def desenhar_forca(erros):
    """Desenha o boneco de acordo com a quantidade de erros (0 a 6)."""
    estagios = [
        """
        |_________________|
        |                 |
        |
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        |_________________|
        |                 |
        |                 O
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        |_________________|
        |                 |
        |                 O
        |                 |
        |                 |
        |
        |
        |
        |
        |
        """,
        """
        |_________________|
        |                 |
        |                 O
        |                /|
        |                 |
        |
        |
        |
        |
        |
        """,
        """
        |_________________|
        |                 |
        |                 O
        |                /|\\
        |                 |
        |
        |
        |
        |
        |
        """,
        """
        |_________________|
        |                 |
        |                 O
        |                /|\\
        |                 |
        |                /
        |
        |
        |
        |
        """,
        """
        |_________________|
        |                 |
        |                 O
        |                /|\\
        |                 |
        |                / \\
        |
        |
        |
        |
        """,
    ]
    print(estagios[erros])


def jogar(palavra, mensagem):
    print(mensagem)
    print(f"A palavra tem {len(palavra)} letras.")
    letras_descobertas = ["_"] * len(palavra)
    tentativas = 6

    while tentativas > 0 and "_" in letras_descobertas:
        desenhar_forca(6 - tentativas)
        print("Palavra: " + " ".join(letras_descobertas))
        palpite = input("Digite uma letra: ").lower().strip()

        if len(palpite) != 1:
            print("Digita só uma letra, mano.")
            continue
        if palpite in letras_descobertas:
            print("Tu já tentou essa letra.")
            continue

        if palpite in palavra:
            for i, letra in enumerate(palavra):
                if letra == palpite:
                    letras_descobertas[i] = letra
            print("Acertou!")
        else:
            tentativas -= 1
            print(f"Errou! Tentativas restantes: {tentativas}")

    desenhar_forca(6 - tentativas)
    if "_" not in letras_descobertas:
        print("Você venceu! A palavra era: " + palavra)
    else:
        print(f"Você perdeu! A palavra era: {palavra}")


def jogo_da_forca():
    print("Vamos jogar o jogo da forca, se perder, você morre kkkk")
    print("Escolha o nível de dificuldade: fácil, médio ou difícil")
    dificuldade = input().lower().strip()
    dificuldade = (dificuldade.replace("á", "a").replace("é", "e")
                               .replace("í", "i").replace("ç", "c"))

    niveis = {
        "facil": ("banana",
                  "Você escolheu fácil né seu medroso! Então bora lá."),
        "medio": ("cafeinoide",
                  "Você escolheu médio né, ta meio indeciso, mas amém, então bora lá."),
        "dificil": ("paralelepípedo",
                    "Você escolheu difícil né bonzão! Então bora lá ver se é bom mesmo."),
    }

    if dificuldade not in niveis:
        print("Dificuldade inválida. Vamos jogar no nível fácil.")
        dificuldade = "facil"

    palavra, mensagem = niveis[dificuldade]
    jogar(palavra, mensagem)


print("Bem-vindo, fico feliz que esteja aqui, está procurando por algo?")
resposta = input().lower().strip()

if any(frase in resposta for frase in ("sim", "quero jogar", "jogo da forca", "bora")):
    print("Beleza, vamos jogar o jogo da forca então, bora lá")
    jogo_da_forca()
else:
    print("Beleza, quando quiser jogar é só rodar de novo. Falou!")
