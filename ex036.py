VR_CASA = float(input('Qual o valor da casa? R$ '))
SAL_COMPRADOR = float(input('Qual o salário do comprador? R$'))
TEMPO_PAGAMENTO = int(input('Em quantos anos será o pagamento? '))

#CONVERTENDO ANOS EM MESES
CONVERSAO_ANO_MES = TEMPO_PAGAMENTO * 12

#PRESTAÇÃO MENSAL
PRESTACAO = VR_CASA / CONVERSAO_ANO_MES

#CÁLCULO 30% DO SALÁRIO
PERCENTUAL_SAL = SAL_COMPRADOR * (30/100)

print('Valor da prestação mensal R${:.2f}'.format(PRESTACAO))

if PRESTACAO > PERCENTUAL_SAL:
    print('Empréstimo Negado')
else:
    print('Parabéns! O seu cédito foi aprovado.')