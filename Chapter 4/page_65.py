#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#Print the message The first three items in the list are:
#Then use a slice to print the first three items from that program’s list. 
#Print the message Three items from the middle of the list are:
#Use a slice to print three items from the middle of the list.
#Print the message The last three items in the list are:
#Use a slice to print the last three items in the list.


valores = [valor for valor in range(1,21)]
quantidade_valores = int(len(valores)/2)

valores_meio = valores[quantidade_valores-1:quantidade_valores+2]

print(f'Os primeiros 3 itens na lista são: {valores[:3]}')
print(f'Os 3 itens no meio da lista são: {valores_meio}')