import os
import pandas as pd

#NOME DO PROJETO
nome_projeto = str(input("DIGITE O NOME DO PROJETO: "));
os.system("cls")

#PRAZO DE ENTREGA

dia_ini = int(input("DIGITE O DIA DE INÍCIO: "));
while dia_ini<1 or dia_ini>30:
    dia_ini = int(input("DIGITE O DIA DE INÍCIO: "));

dia_final = int(input("DIGITE O DIA DE TÉRMINO: "));
while dia_final<1 or dia_final>30:
    dia_final = int(input("DIGITE O DIA DE TÉRMINO: ")); 

mes_ini = int(input("DIGITE O MÊS DE INÍCIO: "));
while mes_ini<1 or mes_ini>12:
    mes_ini = int(input("DIGITE O MÊS DE INÍCIO: "));

mes_final = int(input("DIGITE O MÊS DE TÉRMINO: "));
while mes_final<1 or mes_final>12:
    mes_final = int(input("DIGITE O MÊS DE TÉRMINO: "));


ano_ini = int(input("DIGITE O ANO DE INÍCIO: "));
while ano_ini!=2022:
    ano_ini = int(input("DIGITE O ANO DE INÍCIO: "));

ano_final = int(input("DIGITE O ANO DE TÉRMINO: "));
while ano_final<2022:
    ano_final = int(input("DIGITE O ANO DE TÉRMINO: "));

while ano_ini==ano_final and mes_ini==mes_final and dia_ini>dia_final:
    dia_ini = int(input("DIGITE O DIA DE INÍCIO: "));
    while dia_ini<1 or dia_ini>30:
        dia_ini = int(input("DIGITE O DIA DE INÍCIO: "));

    dia_final = int(input("DIGITE O DIA DE TÉRMINO: "));
    while dia_final<1 or dia_final>30:
        dia_final = int(input("DIGITE O DIA DE TÉRMINO: ")); 

    mes_ini = int(input("DIGITE O MÊS DE INÍCIO: "));
    while mes_ini<1 or mes_ini>12:
        mes_ini = int(input("DIGITE O MÊS DE INÍCIO: "));

    mes_final = int(input("DIGITE O MÊS DE TÉRMINO: "));
    while mes_final<1 or mes_final>12:
        mes_final = int(input("DIGITE O MÊS DE TÉRMINO: "));


    ano_ini = int(input("DIGITE O ANO DE INÍCIO: "));
    while ano_ini!=2022:
        ano_ini = int(input("DIGITE O ANO DE INÍCIO: "));

    ano_final = int(input("DIGITE O ANO DE TÉRMINO: "));
    while ano_final<2022:
        ano_final = int(input("DIGITE O ANO DE TÉRMINO: "));

while ano_ini==ano_final and mes_ini>mes_final:
    dia_ini = int(input("DIGITE O DIA DE INÍCIO: "));
    while dia_ini<1 or dia_ini>30:
        dia_ini = int(input("DIGITE O DIA DE INÍCIO: "));

    dia_final = int(input("DIGITE O DIA DE TÉRMINO: "));
    while dia_final<1 or dia_final>30:
        dia_final = int(input("DIGITE O DIA DE TÉRMINO: ")); 

    mes_ini = int(input("DIGITE O MÊS DE INÍCIO: "));
    while mes_ini<1 or mes_ini>12:
        mes_ini = int(input("DIGITE O MÊS DE INÍCIO: "));

    mes_final = int(input("DIGITE O MÊS DE TÉRMINO: "));
    while mes_final<1 or mes_final>12:
        mes_final = int(input("DIGITE O MÊS DE TÉRMINO: "));

    ano_ini = int(input("DIGITE O ANO DE INÍCIO: "));
    while ano_ini!=2022:
        ano_ini = int(input("DIGITE O ANO DE INÍCIO: "));

    ano_final = int(input("DIGITE O ANO DE TÉRMINO: "));
    while ano_final<2022:
        ano_final = int(input("DIGITE O ANO DE TÉRMINO: "));
os.system("cls")

#PÚBLICO ALVO
#IDADE
idade = int(input("DIGITE A MENOR IDADE PARA O SEU PÚBLICO ALVO: "));
while idade<0:
    idade = int(input("DIGITE A MENOR IDADE PARA O SEU PÚBLICO ALVO: "));
os.system("cls")

#SEXO
sexo = int(input("DIGITE (1) MASCULINO (2) FEMININO (3) AMBOS: "))
while sexo<1 or sexo>3:
    sexo = int(input("DIGITE (1) MASCULINO (2) FEMININO (3) AMBOS: "));
if sexo==1:
    sexo="MASCULINO"
if sexo==2:
    sexo="FEMININO"
if sexo==3:
    sexo="AMBOS"
os.system("cls")
    
#FORMAÇÃO
formação = int(input("(1) ENSINO FUNDAMENTAL\n(2) ENSINO MÉDIO INCOMPLETO\n(3) ENSINO MÉDIO COMPLETO\n(4) ENSINO SUPERIOR INCOMPLETO\n(5) ENSINO SUPERIOR COMPLETO\n(6) PÓS-GRADUAÇÃO\n"));
while formação<1 or formação>6:
    formação = int(input("(1) ENSINO FUNDAMENTAL\n(2) ENSINO MÉDIO INCOMPLETO\n(3) ENSINO MÉDIO COMPLETO\n(4) ENSINO SUPERIOR INCOMPLETO\n(5) ENSINO SUPERIOR COMPLETO\n(6) PÓS-GRADUAÇÃO\n"));
if formação==1:
    formação="ENSINO FUNDAMENTAL";
if formação==2:
    formação="ENSINO MÉDIO INCOMPLETO";
if formação==3:
    formação="ENSINO MÉDIO";
if formação==4:
    formação="ENSINO SUPERIOR INCOMPLETO";
if formação==5:
    formação="ENSINO SUPERIOR COMPLETO";
if formação==6:
    formação="PÓS-GRADUAÇÃO";
os.system("cls")

#PODER AQUISITIVO
poder_aquisitivo = float(input("DIGITE O PODER DE COMPRA DO SEU CONSUMIDOR: "));
while poder_aquisitivo<0:
    poder_aquisitivo = float(input("DIGITE O PODER DE COMPRA DO SEU CONSUMIDOR: "));
os.system("cls")

#CLASSE SOCIAL
classe_social = int(input("DIGITE (1)CLASSE BAIXA (2)CLASSE MÉDIA (3)CLASSE ALTA\n"));
while classe_social<1 or classe_social>3:
    classe_social = int(input("DIGITE (1)CLASSE BAIXA (2)CLASSE MÉDIA (3)CLASSE ALTA\n"));
if classe_social==1:
    classe_social="CLASSE BAIXA";
if classe_social==2:
    classe_social="CLASSE MÉDIA";
if classe_social==3:
    classe_social="CLASSE ALTA";
os.system("cls")


data = {"ITENS":["NOME DO PROJETO: ", "DATA DE INÍCIO: ", "DATA DE TÉRMINO: ", "PÚBLICO ALVO", "IDADE: "," SEXO: ", " FORMAÇÃO: ", " PODER AQUISITIVO ($): ", " CLASSE SOCIAL: ", ],
"INFORMAÇÕES:":[nome_projeto, "%i/%i/%i" %(dia_ini, mes_ini, ano_ini), "%i/%i/%i" %(dia_final, mes_final, ano_final),"True",idade, sexo, formação, poder_aquisitivo, classe_social, ]}


df = pd.DataFrame(data)
print(df)
os.system("PAUSE");
