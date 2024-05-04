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

a = 'AAAAA'
b='B'
c=1.1
#pegando os valores na ordem da declaracao
string = 'a={}, b={}, c={}'
formato = string.format(a,b,c)

print (formato)

#pegando os valores por indice
string2 = 'a={0} a{0} b={1} c={2:.2f}'
formato2 = string2.format(a,b,c)
print(formato2)




