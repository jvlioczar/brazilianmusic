# -*- coding: utf-8 -*-
"""Artistas de rock. Uma linha por artista:
nome|tipo|gêneros (ids separados por vírgula)|ano de início|UF|nível (S/A/B)|tags|resumo pt|resumo en
tipo: band, solo, duo, group, mc, dj, collective. Campos vazios são permitidos."""

ROCK = """
Os Mutantes|band|psicodelico,tropicalia|1966|SP|S|en|Coluna vertebral do Tropicalismo no rock: psicodelia anglo-americana e experimentação de estúdio aplicadas à música brasileira.|The backbone of Tropicália in rock: Anglo-American psychedelia and studio experimentation applied to Brazilian music.
Sepultura|band|thrash-death|1984|MG|S|en|Maior exportação do metal brasileiro; "Chaos A.D." e "Roots" trouxeram percussão e temas indígenas ao thrash.|Brazil's biggest metal export; "Chaos A.D." and "Roots" brought percussion and Indigenous themes into thrash.
Legião Urbana|band|brock,pos-punk,rock-brasilia|1982|DF|S||Letras poéticas e críticas que viraram referências geracionais; discografia coesa mesmo após o fim, em 1996.|Poetic, critical lyrics that became generational references; a cohesive catalogue even after the end in 1996.
Charlie Brown Jr.|band|rap-rock,hardcore,rock-alternativo|1992|SP|S||Hardcore, rap, reggae e cultura de skate com refrões massivos que dominaram rádio e TV do fim dos 90 aos anos 2000.|Hardcore, rap, reggae and skate culture with massive choruses that ruled radio and TV from the late 90s through the 2000s.
Titãs|band|brock,punk,pop-rock|1982|SP|S||Versatilidade e reinvenção constantes; "Cabeça Dinossauro" é o ponto de virada entre punk, crítica social e pop.|Constant versatility and reinvention; "Cabeça Dinossauro" is the turning point between punk, social critique and pop.
Barão Vermelho|band|brock,hard-rock|1981|RJ|S||A parceria Cazuza/Frejat criou clássicos do blues-rock urbano e definiu o rock de rádio dos anos 1980.|The Cazuza/Frejat partnership created urban blues-rock classics and defined 1980s radio rock.
Os Paralamas do Sucesso|band|brock,ska,pop-rock|1982|RJ|S||Popularizaram a fusão de rock com reggae e ska, com repertório radiofônico e consciência social.|Popularized the fusion of rock with reggae and ska, with a radio-friendly catalogue and social awareness.
Novos Baianos|band|psicodelico,samba-rock|1969|BA|S||Fundiram samba, choro e rock com poesia e vida coletiva; "Acabou Chorare" é um dos maiores discos brasileiros.|Fused samba, choro and rock with poetry and communal living; "Acabou Chorare" is one of Brazil's greatest records.
Secos & Molhados|band|psicodelico|1971|SP|S||Teatralidade glam e poesia; o disco de estreia (1973) bateu recordes de venda e revelou Ney Matogrosso.|Glam theatricality and poetry; the 1973 debut broke sales records and revealed Ney Matogrosso.
Chico Science & Nação Zumbi|band|manguebeat|1991|PE|S||Fundadores do manguebeat: maracatu, guitarras e hip-hop com crítica social; recolocaram o Nordeste na vanguarda.|Founders of manguebeat: maracatu, guitars and hip-hop with social critique; they put the Northeast back at the vanguard.
Engenheiros do Hawaii|band|brock,rock-gaucho|1985|RS|S||Rock de ideias com as letras de Humberto Gessinger, arranjos engenhosos e milhões de discos vendidos.|Rock of ideas with Humberto Gessinger's lyrics, clever arrangements and millions of records sold.
O Rappa|band|rap-rock,reggae-brasileiro|1993|RJ|A||Rock, reggae, funk, hip-hop e samba em crônicas urbanas; "Lado B Lado A" é o marco.|Rock, reggae, funk, hip-hop and samba in urban chronicles; "Lado B Lado A" is the landmark.
Skank|band|pop-rock,ska|1991|MG|A||Do ska a um pop sofisticado, com presença constante em rádios e estádios por três décadas.|From ska to sophisticated pop, a constant presence on radio and in stadiums for three decades.
Capital Inicial|band|brock,pos-punk,rock-brasilia|1982|DF|A||Transformou o pós-punk brasiliense em linguagem de massa; nasceu das cinzas do Aborto Elétrico.|Turned Brasília post-punk into a mass language; born from the ashes of Aborto Elétrico.
Angra|band|heavy-power|1991|SP|A|en|Power/prog de alta técnica com influências eruditas; discos conceituais e forte circulação na Europa e no Japão.|High-technique power/prog with classical influences; concept albums and a strong following in Europe and Japan.
Clube da Esquina|collective|clube-da-esquina|1972|MG|A||Movimento mineiro que une rock, bossa, jazz e folclore; o álbum de 1972 é o marco.|The Minas movement joining rock, bossa, jazz and folklore; the 1972 album is the landmark.
Ira!|band|brock,pos-punk|1981|SP|A||Pós-punk paulista de riffs angulosos e letras urbanas; clássicos dos anos 1980 e retorno aos palcos.|São Paulo post-punk with angular riffs and urban lyrics; 1980s classics and a return to the stage.
Planet Hemp|band|rap-rock|1993|RJ|A||Rap-rock com ativismo pela legalização da maconha; enfrentou prisão e censura em 1997.|Rap-rock with cannabis-legalization activism; faced arrest and censorship in 1997.
Los Hermanos|band|indie,rock-alternativo|1997|RJ|A||De hits adolescentes a arranjos sofisticados; "Ventura" influenciou muito além do indie.|From teen hits to sophisticated arrangements; "Ventura" influenced far beyond indie.
Raimundos|band|hardcore,punk,rock-comico|1987|DF|A||Hardcore com levadas de forró e humor; uma trilha de hits nos anos 1990.|Hardcore with forró grooves and humour; a trail of hits in the 1990s.
Mamonas Assassinas|band|rock-comico|1989|SP|A||Fenômeno de um único álbum (1995), humor e milhões de cópias; a tragédia de 1996 encerrou a história.|A one-album phenomenon (1995), humour and millions of copies; the 1996 tragedy ended the story.
Pitty|solo|rock-alternativo,hardcore|1997|BA|A||Com "Admirável Chip Novo" (2003) recolocou guitarras e voz feminina no centro do pop-rock.|With "Admirável Chip Novo" (2003) she put guitars and a female voice back at the centre of pop-rock.
RPM|band|brock,pos-punk|1983|SP|A||Sintetizadores e "Rádio Pirata ao Vivo", um dos discos mais vendidos do rock nacional.|Synthesizers and "Rádio Pirata ao Vivo", one of the best-selling records of Brazilian rock.
CPM 22|band|hardcore,pop-punk|1995|SP|A||Levou o hardcore melódico ao grande público; Grammy Latino de Melhor Álbum de Rock Brasileiro em 2008.|Took melodic hardcore to the mass public; Latin Grammy for Best Brazilian Rock Album in 2008.
Kid Abelha|band|brock,pop-rock|1981|RJ|A||Pop-rock de melodias marcantes e a voz de Paula Toller; milhões de discos vendidos.|Pop-rock of catchy melodies and Paula Toller's voice; millions of records sold.
Pato Fu|band|pop-rock,rock-alternativo|1992|MG|A||Com "Música de Brinquedo" mostrou que um conceito lúdico pode chegar ao topo.|With "Música de Brinquedo" it showed a playful concept can reach the top.
Jota Quest|band|pop-rock|1993|MG|A||Pop, funk e soul com pegada de banda ao vivo; presença contínua em rádios desde os anos 1990.|Pop, funk and soul with a live-band feel; a continuous radio presence since the 1990s.
Ultraje a Rigor|band|brock,punk,rock-comico|1981|SP|A||Humor, guitarras e crítica social, com "Inútil"; marcos para a geração das Diretas Já.|Humour, guitars and social critique, with "Inútil"; landmarks for the Diretas Já generation.
Camisa de Vênus|band|punk,rock-comico|1980|BA|A||Rock cru e provocador, letras ácidas e a persona de Marcelo Nova.|Raw, provocative rock, acid lyrics and Marcelo Nova's persona.
NX Zero|band|emo,hardcore|2001|SP|A||Consolidou o emo/hardcore no mainstream dos anos 2000, com prêmios e discos de platina.|Cemented emo/hardcore in the 2000s mainstream, with awards and platinum records.
Ratos de Porão|band|hardcore,punk,thrash-death|1981|SP|B|en|Pioneiros do hardcore/crossover no Brasil, abrindo caminho para o metal extremo nacional.|Pioneers of hardcore/crossover in Brazil, opening the way for the national extreme-metal scene.
Sarcófago|band|thrash-death|1985|MG|B|en|Seminal no black/death metal brasileiro, com "INRI" e "The Laws of Scourge".|Seminal in Brazilian black/death metal, with "INRI" and "The Laws of Scourge".
Krisiun|band|thrash-death|1990|RS|B|en|Trio de death metal técnico e veloz, com alcance internacional e grandes festivais.|A fast, technical death-metal trio with international reach and big festivals.
Plebe Rude|band|pos-punk,rock-brasilia|1981|DF|B||Nome-chave do BRock brasiliense: pós-punk e letras sociopolíticas.|A key name of Brasília's BRock: post-punk and socio-political lyrics.
Inocentes|band|punk|1981|SP|B||Uma das bases do punk paulistano, com trajetória longa e influência em dezenas de bandas.|One of the foundations of São Paulo punk, with a long career and influence on dozens of bands.
Nervosa|band|thrash-death|2010|SP|B|en|Power trio feminino que projetou o thrash brasileiro no exterior.|A female power trio that projected Brazilian thrash abroad.
Viper|band|heavy-power|1985|SP|B|en|Pilar do heavy/power metal nacional; revelou Andre Matos no fim dos anos 1980.|A pillar of Brazilian heavy/power metal; it revealed Andre Matos in the late 1980s.
Cólera|band|punk|1979|SP|B||Símbolo do punk/hardcore paulista, postura militante e atuação DIY.|A symbol of São Paulo punk/hardcore, militant stance and DIY practice.
Korzus|band|thrash-death|1983|SP|B||Veterana do thrash paulista, presente em coletâneas históricas como "SP Metal II".|A veteran of São Paulo thrash, on historic compilations such as "SP Metal II".
Dead Fish|band|hardcore|1991|ES|B||Hardcore melódico de crítica social e forte base independente; "Zero e Um" (2004) deu projeção nacional.|Melodic hardcore with social critique and a strong independent base; "Zero e Um" (2004) brought national reach.
Garotos Podres|band|punk|1982|SP|B||Punk debochado e politizado, com "Mais Podres do que Nunca" e "Papai Noel, Velho Batuta".|Cheeky, political punk, with "Mais Podres do que Nunca" and "Papai Noel, Velho Batuta".
Dr. Sin|band|hard-rock,heavy-power|1991|SP|B||Power trio virtuoso que elevou o padrão técnico do hard/heavy no Brasil.|A virtuoso power trio that raised the technical bar of Brazilian hard/heavy.
Shaman|band|heavy-power|2000|SP|B|en|Power/prog formado por ex-integrantes do Angra, com o sucesso "Fairy Tale".|Power/prog formed by former Angra members, with the hit "Fairy Tale".
Cavalera Conspiracy|band|thrash-death|2007|SP|B||Reúne os irmãos Max e Igor Cavalera e reativa o thrash/groove brasileiro no mundo.|Reunites brothers Max and Igor Cavalera and revives Brazilian thrash/groove worldwide.
Aborto Elétrico|band|punk,rock-brasilia|1978|DF|B||Origem do Legião Urbana e do Capital Inicial: existência curta, influência enorme.|The origin of Legião Urbana and Capital Inicial: short-lived, hugely influential.
Os Replicantes|band|punk,rock-gaucho|1983|RS|B||Punk irreverente que uniu cinema e contracultura com humor ácido.|Irreverent punk joining cinema and counterculture with acid humour.
Made in Brazil|band|hard-rock|1967|SP|B||Lenda do rock paulistano, longevidade e força no palco.|A São Paulo rock legend, long-lived and powerful on stage.
Blitz|band|brock,pos-punk|1981|RJ|B||Detonou o boom do BRock no início dos anos 1980, com teatro, humor e hits.|Set off the BRock boom in the early 1980s, with theatre, humour and hits.
Biquini Cavadão|band|brock,pop-rock|1985|RJ|B||Veterana de "Vento Ventania" e "Janaína", ainda em grandes palcos; hoje chamada Biquini.|A veteran of "Vento Ventania" and "Janaína", still on big stages; now called Biquini.
Nenhum de Nós|band|pop-rock,rock-gaucho|1986|RS|B||Pop/rock gaúcho de melodias fortes, com "Camila, Camila" e "O Astronauta de Mármore".|Pop/rock from Rio Grande do Sul with strong melodies, "Camila, Camila" and "O Astronauta de Mármore".
Raulzito e os Panteras|band|jovem-guarda|1967|BA|B||Primeiro registro de Raul Seixas; origem do rock brasileiro do fim dos anos 1960.|Raul Seixas's first recording; an origin point of late-1960s Brazilian rock.
Lobão & Os Ronaldos|band|brock|1984|RJ|B||Projeto com o hit "Me Chama", que ajudou a formatar o rock oitentista.|The project behind the hit "Me Chama", which helped shape 1980s rock.
Os Cascavelletes|band|rock-comico,rock-gaucho|1986|RS|B||Ícones do "porn-rock" sulista, ironia e polêmica.|Icons of southern "porn-rock", irony and controversy.
Cachorro Grande|band|garage,rock-gaucho|1999|RS|B||Revivalismo sixties/seventies com energia de palco e prêmios na era MTV.|Sixties/seventies revivalism with stage energy and awards in the MTV era.
Matanza|band|punk,rock-comico|1996|RJ|B||Criou o "countrycore": hardcore, metal e imagética de faroeste.|Created "countrycore": hardcore, metal and Western imagery.
Velhas Virgens|band|rock-comico|1986|SP|B||Independente e longeva, humor adulto e rock de bar com público fiel.|Independent and long-lived, adult humour and bar rock with a loyal crowd.
O Terço|band|progressivo,psicodelico|1968|RJ|B||Pilar do prog dos anos 1970: psicodelia, rock rural e "Criaturas da Noite".|A pillar of 1970s prog: psychedelia, rural rock and "Criaturas da Noite".
A Cor do Som|band|psicodelico|1977|BA|B||Rock com frevo, baião e choro, nascido no entorno dos Novos Baianos.|Rock with frevo, baião and choro, born around Novos Baianos.
Voluntários da Pátria|band|pos-punk|1981|SP|B||Primeiro pós-punk brasileiro com proposta estética clara, em São Paulo.|The first Brazilian post-punk with a clear aesthetic, in São Paulo.
Carne Doce|band|indie|2013|GO|B||Indie de lirismo afiado; "Tônus" figurou entre os melhores do ano.|Indie with sharp lyricism; "Tônus" ranked among the year's best.
Boogarins|band|psicodelico,indie|2012|GO|B||Psicodelia moderna com alcance internacional desde o primeiro disco; o "Tame Impala brasileiro".|Modern psychedelia with international reach from the first album; the "Brazilian Tame Impala".
Far From Alaska|band|stoner,rock-alternativo|2012|RN|B|en|Stoner/alt-rock pesado, nascida em Natal e radicada em São Paulo; presença constante em festivais.|Heavy stoner/alt-rock, born in Natal and based in São Paulo; a festival regular.
O Terno|band|indie|2009|SP|B||Trio de pop sofisticado e letras de cronista urbano; referência do indie dos anos 2010.|A trio of sophisticated pop and urban-chronicler lyrics; an indie reference of the 2010s.
Terno Rei|band|indie,shoegaze|2010|SP|B||Indie/shoegaze de apelo geracional e grandes festivais, com "Violeta".|Indie/shoegaze with generational appeal and big festivals, with "Violeta".
Ego Kill Talent|band|grunge,rock-alternativo|2014|SP|B|en|Rock moderno de alcance internacional e passagens por festivais globais.|Modern rock with international reach and appearances at global festivals.
Detonautas Roque Clube|band|rock-alternativo|1997|RJ|B||Rock alternativo com crônica social; surgiu na internet e alcançou grande público.|Alternative rock with social chronicle; it emerged online and reached a wide audience.
Fresno|band|emo,rock-gaucho|1999|RS|B||Símbolo do emo brasileiro, reinventado ao longo de muitos álbuns.|The symbol of Brazilian emo, reinvented across many albums.
Oficina G3|band|rock-cristao,heavy-power|1987|SP|B||Pioneira do metal cristão e progressivo no Brasil.|A pioneer of Christian and progressive metal in Brazil.
Forfun|band|ska,pop-rock|2001|RJ|B||Do surf/alt-rock ao reggae e à MPB, com letras positivas marcantes nos anos 2000; encerrou em 2015.|From surf/alt-rock to reggae and MPB, with upbeat lyrics that marked the 2000s; ended in 2015.
Supercombo|band|indie,rock-alternativo|2007|ES|B||Indie/alt-rock de refrões geracionais, com "Piloto Automático".|Indie/alt-rock with generational choruses, with "Piloto Automático".
Scalene|band|stoner,rock-alternativo,rock-brasilia|2009|DF|B||Post-stoner/alt-rock; Grammy Latino por "Éter" e vice do Superstar.|Post-stoner/alt-rock; a Latin Grammy for "Éter" and runner-up on Superstar.
Selvagens à Procura de Lei|band|indie,garage|2009|CE|B||Rock contemporâneo cearense com lírica urbana e discografia consistente.|Contemporary rock from Ceará with urban lyrics and a consistent catalogue.
Lagum|band|pop-rock|2014|MG|B||Pop-rock de grande alcance digital e radiofônico nos anos 2020.|Pop-rock with big digital and radio reach in the 2020s.
O Teatro Mágico|collective|indie|2003|SP|B||Projeto multimídia que une circo, teatro e música, com downloads massivos.|A multimedia project joining circus, theatre and music, with massive downloads.
Massacration|band|rock-comico,heavy-power|2004|SP|B||Paródia do metal que virou fenômeno, com shows, álbuns e programa na MTV.|A metal parody that became a phenomenon, with shows, albums and an MTV programme.
Rancore|band|hardcore,rock-alternativo|2001|SP|B||Hardcore/alt com o disco cultuado "Seiva" e performances intensas.|Hardcore/alt with the cult album "Seiva" and intense performances.
Casa das Máquinas|band|progressivo,hard-rock|1973|SP|B||Pilar dos anos 1970, do hard ao progressivo; reunião após décadas.|A 1970s pillar, from hard rock to prog; reunited after decades.
Patrulha do Espaço|band|hard-rock,progressivo|1977|SP|B||Hard/prog com álbuns de culto e o riff de "Columbia".|Hard/prog with cult albums and the "Columbia" riff.
LS Jack|band|pop-rock|1997|RJ|B||Pop/rock de forte presença radiofônica entre 1999 e 2005.|Pop/rock with a strong radio presence between 1999 and 2005.
Gloria|band|metalcore,emo|2002|SP|B||Peso moderno entre post-hardcore, emo e metal, do underground aos grandes palcos.|Modern heaviness between post-hardcore, emo and metal, from underground to big stages.
Restart|band|pop-punk,pop-rock|2008|SP|B||Fenômeno teen do "happy rock" no fim dos anos 2000.|The teen phenomenon of "happy rock" in the late 2000s.
Tihuana|band|rap-rock|1999|SP|B||Rock, reggae, rap e latinidades, com o hit "Tropa de Elite".|Rock, reggae, rap and Latin flavours, with the hit "Tropa de Elite".
Black Pantera|band|thrash-death,hardcore|2014|MG|B||Trio de crossover thrash/hardcore com discurso antirracista.|A crossover thrash/hardcore trio with an anti-racist message.
O Surto|band|grunge,rock-alternativo|1994|GO|B||Rock do início dos anos 2000, conhecido por "A Cera".|Early-2000s rock, known for "A Cera".
Reação em Cadeia|band|emo,grunge,rock-gaucho|1999|RS|B||Pop rock/emo dos anos 2000, letras confessionais e refrões de rádio.|2000s pop rock/emo, confessional lyrics and radio choruses.
Hateen|band|emo,hardcore|1994|SP|B||Emo/melodic hardcore que ajudou a consolidar a cena independente paulistana.|Emo/melodic hardcore that helped build São Paulo's independent scene.
Móveis Coloniais de Acaju|band|indie,ska,rock-brasilia|1998|DF|B||Indie com sopros que mistura ska, rock e MPB em shows festivos.|Horn-driven indie mixing ska, rock and MPB in festive shows.
Roupa Nova|band|pop-rock|1980|RJ|A||Soft rock de trilhas de novela: "Anjo", "Dona", "Whisky a Go-Go".|Soap-opera soft rock: "Anjo", "Dona", "Whisky a Go-Go".
Lulu Santos|solo|pop-rock,brock|1974|RJ|A||Guitarrista e compositor do pop rock desde os anos 1980; "Tempos Modernos", "Toda Forma de Amor".|Pop-rock guitarist and songwriter since the 1980s; "Tempos Modernos", "Toda Forma de Amor".
Lobão|solo|brock,pos-punk|1974|RJ|A||Baterista da Blitz e depois solo: "Vida Bandida", "Me Chama".|Blitz's drummer, then solo: "Vida Bandida", "Me Chama".
Ritchie|solo|pos-punk|1972|RJ|A||Inglês radicado no Brasil; "Menina Veneno" (1983).|An Englishman based in Brazil; "Menina Veneno" (1983).
Metrô|band|pos-punk|1978|SP|B||New wave paulistana com Virginie Boutaud: "Beat Acelerado".|São Paulo new wave with Virginie Boutaud: "Beat Acelerado".
Zero|band|pos-punk|1983|SP|B||Pós-punk com Guilherme Isnard: "Agora Eu Sei", "Formosa".|Post-punk with Guilherme Isnard: "Agora Eu Sei", "Formosa".
Inimigos do Rei|band|rock-comico|1986|RJ|B||"Adelaide", "Uma Barata Chamada Kafka".|"Adelaide", "Uma Barata Chamada Kafka".
João Penca e Seus Miquinhos Amestrados|band|rock-comico|1980|RJ|B||Rockabilly cômico dos anos 1980.|Comic rockabilly of the 1980s.
Dr. Silvana & Cia.|band|rock-comico|1983|RJ|B||"Serão Extra", "Taca a Mãe pra Ver se Quica".|"Serão Extra", "Taca a Mãe pra Ver se Quica".
Cássia Eller|solo|rock-alternativo,mpb-classica|1990|RJ|A||Uma das maiores vozes do rock brasileiro dos anos 1990: "Malandragem", "O Segundo Sol".|One of the greatest voices of 1990s Brazilian rock: "Malandragem", "O Segundo Sol".
Rita Lee|solo|psicodelico,pop-rock|1963|SP|S||Dos Mutantes à carreira solo: a "rainha do rock brasileiro".|From Os Mutantes to a solo career: the "queen of Brazilian rock".
Raul Seixas|solo|psicodelico,jovem-guarda|1967|BA|S||O "maluco beleza": "Metamorfose Ambulante", "Gita", "Maluco Beleza".|The "maluco beleza": "Metamorfose Ambulante", "Gita", "Maluco Beleza".
Roberto Carlos|solo|jovem-guarda,pop-rock|1960|ES|S||O "Rei": do iê-iê-iê da Jovem Guarda às baladas românticas.|The "King": from Jovem Guarda's iê-iê-iê to romantic ballads.
Erasmo Carlos|solo|jovem-guarda,pop-rock|1958|RJ|A||O "Tremendão", parceiro de Roberto Carlos e pioneiro do rock brasileiro.|The "Tremendão", Roberto Carlos's partner and a Brazilian rock pioneer.
Wanderléa|solo|jovem-guarda|1963|MG|A||A "Ternurinha" da Jovem Guarda.|Jovem Guarda's "Ternurinha".
Celly Campello|solo|jovem-guarda|1958|SP|A||"Estúpido Cupido" (1959): o primeiro ídolo teen do rock brasileiro.|"Estúpido Cupido" (1959): Brazilian rock's first teen idol.
Renato e Seus Blue Caps|band|jovem-guarda|1959|RJ|A||"Menina Linda", "Feche os Olhos".|"Menina Linda", "Feche os Olhos".
Os Incríveis|band|jovem-guarda|1962|SP|A||"Era Um Garoto Que Como Eu Amava os Beatles e os Rolling Stones".|"Era Um Garoto Que Como Eu Amava os Beatles e os Rolling Stones".
Golden Boys|group|jovem-guarda|1958|RJ|B||"Alguém na Multidão", "Andança".|"Alguém na Multidão", "Andança".
Jerry Adriani|solo|jovem-guarda|1964|SP|A||Ídolo romântico da Jovem Guarda.|Jovem Guarda's romantic idol.
Ronnie Von|solo|jovem-guarda,psicodelico|1966|RJ|A||O "Príncipe"; "A Máquina Voadora" (1970) é cult psicodélico.|The "Prince"; "A Máquina Voadora" (1970) is a psychedelic cult record.
Ed Wilson|solo|jovem-guarda|1960|RJ|B||"Telefonema", "Biquini de Bolinha Amarelinha".|"Telefonema", "Biquini de Bolinha Amarelinha".
Os Baobás|band|jovem-guarda,garage|1965|SP|B||Garage da Jovem Guarda: "Pintada de Preto".|Jovem Guarda garage: "Pintada de Preto".
Som Imaginário|band|progressivo,clube-da-esquina|1970|MG|B||Banda de Milton Nascimento; "Feira Moderna".|Milton Nascimento's band; "Feira Moderna".
Lô Borges|solo|clube-da-esquina|1972|MG|A||"O Trem Azul", "Paisagem da Janela", "Um Girassol da Cor do Seu Cabelo".|"O Trem Azul", "Paisagem da Janela", "Um Girassol da Cor do Seu Cabelo".
Beto Guedes|solo|clube-da-esquina|1971|MG|A||"Amor de Índio", "Sol de Primavera", "O Sal da Terra".|"Amor de Índio", "Sol de Primavera", "O Sal da Terra".
14 Bis|band|clube-da-esquina,pop-rock|1979|MG|A||"Planeta Sonho", "Linda Juventude", "Todo Azul do Mar".|"Planeta Sonho", "Linda Juventude", "Todo Azul do Mar".
Bacamarte|band|progressivo|1974|RJ|B||"Depois do Fim" (1983), clássico do prog brasileiro.|"Depois do Fim" (1983), a Brazilian prog classic.
Bixo da Seda|band|progressivo,rock-gaucho|1976|RS|B||Prog gaúcho dos anos 1970.|1970s prog from Rio Grande do Sul.
A Bolha|band|psicodelico,hard-rock|1965|RJ|B||Psicodelia e hard dos anos 1970.|1970s psychedelia and hard rock.
O Peso|band|hard-rock,psicodelico|1971|RJ|B||Hard rock pioneiro.|Pioneering hard rock.
Ave Sangria|band|psicodelico|1969|PE|B||Psicodelia pernambucana dos anos 1970.|1970s psychedelia from Pernambuco.
Módulo 1000|band|psicodelico|1969|RJ|B||"Não Fale com Paredes" (1972), cult psicodélico.|"Não Fale com Paredes" (1972), a psychedelic cult record.
Marina Lima|solo|pop-rock|1977|RJ|A||"Fullgás" (1984) abriu espaço para mulheres no pop rock.|"Fullgás" (1984) opened room for women in pop rock.
Cazuza|solo|brock,pop-rock|1980|RJ|S||Do Barão Vermelho à carreira solo: "Exagerado", "Ideologia", "O Tempo Não Para".|From Barão Vermelho to a solo career: "Exagerado", "Ideologia", "O Tempo Não Para".
Frejat|solo|pop-rock|1981|RJ|A||Guitarrista do Barão Vermelho; solo com "Segredos" e "Amor pra Recomeçar".|Barão Vermelho's guitarist; solo with "Segredos" and "Amor pra Recomeçar".
Nando Reis|solo|pop-rock|1982|SP|A||Baixista dos Titãs e compositor de sucessos para Cássia Eller, Skank e Marisa Monte.|Titãs bassist and hit songwriter for Cássia Eller, Skank and Marisa Monte.
Lenine|solo|mpb-classica,pop-rock|1979|PE|A||Violão percussivo pernambucano: "Na Pressão", "Paciência".|Percussive guitar from Pernambuco: "Na Pressão", "Paciência".
Fábio Jr.|solo|pop-rock|1969|SP|A||Baladas românticas desde os anos 1970.|Romantic ballads since the 1970s.
Marjorie Estiano|solo|pop-rock|2003|PR|B||Atriz e cantora, "Você Sempre Será".|Actress and singer, "Você Sempre Será".
Vitor Kley|solo|pop-rock|2009|RS|A||"O Sol" (2018), "Adrenalizou".|"O Sol" (2018), "Adrenalizou".
Zimbra|band|pop-rock|2010|SP|B||Pop rock de Santos; Lollapalooza 2015 e Rock in Rio 2019.|Pop rock from Santos; Lollapalooza 2015 and Rock in Rio 2019.
Anavitória|duo|pop-rock,nova-mpb|2014|TO|A||Duo de voz e violão: "Trevo (Tu)", "Fica".|A voice-and-guitar duo: "Trevo (Tu)", "Fica".
Laura Schadeck|solo|pop-punk|2014|SC|B||Pop punk cantado em português.|Pop punk sung in Portuguese.
Isa Buzzi|solo|pop-rock|2019|SP|B||Nova geração do pop rock: "Vilã", "Direitos Autorais".|The new generation of pop rock: "Vilã", "Direitos Autorais".
Ginger and the Peppers|band|hard-rock|2020|SP|B|en|Hard/blues rock cantado em inglês.|Hard/blues rock sung in English.
Golpe de Estado|band|hard-rock|1985|SP|B||Hard rock paulistano dos anos 1980.|1980s São Paulo hard rock.
Anjos da Noite|band|hard-rock|1989|SP|B||Hard/glam dos anos 1990.|1990s hard/glam.
Tianastácia|band|rock-comico,hard-rock|1992|MG|B||Rock mineiro bem-humorado: "Cabrobró".|Good-humoured rock from Minas: "Cabrobró".
Black Drawing Chalks|band|stoner,hard-rock|2005|GO|B|en|Stoner/hard rock goiano em inglês; "Life Is a Big Holiday for Us".|Stoner/hard rock from Goiás in English; "Life Is a Big Holiday for Us".
Hellbenders|band|stoner,hard-rock|2007|GO|B|en|Hard rock e stoner de Goiânia.|Hard rock and stoner from Goiânia.
Kiara Rocks|band|hard-rock|2007|SP|B||Hard rock com Kiara.|Hard rock fronted by Kiara.
Sioux 66|band|hard-rock|2011|SP|B||Hard rock paulistano.|São Paulo hard rock.
Electric Mob|band|hard-rock|2016|PR|B|en|Hard rock curitibano em inglês.|Hard rock from Curitiba, in English.
Violeta de Outono|band|psicodelico,shoegaze|1985|SP|B||Psicodelia e pós-punk paulistano desde os anos 1980.|São Paulo psychedelia and post-punk since the 1980s.
Adorável Clichê|band|shoegaze,psicodelico|2013|SP|B||Shoegaze e psicodelia.|Shoegaze and psychedelia.
Não Ao Futebol Moderno|band|shoegaze|2013|SP|B||Shoegaze/indie.|Shoegaze/indie.
Luziluzia|band|psicodelico|2014|SP|B||Psicodelia contemporânea.|Contemporary psychedelia.
Stolen Byrds|band|stoner,psicodelico,indie|2015|SP|B|en|Stoner e psicodelia em inglês.|Stoner and psychedelia in English.
Brvnks|band|indie,shoegaze|2016|SP|B|en|Indie/folk em inglês e português.|Indie/folk in English and Portuguese.
Crime Caqui|band|shoegaze,psicodelico|2017|SP|B||Shoegaze/psicodelia.|Shoegaze/psychedelia.
Pluma|band|indie,psicodelico|2020|SP|B||Indie contemporâneo.|Contemporary indie.
Quarto Vazio|band|indie,shoegaze|2020|SP|B||Indie/shoegaze.|Indie/shoegaze.
Clara Bicho|solo|psicodelico|2023|SP|B||Nova psicodelia.|New psychedelia.
Canto dos Malditos Na Terra do Nunca|band|grunge,rock-alternativo|2003|BA|B||Pós-punk e grunge baiano, letras melancólicas.|Post-punk and grunge from Bahia, melancholy lyrics.
Soro|band|grunge|2007|SP|B||Grunge.|Grunge.
Cruz|band|grunge,hard-rock|2008|SP|B|en|Grunge/hard rock em inglês.|Grunge/hard rock in English.
Dry|band|stoner,grunge|2010|GO|B|en|Stoner goiano em inglês; vocal de Marco Bauer.|Stoner from Goiás in English; fronted by Marco Bauer.
Malta|band|grunge,rock-alternativo|2013|SP|B||Vencedora da 1ª temporada do Superstar; "Diz pra Mim", "Memórias".|Winner of the first season of Superstar; "Diz pra Mim", "Memórias".
Impavid Colossus|band|grunge,hard-rock|2019|SP|B|en|Grunge/hard rock em inglês.|Grunge/hard rock in English.
Loomer|band|shoegaze|2008|SP|B||Shoegaze paulistano.|São Paulo shoegaze.
Lupe de Lupe|band|shoegaze|2009|MG|B||Shoegaze/noise mineiro.|Shoegaze/noise from Minas.
Marianaa|band|shoegaze|2014|SP|B||Shoegaze.|Shoegaze.
Gorduratrans|band|shoegaze|2015|SP|B||Shoegaze/noise.|Shoegaze/noise.
Magnólia|band|shoegaze|2019|SP|B||Shoegaze.|Shoegaze.
Maquinas|band|shoegaze|2015|SP|B||Shoegaze.|Shoegaze.
Eliminadorzinho|band|shoegaze|2016|SP|B||Shoegaze.|Shoegaze.
Fernando Motta|solo|shoegaze|2016|SP|B||Shoegaze/dream pop.|Shoegaze/dream pop.
Lvcasu|solo|shoegaze|2016|SP|B||Shoegaze.|Shoegaze.
Homeninvisivel|band|shoegaze|2017|SP|B||Shoegaze.|Shoegaze.
Terraplana|band|shoegaze|2017|SP|B||Shoegaze.|Shoegaze.
Quasar|band|shoegaze|2017|SP|B||Shoegaze.|Shoegaze.
Mafius|band|shoegaze|2018|SP|B||Shoegaze.|Shoegaze.
Chão de Taco|band|shoegaze,indie|2019|SP|B||Indie/shoegaze.|Indie/shoegaze.
Fntsma|band|shoegaze|2019|SP|B||Shoegaze.|Shoegaze.
Algésico|band|shoegaze|2022|SP|B||Shoegaze.|Shoegaze.
Virtudes Fantasmas|band|shoegaze|2022|SP|B||Shoegaze.|Shoegaze.
Stela|band|shoegaze|2023|SP|B||Shoegaze.|Shoegaze.
Macaco Bong|band|stoner|2004|MT|B||Rock instrumental de Cuiabá; "Artista Igual Pedreiro".|Instrumental rock from Cuiabá; "Artista Igual Pedreiro".
Muñoz|duo|stoner,hard-rock|2012|MG|B|en|Stoner/blues rock em duo.|Stoner/blues rock duo.
Red Boots|band|stoner,grunge|2013|RN|B|en|Grunge/stoner potiguar em inglês.|Grunge/stoner from Rio Grande do Norte, in English.
The Muddy Brothers|band|stoner,hard-rock|2012|ES|B|en|Blues rock/stoner capixaba.|Blues rock/stoner from Espírito Santo.
Disaster Boots|band|stoner|2012|PR|B||Stoner/blues rock.|Stoner/blues rock.
Dogman|band|stoner,grunge|2013|GO|B|en|Stoner/grunge/doom.|Stoner/grunge/doom.
Marrero|band|stoner|2012|SP|B||Stoner/hard rock.|Stoner/hard rock.
Amp|band|stoner|2012|PE|B||Stoner/hard rock pernambucano.|Stoner/hard rock from Pernambuco.
Cherry Devil|band|stoner,hard-rock|2012|GO|B||Hard rock/stoner.|Hard rock/stoner.
Overfuzz|band|stoner,hard-rock|2010|GO|B|en|Hard rock/stoner goiano.|Hard rock/stoner from Goiás.
Pantanum|band|stoner|2012|PR|B||Stoner/doom.|Stoner/doom.
Red Mess|band|stoner|2012|PR|B||Stoner/doom.|Stoner/doom.
Son of a Witch|band|stoner|2012|RN|B||Stoner/doom.|Stoner/doom.
Monte Resina|band|stoner|2012|SC|B||Stoner instrumental.|Instrumental stoner.
Saturndust|band|stoner|2012|SP|B||Stoner/doom.|Stoner/doom.
Pesta|band|stoner|2012|MG|B||Stoner/doom.|Stoner/doom.
Mondo Bizarro|band|stoner|2012|PE|B||Stoner/hard rock.|Stoner/hard rock.
Grindhouse Hotel|band|stoner|2012|SP|B||Stoner.|Stoner.
Letters From|band|stoner|2012|RJ|B||Stoner/doom.|Stoner/doom.
Fuzzly|band|stoner|2012|MT|B||Stoner.|Stoner.
Blind Horse|band|stoner|2012|RJ|B||Stoner/blues rock.|Stoner/blues rock.
Space Guerrilla|band|stoner|2012|RS|B||Stoner.|Stoner.
Red Light House|band|stoner,punk|2012|GO|B||Hard rock/punk/stoner.|Hard rock/punk/stoner.
Japanese Bondage|band|stoner|2012|SP|B||Stoner.|Stoner.
Huey|band|stoner|2012|SP|B||Stoner/blues/acid noise.|Stoner/blues/acid noise.
Australopithecus|band|stoner|2012|SP|B||Stoner/doom.|Stoner/doom.
Arcazas|band|stoner|2012|SP|B||Rock instrumental/stoner.|Instrumental rock/stoner.
Monster Coyote|band|stoner,heavy-power|2012|RN|B||Metal/stoner.|Metal/stoner.
Old Stove|band|stoner|2012|BA|B||Stoner.|Stoner.
Isso|band|stoner,grunge|2012|MG|B||Grunge/stoner.|Grunge/stoner.
The Arataca Stoned Farmer|band|stoner|2012|SC|B||Stoner/doom.|Stoner/doom.
Hammerhead Blues|band|stoner|2014|SP|B|en|Stoner/blues rock.|Stoner/blues rock.
Thymus Boogie|band|stoner|2012|SP|B||Stoner/doom.|Stoner/doom.
Billy Goat|band|stoner|2012|RJ|B||Stoner.|Stoner.
Rural Killers|band|stoner|2015|SP|B|en|Stoner/hard rock.|Stoner/hard rock.
Wolf Among Us|band|stoner|2018|SP|B|en|Stoner rock.|Stoner rock.
King Void|duo|stoner|2013|DF|B|en|Duo de stoner.|Stoner duo.
Alohatomic|band|stoner,hardcore|2012|SP|B|en|Hardcore/surf/stoner.|Hardcore/surf/stoner.
Autoramas|band|garage|1997|RJ|B||Garage/surf/new wave: "Você Sabe", "Abstrai".|Garage/surf/new wave: "Você Sabe", "Abstrai".
Forgotten Boys|band|garage|1997|SP|B|en|Garage punk/hard rock em inglês.|Garage punk/hard rock in English.
Ecos Falsos|band|garage,indie|2002|SP|B||Garage/indie.|Garage/indie.
Vivendo do Ócio|band|garage,indie|2006|BA|B||Garage/indie baiano premiado: "Nostalgia", "Radioatividade".|Award-winning garage/indie from Bahia: "Nostalgia", "Radioatividade".
Vespas Mandarinas|band|garage,indie|2009|SP|B||"Animal Nacional" indicado ao Grammy Latino 2013.|"Animal Nacional" nominated for the 2013 Latin Grammy.
Canil|band|garage|2012|SP|B||Garage rock.|Garage rock.
Twin Pumpkin|band|indie,garage|2015|SP|B|en|Indie em inglês.|Indie in English.
Karen Dió|solo|punk,garage|2017|SP|B|en|Punk/garage em inglês; "Sick Ride".|Punk/garage in English; "Sick Ride".
Violet Soda|band|garage,punk|2018|SP|B|en|Garage punk em inglês.|Garage punk in English.
Water Rats|band|garage,punk|2012|SP|B|en|Garage punk em inglês.|Garage punk in English.
Marcelo Nova|solo|punk,rock-comico|1980|BA|B||Voz do Camisa de Vênus; parceiro de Raul Seixas em 1989.|Camisa de Vênus's voice; Raul Seixas's partner in 1989.
Supla|solo|punk,rock-alternativo|1984|SP|B||Punk e rock com persona midiática: "Garota de Berlim", "Green Hair".|Punk and rock with a media persona: "Garota de Berlim", "Green Hair".
Blind Pigs|band|punk|1993|SP|B|en|Punk em inglês e português; "O Idiota".|Punk in English and Portuguese; "O Idiota".
Mukeka di Rato|band|punk,hardcore|1995|ES|B||Punk/hardcore capixaba, humor e crítica.|Punk/hardcore from Espírito Santo, humour and critique.
Holly Tree|band|punk|1996|SP|B|en|Punk em inglês.|Punk in English.
Tokyo Savannah|band|garage,punk|2000|SP|B|en|Garage punk em inglês.|Garage punk in English.
Anti-Corpos|band|punk,hardcore|2003|SP|B|en|Punk/hardcore em inglês.|Punk/hardcore in English.
Sky Down|band|punk|2011|SP|B|en|Punk em inglês.|Punk in English.
Ant Strike|band|pop-punk|2011|SP|B|en|Punk/pop punk em inglês.|Punk/pop punk in English.
Cogumelo Plutão|band|pos-punk,rock-alternativo|1997|SP|B||"Esperando na Janela", "Cada Instante Sem Você".|"Esperando na Janela", "Cada Instante Sem Você".
Lúbrica|band|pos-punk|2019|SP|B||Pós-punk contemporâneo.|Contemporary post-punk.
Gram|band|indie,rock-alternativo|2002|MG|B||"Você Pode Ir na Janela".|"Você Pode Ir na Janela".
Vanguart|band|indie|2002|MT|B||Folk rock de Cuiabá: "Meu Sol", "Demorou pra Ser".|Folk rock from Cuiabá: "Meu Sol", "Demorou pra Ser".
Ludov|band|indie|2003|SP|B||"Princesa".|"Princesa".
Moptop|band|indie|2004|RJ|B||"O Rock Acabou", "Contramão".|"O Rock Acabou", "Contramão".
Stevens|band|indie|2007|SP|B||"Parecia Estar".|"Parecia Estar".
Tópaz|band|indie|2007|SP|B||"O Maior Idiota do Mundo".|"O Maior Idiota do Mundo".
A Banda Mais Bonita da Cidade|band|indie|2009|PR|B||"Oração" viralizou em 2011.|"Oração" went viral in 2011.
Maglore|band|indie,rock-alternativo|2009|BA|B||Rock alternativo, MPB e folk: "Café com Pão".|Alternative rock, MPB and folk: "Café com Pão".
Suricato|band|indie|2009|RJ|B||Rodrigo Suricato; "Um Certo Alguém" com Lulu Santos.|Rodrigo Suricato; "Um Certo Alguém" with Lulu Santos.
Plutão Já Foi Planeta|band|indie|2013|PB|B||Indie da Paraíba.|Indie from Paraíba.
Young Lights|band|indie,rock-alternativo|2013|SP|B|en|Alternativo/folk em inglês.|Alternative/folk in English.
Banda do Mar|band|indie|2014|SP|B||Mallu Magalhães, Marcelo Camelo e Fred Ferreira.|Mallu Magalhães, Marcelo Camelo and Fred Ferreira.
O Grilo|band|indie,ska|2016|SP|B||"Serenata Existencialista", "Sambinha".|"Serenata Existencialista", "Sambinha".
Dani Bessa|solo|indie|2019|SP|B||Indie pop.|Indie pop.
Jovem Dionisio|band|indie,pop-rock|2019|PR|A||"Acorda Pedrinho" (2022) foi um dos maiores virais do país.|"Acorda Pedrinho" (2022) was one of the country's biggest viral hits.
Apanhador Só|band|indie,rock-gaucho|2007|RS|B||Experimental; destaque do "novo rock nacional".|Experimental; a highlight of the "new Brazilian rock".
Júpiter Maçã|solo|psicodelico,rock-gaucho|1990|RS|B||"A Sétima Efervescência" (1997), psicodelia cult.|"A Sétima Efervescência" (1997), cult psychedelia.
Bidê ou Balde|band|indie,rock-gaucho|1999|RS|B||"Melissa", "Mesmo Que Mude".|"Melissa", "Mesmo Que Mude".
Cidadão Quem|band|pop-rock,rock-gaucho|1991|RS|B||"Dia Especial", "O Amanhã Colorido".|"Dia Especial", "O Amanhã Colorido".
Dazaranha|band|ska,rock-alternativo|1992|SC|B||Rock catarinense com rabeca e violino: "Vagabundo Confesso".|Rock from Santa Catarina with rabeca and violin: "Vagabundo Confesso".
Garage Fuzz|band|hardcore|1991|SP|B|en|Hardcore em inglês com sucesso no exterior desde 1994.|Hardcore in English with success abroad since 1994.
Sugar Kane|band|hardcore|1997|PR|B||Do inglês ao português em "Por Nossa Paz" (2001); "Medo", "Janeiro".|From English to Portuguese on "Por Nossa Paz" (2001); "Medo", "Janeiro".
Zander|band|hardcore,emo|2008|RJ|B||"Brasa" (2010) abriu show do Green Day; "Auto Falantes".|"Brasa" (2010) opened for Green Day; "Auto Falantes".
Pense|band|hardcore|2007|MG|B||"Além Daquilo Que Te Cega" (2014), cerca de 50 shows em 10 meses.|"Além Daquilo Que Te Cega" (2014), about 50 shows in 10 months.
Menores Atos|band|metalcore,hardcore|2014|RJ|B||Post-hardcore: "Animalia", "Lapso".|Post-hardcore: "Animalia", "Lapso".
Bullet Bane|band|metalcore,hardcore|2009|SP|B|en|Post-hardcore em inglês e português: "Continental".|Post-hardcore in English and Portuguese: "Continental".
Colligere|band|hardcore|2000|SP|B||Hardcore melódico.|Melodic hardcore.
Cueio Limão|band|hardcore,rock-comico|2000|SP|B||Hardcore cômico: "Prego", "Quem Matou o Bozo?".|Comic hardcore: "Prego", "Quem Matou o Bozo?".
Rodox|band|hardcore,rap-rock|2002|SP|B||Hardcore/nu metal.|Hardcore/nu metal.
Plastic Fire|band|hardcore|2005|SP|B||Hardcore melódico.|Melodic hardcore.
Chuva Negra|band|hardcore|2009|SP|B||Hardcore.|Hardcore.
Bayside Kings|band|hardcore|2010|SP|B||Hardcore.|Hardcore.
Malvina|band|hardcore,thrash-death|2013|SP|B|en|Hardcore/metal alternativo em inglês.|Hardcore/alternative metal in English.
Dance of Days|band|emo,hardcore|1996|SP|B||Pioneira do emo paulistano: "Adeus Sofia".|A pioneer of São Paulo emo: "Adeus Sofia".
Gritando HC|band|hardcore|1990|SP|B||"Velho Punk".|"Velho Punk".
Houdini|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Street Bulldogs|band|hardcore|1996|SP|B||Hardcore.|Hardcore.
Aurora Rules|band|metalcore|2008|SP|B||Post-hardcore.|Post-hardcore.
Carbona|band|punk|1998|RJ|B||Punk rock.|Punk rock.
Noção de Nada|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Aditive|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Nitrominds|band|hardcore|1998|SP|B||Hardcore melódico.|Melodic hardcore.
Black Days|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Fistt|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Deluxe Trio|band|hardcore|2003|RJ|B||Antecessora do Zander.|Zander's predecessor.
End of Pipe|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Fire Driven|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Reffer|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Radical Karma|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Maguerbes|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Alternative System|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Benin|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Def|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Os Cabeloduro|band|hardcore|2000|SP|B||Hardcore.|Hardcore.
Hardneja Sertacore|band|hardcore,rock-comico|2005|SP|B||Hardcore com sertanejo e humor.|Hardcore with sertanejo and humour.
Devotos|band|hardcore,manguebeat|1988|PE|B||Hardcore do Alto José do Pinho, Recife.|Hardcore from Alto José do Pinho, Recife.
Mundo Livre S/A|band|manguebeat|1984|PE|A||Fred Zero Quatro; "Samba Esquema Noise" (1994).|Fred Zero Quatro; "Samba Esquema Noise" (1994).
Strike|band|pop-punk|2003|MG|B||Pop punk, skate punk e rap rock de Juiz de Fora: "Aquela História".|Pop punk, skate punk and rap rock from Juiz de Fora: "Aquela História".
Dibob|band|pop-punk,ska|2001|SP|B||Pop punk/ska.|Pop punk/ska.
Fake Number|band|pop-punk,emo|2006|SP|B||"Aquela Música", "Primeira Lembrança".|"Aquela Música", "Primeira Lembrança".
Replace|band|pop-punk|2006|SP|B||"Ponto de Paz".|"Ponto de Paz".
Minerva|band|pop-punk|2015|SP|B||Pop punk.|Pop punk.
O Quarentener Só|band|pop-punk|2020|SP|B||Pop punk.|Pop punk.
Julio Ito|solo|pop-punk|2021|SP|B||Pop punk.|Pop punk.
Granada|band|emo|2005|SP|B||Emo.|Emo.
Hevo84|band|emo|2005|SP|B||"Passos Escuros", "Minha Vida É Você".|"Passos Escuros", "Minha Vida É Você".
Vowe|band|emo|2009|SP|B||Emo.|Emo.
Cefa|band|emo,metalcore|2012|SP|B||Emo/post-hardcore.|Emo/post-hardcore.
Terceiro Andar|band|emo|2022|SP|B||Emo.|Emo.
Paralelo Ao Fim|band|emo,rock-alternativo|2025|SP|B||Emo/alternativo.|Emo/alternative.
Cine|band|pop-rock|2008|SP|B||"Garota Radical", "As Cores".|"Garota Radical", "As Cores".
Scracho|band|ska,pop-rock|2004|RJ|B||Reggae rock: "Morena", "Divina Comédia".|Reggae rock: "Morena", "Divina Comédia".
Luxúria|band|rock-alternativo|2005|SP|B||"Lama", "Ódio".|"Lama", "Ódio".
Medulla|band|rock-alternativo|2012|SP|B||"Eterno Retorno".|"Eterno Retorno".
Felipe Dylon|solo|pop-rock|2003|RJ|B||Ídolo teen: "Musa do Verão".|Teen idol: "Musa do Verão".
Brava|band|pop-rock|2004|SP|B||"Todo Mundo Quer Cuidar de Mim".|"Todo Mundo Quer Cuidar de Mim".
K-Sis|group|pop-rock|2006|SP|B||"Beijos, Blues e Poesia".|"Beijos, Blues e Poesia".
P.O.Box|band|rap-rock|1997|SP|B||"Papo de Jacaré".|"Papo de Jacaré".
Rock Rocket|band|punk|2001|SP|B||Punk rock.|Punk rock.
Envydust|band|metalcore|2003|SP|B||Metalcore.|Metalcore.
Drive.in|band|metalcore|2005|SP|B||Post-hardcore.|Post-hardcore.
Ponto Nulo no Céu|band|metalcore|2007|SP|B||"Horizontal".|"Horizontal".
John Wayne|band|metalcore|2008|SP|B||Metalcore.|Metalcore.
Project46|band|metalcore,thrash-death|2008|SP|B||Metalcore: "Erro +55", "Rédeas".|Metalcore: "Erro +55", "Rédeas".
A Última Theoria|band|metalcore|2010|SP|B||Metalcore.|Metalcore.
Theoria de Allice|band|metalcore|2012|SP|B||Metalcore.|Metalcore.
Crônica Ativa|band|metalcore|2017|SP|B||Metal alternativo.|Alternative metal.
Emphuria|band|metalcore|2019|SP|B||Metalcore.|Metalcore.
Hollowmind|band|heavy-power|1993|SP|B||Heavy metal.|Heavy metal.
Hibria|band|heavy-power|1996|RS|B||Power metal gaúcho.|Power metal from Rio Grande do Sul.
Almah|band|heavy-power|2006|SP|B||Projeto de Edu Falaschi.|Edu Falaschi's project.
Kryour|band|thrash-death|2014|SP|B|en|Death metal melódico em inglês.|Melodic death metal in English.
Vulcano|band|thrash-death|1981|SP|B||Pioneira do metal extremo brasileiro.|A pioneer of Brazilian extreme metal.
Leviaethan|band|thrash-death|1983|SP|B||Thrash dos anos 1980.|1980s thrash.
Attomica|band|thrash-death|1985|SP|B||Thrash dos anos 1980.|1980s thrash.
Headhunter D.C.|band|thrash-death|1987|BA|B||Death metal baiano.|Death metal from Bahia.
Torture Squad|band|thrash-death|1990|SP|B|en|Thrash/death em inglês.|Thrash/death in English.
Soulfly|band|thrash-death|1997|SP|A|en|Projeto de Max Cavalera após o Sepultura; sediado nos EUA.|Max Cavalera's project after Sepultura; based in the US.
Confronto|band|thrash-death,hardcore|1999|RJ|B||Metal/hardcore carioca.|Rio metal/hardcore.
Kamala|band|thrash-death|2003|SP|B||Groove metal.|Groove metal.
Semblant|band|heavy-power|2006|PR|B|en|Metal melódico em inglês.|Melodic metal in English.
Astafix|band|thrash-death|2008|SP|B||Thrash.|Thrash.
Surra|band|thrash-death,hardcore|2012|SP|B||Crossover.|Crossover.
Póstuma|band|thrash-death|2017|SP|B||Metal extremo.|Extreme metal.
Sujera|band|thrash-death|2020|SP|B||Metal extremo.|Extreme metal.
Crypta|band|thrash-death|2019|SP|B|en|Death metal com Fernanda Lira e Tainá Bergamaschi.|Death metal with Fernanda Lira and Tainá Bergamaschi.
Ajna|band|heavy-power|1990|SP|B|en|Heavy/thrash em inglês.|Heavy/thrash in English.
Miasthenia|band|thrash-death|1994|DF|B|en|Black/death metal.|Black/death metal.
Paura|band|hardcore,thrash-death|1995|SP|B|en|Hardcore/groove em inglês.|Hardcore/groove in English.
Endigna|band|thrash-death|2007|SP|B|en|Deathcore.|Deathcore.
Fenrir's Scar|band|heavy-power|2015|SP|B|en|Metal gótico/alternativo.|Gothic/alternative metal.
Heaven|band|heavy-power|2017|SP|B|en|Heavy metal.|Heavy metal.
Impact7|band|heavy-power|2017|SP|B|en|Metal melódico/alternativo.|Melodic/alternative metal.
Inraza|band|thrash-death|2017|SP|B|en|Metal extremo.|Extreme metal.
Kuroi|band|heavy-power|2017|SP|B|en|Heavy metal/J-rock.|Heavy metal/J-rock.
Machete Bomb|band|rap-rock|2013|SP|B||Rap rock.|Rap rock.
InDharma|band|rap-rock|2022|SP|B||Rap rock/nu metal.|Rap rock/nu metal.
Lvcas|solo|heavy-power,rock-alternativo,fock|2023|SP|B||Metal alternativo: "Odisseia".|Alternative metal: "Odisseia".
Zepelim e o Sopro do Cão|band|rock-alternativo|2006|SP|B||Rock alternativo.|Alternative rock.
Molho Negro|band|rock-alternativo|2012|SP|B||Rock alternativo.|Alternative rock.
Raça|band|rock-alternativo|2012|SP|B||Rock alternativo.|Alternative rock.
The Mönic|band|rock-alternativo,garage|2018|SP|B|en|Garage punk/hard rock em inglês.|Garage punk/hard rock in English.
Darvin|band|ska|1997|SP|B||Reggae rock.|Reggae rock.
Orquestra Brasileira de Música Jamaicana|band|ska|2008|SP|B||Big band que toca clássicos brasileiros em ritmo jamaicano.|A big band playing Brazilian classics in Jamaican rhythms.
Canvas|band|ska|2024|SP|B||Reggae rock.|Reggae rock.
Música Agosto|band|ska|2005|SP|B||Rock'n'roll e ska contestador.|Protest rock'n'roll and ska.
Abaskadabra|band|ska|2005|PR|B|en|Ska em inglês de Curitiba.|Ska in English from Curitiba.
Sapo Banjo|band|ska|1995|SP|B||Ska sarcástico e politizado, uma das mais antigas do país.|Sarcastic, political ska, one of the country's oldest.
Legalê|band|ska|2005|SP|B||Rock, ska, grooves e psicodelia, de Bauru.|Rock, ska, grooves and psychedelia, from Bauru.
Desorquestra|band|ska|2005|MG|B||Ska de Belo Horizonte.|Ska from Belo Horizonte.
Ba-Boom|band|ska|2005|SP|B||Afoxé, samba e baião com música jamaicana.|Afoxé, samba and baião with Jamaican music.
La Digna Rabia|band|ska|2005|RS|B||Ska cantado em espanhol, de Porto Alegre.|Ska sung in Spanish, from Porto Alegre.
Skabong|band|ska|2005|SE|B|en|Ska em inglês de Aracaju.|Ska in English from Aracaju.
Clarence|band|ska|2005|SP|B||Ska de Bauru.|Ska from Bauru.
Coquetel Acapulco|band|ska|2005|RJ|B||Ska tranquilo com vocais femininos.|Mellow ska with female vocals.
Skafandros Orkestra|band|ska|2005|SP|B||Ska instrumental com 11 músicos, de Campinas.|Instrumental ska with 11 musicians, from Campinas.
Skamoondongos|band|ska,punk|2005|SP|B||Ska punk.|Ska punk.
Pequena Morte|band|ska|2005|MG|B||Ska de Belo Horizonte.|Ska from Belo Horizonte.
Skavarone|band|ska|2005|GO|B||Ska, rocksteady e reggae de Goiás.|Ska, rocksteady and reggae from Goiás.
Virna Lisi|band|rock-comico|1989|SP|B||Rock cômico paulistano.|São Paulo comic rock.
Rogério Skylab|solo|rock-comico|1991|RJ|B||Humor negro e canções escrachadas.|Dark humour and outrageous songs.
Baba Cósmica|band|rock-comico|1994|MG|B||Rock cômico mineiro.|Comic rock from Minas.
Maria do Relento|band|rock-comico|1994|SP|B||Rock cômico.|Comic rock.
Os Ostras|band|rock-comico|1994|SP|B||Rock cômico.|Comic rock.
U.D.R.|band|rock-comico|2003|SP|B||Rock cômico.|Comic rock.
Pedra Letícia|band|rock-comico|2005|SP|B||"Em Plena Lua de Mel", "Eu Não Toco Raul".|"Em Plena Lua de Mel", "Eu Não Toco Raul".
Exclusive Os Cabides|band|rock-comico|2018|SP|B||Rock cômico retrô.|Retro comic rock.
André Prando|solo|jovem-guarda|2011|ES|B||Rockabilly contemporâneo.|Contemporary rockabilly.
Morcegula|band|jovem-guarda|2023|SP|B||Rock'n'roll retrô.|Retro rock'n'roll.
Baby do Brasil|solo|psicodelico|1970|RJ|A||Dos Novos Baianos a "Menino do Rio".|From Novos Baianos to "Menino do Rio".
Pholhas|band|progressivo|1969|SP|B|en|Rock progressivo/power pop em inglês, com "My Mistake".|Progressive rock/power pop in English, with "My Mistake".
Light Reflections|band|pop-rock|1972|SP|B|en|Soft rock em inglês dos anos 1970.|1970s soft rock in English.
Hover|band|grunge|2008|SP|B|en|Post grunge em inglês.|Post grunge in English.
Sound Bullet|band|indie|2009|SP|B|en|Indie em inglês.|Indie in English.
The Baudelaires|band|indie|2009|SP|B|en|Indie/power pop em inglês.|Indie/power pop in English.
Cambriana|band|indie,psicodelico|2010|SP|B|en|Pop psicodélico em inglês; "The Sad Facts".|Psychedelic pop in English; "The Sad Facts".
The Outs|band|indie,psicodelico|2010|SP|B|en|Indie psicodélico em inglês e português.|Psychedelic indie in English and Portuguese.
Inky|band|rock-alternativo|2011|SP|B|en|Rock alternativo em inglês.|Alternative rock in English.
Mustache e os Apaches|band|indie|2011|SP|B|en|Bluegrass/folk em inglês.|Bluegrass/folk in English.
Rakta|band|psicodelico,punk|2011|SP|B|en|Rock experimental e punk, cultuada no exterior.|Experimental rock and punk, a cult name abroad.
LeftZero|band|pop-rock|2012|PR|B|en|Pop rock em inglês de Maringá.|Pop rock in English from Maringá.
Melodizzy|band|hard-rock|2012|SP|B|en|Hard rock/folk em inglês.|Hard rock/folk in English.
Melrya|band|heavy-power|2012|SP|B|en|Heavy metal/hard rock em inglês.|Heavy metal/hard rock in English.
Naked Girls and Aeroplanes|band|pop-rock|2012|SP|B|en|Pop rock/folk em inglês.|Pop rock/folk in English.
Name The Band|band|indie|2012|SP|B|en|Indie em inglês.|Indie in English.
Shotgun Wives|band|indie|2012|SP|B|en|Folk rock em inglês.|Folk rock in English.
Blear|band|grunge,indie|2013|SP|B|en|Grunge/indie em inglês.|Grunge/indie in English.
Chalk Outlines|band|indie|2013|SP|B|en|Indie em inglês.|Indie in English.
Garden of the Eatingtapes|band|indie|2013|PR|B|en|Indie em inglês de Curitiba.|Indie in English from Curitiba.
My Magical Glowing Lens|band|psicodelico|2013|SP|B|en|Rock experimental em inglês.|Experimental rock in English.
Npkn|band|rock-alternativo|2013|SP|B|en|Alternativo/pop em inglês.|Alternative/pop in English.
Oudn|band|thrash-death|2013|SP|B|en|Death metal/metalcore em inglês.|Death metal/metalcore in English.
Rascal Experience|band|indie|2013|SP|B|en|Indie em inglês.|Indie in English.
Republica|band|hard-rock|2013|SP|B|en|Hard rock em inglês.|Hard rock in English.
BBGG|band|garage,hard-rock|2014|SP|B|en|Garage punk/hard rock em inglês.|Garage punk/hard rock in English.
Dodelle|band|pop-rock|2014|SP|B|en|Pop rock em inglês.|Pop rock in English.
Kill All The Super Stars|band|hard-rock|2014|SP|B|en|Hard rock em inglês.|Hard rock in English.
New Age Travellers|band|rock-alternativo|2014|RS|B|en|Funk rock em inglês e português, de Porto Alegre.|Funk rock in English and Portuguese, from Porto Alegre.
The Shorts|band|indie|2014|SP|B|en|Indie em inglês.|Indie in English.
Deb and The Mentals|band|garage,indie|2015|SP|B|en|Garage punk/indie em inglês.|Garage punk/indie in English.
Fluxe|band|indie|2015|SP|B|en|Art rock em inglês.|Art rock in English.
Loyal Gun|band|indie|2015|SP|B|en|Art rock em inglês.|Art rock in English.
Vamoz!|band|hard-rock|2015|SP|B|en|Hard rock em inglês.|Hard rock in English.
Blowdrivers|band|hard-rock|2016|SP|B|en|Hard/blues rock em inglês.|Hard/blues rock in English.
Mama Feet|band|indie|2016|SP|B|en|Indie rock em inglês.|Indie rock in English.
Midwest Harvest|band|indie|2016|SP|B|en|Folk rock em inglês.|Folk rock in English.
Mushroom Storm|band|hard-rock|2016|ES|B|en|Blues rock capixaba em inglês.|Blues rock from Espírito Santo in English.
Taunting Glaciers|band|grunge|2016|SP|B|en|Grunge/noise rock em inglês.|Grunge/noise rock in English.
Crazy Bastards|band|pop-punk|2017|SP|B|en|Pop punk em inglês.|Pop punk in English.
Aberdeen|band|grunge|2018|SP|B|en|Post grunge em inglês.|Post grunge in English.
Disaster Cities|band|rock-alternativo|2016|SP|B|en|"Mice and Trash Cans".|"Mice and Trash Cans".
Deafkids|band|psicodelico,punk|2010|RJ|B||Psicodelia percussiva e punk com projeção internacional; "Selva Pulsátil".|Percussive psychedelia and punk with international reach; "Selva Pulsátil".
Bellamore|band|rock-alternativo|2010|SP|B||Rock alternativo.|Alternative rock.
Versalle|band|rock-alternativo|2012|SP|B||Vencedora do Superstar 2016; "Verde Mansidão".|Winner of Superstar 2016; "Verde Mansidão".
Dona Cislene|band|indie|2010|SP|B||Indie.|Indie.
Melim|group|pop-rock,pop-alternativo|2016|RJ|A||Trio de irmãos; "Meu Abrigo", "Ouvi Dizer".|A sibling trio; "Meu Abrigo", "Ouvi Dizer".
OutroEu|band|pop-rock|2016|RJ|B||"Ai de Mim" com Sandy; "Outrória".|"Ai de Mim" with Sandy; "Outrória".
Silva|solo|nova-mpb,pop-rock|2012|ES|A||Pop eletrônico e MPB: "Não Vá Embora", "Sorte" com Liniker.|Electronic pop and MPB: "Não Vá Embora", "Sorte" with Liniker.
Rosa de Saron|band|rock-cristao|1988|SP|A||Rock católico: "Sem Você", "Mire as Estrelas".|Catholic rock: "Sem Você", "Mire as Estrelas".
Resgate|band|rock-cristao|1989|SP|B||Rock cristão desde os anos 1980.|Christian rock since the 1980s.
Catedral|band|rock-cristao|1988|RJ|B||Pop rock cristão.|Christian pop rock.
Mulamba|band|rock-alternativo|2015|PR|B||Banda feminina curitibana: "Interstelar".|An all-female band from Curitiba: "Interstelar".
Caiçara Clã|band|rock-alternativo|2020|SP|B||"Frases Para Seu Status".|"Frases Para Seu Status".
Maré Tardia|band|indie|2020|ES|B||"Prefiro Vila Velha".|"Prefiro Vila Velha".
Hotelo|band|indie|2018|SP|B||"Sorte".|"Sorte".
Daparte|band|indie|2016|MG|B||"Nunca Fui Desse Lugar" com Lagum.|"Nunca Fui Desse Lugar" with Lagum.
Quem é Você, Alice?|band|indie|2020|MG|B||"Diamantina".|"Diamantina".
Di Ferrero|solo|pop-rock|2001|SP|B||Vocalista do NX Zero; carreira solo.|NX Zero's singer; solo career.
CSS|band|indie,electro-funk|2003|SP|A|en|Cansei de Ser Sexy: indie-electro em inglês com sucesso internacional.|Cansei de Ser Sexy: indie-electro in English with international success.
Bonde do Rolê|band|electro-funk|2005|PR|B|en|Funk carioca e eletrônica lançados pela Domino, com Diplo.|Funk carioca and electronics released by Domino, with Diplo.
"""
