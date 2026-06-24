from abc import ABC, abstractmethod

# ==========================================
# 1. A REGRA GERAL (A Interface da Estratégia)
# ==========================================
class EstrategiaAtaque(ABC):
    @abstractmethod
    def atacar(self):
        pass

# ==========================================
# 2. AS ESTRATÉGIAS ESPECÍFICAS (As Armas)
# ==========================================
class AtaqueEspada(EstrategiaAtaque):
    def atacar(self):
        print("⚔️ Atacou com a Espada! Dano corpo-a-corpo infligido.")

class AtaqueArco(EstrategiaAtaque):
    def atacar(self):
        print("🏹 Atirou uma flecha! Dano à distância infligido.")

class AtaqueMagia(EstrategiaAtaque):
    def atacar(self):
        print("🔥 Lançou uma bola de fogo! Dano mágico em área infligido.")

# ==========================================
# 3. O CONTEXTO (Quem usa a Estratégia)
# ==========================================
class Heroi:
    def __init__(self, nome):
        self.nome = nome
        self.arma_atual = None # O herói começa desarmado

    # Método para trocar a estratégia em tempo real!
    def equipar_arma(self, nova_arma: EstrategiaAtaque):
        self.arma_atual = nova_arma
        print(f"\n>>> {self.nome} trocou de equipamento! <<<")

    # O herói não sabe COMO a arma bate, ele só manda atacar.
    def realizar_ataque(self):
        if self.arma_atual:
            self.arma_atual.atacar()
        else:
            print(f"{self.nome} está desarmado e não pode atacar!")


# ==========================================
# 4. TESTANDO (Simulando o Jogo)
# ==========================================
if __name__ == "__main__":
    # Criamos o nosso personagem
    personagem = Heroi("Super Edécio")

    # Inimigo perto! Vamos usar a espada.
    personagem.equipar_arma(AtaqueEspada())
    personagem.realizar_ataque()

    # O inimigo correu para longe! Trocamos rápido para o arco.
    personagem.equipar_arma(AtaqueArco())
    personagem.realizar_ataque()

    # Apareceram vários inimigos de uma vez! Hora da magia.
    personagem.equipar_arma(AtaqueMagia())
    personagem.realizar_ataque()