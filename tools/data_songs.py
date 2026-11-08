# -*- coding: utf-8 -*-
"""Músicas icônicas (rock e funk), discos essenciais e sertanejo por ano. Formato compacto: campos separados por |."""

# ano|título|artista(s)  — rock brasileiro, por ano
ROCK_SONGS = """
1954|Neurastênico|Betinho e Seu Conjunto
1955|Ronda das Horas|Heleninha Silveira
1956|Enrolando o Rock|Betinho e Seu Conjunto; Cauby Peixoto
1957|Rock 'N' Roll Em Copacabana|Cauby Peixoto
1958|Here's The Blue Jean Rockers|The Blue Jean Rockers
1959|Estúpido Cupido|Celly Campello
1959|Lacinhos Cor-de-Rosa|Celly Campello
1959|Túnel do Amor|Celly Campello
1959|Querida|Sérgio Murilo
1960|Banho de Lua|Celly Campello
1960|Broto Legal|Sérgio Murilo
1960|Pobre de Mim|Tony Campello
1960|Baby Rock|Tony Campello
1960|Calypso Rock|The Snakes
1960|Pra Sempre|The Snakes
1961|Alguém É Sempre Bobo de Alguém|Wilson Miranda
1962|Estou Louco|Baby Santiago
1963|Splish Splash|Roberto Carlos
1963|Parei na Contramão|Roberto Carlos
1963|Telefonema|Ed Wilson
1963|Boogie do Bebê|Tony Campello
1963|Biquini de Bolinha Amarelinha Tão Pequeninho|Ed Wilson
1964|O Calhambeque|Roberto Carlos
1964|É Proibido Fumar|Roberto Carlos
1964|Rua Augusta|Ronnie Cord
1965|O Milionário|Os Incríveis
1965|Menina Linda|Renato e Seus Blue Caps
1965|Feche os Olhos|Renato e Seus Blue Caps
1965|Pare o Casamento|Wanderléa
1965|Festa de Arromba|Erasmo Carlos
1965|O Escândalo|Renato e Seus Blue Caps
1965|Amar Você|Renato e Seus Blue Caps
1966|Alguém na Multidão|Golden Boys
1966|Gatinha Manhosa|Erasmo Carlos
1966|Pobre Menina|Lilian Wilson; Ed Wilson
1966|Devolva-me|Lilian Wilson; Ed Wilson
1966|Theme for Young Lovers|The Jet Blacks
1966|Pintada de Preto|Os Baobás
1967|A Minha Menina|Os Mutantes
1967|Coração de Papel|Sérgio Reis
1967|Era Um Garoto Que Como Eu Amava os Beatles e os Rolling Stones|Os Incríveis
1967|És Meu Amor|Jerry Adriani
1967|Vem Quente Que Eu Estou Fervendo|Erasmo Carlos
1967|Pensando Nela|Golden Boys
1967|Escuta Meu Amor|Ronnie Von
1967|Prova de Fogo|Wanderléa
1968|Panis Et Circenses|Os Mutantes
1968|Você Ainda Pode Sonhar|Raulzito e os Panteras
1968|A Lenda de Xanadu|The Clevers
1968|Me Deixa em Paz|Raulzito e os Panteras
1969|Carolina, Carol Bela|Os Brazões
1969|Sentado À Beira do Caminho|Erasmo Carlos; Roberto Carlos
1969|Andança|Golden Boys
1969|A Distância|Os Brasas
1970|Ando Meio Desligado|Os Mutantes
1970|Feira Moderna|Som Imaginário
1970|Anjo da Guarda|Made in Brazil
1971|É Preciso Dar Um Jeito, Meu Amigo|Erasmo Carlos
1971|Doce, Doce Amor|Jerry Adriani
1971|Sempre Existe Alguém|Trio Ternura
1972|Mistério do Planeta|Novos Baianos
1972|A Menina Dança|Novos Baianos
1972|Um Girassol da Cor do Seu Cabelo|Lô Borges
1972|O Trem Azul|Lô Borges
1972|Agora Só Falta Você|Rita Lee; Tutti Frutti
1972|Paisagem da Janela|Lô Borges
1972|Balada do Louco|Os Mutantes
1972|Calibre|Lô Borges
1972|Esse Tal de Roque Enrow|Rita Lee; Tutti Frutti
1972|Trem de Doido|Lô Borges
1972|Cavaleiro de Aruanda|Ronnie Von
1972|Hey Girl|Lee Jackson
1973|Metamorfose Ambulante|Raul Seixas
1973|Sangue Latino|Secos & Molhados
1973|Ouro de Tolo|Raul Seixas
1973|Mosca na Sopa|Raul Seixas
1974|Gita|Raul Seixas
1974|Medo da Chuva|Raul Seixas
1974|Sociedade Alternativa|Raul Seixas
1974|O Trem das 7|Raul Seixas
1974|Fala|Secos & Molhados
1974|É Preciso Saber Viver|Roberto Carlos
1974|Será Que Eu Vou Virar Bolor?|Arnaldo Baptista
1974|Tão Longe de Mim|Os Brazões
1974|Conto Contigo|Moto Perpétuo
1974|Lady Jane|A Barca do Sol
1975|Tente Outra Vez|Raul Seixas
1975|Ovelha Negra|Rita Lee
1975|A Maça|Raul Seixas
1975|Vou Morar No Ar|Casa das Máquinas
1975|Hey Amigo|O Terço
1975|Lar de Maravilhas|Casa das Máquinas
1975|De Sol a Sol|Serguei
1976|Eu Nasci Há 10 Mil Anos Atrás|Raul Seixas
1976|Como Nossos Pais|Belchior
1976|Casa de Rock|Casa das Máquinas
1976|Bixo da Seda|Bixo da Seda
1977|Maluco Beleza|Raul Seixas
1977|O Dia em que a Terra Parou|Raul Seixas
1977|Amigo|Roberto Carlos
1977|É Proibido Fumar|A Bolha
1978|Menino do Rio|Baby do Brasil
1978|Amor de Índio|Beto Guedes
1978|Zanzibar (As Cores)|A Cor do Som
1979|Mania de Você|Rita Lee
1979|Sol de Primavera|Beto Guedes
1980|Lança Perfume|Rita Lee
1980|Caso Sério|Rita Lee
1980|Aluga-se|Raul Seixas
1980|Além do Horizonte|Erasmo Carlos
1980|Bola de Meia, Bola de Gude|14 Bis
1980|Rock das "Aranha"|Raul Seixas
1980|Planeta Sonho|14 Bis
1980|Vela Aberta|Walter Franco
1980|John Travolta|AI-5
1981|Sapato Velho|Roupa Nova
1981|O Sal da Terra|Beto Guedes
1981|Te Amo, Que Mais Posso Dizer|Ovelha
1981|Minha Vida É Rock 'n' Roll|Made In Brazil
1982|Tempos Modernos|Lulu Santos
1982|Você Não Soube Me Amar|Blitz
1982|Eva|Rádio Táxi
1982|Linda Juventude|14 Bis
1982|De Repente Califórnia|Lulu Santos
1982|Todo Amor Que Houver Nessa Vida|Barão Vermelho
1982|Mais Uma de Amor (Geme Geme)|Blitz
1982|Lindo Balão Azul|Moraes Moreira; Baby do Brasil
1982|Garota Dourada|Rádio Táxi
1982|Erva Venenosa|Herva Doce
1982|Pânico em S.P.|Inocentes
1982|Columbia|Patrulha do Espaço
1983|Apenas Mais Uma de Amor|Lulu Santos
1983|Menina Veneno|Ritchie
1983|Pintura Íntima|Kid Abelha
1983|A Dois Passos do Paraíso|Blitz
1983|Vital e Sua Moto|Os Paralamas do Sucesso
1983|Um Certo Alguém|Lulu Santos
1983|Pro Dia Nascer Feliz|Barão Vermelho
1983|A Vida Tem Dessas Coisas|Ritchie
1983|Desculpe o Auê|Rita Lee
1983|Todo Azul do Mar|14 Bis
1983|Tudo Azul|Lulu Santos
1983|Betty Frígida|Blitz
1983|Sou Boy|Magazine
1983|Por Que Não Eu?|Kid Abelha
1983|Perdidos na Selva|Gang 90 e as Absurdettes
1983|Bete Morreu|Camisa de Vênus
1983|Tic Tic Nervoso|Magazine
1983|Smog Alado|Bacamarte
1984|Cama e Mesa|Roberto Carlos
1984|Bete Balanço|Barão Vermelho
1984|Whisky a Go-Go|Roupa Nova
1984|Sonífera Ilha|Titãs
1984|Tão Bem|Lulu Santos
1984|Óculos|Os Paralamas do Sucesso
1984|Como Eu Quero|Kid Abelha
1984|Fullgás|Marina Lima
1984|Maior Abandonado|Barão Vermelho
1984|Me Chama|Lobão
1984|Mesmo Que Seja Eu|Marina Lima
1984|Chuva de Prata|Roupa Nova
1984|Eu Não Matei Joana d'Arc|Camisa de Vênus
1984|Serão Extra|Dr. Silvana & Cia.
1984|Ska|Os Paralamas do Sucesso
1984|Weekend|Blitz
1984|Um Amor de Verão|Rádio Táxi
1984|Taca a Mãe pra Ver se Quica|Dr. Silvana & Cia.
1984|Crucificados pelo Sistema|Ratos de Porão
1984|Verdades e Mentiras|Voluntários da Pátria
1985|Exagerado|Cazuza
1985|Será|Legião Urbana
1985|Meu Erro|Os Paralamas do Sucesso
1985|Codinome Beija-Flor|Cazuza
1985|Ainda É Cedo|Legião Urbana
1985|Olhar 43|RPM
1985|Geração Coca-Cola|Legião Urbana
1985|Dona|Roupa Nova
1985|Até Quando Esperar|Plebe Rude
1985|Linda Demais|Roupa Nova
1985|Rádio Pirata|RPM
1985|A Fórmula do Amor|Leo Jaime; Kid Abelha
1985|Seguindo no Trem Azul|Roupa Nova
1985|Primeiros Erros (Chove)|Kiko Zambianchi
1985|Inútil|Ultraje a Rigor
1985|Lágrimas e Chuva|Kid Abelha
1985|Amante Profissional|Herva Doce
1985|Nós Vamos Invadir Sua Praia|Ultraje a Rigor
1985|Beat Acelerado|Metrô
1985|Ciúme|Ultraje a Rigor
1985|Tudo Pode Mudar|Metrô
1985|A Vida Não Presta|Leo Jaime
1985|Me Liga|Os Paralamas do Sucesso
1985|A Cruz e a Espada|RPM
1985|Televisão|Titãs
1985|Garota de Berlim|Supla; Metrópolis
1985|Proteção|Plebe Rude
1985|Núcleo Base|Ira!
1985|Papai Noel, Velho Batuta|Garotos Podres
1985|Sândalo de Dândi|Metrô
1985|Agora Eu Sei|Zero
1985|Formosa|Zero
1985|Corações Psicodélicos|Lobão
1985|Fazê Um Bolo|Taranatiriça
1986|Tempo Perdido|Legião Urbana
1986|Eduardo e Mônica|Legião Urbana
1986|Envelheço na Cidade|Ira!
1986|Índios|Legião Urbana
1986|Tédio|Biquini Cavadão
1986|Alvorada Voraz|RPM
1986|Música Urbana|Capital Inicial
1986|Dias de Luta|Ira!
1986|Toda Forma de Poder|Engenheiros do Hawaii
1986|Flores em Você|Ira!
1986|Fátima|Capital Inicial
1986|Alagados|Os Paralamas do Sucesso
1986|Totalmente Demais|Hanói Hanói
1986|Só Pro Meu Prazer|Heróis da Resistência
1986|Lágrimas de Crocodilo|João Penca e Seus Miquinhos Amestrados
1986|Veraneio Vascaína|Capital Inicial
1986|Popstar|João Penca e Seus Miquinhos Amestrados
1986|Surfista Calhorda|Os Replicantes
1986|Aa Uu|Titãs
1986|Silvia|Camisa de Vênus
1986|Simca Chambord|Camisa de Vênus
1986|Polícia|Titãs
1986|Doublê de Corpo|Heróis da Resistência
1986|Leve Desespero|Capital Inicial
1986|Revanche|Lobão
1987|Faroeste Caboclo|Legião Urbana
1987|Que País É Este|Legião Urbana
1987|Cowboy Fora da Lei|Raul Seixas
1987|Camila, Camila|Nenhum de Nós
1987|Terra de Gigantes|Engenheiros do Hawaii
1987|Infinita Highway|Engenheiros do Hawaii
1987|O Nosso Amor a Gente Inventa (Estória Romântica)|Cazuza
1987|Homem Primata|Titãs
1987|Bichos Escrotos|Titãs
1987|Uma Noite e 1/2|Marina Lima
1987|Blá Blá Blá... Eu Te Amo|Lobão
1987|Independência|Capital Inicial
1987|Família|Titãs
1987|Troops of Doom|Sepultura
1987|Mais Uma Vez|14 Bis; Renato Russo
1987|Vida Bandida|Lobão
1987|São Paulo|365
1987|Pelado|Ultraje a Rigor
1987|Quimeras|Zero
1987|Muita Estrela, Pouca Constelação|Camisa de Vênus; Raul Seixas
1987|Festa Punk|Os Replicantes
1987|Anarkia Oi|Garotos Podres
1987|Sexo!|Ultraje a Rigor
1987|Quadrinhos|Picassos Falsos
1987|Restos de Nada|Restos de Nada
1988|O Tempo Não Para|Cazuza
1988|Toda Forma de Amor|Lulu Santos
1988|Ideologia|Cazuza
1988|Mordida de Amor|Yahoo
1989|Pais e Filhos|Legião Urbana
1989|Lanterna dos Afogados|Os Paralamas do Sucesso
1989|O Astronauta de Mármore|Nenhum de Nós
1989|Há Tempos|Legião Urbana
1989|À Francesa|Marina Lima
1989|Flores|Titãs
1989|Somos Quem Podemos Ser|Engenheiros do Hawaii
1989|Carpinteiro do Universo|Raul Seixas
1989|Adelaide|Inimigos do Rei
1989|Beber Até Morrer|Ratos de Porão
1989|Living for the Night|Viper
1989|Uma Barata Chamada Kafka|Inimigos do Rei
1989|Aids, Pop, Repressão|Ratos de Porão
1989|Sou Solteiro|Kid Vinil
1990|Por Você|Barão Vermelho
1990|Era um Garoto que como Eu Amava os Beatles e os Rolling Stones|Engenheiros do Hawaii
1990|Pra Ser Sincero|Engenheiros do Hawaii
1990|O Papa É Pop|Engenheiros do Hawaii
1990|Exército de Um Homem Só|Engenheiros do Hawaii
1990|Por Enquanto|Cássia Eller
1990|Puro Êxtase|Barão Vermelho
1990|Tarde Vazia|Ira!
1990|Caleidoscópio|Os Paralamas do Sucesso
1991|Vento Ventania|Biquini Cavadão
1991|Arise|Sepultura
1991|Dead Embryonic Cells|Sepultura
1991|Sofrer|Ratos de Porão
1993|Refuse / Resist|Sepultura
1993|Territory|Sepultura
1993|Carry On|Angra
1993|Wuthering Heights|Angra
1993|Slave New World|Sepultura
1993|Pastor João e a Igreja Invisível|Marcelo Nova; Raul Seixas
1993|When All The Things|Garage Fuzz
1994|Malandragem|Cássia Eller
1994|A Praieira|Chico Science & Nação Zumbi
1994|Puteiro em João Pessoa|Raimundos
1994|Da Lama ao Caos|Chico Science & Nação Zumbi
1994|A Cidade|Chico Science & Nação Zumbi
1994|É Proibido Fumar|Skank
1994|Biquini de Bolinha Amarelinha Tão Pequeninho|Blitz
1994|ECT|Cássia Eller
1994|Selim|Raimundos
1994|Nêga Jurema|Raimundos
1994|Samba Makossa|Chico Science & Nação Zumbi
1994|Esmola|Skank
1994|Palhas do Coqueiro|Raimundos
1994|Bê a Bá|Raimundos
1994|Rapante|Raimundos
1995|Uma Brasileira|Os Paralamas do Sucesso; Djavan
1995|Pelados em Santos|Mamonas Assassinas
1995|Jackie Tequila|Skank
1995|Vira-Vira|Mamonas Assassinas
1995|Robocop Gay|Mamonas Assassinas
1995|Eu Quero Ver o Oco|Raimundos
1995|Mantenha o Respeito|Planet Hemp
1995|Chopis Centis|Mamonas Assassinas
1995|Te Ver|Skank
1995|1406|Mamonas Assassinas
1995|I Saw You Saying (That You Say That You Saw)|Raimundos
1995|Jumento Celestino|Mamonas Assassinas
1995|Uma Arlinda Mulher|Mamonas Assassinas
1995|Lá Vem o Alemão|Mamonas Assassinas
1995|Mundo Animal|Mamonas Assassinas
1995|Sobre o Tempo|Pato Fu
1995|Legalize Já|Planet Hemp
1995|Pacato Cidadão|Skank
1995|Esporrei na Manivela|Raimundos
1995|Dig Dig Dig (Hempa)|Planet Hemp
1996|Roots Bloody Roots|Sepultura
1996|Pescador de Ilusões|O Rappa
1996|Garota Nacional|Skank
1996|A Feira|O Rappa
1996|Maracatu Atômico|Chico Science & Nação Zumbi
1996|Amor Meu Grande Amor|Barão Vermelho
1996|Attitude|Sepultura
1996|Manguetown|Chico Science & Nação Zumbi
1996|Na Rua, na Chuva, na Fazenda (Casinha de Sapê)|Kid Abelha
1996|As Dores do Mundo|Jota Quest
1996|Green Hair (Japa Girl)|Supla
1997|Proibida pra Mim (Grazon)|Charlie Brown Jr.
1997|Tudo Que Ela Gosta de Escutar|Charlie Brown Jr.
1997|O Côro Vai Comê|Charlie Brown Jr.
1997|Papo de Jacaré|P.O.Box
1997|É Uma Partida de Futebol|Skank
1997|Quinta-Feira|Charlie Brown Jr.
1997|Quemando Tudo|Planet Hemp
1997|Nega do Cabelo Duro|Planet Hemp
1997|Encontrar Alguém|Jota Quest
1997|Gimme o Anel|Charlie Brown Jr.
1997|Zerovinteum|Planet Hemp; Fernanda Abreu
1997|Charlie Brown Jr.|Charlie Brown Jr.
1997|Uns Drinks|Velhas Virgens
1997|Aquela Paz|Charlie Brown Jr.
1997|Caio no Suingue|Pedro Luís e a Parede
1997|Abre Essas Pernas Pra Mim|Velhas Virgens
1997|Bagulho no Bumba|Os Virgulóides
1997|Heloísa, Mexe a Cadeira|Vinny
1997|Velho Punk|Gritando HC
1997|Mancha|Garotos Podres
1997|Futebol, Mulher & Rock'n Roll|Dr. Sin
1998|Resposta|Skank
1998|Fácil|Jota Quest
1998|É Preciso Saber Viver|Titãs
1998|Você Vai Lembrar de Mim|Nenhum de Nós
1998|Saideira|Skank
1998|Dani|Biquini Cavadão
1998|Vagabundo Confesso / Cantiga da Puxada de Rede|Dazaranha
1998|De Volta ao Planeta|Jota Quest
1998|Canção Pra Você Viver Mais|Pato Fu
1998|Bleed|Soulfly
1998|Cabrobro|Tianastacia
1998|Eu Vou Estar|Zélia Duncan
1998|Sempre Assim|Jota Quest
1998|Dia Especial|Cidadão Quem
1998|Nós|Cássia Eller
1998|Conto de Fraldas|Tianastacia
1998|Eye For an Eye|Soulfly
1999|Zóio de Lula|Charlie Brown Jr.
1999|Mulher de Fases|Raimundos
1999|Minha Alma (A Paz Que Eu Não Quero)|O Rappa
1999|Anna Júlia|Los Hermanos
1999|Palavras ao Vento|Cássia Eller
1999|Me Deixa|O Rappa
1999|Poema|Ney Matogrosso
1999|O Segundo Sol|Cássia Eller
1999|Te Levar Daqui|Charlie Brown Jr.
1999|A Mais Pedida|Raimundos; Érika Martins
1999|Me Lambe|Raimundos
1999|Não Deixe o Mar Te Engolir|Charlie Brown Jr.
1999|Confisco|Charlie Brown Jr.
1999|Primavera|Los Hermanos
1999|Nada a Declarar|Ultraje a Rigor
1999|Perdendo Dentes|Pato Fu
1999|Sonho Médio|Dead Fish
1999|Você Chegou|LS Jack
2000|A Cera|O Surto
2000|O Que Sobrou do Céu|O Rappa
2000|Não É Sério|Charlie Brown Jr.; Negra Li
2000|Tudo Que Vai|Capital Inicial
2000|Tropa de Elite|Tihuana
2000|Regina Let's Go!|CPM 22
2000|O Passageiro|Capital Inicial
2000|Rubão, o Dono do Mundo|Charlie Brown Jr.
2000|Lado B Lado A|O Rappa
2000|Natasha|Capital Inicial
2000|Pagu|Rita Lee; Zélia Duncan
2000|Contexto|Planet Hemp
2000|Fogo|Capital Inicial
2000|O Mundo Dá Voltas|CPM 22
2000|Que Ves?|Tihuana
2000|O Tempo|Oficina G3
2000|Back to the Primitive|Soulfly
2000|Pula|Tihuana
2000|Quem Sabe|Los Hermanos
2000|Aquela|Raimundos
2000|Tudo É Possível|O Surto
2000|Tudo Mudar|Charlie Brown Jr.
2000|Ex-Quadrilha da Fumaça|Planet Hemp
2000|Anteontem|CPM 22
2000|Melissa|Bidê ou Balde
2000|Esperando na Janela|Cogumelo Plutão
2001|Epitáfio|Titãs
2001|Lugar Ao Sol|Charlie Brown Jr.
2001|Relicário|Cássia Eller; Nando Reis
2001|Como Tudo Deve Ser|Charlie Brown Jr.
2001|Segredos|Frejat
2001|Amor Pra Recomeçar|Frejat
2001|Acima do Sol|Skank
2001|Jumpdafuckup|Soulfly; Corey Taylor
2001|Sentimental|Los Hermanos
2001|Hoje Eu Acordei Feliz|Charlie Brown Jr.
2001|Tarde de Outubro|CPM 22
2001|Luz dos Olhos|Cássia Eller
2001|Minha Vida|Rita Lee
2001|Dias Melhores|Jota Quest
2001|Isso|Titãs
2001|My Favorite Way|Gabriel O Pensador
2001|Rebirth|Angra
2001|Amanhã ou Depois|Nenhum de Nós
2001|Todo Carnaval Tem Seu Fim|Los Hermanos
2001|Ela Roubou Meu Caminhão|Matanza
2001|Ando Meio Desligado|Pato Fu
2001|Sino Dourado|Charlie Brown Jr.
2001|Alma|Zélia Duncan
2001|Pain|Soulfly
2001|Tudo Pro Alto|Charlie Brown Jr.
2001|Dia Perfeito|Cachorro Grande
2001|Eu Protesto|Charlie Brown Jr.
2001|Medo|Sugar Kane
2001|Ninguém Regula a América|O Rappa
2002|Só Por Uma Noite|Charlie Brown Jr.
2002|Só Hoje|Jota Quest
2002|Quando o Sol Se For|Detonautas
2002|Papo Reto (Prazer é Sexo, o Resto é Negócio)|Charlie Brown Jr.
2002|Olhos Certos|Detonautas
2002|Carla|LS Jack
2002|Outro Lugar|Detonautas
2002|À Sua Maneira (De Música Ligera)|Capital Inicial
2002|Nada Sei (Apnéia)|Kid Abelha
2002|Fairy Tale|Shaman
2002|Desconfio|CPM 22
2002|Me Odeie|Reação em Cadeia
2002|Na Moral|Jota Quest; Seu Jorge
2002|Uma Carta|LS Jack
2002|No Recreio|Cássia Eller
2002|Sonhos e Planos|CPM 22
2002|Sexperienced|Cachorro Grande
2002|Talvez|LS Jack
2002|For Tomorrow|Shaman
2002|Olhos Vermelhos|Capital Inicial
2002|Eu Não Pertenço À Você|Reação em Cadeia
2002|Espero|Reação em Cadeia
2002|Prego|Cueio Limão
2002|Quem Matou o Bozo?|Cueio Limão
2002|O Idiota|Blind Pigs
2003|Equalize|Pitty
2003|Vou Deixar|Skank
2003|Amor e Sexo|Rita Lee; Roberto de Carvalho
2003|Último Romance|Los Hermanos
2003|Dias Atrás|CPM 22
2003|Não Sei Viver Sem Ter Você|CPM 22
2003|Admirável Chip Novo|Pitty
2003|Dois Rios|Skank
2003|Teto de Vidro|Pitty
2003|Reza Vela|O Rappa
2003|Pensando em Você|Paulinho Moska
2003|Sem Radar|LS Jack
2003|O Vencedor|Los Hermanos
2003|Máscara|Pitty
2003|Semana Que Vem|Pitty
2003|Amanhã Não Se Sabe|LS Jack
2003|Amor Maior|Jota Quest
2003|Musa do Verão|Felipe Dylon
2003|Minha Juventude|Mr. Gyn
2003|Cara Estranho|Los Hermanos
2003|Pé Na Porta, Soco Na Cara|Matanza
2003|Bom É Quando Faz Mal|Matanza
2003|História de Verão|Forfun
2003|Deixa Disso|Felipe Dylon
2003|I Wanna Be|Pitty
2003|O Meu Pau Fica Duro|Rogério Skylab
2003|Stonehenge|Fresno
2003|Você Sabe|Autoramas
2004|Vamos Fugir|Skank
2004|Tamo Aí na Atividade|Charlie Brown Jr.
2004|Longe de Você|Charlie Brown Jr.
2004|Champanhe e Água Benta|Charlie Brown Jr.
2004|Rodo Cotidiano|O Rappa
2004|O Dia Que Não Terminou|Detonautas
2004|Ontem|CPM 22
2004|Queda Livre|Dead Fish
2004|Não Olhe pra Trás|Capital Inicial
2004|Prophecy|Soulfly
2004|Você|Dead Fish
2004|Mesmo Que Mude|Bidê ou Balde
2004|Salão de Festa a Vapor|Dazaranha
2004|Quase Amor|Reação em Cadeia
2004|Bem-Vindo ao Clube|Dead Fish
2004|O Salto|O Rappa
2004|Você Pode Ir Na Janela|Gram
2004|Zero e Um|Dead Fish
2004|Apenas Um Olhar|NX Zero
2004|A Urgência|Dead Fish
2004|Tão Iguais|Dead Fish
2004|Onde Está|Fresno
2004|Tarde Demais|NX Zero
2004|Obrigação|Dead Fish
2004|Princesa|Ludov
2004|Te Procuro|Leela
2004|Adeus Sofia|Dance of Days; Fernanda Takai
2004|Todo Mundo Quer Cuidar de Mim|Brava
2004|Deixe a Terra em Paz|Cólera
2005|Dias de Luta, Dias de Glória|Charlie Brown Jr.
2005|Ela Vai Voltar (Todos os Defeitos de Uma Mulher Perfeita)|Charlie Brown Jr.
2005|Na Sua Estante|Pitty
2005|Um Minuto Para o Fim do Mundo|CPM 22
2005|Senhor do Tempo|Charlie Brown Jr.
2005|Lutar Pelo Que é Meu|Charlie Brown Jr.
2005|Além do Horizonte|Jota Quest
2005|Você Sempre Será|Marjorie Estiano
2005|Déjà Vu|Pitty
2005|Irreversível|CPM 22
2005|Memórias|Pitty
2005|Renata|Tihuana
2005|Condicional|Los Hermanos
2005|Anacrônico|Pitty
2005|Metal is the Law|Massacration
2005|Eu Vi Gnomos|Tihuana
2005|Evil Papagali|Massacration
2005|Good Trip|Forfun
2005|Você Não Sabe o Que Perdeu|Cachorro Grande
2005|Hidropônica|Forfun
2005|Bom Brasileiro|Cachorro Grande
2005|Metal Bucetation|Massacration
2006|Você Me Faz Tão Bem|Detonautas
2006|Razões e Emoções|NX Zero
2006|O Sol|Jota Quest
2006|Além de Mim|NX Zero
2006|Sinceramente|Cachorro Grande
2006|Clube dos Canalhas|Matanza
2006|1997|Hateen
2006|Beijos, Blues e Poesia|K-Sis
2006|Pela Última Vez|NX Zero
2006|Eu Não Gosto de Ninguém|Matanza
2006|Tempo Ruim|Matanza
2006|Meio Psicopata|Matanza
2006|Apostas & Certezas|CPM 22
2006|Quebre As Correntes|Fresno
2006|Quem Já Perdeu Um Sonho Aqui?|Hateen
2006|Lama|Luxúria
2006|Ódio|Luxúria
2006|Alguém Que Te Faz Sorrir|Fresno
2006|Decansar|Canto dos Malditos Na Terra do Nunca
2006|Olha Minha Cara|Canto dos Malditos Na Terra do Nunca
2006|Sinta Vontade de Ficar|Canto dos Malditos Na Terra do Nunca
2006|O Rock Acabou|Moptop
2006|Convicted in Life|Sepultura
2006|Se Um Dia Lembrar de Mim|Hateen
2006|Imperecível|Luxúria
2007|Pontes Indestrutíveis|Charlie Brown Jr.
2007|Sem Você|Rosa de Saron
2007|Paraíso Proibido|Strike
2007|Não Viva em Vão|Charlie Brown Jr.
2007|Uma Criança Com Seu Olhar|Charlie Brown Jr.
2007|Morena|Scracho
2007|O Jogo Virou|Strike
2007|O Amanhã Colorido|Cidadão Quem
2007|Luz Dos Olhos|Nando Reis; Andrea Martins
2007|Polo|Fresno
2007|Aquela História|Strike
2007|Divina Comédia|Scracho
2007|Nossa Música|CPM 22
2007|Aquela Música|Fake Number
2007|Rinha de Magnata|Mukeka di Rato
2008|Ainda Gosto Dela|Skank
2008|Cedo ou Tarde|NX Zero
2008|O Retorno de Saturno|Detonautas
2008|Daqui Pra Frente|NX Zero
2008|Cartas Pra Você|NX Zero
2008|Incondicional|Oficina G3
2008|Em Plena Lua de Mel|Pedra Letícia
2008|Teorema de Carlão|Pedra Letícia
2008|Inflikted|Cavalera Conspiracy
2008|Sol ou Chuva|Forfun
2008|Como Que Ocê Pode Abandoná Eu?|Pedra Letícia
2008|Eu Não Toco Raul|Pedra Letícia
2008|Uma Música|Fresno
2008|Bem ou Mal|NX Zero; Túlio Dek
2008|O Viajante|Forfun
2008|Sanctuary|Cavalera Conspiracy
2008|Aonde Quer Chegar?|Moptop
2008|Escolhas, Provas e Promessas|CPM 22
2008|Contramão|Moptop
2009|Só os Loucos Sabem|Charlie Brown Jr.
2009|Sutilmente|Skank
2009|Me Adora|Pitty
2009|Me Encontra|Charlie Brown Jr.
2009|Súplica Cearense|O Rappa
2009|Levo Comigo|Restart
2009|Desde Quando Você Se Foi|Fresno
2009|Tudo Que Eu Sempre Sonhei|Pullovers
2009|As Cores|Cine
2009|Espero a Minha Vez|NX Zero
2009|Recomeçar|Restart
2009|Só Agora|Pitty
2009|Redenção|Fresno
2009|Fracasso|Pitty
2009|Passos Escuros|Hevo 84
2009|Garota Radical|Cine
2009|Minha Paz|Gloria
2009|O Tempo|Móveis Coloniais de Acaju; Leoni
2009|Minha Vida É Você|Hevo 84
2009|Vou Cantar|Restart
2009|The Bull|Massacration
2009|Usurpadora|Cine
2009|Fora, Mônica|Vivendo do Ócio
2009|Autonomia|Dead Fish
2009|Parecia Estar|Stevens
2009|My Favorite Way|Black Drawing Chalks
2010|Só Rezo|NX Zero
2010|Vida ou Morte|CPM 22
2010|Pra Você Lembrar|Restart
2010|A Tendência|Strike
2010|No Veneno|Strike
2010|Vai Pagar Caro Por Me Conhecer|Gloria
2010|O Maior Idiota do Mundo|Tópaz
2010|Até o Fim|Strike
2010|Tudo Outra Vez|Gloria
2011|Morada|Forfun
2011|Menina Estranha|Restart
2011|Matemática|Restart
2011|Remédios Demais|Matanza
2011|Às Vezes um Clichê|Maglore
2011|Som Sincero|Scracho
2011|Killing Inside|Cavalera Conspiracy
2011|Se For Pra Tudo Dar Errado|Tópaz
2011|Ponto de Paz|Replace
2011|Mulher|Rancore
2011|Mãe|Rancore
2011|Jeito Livre|Rancore
2011|Dois Sorrisos|Móveis Coloniais de Acaju
2011|Abstrai|Autoramas
2012|Reza|Rita Lee
2012|Solitário Surfista|Gabriel O Pensador; Jorge Ben Jor
2012|Fluxo Perfeito|Strike
2012|Hoje o Céu Abriu|NX Zero
2012|Maré|NX Zero
2012|Nostalgia|Vivendo do Ócio
2012|Morto|O Terno
2012|Horizontes|Gloria; Lucas Silveira
2012|Infinito|Fresno
2012|Careless Whisper|Kiara Rocks
2012|The Sad Facts|Cambriana
2012|A Arte de Fazer Inimigos|Gloria
2012|Radioatividade|Vivendo do Ócio
2012|Primeira Lembrança|Fake Number
2013|Anjos (Pra Quem Tem Fé)|O Rappa
2013|Meu Novo Mundo|Charlie Brown Jr.
2013|Amanheceu|Scalene
2013|Um Dia a Gente Se Encontra|Charlie Brown Jr.
2013|Aos Pés da Cruz|Oficina G3
2013|Meu Sol|Vanguart
2013|Viva|Zimbra
2013|Demorou Pra Ser|Vanguart
2013|Um Certo Alguém|Suricato; Lulu Santos
2013|Surreal|Scalene
2013|Despedida|Selvagens À Procura de Lei
2013|Descanso|Oficina G3
2013|Missão Apollo|Zimbra
2013|Amanhã|Zimbra
2013|Não Sei o Que Fazer Comigo|Vespas Mandarinas
2013|Doce|Boogarins
2013|Enquanto Eu Passar Na Sua Rua|Selvagens À Procura de Lei
2013|Brasileiro|Selvagens À Procura de Lei
2013|Dance Macabre|Scalene
2013|Lucifernandis|Boogarins
2013|Cobra de Vidro|Vespas Mandarinas
2013|Sede de Chuva|Móveis Coloniais de Acaju
2013|O Novo Passo|A Banca
2014|Piloto Automático|Supercombo
2014|Um Sonho|Nação Zumbi
2014|Amianto|Supercombo
2014|Diz Pra Mim|Malta
2014|Serpente|Pitty
2014|Memórias|Malta
2014|Ai, Ai, Como Eu Me Iludo|O Terno
2014|Sol da Manhã|Supercombo
2014|A Melhor Hora da Praia|Nação Zumbi
2014|Lendas|Malta
2014|Setevidas|Pitty
2014|Novas Auroras|Nação Zumbi
2014|Vamos Seguir|NX Zero
2014|Todo Dia é Dia de Comemorar|Supercombo
2014|Fé Menina|Dazaranha
2014|Um Tanto|Suricato
2014|Dino vs Dino|Far From Alaska
2014|Eterno Retorno|Medulla
2014|Erro +55|Project46
2014|À Distância|Menores Atos
2014|Trens|Planar
2015|Meu Bem|NX Zero
2015|Já Sei|Zimbra
2015|Fração de Segundos|NX Zero; Lulu Santos
2015|Pedra Murano|NX Zero
2015|Relentless Game|Far From Alaska; Scalene
2015|Café Com Pão|Maglore
2015|Se Você Fosse Minha|Maglore
2015|Dança Diferente|Maglore
2015|Dona da Voz|Malta
2015|Sol de Paz|Strike
2015|Benzin|Boogarins
2015|Um Leão|Pitty
2015|6000 Dias (Ou Mantra dos 20 Anos)|Boogarins
2015|San Lorenzo|Boogarins
2015|Pra Tudo Acontecer|Suricato
2015|Falsa Folha de Rosto|Boogarins
2015|Surrendo|Supercombo
2015|Vitória|Dead Fish
2015|Carranca|Vivendo do Ócio
2015|When It Goes Wrong|Sound Bullet
2015|Fast Relief|Garage Fuzz
2015|Verde Mansidão|Versalle
2015|Option to Repression|Bullet Bane
2016|Volta|O Terno
2016|Não Vá Embora|Silva
2016|Entrelaços|Scalene
2016|Monstros|Supercombo
2016|Culpa|O Terno
2016|João|Oficina G3
2016|Tarde Livre|Selvagens À Procura de Lei
2016|Primeiro Amor|Malta
2016|A História Mais Velha do Mundo|O Terno
2016|Lentes|Supercombo; Negra Li
2016|Grão de Areia|Scalene; Supercombo
2016|Rogério|Supercombo; Keops & Raony
2016|Abraço|Medulla; Martin
2016|Afinar as Rezas|Dazaranha
2016|Azul|Zimbra
2016|Chega Mais Cedo|Dazaranha
2016|The Phoenix|Twin Pumpkin
2016|Passa o Tempo|Hateen
2016|Horizontal|Ponto Nulo no Céu
2016|Bastian Contra o Nada|Zander
2016|Tropical Rain|Fernando Molinari
2016|Se a Gente Tivesse Se Conhecido|El Toro Fuerte
2017|Serenata Existencialista|O Grilo
2017|Ai de Mim|OutroEu; Sandy
2017|Onde Você Anda?|Detonautas
2017|Sambinha|O Grilo
2017|Bonsai|Supercombo
2017|Me Deixa Legal|Maglore
2017|Herói do Futuro|O Grilo
2017|E o Meu Peito Mais Aberto Que o Mar da Bahia|Vanguart
2017|Sublimated|Ego Kill Talent
2017|O Ficar e o Ir da Gente|Plutão Já Foi Planeta
2017|Last Ride|Ego Kill Talent
2017|Collision Course|Far From Alaska
2017|Still Here|Ego Kill Talent
2017|Cobra|Far From Alaska
2017|Rédeas|Project46
2017|Smiles Nike Tim Sprite|Macaco Bong
2017|Cada Instante Sem Você|Cogumelo Plutão
2017|Gangorra|Bullet Bane
2018|Mutação|Bullet Bane
2018|O Sol|Vitor Kley
2018|Não Vou Mentir|Lagum
2018|Adrenalizou|Vitor Kley
2018|Outrória|OutroEu; Anavitória
2018|Pensando Bem|5 a Seco; Tó Brandileone
2018|Maremotos|Supercombo
2018|Interstelar|Mulamba
2018|Mice and Trash Cans|Disaster Cities
2019|Amanhã|Menores Atos
2019|Pupila|Vitor Kley; Anavitória
2019|Oi|Lagum
2019|Solidão de Volta|Terno Rei
2019|Yoko|Terno Rei
2019|Dia Lindo|Terno Rei
2019|Corre Corre|Los Hermanos
2019|Atrás / Além|O Terno
2019|Volta e Meia|O Terno
2019|Menina Largata|Supercombo
2019|Noite Inteira|Pitty; Lazzo Matumbi
2019|Casa Aberta|Scalene
2019|Ninguém É de Ninguém|Pitty
2019|Monolith|Twin Pumpkin
2019|Sangue Nas Mãos|Dead Fish
2019|Para o Grande Amor|Pitty
2019|Bom Dia Senhor|Surra
2020|Cabelo de Anjo|Melim; Lulu Santos
2020|Oceana|OutroEu; Melim
2020|Ainda Bem Que Chegou|Vitor Kley
2020|Mire as Estrelas|Rosa de Saron
2020|Astronauta|Suricato; Melim
2020|Cigana|Suricato
2020|Roda|Pitty; BaianaSystem
2020|O Rio|Scalene
2020|Eva|Far From Alaska
2020|Submersa|Pitty
2020|She Hates the World, We Wanna Die|Twin Pumpkin
2020|Selva Pulsátil|Deafkids
2021|Amarelo, Azul e Branco|Anavitória; Rita Lee
2021|Ninguém Me Ensinou|Lagum
2021|A Cura|Vitor Kley; Lulu Santos
2021|Sorte|Hotelo
2021|Trela|O Grilo
2021|Nunca Fui Desse Lugar|Daparte; Lagum
2021|Motor|Pitty
2021|Bahia Blues|Pitty
2021|The Call|Ego Kill Talent
2022|Acorda Pedrinho|Jovem Dionisio
2022|Tudo Me Lembra Você|Vitor Kley
2022|Dias da Juventude|Terno Rei
2022|Pra Você Gostar de Mim|O Grilo
2022|Intensamente|Di Ferrero; Vitor Kley
2022|Tira a Roupa|O Grilo; Daparte
2022|Fogo Nos Racistas|Black Pantera
2023|Sorte|Silva; Liniker
2023|Infame|Supercombo; Kamaitachi
2023|Delírio|OutroEu; Clarissa
2023|Você Vai Lembrar de Mim|NX Zero
2023|Direitos Autorais|Isa Buzzi
2023|Vilã|Isa Buzzi
2023|Odisseia|Lvcas
2023|Diamantina|Quem é Você, Alice?
2024|Eu Nunca Fui Embora|Fresno
2024|Dentes Amarelos|Dead Fish
2024|Sick Ride|Karen Dió
2024|Frases Para Seu Status|Caiçara Clã
2024|Revenge of the Bull|Massacration
2024|Pinch|Ginger and the Peppers
2024|Prefiro Vila Velha|Maré Tardia
2024|Quando Você Vem|Rancore
"""

