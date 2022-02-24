'''Faça um programa que mostre na tela um contagem regressiva
para o estouro de fogos de artificio, indo de 10 ate 0 com uma
pausa de 1 segundo entre eles'''


from  time import sleep
import time
import sys

'''for i in range(10, 0, -1):
    sys.stdout.write(f"\r{i}")
    sys.stdout.flush()
    time.sleep(1)

print("\nFim")
'''
for i in range(10, -1, -1):
    sleep(1)
    print(i)
print('Fogos estourando ehhhhh!!!')
