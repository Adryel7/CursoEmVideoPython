#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

tbA=('Atletico MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino',
    'Fluminense','América MG','Athlético GO','Santos','Ceará','Internacional','São Paulo',
    'Athletico PR','Cuiabá','Juventude','Gremio','Bahia','Sport','Chapecoense')

print(f'Os cinco primeiros colocados são: {tbA[:5]}')
print(f'Os quatro ultimos colocados são: {tbA[-4:]}')
print(f'Os Times em ordem alfabetica:{sorted(tbA)}')
print(f'O time do Chapecoense se encontra na {tbA.index("Chapecoense")+1}ª posição.')