# ano|título|artista(s) — funk brasileiro, por ano
FUNK_SONGS = """
1991|Rap da Rocinha|MC Galo
1994|Rap do Solitário|MC Marcinho
1994|Garota Nota 100|MC Marcinho
1994|Me Leva|Latino
1994|Não Adianta Chorar|Latino
1995|Rap das Armas|Cidinho e Doca
1995|Rap da Felicidade|Cidinho e Doca
1995|Rap do Silva|MC Bob Rum
1996|Nosso Sonho|Claudinho & Buchecha
1996|Conquista|Claudinho & Buchecha
1996|Rap do Salgueiro|Claudinho & Buchecha
1997|Quero Te Encontrar|Claudinho & Buchecha
1998|Só Love|Claudinho & Buchecha
1998|Glamurosa|MC Marcinho
2000|Jonathan da Nova Geração|Jonathan Costa
2000|Dança da Motinha|MC Beth
2000|Popozuda Rock 'N' Roll|DeFalla
2000|Já É Sensação|MC Andinho
2000|Tchutchuca|Bonde do Tigrão
2000|Diretoria|MC Primo
2000|Tira a Camisa|Cabo
2001|Um Tapinha Não Dói|MC Naldinho e MC Beth
2001|Cerol na Mão|Bonde do Tigrão
2001|O Baile Todo (Só as Cachorras)|Bonde do Tigrão
2001|Um Morto Muito Louco|Bonde do Tigrão
2001|Elas Estão Descontroladas|Bonde do Tigrão
2001|Tá Tudo Dominado|SD Boys
2001|Agora Eu Tô Solteira|Gaiola das Popozudas
2002|Fico Assim Sem Você|Claudinho & Buchecha
2002|Vai Serginho|MC Serginho & Lacraia
2003|Eguinha Pocotó|MC Serginho & Lacraia
2003|Vai Lacraia|MC Serginho & Lacraia
2004|Renata|Latino
2004|Boladona|Tati Quebra Barraco
2004|Namorar Pelado|MC Pelé
2005|Dona Gigi|Os Caçadores
2005|Atoladinha|MC Bola de Fogo e As Foguentas
2006|Ela Só Pensa Em Beijar (Se Ela Dança Eu Danço)|MC Leozinho e DJ Marlboro
2006|Só Zueira|MC Leozinho
2006|Tremendo Vacilão|Perlla
2006|Vira de Ladinho|MalhaFunk
2006|Vem Kikando|Os Hawaianos
2006|Ela Balança Mas Não Pára|MC Buiú
2006|Tô Tranquilão|MC Sapão
2007|Som de Preto|Amilcka e Chocolate
2007|Late Que Eu Tô Passando|Gaiola das Popozudas
2008|Dança do Créu|MC Créu
2008|Tamborzão Tá Rolando|MC Koringa
2009|Adultério|Mr Catra
2009|Uh Papai Chegou!|Mr Catra
2009|Sequência do Pente|Os Havaianos
2010|Sou Foda|Avassaladores
2012|Fala Mal de Mim|MC Beyoncé (Ludmilla)
2012|Aquecimento das Maravilhas (Quadradinho de 8)|Bonde das Maravilhas
2012|Plaquê de 100|MC Guimê
2012|Dança Sensual|MC Koringa
2012|Pra Me Provocar|MC Koringa
2012|Toda Gostosa|MC Leozinho
2012|Meiga e Abusada|Anitta
2012|Meu Namorado É Maior Otário|MC Carol
2012|Angra dos Reis|MC Daleste
2013|Beijinho no Ombro|Valesca Popozuda
2013|País do Futebol|MC Guimê part. Emicida
2013|Ela É Top|MC Bola
2014|Na Batida|Anitta
2014|Bololo Haha|MC Bin Laden
2014|Roça Roça|MC Brinquedo
2014|Vamos Beber|Dennis feat. João Lucas & Marcelo e Ronaldinho Gaúcho
2015|Baile de Favela|MC João
2015|Tá Tranquilo Tá Favorável|MC Bin Laden
2015|Bem Querer|MC Livinho
2015|Tudo de Bom|MC Livinho
2015|Os Mlk É Liso|MC Rodolfinho
2015|Química|Biel
2016|Bum Bum Tam Tam|MC Fioti
2016|Bumbum Granada|MCs Zaac e Jerry
2016|Olha a Explosão|MC Kevinho
2016|Deu Onda|MC G15
2016|Cheia de Marra|MC Livinho
2016|Tenebrosa|MC Livinho
2016|Vai Embrazando|MC Zaac part. MC Vigary
2016|Vou Desafiar Você|MC Sapão
2016|Bom|Ludmilla
2016|Sim Ou Não|Anitta feat. Maluma
2016|Sua Amiga Vou Pegar|MC Lan e MC WM
2016|Grave Faz Bum|MC WM e MC Lan
2017|O Grave Bater|MC Kevinho
2017|Vai Faz A Fila E Vem Uma De Cada Vez|MC Denny
2017|Agora Vai Sentar|MCs Jhowzinho & Kadinho
2017|Rabetão|MC Lan
2017|Abusadamente|MC Gustta e MC DG
2017|Amar, Amei|MC Don Juan
2017|Cheguei|Ludmilla
2017|Fazer Falta|MC Livinho
2017|Vai Malandra|Anitta, MC Zaac, Maejor feat. Tropkillaz & DJ Yuri Martins
2017|Sua Cara|Major Lazer, Anitta & Pabllo Vittar
2017|Dentro Do Carro|MC Kevin O Chris
2018|Só Quer Vrau|MC MM feat. DJ RD
2018|Envolvimento|MC Loma e as Gêmeas Lacração
2018|Dingo Bell|MC Teteu
2018|Cavalo de Troia|MC Kevin
2018|Amor de Verdade|MC Kekel e MC Rita
2018|Fuleragem|MC WM
2018|Malemolência|Dynho Alves
2018|Din Din Din|Ludmilla, MC Pupio & MC Doguinha
2018|Não Perco Meu Tempo|Anitta
2019|Evoluiu|MC Kevin O Chris feat. Sodré
2019|Sentou e Gostou|MC Jottapê e MC M10
2019|Onda Diferente|Anitta, Ludmilla, Snoop Dogg feat. Papatinho
2019|Terremoto|Anitta & Kevinho
2019|Combatchy|Anitta, Lexa, Luisa Sonza feat. MC Rebecca
2019|Coisa Boa|Gloria Groove
2019|No Baile Nós É Mídia|MC Poze do Rodo
2020|Oh Juliana|MC Niack, Two Maloka e DJ Léo da 17
2020|Desce Pro Play (Pa Pa Pa)|MC Zaac, Anitta, Tyga
2020|Modo Turbo|Luísa Sonza, Pabllo Vittar, Anitta
2020|Na Raba Toma Tapão|MC Niack
2021|Bipolar|MC Don Juan, MC Davi e MC Pedrinho
2021|Dolly|Gloria Groove
2021|No Chão Novinha|Anitta, Pedro Sampaio
2021|Taca a Xereca pra Mim|MC Kaique da VP
2021|Beat da Felicidade|MC Nego da Marcone, MC Meno Dani, DJ Jeeh FDC
2021|Trava na Pose, Chama no Zoom Dá Um Close|DJ Patrick Muniz, DJ Olliver, MC Topre & MC Rennan
2021|Se Tá Solteira|FBC & Vhoor ft. Mac Júlia
2021|Bota na Pipokinha|MC Pipokinha
2021|Sobe e Desce (Illusionize Remix)|Pike Confesser feat. MC GW
2022|Casei Com a Putaria|MC Paiva e MC Ryan SP
2022|Roça Em Mim|Zé Felipe, Ana Castela e Luan Pereira
2022|Ai Preto|L7nnon & Biel do Furduncinho
2022|Louco e Sonhador|MC Neguinho do Kaxeta
2022|Vermelho|Gloria Groove
2022|Boka Loka|DJ Boy, MCs Vine 7, Don Juan, Kako, Joãozinho VT, V7, Tuto, Erik, Pê Leal
2022|SentaDONA|Luísa Sonza, Davi Kneip, MC Frog, DJ Gabriel do Borel
2022|Tubarão, Te Amo|MC Ryan SP e Tchakabum
2022|Puta Rara, Puta Mexicana – Vai Sua Cavalona|Jeeh FDC, Menor MT, Yuri Redicopa, Pelé
2022|Pagodeiro|Davi, Grupo Presença, Paiva ZS, Gabb, Paulin da Capital, Cebezinho
2023|Let's Go 4|MC PH, DJ GBR, IG, Ryan SP, Davi, Luki, Don Juan, Kadu, GH do 7, GP, TrapLaudo
2023|Dentro da Hilux|Luan Pereira, MC Daniel, MC Ryan SP
2023|Tá Ok|Kevin o Chris
2023|Faz um Vuk Vuk|Kevin O Chris, DJ Nk da Serra
2023|Os Menino Tá Com o Pacote|MC PH, DJ Murillo, LT, Solanno, Frank
2023|Tropa do Bruxo|Baile do Bruxo, DJ Ws da Igrejinha, Triz, SMU, MC Menor Thalis, R10
2023|Vai Novinha Ah, Ah, Ah|DJ Dyamante e Mano Walter
2023|Noite Fria|MC IG e MC Pipokinha
2024|The Box Medley Funk 2|DJ Oreia, MC Brinquedo, MC Tuto, MC Laranjinha, MC Cebezinho
2024|MTG Quem Não Quer Sou Eu|DJ Topo, MC Leozin, Seu Jorge, MC G15
2024|Maria Mariah Você Não Sai da Minha Cabeça|MC Meno Dani, Silva MC, JC no Beat, DJ F7
2024|Até O Sol Raiar|MC Hariel
2024|Ram Tchum|Dennis, Ana Castela e MC GW
2024|Diz aí qual é o plano?|MC IG, Luki, GP, Ryan, PH, Poze, Oruam, Traplaudo, GH, Nego Micha
2024|Poc Poc|Pedro Sampaio
2024|Entra Na Defender|Luan Pereira e MC Daniel
2024|Recadin no Espelho|Luísa Sonza e Kevin O Chris
2024|Toma Colocadão|Pedro Sampaio, MC GW, MC Delano, MC Meno K
"""

