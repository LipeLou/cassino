# Por trás dos cassinos...
![cassino](/img/cassino.png)

Cassinos são locais que oferecem jogos de azar, como máquinas **caça-níqueis**, **roleta** e **blackjack**, e são populares globalmente, proporcionando entretenimento e prêmios em dinheiro.
Esse projeto é uma forma de mostrar a matemática por trás dos cassinos, e como eles manipulam as pessoas fazendo com que elas joguem cada vez mais, consequentemente, as fazendo perder mais dinheiro.
A diversas técnicas que ajudam o cassino, como:

 > - Ambiente Atraente;
 > - Jogos de Baixa Aposta;
 > - Bebidas Grátis;
 > - Marketing e Promoções;
 > - Desvio de Atenção;
 > - Aposte e Ganhe;
 > Entre outras.

Ou seja, nota-se a quantidade de estratégias para atrair a atenção do cliente e fazer com que ele jogue.

## Técnicas Matemáticas 🧮
Além de técnicas atrativas, a **matemática é fundamental para a operação dos cassinos**, ajudando a estabelecer regras, garantir a lucratividade e modelar o comportamento dos jogadores. Os cassinos utilizam diversas técnicas para garantir a vantagem, aqui estão algumas:

1.  **Probabilidade**: Cada jogo em um cassino tem uma probabilidade associada que determina as chances de ganhar ou perder. Por exemplo, nas roletas, cada número tem uma chance de 1 em 37 (ou 38, dependendo do tipo de roleta).
    
2.  **Vantagem da Casa**: Os cassinos sempre têm uma vantagem matemática, que garante que, a longo prazo, eles ganharão mais do que os jogadores. Essa vantagem é incorporada em jogos como a roleta (onde o zero e o duplo zero favorecem o cassino) e em máquinas caça-níqueis.
    
3.  **Teoria dos Jogos**: Muitos jogos de cassino, como o poker, envolvem estratégias complexas. A teoria dos jogos ajuda a entender as melhores estratégias a serem utilizadas pelos jogadores e como maximizar suas chances de vencer.
    
4.  **Retorno ao Jogador (RTP)**: Essa é a porcentagem de dinheiro apostado que um jogo devolverá aos jogadores ao longo do tempo. Jogos com um RTP mais alto são mais favoráveis para os jogadores, mas, mesmo assim, o cassino ainda mantém a vantagem.
    
5.  **Modelos de Simulação**: Cassinos usam simulações matemáticas para prever o comportamento dos jogadores e otimizar seus lucros. Isso inclui a análise de padrões de apostas e o desenvolvimento de estratégias de marketing.
    
6.  **Estatísticas Comportamentais**: A matemática também é usada para entender o comportamento dos jogadores, como o tempo que eles gastam jogando e as quantias que estão dispostos a apostar.

Para mostrar melhor, esse projeto tem como o principal exemplo as máquinas **caça-níqueis**, que também possui as suas manipulações.

## Caça-níqueis 🎰
Os cassinos utilizam várias técnicas em máquinas caça-níqueis para incentivar os jogadores a continuarem jogando e, muitas vezes, perderem mais dinheiro. Aqui estão algumas das principais estratégias:

1.  **Gerador de Números Aleatórios (RNG)**: As máquinas usam um RNG para garantir que os resultados sejam imprevisíveis. 
    
2.  **Quase Acertos**: As máquinas são programadas para mostrar combinações que estão quase ganhando, o que pode incentivar os jogadores a continuar jogando na esperança de que a próxima rodada será a vencedora.
    
3.  **Recompensas Variáveis**: As recompensas são distribuídas de forma imprevisível, o que mantém os jogadores engajados.
    
4.  **Design Atraente**: As máquinas são projetadas com luzes brilhantes, sons atraentes e temas envolventes para manter os jogadores entretidos e imersos no jogo.
    
5.  **Feedback Positivo**: Mesmo pequenas vitórias são celebradas com sons e luzes, dando aos jogadores uma sensação de realização e incentivando-os a continuar jogando.
    
6.  **Jogos de Bônus**: Muitos caça-níqueis oferecem jogos de bônus que prometem grandes prêmios, incentivando os jogadores a continuar jogando para desbloquear esses bônus.
    
7.  **Facilidade de Acesso**: As máquinas são colocadas em locais estratégicos e de fácil acesso dentro dos cassinos para atrair mais jogadores.
    
8.  **Programação de Pagamentos**: As máquinas são programadas para pagar em intervalos que mantêm os jogadores engajados, mas ainda assim garantem lucro para o cassino.

