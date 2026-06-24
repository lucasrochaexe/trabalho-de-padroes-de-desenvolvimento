PROJETO: PADRÃO STRATEGY

Este projeto mostra o padrão **Strategy** (Estratégia), um dos padrões de projeto clássicos da Gang of Four (GoF).

---

 O QUE SÃO PADRÕES GOF?
São soluções consolidadas para problemas comuns no desenvolvimento de software. Não são códigos prontos que você copia e cola, mas sim formas testadas e aprovadas de organizar suas classes e objetos. 

O **Strategy** é um padrão **comportamental**, ou seja, ele lida com a forma como os objetos interagem e distribuem suas responsabilidades.

---

O PADRÃO STRATEGY
Ele serve para isolar uma família de algoritmos, encapsular cada um deles em classes separadas e fazer com que eles sejam intercambiáveis. Isso permite que o comportamento de um objeto mude em tempo de execução, dependendo da necessidade, sem precisar alterar a classe principal.

Quando usar:
* Sistemas de pagamento com múltiplas opções (Pix, Cartão, Boleto).
* Motores de cálculo de frete ou impostos que mudam por região.
* Inteligência artificial ou armas de personagens em jogos (troca de táticas).
* Algoritmos de ordenação ou compressão de arquivos diferentes para cada situação.

---

📖 O PROJETO

O projeto demonstra a diferença crucial de arquitetura através de dois cenários em um jogo onde um herói precisa atacar com armas diferentes:

* `heroiruim.py` - versão sem o padrão Strategy (uso de condicionais complexas).
* `heroi.py` - versão com o padrão Strategy (uso de polimorfismo).

---

Sem Strategy (Abordagem Rígida)
Cada vez que o personagem ataca, o sistema precisa passar por uma estrutura pesada de `if/else` para descobrir qual é a arma atual e executar a lógica dela ali mesmo:

python
Dentro da classe Heroi
def realizar_ataque(self):
    if self.arma_atual == "espada":
        print("⚔️ Atacou com a Espada! Dano corpo-a-corpo.")
    elif self.arma_atual == "arco":
        print("🏹 Atirou uma flecha! Dano à distância.")
    elif self.arma_atual == "magia":
        print("🔥 Lançou uma bola de fogo! Dano em área.")
Resultado: Se o jogo ganhar 20 armas novas, essa classe vai virar um monstro gigante. Para adicionar uma arma, você é obrigado a alterar e arriscar quebrar um código que já funcionava.

Com Strategy (Abordagem Flexível)
A classe do herói não sabe (e não precisa saber) como cada arma funciona por baixo dos panos. Ela só recebe um "objeto de ataque" genérico e manda ele executar:

python
def realizar_ataque(self):
    if self.arma_atual:
        self.arma_atual.atacar()
        
Resultado: Cada arma vira uma classe isolada (AtaqueEspada, AtaqueArco). Se você precisar criar uma arma nova, o código antigo da classe Heroi continua intacto e totalmente fechado para modificações.

VANTAGENS
Princípio do Aberto/Fechado (SOLID): Você introduz novas estratégias sem precisar mudar o código original.

Isolamento de Código: Bugs em uma estratégia específica (ex: erro no cálculo do arco) são corrigidos na classe dela, sem afetar o herói ou as outras armas.

Eliminação de Condicionais: Substitui estruturas gigantescas de if/else ou switch por polimorfismo limpo.

Troca Dinâmica: Permite mudar o comportamento do objeto no meio da execução do programa.

DESVANTAGENS
Aumento de Classes: Se o sistema tiver poucas variações, criar uma classe para cada uma pode inflar o projeto sem necessidade.

Complexidade Inicial: Exige que o desenvolvedor entenda bem conceitos de interfaces e polimorfismo.

O cliente precisa conhecer as estratégias: Quem vai usar o contexto precisa saber qual estratégia escolher e passar para ele.

 CONCLUSÃO
O padrão Strategy é uma das melhores ferramentas para manter o código limpo, modular e preparado para o crescimento. Ele brilha quando um comportamento tem muitas variações de regras de negócio.