# ano|álbum|artista|nota pt|nota en — discos essenciais do rock brasileiro (ordem cronológica)
ROCK_ALBUMS = """
1959|Estúpido Cupido|Celly Campello|Primeiro grande sucesso juvenil ligado ao rock no Brasil; abriu caminho para a Jovem Guarda.|Brazil's first big rock-linked teen hit; it paved the way for Jovem Guarda.
1963|Samba Esquema Novo|Jorge Ben Jor|Estreia que fundou o samba-rock, com "Mas Que Nada" e "Vem Morena".|The debut that founded samba-rock, with "Mas Que Nada" and "Vem Morena".
1965|Jovem Guarda|Roberto Carlos|Consolidou o ícone juvenil e deu nome ao movimento, entre iê-iê-iê e baladas.|Made Roberto Carlos the teen idol and named the movement, between iê-iê-iê and ballads.
1967|Em Ritmo de Aventura|Roberto Carlos|Trilha do filme homônimo; auge da Jovem Guarda e do rock no mainstream.|Soundtrack to the film of the same name; the peak of Jovem Guarda and of rock in the mainstream.
1968|Os Mutantes|Os Mutantes|Psicodelia, MPB e experimentos de estúdio, com "Panis et Circenses" e "Bat Macumba".|Psychedelia, MPB and studio experiments, with "Panis et Circenses" and "Bat Macumba".
1968|Tropicália ou Panis et Circensis|Vários Artistas|Manifesto sonoro da Tropicália com Caetano, Gil, Gal, Tom Zé e Os Mutantes.|The Tropicália manifesto, with Caetano, Gil, Gal, Tom Zé and Os Mutantes.
1970|A Divina Comédia ou Ando Meio Desligado|Os Mutantes|Psicodelia madura e canções que viraram clássicos.|Mature psychedelia and songs that became classics.
1970|A Máquina Voadora|Ronnie Von|Disco raro e psicodélico que une progressivo e MPB.|A rare psychedelic record joining prog and MPB.
1970|Som Imaginário|Som Imaginário|Banda ligada a Milton Nascimento; psicodelia, jazz-rock e experimentalismo mineiro.|Milton Nascimento's band; psychedelia, jazz-rock and experimentalism from Minas.
1971|Carlos, Erasmo|Erasmo Carlos|Rock'n'roll, soul e MPB na busca do artista por novas sonoridades.|Rock'n'roll, soul and MPB in the artist's search for new sounds.
1972|Acabou Chorare|Novos Baianos|Rock e pop misturados a samba, baião e choro; citado entre os maiores discos brasileiros.|Rock and pop blended with samba, baião and choro; often ranked among Brazil's greatest records.
1972|Clube da Esquina|Milton Nascimento & Lô Borges|Álbum duplo que combina música mineira, jazz, MPB e rock.|A double album combining music from Minas, jazz, MPB and rock.
1972|Transa|Caetano Veloso|Gravado no exílio em Londres: reggae, progressivo e funk com MPB.|Recorded in London exile: reggae, prog and funk with MPB.
1973|Krig-ha, Bandolo!|Raul Seixas|Início da carreira solo e da persona "maluco beleza"; rock, baião e blues.|Start of the solo career and of the "maluco beleza" persona; rock, baião and blues.
1973|Secos & Molhados|Secos & Molhados|Folk-rock, MPB e psicodelia com a performance andrógina de Ney Matogrosso.|Folk-rock, MPB and psychedelia with Ney Matogrosso's androgynous performance.
1974|Gita|Raul Seixas|Fase experimental, misticismo e crítica social; seu disco mais vendido.|Experimental phase, mysticism and social critique; his best-selling record.
1974|Loki?|Arnaldo Baptista|Primeiro solo após os Mutantes, carregado de psicodelia.|First solo record after Os Mutantes, heavy on psychedelia.
1975|Fruto Proibido|Rita Lee & Tutti Frutti|Consolidou Rita Lee no rock, com "Ovelha Negra".|Cemented Rita Lee in rock, with "Ovelha Negra".
1975|Racional|Tim Maia|Soul, funk e rock psicodélico na fase da Cultura Racional.|Soul, funk and psychedelic rock from the Cultura Racional phase.
1975|Criaturas da Noite|O Terço|Apontado como o maior clássico do progressivo brasileiro.|Often called the greatest classic of Brazilian prog.
1975|Lar de Maravilhas|Casa das Máquinas|Transição para o progressivo, com temas esotéricos.|The move into prog, with esoteric themes.
1976|Bixo da Seda|Bixo da Seda|Um dos primeiros discos de progressivo do Rio Grande do Sul.|One of the first prog records from Rio Grande do Sul.
1976|Jack, o Estripador|Made in Brazil|Blues pesado e letras irônicas; referência do underground paulistano.|Heavy blues and ironic lyrics; a São Paulo underground landmark.
1982|As Aventuras da Blitz|Blitz|Pop-rock, reggae e humor que detonaram o boom do BRock.|Pop-rock, reggae and humour that set off the BRock boom.
1982|Barão Vermelho|Barão Vermelho|Estreia de rock urbano cru com Cazuza e Frejat.|Raw urban-rock debut with Cazuza and Frejat.
1983|Camisa de Vênus|Camisa de Vênus|Sarcasmo e letras diretas; clássico do rock contestador.|Sarcasm and blunt lyrics; a classic of protest rock.
1983|Cinema Mudo|Os Paralamas do Sucesso|Base da sonoridade da banda: ska, reggae e rock, com "Vital e Sua Moto".|The band's blueprint: ska, reggae and rock, with "Vital e Sua Moto".
1984|Fullgás|Marina Lima|Grande disco do pop rock dos 80 que abriu espaço para mulheres no rock.|A great 1980s pop-rock record that opened room for women in rock.
1984|O Passo do Lui|Os Paralamas do Sucesso|Oito das dez faixas viraram hits de rádio.|Eight of its ten tracks became radio hits.
1984|Crucificados Pelo Sistema|Ratos de Porão|Considerado o primeiro punk-hardcore da América Latina.|Regarded as Latin America's first punk-hardcore album.
1984|Titãs|Titãs|Estreia dos oito integrantes, punk e new wave com "Sonífera Ilha".|Debut of the eight-piece line-up, punk and new wave with "Sonífera Ilha".
1985|Legião Urbana|Legião Urbana|Renato Russo como voz da geração; pós-punk e new wave.|Renato Russo as the voice of a generation; post-punk and new wave.
1985|Nós Vamos Invadir Sua Praia|Ultraje a Rigor|Humor ácido e letras críticas; primeiro disco de ouro e platina do rock nacional.|Acid humour and critical lyrics; the first gold and platinum record of Brazilian rock.
1985|Revoluções por Minuto|RPM|Sintetizadores e produção sofisticada; grande sucesso de vendas.|Synthesizers and polished production; a huge seller.
1985|Educação Sentimental|Kid Abelha|Pop-rock delicado com "Fixação" e "Como Eu Quero".|Delicate pop-rock with "Fixação" and "Como Eu Quero".
1985|Mais Podres do que Nunca|Garotos Podres|Fundamental para o punk brasileiro, com "Papai Noel Velho Batuta".|Essential Brazilian punk, with "Papai Noel Velho Batuta".
1985|Televisão|Titãs|Mais pop e acessível; crítica ao papel da mídia.|Poppier and more accessible; a critique of the media.
1985|Exagerado|Cazuza|Estreia solo e início da aproximação com a MPB.|Solo debut and the start of his approach to MPB.
1986|Dois|Legião Urbana|Maior sucesso da banda, com "Tempo Perdido" e "Eduardo e Mônica"; mais de 1 milhão de cópias.|The band's biggest hit, with "Tempo Perdido" and "Eduardo e Mônica"; over a million copies.
1986|Cabeça Dinossauro|Titãs|Raivoso e politizado; para muitos críticos o maior disco dos anos 80.|Angry and political; for many critics the greatest album of the 1980s.
1986|Vivendo e Não Aprendendo|Ira!|Consolidou Edgard Scandurra como compositor; pós-punk e pop rock.|Established Edgard Scandurra as a songwriter; post-punk and pop rock.
1986|Pela Paz em Todo Mundo|Cólera|Punk politizado e pacifista; sucesso de um selo independente.|Political, pacifist punk; an independent-label success.
1986|O Concreto Já Rachou|Plebe Rude|Mini-LP politizado produzido por Herbert Vianna.|A political mini-LP produced by Herbert Vianna.
1986|Rádio Pirata ao Vivo|RPM|Gravação ao vivo com teclados; um dos mais vendidos da indústria.|A live, keyboard-heavy recording; one of the industry's biggest sellers.
1986|O Futuro É Vortex|Os Replicantes|Punk rápido e furioso, com "Surfista Calhorda".|Fast, furious punk, with "Surfista Calhorda".
1986|Longe Demais das Capitais|Engenheiros do Hawaii|Estreia gaúcha, letras existenciais; marco da "invasão gaúcha".|Debut from Rio Grande do Sul, existential lyrics; landmark of the "gaúcho invasion".
1986|Capital Inicial|Capital Inicial|Punk e pós-punk, com "Música Urbana" e "Veraneio Vascaína".|Punk and post-punk, with "Música Urbana" and "Veraneio Vascaína".
1986|Cidade Em Torrente|Biquini Cavadão|Consagrou a banda no pop rock nacional.|Established the band in Brazilian pop rock.
1987|Vida Bandida|Lobão|Rock, pop e new wave com "Vida Bandida" e "Me Chama".|Rock, pop and new wave with "Vida Bandida" and "Me Chama".
1987|A Revolta dos Dândis|Engenheiros do Hawaii|Consolidou a sonoridade do grupo; favorito dos fãs.|Defined the band's sound; a fan favourite.
1988|O Tempo Não Para (Ao Vivo)|Cazuza|Disco ao vivo icônico da fase solo, com canções que viraram hinos.|Iconic live album of the solo years, with songs that became anthems.
1988|Psicoacústica|Ira!|Um dos discos mais experimentais da banda.|One of the band's most experimental albums.
1988|Ideologia|Cazuza|Um dos mais aclamados, com "Ideologia", "Brasil" e "Faz Parte do Meu Show".|Among his most acclaimed, with "Ideologia", "Brasil" and "Faz Parte do Meu Show".
1988|Os Cascavelletes|Os Cascavelletes|Humor ácido e erotismo em rockabilly, garage e punk.|Acid humour and eroticism in rockabilly, garage and punk.
1988|Ouça o que Eu Digo: Não Ouça Ninguém|Engenheiros do Hawaii|Letras filosóficas de Gessinger, com "Terra de Gigantes".|Gessinger's philosophical lyrics, with "Terra de Gigantes".
1989|As Quatro Estações|Legião Urbana|Fase introspectiva, com "Pais e Filhos".|The introspective phase, with "Pais e Filhos".
1989|Õ Blésq Blom|Titãs|Auge da fase áurea da banda em produção e variedade.|Peak of the band's golden era in production and range.
1989|Theatre of Fate|Viper|Primeiro metal melódico brasileiro a ganhar atenção fora do país.|The first Brazilian melodic metal to draw attention abroad.
1990|O Papa é Pop|Engenheiros do Hawaii|Som mais pop e comercial; grande sucesso na década.|A poppier, more commercial sound; a 1990s hit.
1991|Tudo Ao Mesmo Tempo Agora|Titãs|Experimental e pesado; surpreendeu crítica e público.|Experimental and heavy; it surprised critics and fans.
1992|Acústico MTV|Legião Urbana|O álbum mais vendido da banda e um dos mais icônicos do país.|The band's best-selling album and one of the country's most iconic.
1992|Skank|Skank|Estreia de rock, ska e reggae, com "Garganta".|Rock, ska and reggae debut, with "Garganta".
1993|Chaos A.D.|Sepultura|Divisor de águas: música tribal e industrial no thrash metal.|A watershed: tribal and industrial music inside thrash metal.
1993|Angels Cry|Angra|Power metal e música erudita, com a voz de Andre Matos.|Power metal and classical music, with Andre Matos's voice.
1994|Calango|Skank|Mais de um milhão de cópias; consolidou o som da banda.|Over a million copies; it cemented the band's sound.
1994|Da Lama ao Caos|Chico Science & Nação Zumbi|Obra fundadora do manguebeat: rock, maracatu e crítica social.|The founding work of manguebeat: rock, maracatu and social critique.
1994|Raimundos|Raimundos|Punk à Ramones com forró; cerca de 200 mil cópias.|Ramones-style punk with forró; around 200,000 copies.
1994|Cássia Eller|Cássia Eller|Rock, pop e MPB, com "Malandragem".|Rock, pop and MPB, with "Malandragem".
1994|Samba Esquema Noise|Mundo Livre S/A|Eletrônica, maracatu, samba e rock; outro marco do manguebeat.|Electronics, maracatu, samba and rock; another manguebeat landmark.
1994|O Rappa|O Rappa|Estreia focada em crítica social, violência policial e racismo.|A debut centred on social critique, police violence and racism.
1995|Usuário|Planet Hemp|Skate-punk e rap-rock pela legalização; disco de ouro.|Skate-punk and rap-rock for legalization; a gold record.
1995|Mamonas Assassinas|Mamonas Assassinas|Único álbum da banda; humor e paródias, sucesso de vendas.|The band's only album; humour and parody, a sales phenomenon.
1996|Roots|Sepultura|Clássico do metal global com música indígena e ritmos brasileiros.|A global metal classic with Indigenous music and Brazilian rhythms.
1996|Sobre Todas as Forças|Cidade Negra|Reggae e MPB, com "Onde Você Mora".|Reggae and MPB, with "Onde Você Mora".
1996|Tem Mas Acabou|Pato Fu|Primeira parte de um projeto duplo de sonoridade retrô.|First half of a two-album, retro-sounding project.
1996|Jota Quest|Jota Quest|Pop, funk e rock, com "Encontrar Alguém" e "Daqui pra Frente".|Pop, funk and rock, with "Encontrar Alguém" and "Daqui pra Frente".
1997|Transpiração Contínua Prolongada|Charlie Brown Jr.|Estreia com cerca de 250 mil cópias e "Proibida pra Mim".|Debut with around 250,000 copies and "Proibida pra Mim".
1997|A Sétima Efervescência|Júpiter Maçã|Psicodélico e experimental; vanguarda da cena independente.|Psychedelic and experimental; indie avant-garde.
1997|Acústico MTV|Titãs|Versões intimistas com Caetano Veloso e Marina Lima.|Intimate versions with Caetano Veloso and Marina Lima.
1999|Preço Curto, Prazo Longo|Charlie Brown Jr.|Mais de 250 mil cópias e "Zóio de Lula".|Over 250,000 copies and "Zóio de Lula".
1999|Só No Forevis|Raimundos|Forró e carimbó no punk, com "Mulher de Fases".|Forró and carimbó inside punk, with "Mulher de Fases".
1999|Lado B Lado A|O Rappa|Experimental e pesado, com as letras sociais de Marcelo Yuka.|Experimental and heavy, with Marcelo Yuka's social lyrics.
2000|Nadando com os Tubarões|Charlie Brown Jr.|Juventude e temas sociais, com "Não é Sério" e Negra Li.|Youth and social themes, with "Não é Sério" featuring Negra Li.
2000|Ilegal|Tihuana|Rock, reggae e rap, com "Que Ves?".|Rock, reggae and rap, with "Que Ves?".
2001|100% Charlie Brown Jr. – Abalando a Sua Fábrica|Charlie Brown Jr.|Skate punk, rap e hardcore, com "Lugar ao Sol".|Skate punk, rap and hardcore, with "Lugar ao Sol".
2001|Ao Vivo MTV|Skank|Versões desplugadas; uma das maiores vendas da banda.|Unplugged versions; one of the band's biggest sellers.
2001|Acústico MTV|Cássia Eller|Álbum póstumo que reforçou a força da cantora.|A posthumous album that confirmed the singer's power.
2001|Rebirth|Angra|Novo capítulo com formação renovada, com "Nova Era".|A new chapter with a new line-up, with "Nova Era".
2001|Bloco do Eu Sozinho|Los Hermanos|Evolução para um som mais complexo e maduro.|A step toward a more complex, mature sound.
2002|Ritual|Shaman|Metal melódico com influências brasileiras, por ex-membros do Angra.|Melodic metal with Brazilian influences, by former Angra members.
2002|Bocas Ordinárias|Charlie Brown Jr.|Mais rock'n'roll, com "Papo Reto" nas rádios.|More rock'n'roll, with "Papo Reto" on the radio.
2002|Chegou A Hora de Recomeçar|CPM 22|Consolidou o hardcore melódico, com "Dias Atrás" e "Regina Let's Go".|Cemented melodic hardcore, with "Dias Atrás" and "Regina Let's Go".
2003|Ventura|Los Hermanos|Ápice criativo: rock e MPB com arranjos complexos.|Creative peak: rock and MPB with complex arrangements.
2003|Admirável Chip Novo|Pitty|Estreia que trouxe de volta uma voz feminina de força no rock.|A debut that brought a powerful female voice back to rock.
2003|Acústico MTV|Charlie Brown Jr.|Versões desplugadas que viraram marco na discografia.|Unplugged versions that became a landmark in the catalogue.
2003|Detonautas|Detonautas|Rock alternativo de protesto.|Alternative protest rock.
2004|Zero e Um|Dead Fish|Marco do hardcore brasileiro, engajado e potente.|A landmark of Brazilian hardcore, committed and powerful.
2005|Pista Livre|Cachorro Grande|Rock de garagem direto, com rock clássico e blues.|Direct garage rock with classic-rock and blues roots.
2006|NX Zero|NX Zero|Levou a banda ao mainstream do emo e pop punk.|Took the band into emo and pop-punk mainstream.
2006|Ciano|Fresno|Disco seminal do emo brasileiro.|A seminal Brazilian emo record.
2006|Canto dos Malditos Na Terra do Nunca|Canto dos Malditos Na Terra do Nunca|Estreia baiana melancólica, pós-punk e grunge.|A melancholy debut from Bahia, post-punk and grunge.
2007|Desvio de Conduta|Strike|Símbolo do pop punk nacional, com rock, pop e reggae.|A symbol of Brazilian pop punk, with rock, pop and reggae.
2009|Gloria|Gloria|Som pesado e letras impactantes; relevante no metalcore.|Heavy sound and striking lyrics; a metalcore reference.
2009|C_Mpl_Te|Móveis Coloniais de Acaju|Rock, MPB e elementos orquestrais do rock independente.|Rock, MPB and orchestral elements from the indie scene.
2009|Life Is A Big Holiday For Us|Black Drawing Chalks|Stoner, hard rock e blues rock.|Stoner, hard rock and blues rock.
2010|Apanhador Só|Apanhador Só|Experimental e inovador; destaque do "novo rock nacional".|Experimental and inventive; a highlight of the "new Brazilian rock".
2011|Seiva|Rancore|Marco do hardcore melódico e experimental.|A landmark of melodic, experimental hardcore.
2012|O Pensamento É Um Imã|Vivendo do Ócio|Letras poéticas que consolidaram a banda no rock independente.|Poetic lyrics that established the band in indie rock.
2012|Fast Relief|Garage Fuzz|Hardcore melódico direto, com riffs marcantes.|Direct melodic hardcore with memorable riffs.
2013|Real / Surreal|Scalene|Post-stoner, alternativo e progressivo.|Post-stoner, alternative and progressive.
2014|Amianto|Supercombo|Indie, alternativo e emocore com letras emotivas.|Indie, alternative and emocore with emotional lyrics.
2014|Modehuman|Far From Alaska|Som pesado e energético, stoner e metal alternativo.|Heavy, energetic sound, stoner and alternative metal.
2015|Manual ou Guia Livre de Dissolução dos Sonhos|Boogarins|Psicodelia orgânica entre rock, pop e MPB.|Organic psychedelia between rock, pop and MPB.
2015|III|Maglore|Rock alternativo, MPB e folk.|Alternative rock, MPB and folk.
2015|Éter|Scalene|Intensidade e atmosfera; vencedor do Grammy Latino.|Intensity and atmosphere; a Latin Grammy winner.
2017|Ego Kill Talent|Ego Kill Talent|Troca de instrumentos entre os membros; reconhecimento internacional.|Members swap instruments; international recognition.
2017|Continental|Bullet Bane|Post-hardcore agressivo com letras sociais.|Aggressive post-hardcore with social lyrics.
2017|Lá Vem a Morte|Boogarins|Psicodelia atmosférica que lembra os anos 60 e 70.|Atmospheric psychedelia recalling the 60s and 70s.
2019|<atrás/além>|O Terno|Um dos trabalhos mais maduros da banda, sobre existência e tempo.|One of the band's most mature works, about existence and time.
2019|Violeta|Terno Rei|Indie rock melancólico e nostálgico.|Melancholy, nostalgic indie rock.
2022|Ascensão|Black Pantera|Thrash com letras sobre racismo, intolerância e ativismo.|Thrash with lyrics on racism, intolerance and activism.
"""

