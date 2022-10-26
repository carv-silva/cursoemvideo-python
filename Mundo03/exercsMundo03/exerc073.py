'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação.Depos
mostre:
A) Apenas os 5 primeiros colocados.
B) Os ultimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabetica
D) Em que posição na tabela esta o time da Chapecoensa.

'''

times = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí',
         'Botafogo', 'Bragantino', 'Ceará', 'Corinthians', 'Coritiba',
         'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás',
         'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'São Paulo')

print('-=' * 35)
print(f'Os times do Brasileirão sao: {times}')
print('-=' * 35)
print(f'5 primeiros colocados: {times[0:5]}')
print('-=' * 35)
print(f'Os ultimos 4 colocados da tabela: {times[16:]}')
print('-=' * 35)
print(f'Os times em ordem alfabetica: {sorted(times)}')
print('-=' * 35)
print(f"o time da Santos esta na posição: {times.index('Santos')}º posição")




