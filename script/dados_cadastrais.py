import pandas as pd
import os

#NOME
nome = str(input("DIGITE O NOME DA INSTITUIÇÃO EM LETRAS MAÍUSCULAS: "));
os.system("cls")

#CNPJ
cnpj = str(input("DIGITE O CNPJ: "));
while len(cnpj)!=14:
    cnpj = str(input("DIGITE O CNPJ: "));
os.system("cls")


#SOCIEDADE CIVIL
sociedade_civil = int(input("DIGITE O TIPO DE ORGANIZAÇÃO DA SOCIEDADE CIVIL:\n(1) SEM FINS LUCRATIVOS\n(2) COOPERATIVA\n(3) RELIGIOSA\n"));
while sociedade_civil<1 or sociedade_civil>3:
    sociedade_civil = int(input("DIGITE O TIPO DE ORGANIZAÇÃO DA SOCIEDADE CIVIL:\n(1) SEM FINS LUCRATIVOS\n(2) COOPERATIVA\n(3) RELIGIOSA\n"));
if sociedade_civil==1:
    sociedade_civil="SEM FINS LUCRATIVOS";
if sociedade_civil==2:
    sociedade_civil="COOPERATIVA";
if sociedade_civil==3:
    sociedade_civil="RELIGIOSA";
os.system("cls")

#ENDEREÇO
endereço = str(input("DIGITE O SEU ENDEREÇO:"));
os.system("cls")

#BAIRRO
bairro = str(input("DIGITE O SEU BAIRRO: "))
os.system("cls")

#CIDADE
cidade = str(input("DIGITE O NOME DA SUA CIDADE: "))
os.system("cls")

#U.F.
estado = int(input("DIGITE O NÚMERO DO SEU ESTADO:\n(1) Roraima	 RR	Norte\n(2) Amapá	 AP	Norte\n(3) Amazonas AM Norte\n(4) Pará	 PA	Norte\n(5) Acre	 AC	Norte\n(6) Rondônia RO	Norte\n(7) Tocantins TO Norte\n(8) Maranhão  MA Nordeste\n(9) Piauí	  PI Nordeste\n(10) Ceará	  CE Nordeste\n(11) Rio Grande do Norte RN Nordeste\n(12) Paraíba	PB Nordeste\n(13) Pernambuco	PE Nordeste\n(14) Alagoas	AL Nordeste\n(15) Sergipe	SE Nordeste\n(16) Bahia	BA Nordeste\n(17) Mato Grosso	MT Centro-oeste\n(18) Distrito Federal DF Centro-oeste\n(19) Goiás GO Centro-oeste\n(20) Mato Grosso do Sul	MS  Centro-oeste\n(21) Minas Gerais	MG Sudeste\n(22) Espírito Santo	ES Sudeste\n(23) Rio de Janeiro	RJ Sudeste\n(24) São Paulo	SP Sudeste\n(25) Paraná	PR  Sul\n(26) Santa Catarina	SC Sul\n(27) Rio Grande do sul RS  Sul\n"));
while estado<1 or estado>27:
    estado = int(input("DIGITE O NÚMERO DO SEU ESTADO:\n(1) Roraima	 RR	Norte\n(2) Amapá	 AP	Norte\n(3) Amazonas AM Norte\n(4) Pará	 PA	Norte\n(5) Acre	 AC	Norte\n(6) Rondônia RO	Norte\n(7) Tocantins TO Norte\n(8) Maranhão  MA Nordeste\n(9) Piauí	  PI Nordeste\n(10) Ceará	  CE Nordeste\n(11) Rio Grande do Norte RN Nordeste\n(12) Paraíba	PB Nordeste\n(13) Pernambuco	PE Nordeste\n(14) Alagoas	AL Nordeste\n(15) Sergipe	SE Nordeste\n(16) Bahia	BA Nordeste\n(17) Mato Grosso	MT Centro-oeste\n(18) Distrito Federal DF Centro-oeste\n(19) Goiás GO Centro-oeste\n(20) Mato Grosso do Sul	MS  Centro-oeste\n(21) Minas Gerais	MG Sudeste\n(22) Espírito Santo	ES Sudeste\n(23) Rio de Janeiro	RJ Sudeste\n(24) São Paulo	SP Sudeste\n(25) Paraná	PR  Sul\n(26) Santa Catarina	SC Sul\n(27) Rio Grande do sul RS  Sul\n"));
if estado==1:
    estado="Roraima (RR) Norte";
if estado==2:
    estado="Amapá (AP) Norte";
if estado==3:
    estado="Amazonas (AM) Norte";
if estado==4:
    estado="Pará (PA) Norte";
if estado==5:
    estado="Acre (AC)Norte";
if estado==6:
    estado="Rondônia (RO) Norte";
if estado==7:
    estado="Tocantins (TO) Norte";
if estado==8:
    estado="Maranhão (MA) Nordeste";
if estado==9:
    estado="Piauí (PI) Nordeste";
if estado==10:
    estado="Ceará (CE) Nordeste";
if estado==11:
    estado="Rio Grande do Norte (RN) Nordeste";
if estado==12:
    estado="Paraíba (PB) Nordeste";
if estado==13:
    estado="Pernambuco	(PE) Nordeste";
if estado==14:
    estado="Alagoas (AL) Nordeste";
if estado==15:
    estado="Sergipe (SE) Nordeste";
if estado==16:
    estado="Bahia (BA) Nordeste";
