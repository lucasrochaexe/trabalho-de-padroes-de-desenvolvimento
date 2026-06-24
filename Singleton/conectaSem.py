class ConexaoBanco:
    def __init__(self, origem):
        self.origem = origem
        print(f"Nova conexao criada para {origem}")

    def conectar(self):
        print(f"{self.origem}: conectado ao banco")


def main():
    for origem in ("modulo A", "modulo B", "modulo C"):
        conexao = ConexaoBanco(origem)
        conexao.conectar()


if __name__ == "__main__":
    main()