Essas técnicas são cuidadosamente projetadas para maximizar o tempo e o dinheiro que os jogadores gastam nas máquinas caça-níqueis.

# Cassino em PYTHON  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="38" alt="python logo"/>

Para melhor aprendizado sobre a matemática por trás dos cassinos, o projeto tem como base um programa em **Python** de uma máquina caça-níquel.

> Por que Python?

Linguagem que estou me aprofundando mais, então esse projeto serve como um reforço dos meus estudos em Python. Como também, Python é uma ótima linguagem para trabalhar com dados, e vamos precisar analisar dados, visto que, faremos simulações.

> app .py

Arquivo para rodar simulações e testes.

> main. py

Arquivo principal do programa, onde armazenei as classes **CasseNiquel** e **Player**.

## Simulações 📊

> Todas as simulações foram feitas com a máquina no **level 3.**

### Simulação 1 📈

     JOGADORES_POR_DIA  = 30 
     APOSTAS_POR_DIA = 5 
     DIAS = 5
     VALOR_MAXIMO = 200
     
💲 **Ganho do Cassino**

![ganho cassino1](/img/ganho-cassino1.png)

R$16.000,00.

💲 **Ganho Jogadores** [30 players]

![ganho jogadores1](/img/ganho-jogadores1.png)

Alguns com lucro porém a maioria perderam.

### Simulação 2 📉

     JOGADORES_POR_DIA = 30 
     APOSTAS_POR_DIA = 5 
     DIAS = 10
     VALOR_MAXIMO = 200

💲 **Ganho do Cassino**

![ganho cassino2](/img/ganho-cassino2.png)

R$40.000,00.

💲 **Ganho Jogadores** [30 players]

![ganho jogadores2](/img/ganho-jogadores2.png)

Quase todos perderam, e os que ganharam não ganharam muito.

### Simulação 3 📈

     JOGADORES_POR_DIA = 30
     APOSTAS_POR_DIA = 5
     DIAS = 30
     VALOR_MAXIMO = 20
   
💲 **Ganho do Cassino**

![ganho cassino 3](/img/ganho-cassino3.png)

R$100.000,00.

💲 **Ganho Jogadores** [30 players]

![ganho jogadores3](/img/ganho-jogadores3.png)

Nenhum jogador ganhou.

### Simulação Final 📉

    JOGADORES_POR_DIA = 1000
    APOSTAS_POR_DIA = 10
    DIAS =  180
    VALOR_MAXIMO = 200
    
💲 **Ganho do Cassino**

![ganho cassino4](/img/ganho-cassino4.png) 

R$40.000.000,00

💲 **Ganho Jogadores** [1000 players]

![ganho jogadores4](/img/ganho-jogadores4.png)

Todos perderam, e perderam muito (em média **-R$45.000,00**).

# Conclusão 🚩

Com base nas simulações e em todos os dados, percebe-se que **quanto mais você joga, mais você perde**. Diante disso, destaca-se como todos os cassinos tem total controle sobre seus ganhos, podendo manipular psicologicamente, como também estatisticamente, baseando na analise de dados. Ou seja, jogos de azar são um vicio e os cassinos querem que você vicie, então para contornar a situação **não aposte em jogos de azar** ou **aposte com responsabilidade**.

> Para saber mais: [Jogo responsável](https://ibjr.org/jogo-responsavel/)

# Referências 💭
<img src="https://www.svgrepo.com/show/13671/youtube.svg" height="15" alt="youtube logo"/> Youtube: 

 - [Entenda a matemática por trás dos
   CASSINOS! - Universo Programado](https://www.youtube.com/watch?v=2jQuuCMRpZk) (recomendo)
   
 - [A VERDADE sobre o CASSINO ONLINE (Daniel Penin)- Cortes do
   Flow](https://www.youtube.com/watch?v=9mvXRemmlp8)
 
 - [POR QUE A CASA SEMPRE GANHA? | ENTENDA O SEGREDO POR TRÁS DOS JOGOS
   DE AZAR - Matemática em Evidência](https://www.youtube.com/watch?v=-wjdOv3IIB4)

📃 Artigos: 

 - [A Chance Matemática De Ganhar Nos Caça-níqueis - Quit
   Gamble](https://quitgamble.com/br/voce-pode-vencer/)
   
 - [Como funciona o algoritmo das máquinas de caça-niquel? -
   maistecnologia.com](https://www.maistecnologia.com/algoritmo-das-maquinas-de-caca-niquel/)
   
 - [Como funciona o algoritmo das máquinas de caça-níquel? - Portal TUDO
   AQUI](https://www.portaltudoaqui.com.br/como-funciona-o-algoritmo-das-maquinas-de-caca-niquel/)