# discos dos demais gêneros: ver data_albums.py

# ano|artista|destaque(1/0) — sertanejo: artistas por ano de estreia
SERTANEJO = """
1920|Laureano|0
1928|Augusto Calheiros|0
1928|Cornélio Pires|1
1929|Jararaca & Ratinho|0
1930|Mandi & Sorocabinha|0
1936|Alvarenga & Ranchinho|1
1939|Mariano e Caçula|0
1940|Nhô Pai & Nhá Zefa|0
1942|Palmeira & Piraci|0
1942|Raul Torres & Florêncio|1
1944|Bob Nelson|0
1946|Palmeira & Luizinho|0
1947|Nhô Pai & Nhô Fio|0
1950|Zé Carreiro & Carreirinho|1
1951|Cascatinha & Inhana|1
1951|Inezita Barroso|1
1952|Vieira e Vieirinha|0
1953|Zico & Zeca|0
1955|Irmãs Galvão|0
1955|Luizinho e Limeira|0
1955|Sulino & Marrueiro|0
1956|Mazzaropi|1
1956|Zé Fortuna & Pitangueira|0
1958|Tonico & Tinoco|1
1958|Craveiro & Cravinho|0
1959|Délio & Delinha|0
1959|Duo Glacial|0
1959|Nhô Belarmino & Nhá Gabriela|0
1959|Pedro Bento & Zé da Estrada|0
1960|Duo Ciriema|0
1960|Caçula e Marinheiro|0
1960|Tibagi & Miltinho|0
1961|Praião & Prainha|0
1961|Tião Carreiro & Pardinho|1
1961|Canário e Passarinho|0
1962|Marcelo Costa|0
1962|Liu & Léu|0
1964|Teixeirinha e Mary Terezinha|0
1964|Gildo de Freitas|0
1965|Os Filhos de Goiás|0
1966|Abel & Caim|0
1966|Lourenço & Lourival|0
1966|Nalva Aguiar|0
1967|Sérgio Reis|1
1967|Belmonte & Amaraí|1
1968|Dino Franco|0
1969|Léo Canhoto & Robertinho|0
1969|Gilberto & Gilmar|0
1969|Carmen Silva|0
1969|Chitãozinho & Xororó|1
1970|Gino & Geno|0
1971|Durval & Davi|0
1972|Milionário & José Rico|1
1973|Delmir & Delmon|0
1973|Di Paullo & Paulino|0
1973|Trio Parada Dura|1
1973|João Mineiro & Marciano|1
1974|Cezar & Paulinho|0
1975|Voninho|0
1975|Amado Batista|1
1975|Zé do Rancho & Zé do Pinho|0
1976|Matogrosso & Mathias|1
1977|Joaquim & Manuel|0
1977|André & Andrade|0
1978|Zé Mulato & Cassiano|0
1978|Pardinho & Pardal|0
1978|Duduca & Dalvan|0
1979|Donizeti Camargo|0
1980|Zazá & Zezé|0
1980|João Mulato & Douradinho|0
1980|Pena Branca & Xavantinho|0
1980|Rony e Robison|0
1980|Zé do Cedro e João do Pinho|0
1981|Almir Sater|0
1981|Alan & Aladim|0
1981|Chico Rey & Paraná|0
1981|Teodoro & Sampaio|0
1982|As Mineirinhas|0
1983|Cacique & Pajé|0
1983|Althair & Alexandre|0
1983|Leandro & Leonardo|1
1983|Chrystian & Ralf|0
1984|As Marcianas|0
1985|João Paulo & Daniel|1
1986|Felipe & Falcão|0
1986|Mococa & Paraíso|0
1986|Sula Miranda|0
1986|Roberta Miranda|1
1987|Célia & Celma|0
1988|Renê & Ronaldo|0
1988|Gian & Giovani|0
1989|Beth Guzzo|0
1989|Jayne|0
1989|Rionegro & Solimões|0
1990|Juliano Cezar|0
1990|Jads & Jadson|0
1991|Maurício & Mauri|0
1991|Zezé Di Camargo & Luciano|1
1991|Rick & Renner|1
1992|Wilson & Soraia|0
1992|Marlon & Maicon|0
1993|Os Nonatos|0
1994|Rayssa & Ravel|0
1994|Bruno & Marrone|1
1995|Edson & Hudson|1
1995|Racyne & Rafael|0
1995|Daniel & Samuel|0
1995|João Pedro & Cristiano|0
1996|Rosa & Rosinha|0
1996|Sandro Coelho|0
1996|Cleiton & Camargo|0
1997|Lais Yasmin|0
1998|João Neto & Frederico|0
1999|Sandro & Gustavo|0
1999|Canção & Louvor|0
2000|Janaynna Targino|0
2000|Dani Boy|0
2001|André e Felipe|0
2002|Pedro & Thiago|0
2002|Zé Henrique & Gabriel|0
2002|Victor & Leo|1
2003|Eduardo Costa|1
2003|Carlos & Jader|0
2003|João Bosco & Vinícius|0
2003|João Carreiro & Capataz|0
2004|Mayck & Lyan|0
2004|Hugo & Tiago|0
2004|Maiara & Maraisa|1
2004|Simone & Simaria|1
2005|Paula Fernandes|1
2006|Pedro Paulo & Matheus|0
2007|Adair Cardoso|0
2007|Jorge & Mateus|1
2007|Edu & Maraial|0
2007|César Menotti & Fabiano|0
2008|Fred & Gustavo|0
2008|Fernando & Sorocaba|0
2008|Maria Cecília e Rodolfo|0
2008|Marcos & Belutti|0
2008|Alex Ferrari|0
2009|Luan Santana|1
2009|Gusttavo Lima|1
2009|Michel Teló|1
2009|Clayton e Romário|0
2009|Conrado & Aleksandro|0
2009|Humberto & Ronaldo|0
2009|Munhoz & Mariano|0
2010|Bruninho & Davi|0
2010|Henrique e Diego|0
2011|Thaeme & Thiago|0
2011|Henrique & Juliano|1
2011|João Lucas & Marcelo|0
2011|Israel & Rodolffo|0
2011|Naiara Azevedo|0
2011|Cristiano Araújo|1
2011|Gabriel Gava|0
2011|George Henrique & Rodrigo|0
2012|Matheus & Kauan|0
2012|Zé Ricardo & Thiago|0
2012|Raffael Machado|0
2012|Thiago Brava|0
2012|Israel Novaes|0
2012|Zé Neto & Cristiano|1
2013|Breno & Caio Cesar|0
2013|Loubet|0
2013|Lucas Lucco|0
2014|Diego e Victor Hugo|0
2014|Zé Felipe|0
2014|Erikka Rodrigues|0
2015|Bruna Viola|0
2015|Paula Mattos|0
2015|Bruno & Barretto|0
2015|Wesley Safadão|1
2015|Marília Mendonça|1
2015|Jefferson Moraes|0
2016|Lauana Prado|0
2016|Hugo & Guilherme|0
2016|Maycon & Vinícius|0
2016|Day & Lara|0
2017|Gustavo Mioto|0
2017|Luíza & Maurílio|0
2017|Felipe Araújo|0
2018|Murilo Huff|0
2018|Yasmin Santos|0
2019|Guilherme e Benuto|0
2019|Enzo Rabelo|0
2021|Ana Castela|1
2021|Fred & Fabrício|0
2021|Luan Pereira|0
2022|Felipe e Rodrigo|0
2023|Simone Mendes|0
"""


def rows(block, n):
    out = []
    for line in block.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split("|")]
        assert len(parts) == n, line
        out.append(parts)
    return out
