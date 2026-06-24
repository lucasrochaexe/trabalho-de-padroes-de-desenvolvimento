PROJETO: PADRÃO SINGLETON
Este projeto mostra o padrão Singleton, um dos padrões de projeto da Gang of Four (GoF).

O QUE SÃO PADRÕES GOF?
São soluções prontas para problemas comuns no desenvolvimento de software. 
Não são códigos prontos, mas formas testadas de organizar classes e objetos. O Singleton é um padrão criacional, ou seja, lida com a criação de objetos.

O PADRÃO SINGLETON
Garante que uma classe tenha apenas uma instância durante todo o programa e fornece um ponto de acesso global a ela.

Quando usar:

Conexão com banco de dados

Arquivo de log

Configurações da aplicação

Controle de serviços centrais

📖 O PROJETO 📖


conectaSem.py - versão sem Singleton

conectaCom.py - versão com Singleton

---> Sem Singleton
Cada chamada cria um novo objeto:

python
for origem in ("modulo A", "modulo B", "modulo C"):
    conexao = ConexaoBanco(origem)
    conexao.conectar()
Resultado: 3 objetos diferentes são criados.

<img src="img/Screenshot_1.png" alt="Diagrama do Singleton" width="500">

---> Com Singleton
A classe sobrescreve o método __new__ para controlar a criação:

python
conexoes = [SingletonConexao() for _ in range(3)]

for indice, conexao in enumerate(conexoes, start=1):
    print(f"Instancia {indice}: {id(conexao)}")
    conexao.conectar()

print(conexoes[0] is conexoes[1] is conexoes[2])  # True
Todas as variáveis apontam para o mesmo objeto.

<img src="img/Screenshot_2.png" alt="Diagrama do Singleton" width="500">

COMPARAÇÃO

Sem Singleton	Com Singleton
Cria objetos novos a cada chamada	Apenas uma instância existe
Pode desperdiçar recursos	Recursos são compartilhados
Controle disperso	Acesso centralizado


VANTAGENS
Garante instância única
 Facilita controle de recursos compartilhados
Evita criação repetida de objetos custosos
 Simplifica acesso global

DESVANTAGENS
Cria dependências globais escondidas
Dificulta testes automatizados
Pode virar "atalho" para código global
 Reduz flexibilidade do sistema

CONCLUSÃO
O Singleton é útil quando realmente necessário, como no caso de conexões com banco de dados. 
Porém, não deve ser usado sem critério, pois pode tornar o sistema rígido e difícil de testar. A decisão de usá-lo deve ser consciente e justificada pelo contexto.