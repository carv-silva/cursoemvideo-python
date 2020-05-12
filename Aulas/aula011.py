###Cores no Python 

'''
\033[0;33;44m



0 None
1 Bold
4 Underline
7 Negative

text                      black 
30 --> branco             40 
31 --> vermelho           41
32 --> verde              42  
33 --> amarelo            43  
34 --> azul               44  
35 --> roxo               45  
36 --> verde claro        46  
37 --> cinza              47    


#vermelho  com teste em branco
teste \033[0;30;41m 

#azul com teste em amarelo
teste \033[4;33;44m

#amarelo com teste em roxo
teste \[033[1;35;43m

#verde com teste em branco 
\033[30;42m

#preto com teste em cinza
\033[m

#BRanco com teste em preto

\033[7;30m  

print('\033[1;4;31;43m Hello bitch\033[m')  #--> hello em vermelho negrito e subliado e fundo amarelo

print('\033[1;4;33;44m Hello baby! \033[m') # --> Hello em amarelo negrito e subliando e fundo verde

print('\033[30m Hello thanks! \033[m')  '''

cores = {'limpa':'\033[m',
 'azul':'\033[34m', 
 'amarelo':'\033[6;33m',
 'pretoebranco':'\033[7;30m'}



###cores = {'limpa':'\033[1;4;33;30m'}
print(f"Carlooss {cores['azul']} Carlao")
