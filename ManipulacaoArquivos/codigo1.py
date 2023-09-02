arq = open('oi.txt', "w") 

temp1 = 5
temp2 = 10
temp3 = 15
temp4 = 5
temp5 = 43
temp6 = 41
temp7 = 9
temp8 = 8
temp9 = 15
temp10 = 65
temp11 = 89
temp12 = 99
arq.write("%f\n %f\n %f\n %f\n %f\n %f\n  %f\n %f\n %f\n  %f\n %f\n %f\n" %(temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8, temp9, temp10, temp11, temp12) )    
arq.close()

#PARTE UM DO CÓDIGO: Fazer um código que leia 12 temps medidas em um dia de 0 até 23h e informe:
    #maior temp do dia, media da temp de manhã tarde noite e do dia todo
import math 
arq = open('oi.txt', "r") 
maiorTemp = -math.inf
media = 0
somaManha = 0
somaTarde = 0
somaNoite = 0 
somaDia = 0
hora = 0

for linha in arq:
    temp = float(linha.strip())
    somaDia += temp
    if temp > maiorTemp:
        maiorTemp = temp
    if hora <12:
        somaManha += temp
    elif hora < 18:
        somaTarde += temp
    else:
        somaNoite += temp
    hora += 2
        
mediaManha = somaManha / 6
mediaTarde = somaTarde / 7 
mediaNoite = somaNoite / 5         
mediaDia = somaDia / 12
        
arq.close()
print(mediaManha, ",", mediaTarde,",",mediaNoite, ",", mediaDia)

#PARTE 2 DO CÓDIGO:
"""Crie uma lista com 10 pares de listas. Cada sublista deve conter um n de mes e a
 qtd de dias chuvosos no mês. """
 


arq = open('ok.txt', "w") 

meses = [[1,4], [2,7], [3, 8], [4,5], [5,8], [6,7], [7,2], [8,0], [9,1], [10,0]]

for par in meses:
    mes = str(par[0])
    dias = str(par[1])
    arq.write("No mês %s,chuveu em %s dias.\n" %(mes, dias))
            

arq.close()