if estado==17:
    estado="Mato Grosso (MT) Centro-oeste";
if estado==18:
    estado="Distrito Federal (DF) Centro-oeste";
if estado==19:
    estado="Goiás (GO) Centro-oeste";
if estado==20:
    estado="Mato Grosso do Sul	(MS) Centro-oeste";
if estado==21:
    estado="Minas Gerais (MG) Sudeste";
if estado==22:
    estado="Espírito Santo	(ES) Sudeste";
if estado==23:
    estado="Rio de Janeiro	(RJ) Sudeste";
if estado==24:
    estado="São Paulo (SP) Sudeste";
if estado==25:
    estado="Paraná	(PR) Sul";
if estado==26:
    estado="Santa Catarina	(SC) Sul";
if estado==27:
    estado="Rio Grande do sul (RS) Sul";
os.system("cls");

#CEP
cep = str(input("DIGITE O NÚMERO DO SEU CEP: "));
while len(cep)!=8:
    cep = str(input("DIGITE O NÚMERO DO SEU CEP: "));
os.system("cls");

#EMAIL
email = str(input("DIGITE O SEU EMAIL: "));
email = str(input("REPITA O SEU ENDEREÇO DE E-MAIL: "));
os.system("cls");

#TELEFONE
prefixo = str(input("DIGITE O PREFIXO DO SEU TELEFONE BR(55): "))
if len(prefixo)!=2:
    prefixo = str(input("DIGITE O PREFIXO DO SEU TELEFONE BR(55): "));
telefone = str(input("DIGITE O NÚMERO DO SEU TELEFONE: "));
if len(telefone)!=9:
    telefone = str(input("DIGITE O NÚMERO DO SEU TELEFONE: "));
os.system("cls");

#NOME DO RESPONSÁVEL
nome_responsável = str(input("DIGITE O NOME DO RESPONSÁVEL: "));
os.system("cls");

#CPF RESPONSÁVEL
cpf_responsável = str(input("DIGITE O NÚMERO DE CPF DO RESPONSÁVEL: "));
while len(cpf_responsável)!=11:
    cpf_responsável = str(input("DIGITE O NÚMERO DE CPF DO RESPONSÁVEL: "));
os.system("cls");

#ID
id = str(input("DIGITE O NÚMERO DA CARTEIRA DE IDENTIDADE DO RESPONSÁVEL: "));
while len(id)!=10:
    id = str(input("DIGITE O NÚMERO DA CARTEIRA DE IDENTIDADE DO RESPONSÁVEL: "));
os.system("cls");

#ENDEREÇO DO RESPONSÁVEL
endereço_responsável = str(input("DIGITE O ENDEREÇO DO RESPONSÁVEL: "));
os.system("cls");

#CEP
cep_responsável = str(input("DIGITE O NÚMERO DO SEU CEP: "));
while len(cep_responsável)!=8:
    cep_responsável = str(input("DIGITE O NÚMERO DO SEU CEP: "));
os.system("cls");

#CARGO
cargo = str(input("DIGITE O CARGO: "));
os.system("cls");

#BANCO
banco = int(input("DIGITE O NÚMERO PARA O BANCO:\n(1) BANCO DO BRASIL\n(2) ITAÚ\n(3) CAIXA ECONÔMICA FEDERAL\n(4) BRADESCO\n(5) SANTANDER\n(6) NUBANK\n"));
if banco==1:
    banco="BANCO DO BRASIL";
if banco==2:
    banco="ITAÚ";
if banco==3:
    banco="CAIXA ECONÔMICA FEDERAL";
if banco==4:
    banco="BRADESCO";
if banco==5:
    banco="SANTANDER";
if banco==6:
    banco="NUBANK";
os.system("cls");

#AGÊNCIA
agência = str(input("DIGITE O NÚMERO DA AGÊNCIA: "));
while len(agência)!=4:
    agência = str(input("DIGITE O NÚMERO DA AGÊNCIA: "));
os.system("cls");

#CONTA
conta = str(input("DIGITE O NÚMERO DA CONTA: "));
while len(conta)!=7:
    conta = str(input("DIGITE O NÚMERO DA CONTA: "));
os.system("cls");

#DÍGITO
digito = str(input("DIGITE O DÍGITO: "));
while len(digito)!=1:
    digito = str(input("DIGITE O DÍGITO: "));
os.system("cls");


dados_cadastrais = {"ITENS":["NOME DA INSTITUIÇÃO: ","CNPJ: ","TIPO DE ORGANIZAÇÃO DA SOCIEDADE CIVIL: ","ENDEREÇO: ","BAIRRO: ", "CIDADE: ","U.F.: ","CEP: ","E-MAIL: ", "CONTATO: ", "NOME DO RESPONSÁVEL: ", "CPF DO RESPONSÁVEL: ", "RG: ", "ENDEREÇO DO RESPONSÁVEL: ", "CEP RESPONSÁVEL: ", "CARGO: ", "BANCO: ", "AGÊNCIA: ", "CONTA: "],"DADOS CADASTRAIS":[nome,cnpj,sociedade_civil,endereço,bairro,cidade,estado,cep,email,prefixo+telefone, nome_responsável, cpf_responsável, id, endereço_responsável, cep_responsável, cargo, banco, agência, conta+"-"+digito]};
dados_cadastrais = pd.DataFrame(dados_cadastrais)
print(dados_cadastrais);

os.system("PAUSE");