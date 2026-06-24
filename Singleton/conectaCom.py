class SingletonConexao:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Criando conexao unica")
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def conectar(self):
        print("Conectado ao banco")


def main():
    conexoes = [SingletonConexao() for _ in range(3)]

    for indice, conexao in enumerate(conexoes, start=1):
        print(f"Instancia {indice}: {id(conexao)}")
        conexao.conectar()

    print(conexoes[0] is conexoes[1] is conexoes[2])


if __name__ == "__main__":
    main()
