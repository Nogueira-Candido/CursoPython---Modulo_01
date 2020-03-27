salario = float(input('Digite o salário do funcionário R$: '))

salarioSuperior = salario + (salario * 10/100)
salarioInferior = salario + (salario * 15/100)

if salario > 1250:
    print('Quem ganhava R${:.2f}, agora passa a ganhar R${:.2f}, pois teve um aumento de 10%.'.format(salario, salarioSuperior))
if salario <= 1250:
    print('Quem ganhava R${:.2f}, agora passa a ganhar R${:.2f}, pois teve um aumento de 15%.'.format(salario, salarioInferior))
