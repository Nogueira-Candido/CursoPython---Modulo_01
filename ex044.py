print('{:=^40}'.format(' LOJAS NOGUEIRA '))

compra = float(input('Digite o valor da compra R$: '))

opcao = int(input('''
FORMAS DE PAGAMENTO: 
[1] - A vista Dinheiro/Cheque 
[2] - A vista no cartão 
[3] - Duas vezez no cartão 
[4] - Três vezes ou mais no cartão 
QUAL A OPÇÃO ESCOLHIDA? '''))

if opcao == 1:
    vrFinal = compra - (compra * (10/100))
elif opcao == 2:
    vrFinal = compra - (compra * (5/100))
elif opcao == 3:
    parcelado = compra / 2
    print('Sua compra será parcelado em 2X de R${:.2f}'.format(parcelado))
    vrFinal = compra
elif opcao == 4:
    parcela = int(input('Quantas vezes? '))
    vlrparcela = compra / parcela
    if parcela >=3:
        vrFinal = compra + (compra *(20/100))
    print('Valor da parcela em {} vezes =  R${:.2f}'.format(parcela, vlrparcela))
print('Uma compra no valor de R${:.2f} saiu por R${:.2f}'.format(compra,vrFinal))

