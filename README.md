 Padrões de Projeto: Singleton e Strategy

Este repositório reúne dois exemplos de padrões de projeto da GoF:

- [Singleton](Singleton/README.txt)
- [Strategy](Strategy/readme.md)

Visão Geral

O **Singleton** garante que uma classe tenha apenas uma instância durante a execução do programa.

O **Strategy** permite trocar o comportamento de um objeto em tempo de execução, escolhendo entre várias estratégias compatíveis.

Semelhanças

- Os dois padrões ajudam a organizar melhor o código.
- Ambos reduzem duplicação e facilitam manutenção.
- Os dois incentivam o uso de abstração em vez de lógica espalhada.
- Em ambos, o comportamento fica mais claro e modular.

 Diferenças

| Aspecto | Singleton | Strategy |
| --- | --- | --- |
| Tipo de padrão | Criacional | Comportamental |
| Foco principal | Controlar a criação de instâncias | Trocar comportamentos/algoritmos |
| Quantidade de objetos | Apenas uma instância | Várias estratégias possíveis |
| Mudança em tempo de execução | Não é o objetivo principal | É uma característica central |
| Exemplo no projeto | `Singleton/conectaCom.py` | `Strategy/heroi.py` |

Quando usar

Singleton

Use quando for importante existir apenas um objeto compartilhado, como:

- conexão com banco de dados;
- configuração global da aplicação;
- sistema de logs;
- controle de um recurso central.

Strategy

Use quando o comportamento variar bastante e você quiser trocar a regra sem alterar a classe principal, como:

- tipos diferentes de ataque em um jogo;
- formas de pagamento;
- cálculo de frete;
- regras de desconto.

Exemplos do Projeto

Singleton

- `Singleton/conectaSem.py`: cria uma nova conexão a cada chamada.
- `Singleton/conectaCom.py`: reaproveita a mesma instância usando `__new__`.

Strategy

- `Strategy/heroiruim.py`: usa vários `if/elif` para decidir o ataque.
- `Strategy/heroi.py`: troca a estratégia de ataque por polimorfismo.

Conclusão

Os dois padrões melhoram a organização do código, mas resolvem problemas diferentes.

O **Singleton** controla a criação de objetos.
O **Strategy** controla a variação de comportamento.

Em resumo, o Singleton responde à pergunta “quantas instâncias existem?”, enquanto o Strategy responde à pergunta “qual comportamento deve ser usado agora?”.
