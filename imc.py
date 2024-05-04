nome = 'Douglas'
altura = 1.75
peso = 80
imc = peso / altura ** 2

print('O ' + nome + ' tem altura de ' + str(altura),)
print('pesa', peso, 'quilos e seu IMC é', )
print(imc)

#Utilizando fstring para imprimir os resultados
f_string =  f'{nome} tem {altura:.2f} de altura'
f_string2 = f'pesa, {peso} quilos'
f_string3 = f'Seu IMC é, {imc:.2f}'

print(f_string)
print(f_string2)
print(f_string3)

#Funcão format 

