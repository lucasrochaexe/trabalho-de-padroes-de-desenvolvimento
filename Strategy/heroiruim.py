# ==========================================
# CÓDIGO SEM DESIGN PATTERN (Modo "Gambi")
# ==========================================

class HeroiRuim:
    def __init__(self, nome):
        self.nome = nome
        # Em vez de uma classe de estratégia, guardamos o tipo como texto (string)
        self.arma_atual = "desarmado" 

    def equipar_arma(self, nome_da_arma: str):
        self.arma_atual = nome_da_arma.lower()
        print(f"\n>>> {self.nome} mudou a arma para: {nome_da_arma} <<<")

    # O PROBLEMA ESTÁ AQUI: O método acumula todas as lógicas do jogo
    def realizar_ataque(self):
        if self.arma_atual == "desarmado":
            print(f"{self.nome} está desarmado e não pode atacar!")
            
        elif self.arma_atual == "espada":
            # Imagine 20 linhas de código de animação/lógica da espada aqui
            print("⚔️ Atacou com a Espada! Dano corpo-a-corpo infligido.")
            
        elif self.arma_atual == "arco":
            # Imagine mais 20 linhas de código do arco aqui
            print("🏹 Atirou uma flecha! Dano à distância infligido.")
            
        elif self.arma_atual == "magia":
            # Imagine mais 20 linhas de código de fogo aqui
            print("🔥 Lançou uma bola de fogo! Dano mágico em área infligido.")
            
        else:
            print(f"⚠️ Erro: A arma '{self.arma_atual}' não existe no jogo!")


# ==========================================
# TESTANDO O CÓDIGO RUIM
# ==========================================
if __name__ == "__main__":
    personagem = HeroiRuim("Super Edecio")

    personagem.equipar_arma("espada")
    personagem.realizar_ataque()

    personagem.equipar_arma("arco")
    personagem.realizar_ataque()