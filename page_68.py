'''
4-13. Buffet: A buffet-style restaurant offers only five basic foods. 
Think of five simple foods, and store them in a tuple.
Use a for loop to print each food the restaurant offers.
Try to modify one of the items, and make sure that Python rejects thechange.
The restaurant changes its menu, replacing two of the items with different foods. 
Add a line that rewrites the tuple
Then use a for loop to print each of the items on the revised menu.
'''

#Lista de pratos.
meus_pratos = ('macarrão','bife','strogonoff','miojo','batata frita')

#Inicia vírgula pra questões estéticas.
virgula = ','

#Os pratos são printados na tela do usuário de maneira que fique ortograficamente aceitável.
print("Meus pratos:",end='')
for prato in meus_pratos:
    
    #Testa se o prato atual é ou não o ultimo prato do cardápio.
    if meus_pratos[-1] == prato:
        virgula = '.'
    print(f'{prato}{virgula}', end= '')


meus_pratos = ('macarrão','bife','strogonoff','arroz','feijão')

#Reseta vírgula.
virgula = ','

#Pratos modificados são printados.
print("\nMeus pratos modificado:",end='')
for prato in meus_pratos:
    if meus_pratos[-1] == prato:
        virgula = '.'
    print(f'{prato}{virgula}', end= '')