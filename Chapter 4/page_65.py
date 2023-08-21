'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
Print the message The first three items in the list are:
Then use a slice to print the first three items from that program’s list. 
Print the message Three items from the middle of the list are:
Use a slice to print three items from the middle of the list.
Print the message The last three items in the list are:
Use a slice to print the last three items in the list.
'''

valores = [valor for valor in range(1,21)]
quantidade_valores = int(len(valores)/2)

valores_meio = valores[quantidade_valores-1:quantidade_valores+2]

print(f'Os primeiros 3 itens na lista são: {valores[:3]}')
print(f'Os 3 itens no meio da lista são: {valores_meio}')
print(f'Os 3 últimos itens da lista são: {valores[-3:]}\n')


'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
Add a new pizza to the original list.
Add a different pizza to the list friend_pizzas.
Prove that you have two separate lists. Print the message My favorite pizzas are:
Then use a for loop to print the first list. 
Print the message My friend's favorite pizzas are:
Then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list.
Se baseando no exercício acima
'''
meus_pratos = ['macarrão','bife','strogonoff','miojo']
pratos_amigo = meus_pratos[:]                         #usado slice para que qualquer alteração que houver não afete a outra lista
pratos_amigo.append('feijão')
print(f'Meus pratos:{meus_pratos}\nPratos de meu amigo:{pratos_amigo}\n')

#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space. 
#Choose a version of foods.py, and write two for loops to print each list of foods.

virgula = ','                       #Inicia vírgula pra questões estéticas.
print("Meus pratos:",end='')
for prato in meus_pratos:
    if meus_pratos[-1] == prato:
        virgula = '.'
    print(f'{prato}{virgula}', end= '')

virgula = ','                       #Reseta a vírgula anteriormente alterada.
print('\n')
print("Pratos de meu amigo:",end='')
for prato in pratos_amigo:
    if pratos_amigo[-1] == prato:
        virgula = '.'
    print(f'{prato}{virgula}', end= '')

print("\n:)")