NACIONALIDADE = [
    "afegão",
    "sul-africano",
    "albanês",
    "alemão",
    "andorrano",
    "angolano",
    "antiguano",
    "saudito",
    "argelino",
    "argentino",
    "armênio",
    "australiano",
    "austríaco",
    "azerbaijano",
    "bengalês",
    "barbadiano",
    "bielo-russo",
    "belizenho",
    "boliviano",
    "bósnio",
    "bechuano",
    "brasileiro",
    "bruneano",
    "búlgaro",
    "burundinês",
    "butanês",
    "caboverdiano",
    "cambojano",
    "catariano",
    "chadiano",
    "chileno",
    "chinês",
    "cingapuriano",
    "colombiano",
    "congolês",
    "norte-coreano",
    "sul-coreano",
    "costarriquenho",
    "cubano",
    "dinamarquês",
    "djibutiano",
    "dominicano",
    "egípcio",
    "salvadorenho",
    "equatoriano",
    "eritreu",
    "eslovaco",
    "esloveno",
    "espanhol",
    "americano",
    "estoniano",
    "fijiano",
    "filipino",
    "finlandês",
    "francês",
    "gambiano",
    "ganês",
    "georgiano",
    "granadino",
    "grego",
    "guatemalteco",
    "guianês",
    "guinéu-equatoriano",
    "haitiano",
    "hondurenho",
    "húngaro",
    "marshalino",
    "salomônico",
    "indiano",
    "indonésio",
    "iraniano",
    "iraquiano",
    "irlandês",
    "islandês",
    "italiano",
    "jamaicano",
    "japonês",
    "libanês	",
    "liberiano",
    "líbio",
    "lituano",
    "luxemburguês",
    "macedônio",
    "malaio",
    "malauiano",
    "maldivo",
    "maltês",
    "marroquino",
    "mauriciano",
    "mauritano",
    "mexicano",
    "micronésio",
    "moçambicano",
    "birmanês",
    "moldávio",
    "monegasco",
    "montenegrino",
    "nepalês",
    "nigerino",
    "nigeriano",
    "norueguês",
    "neozelandês",
    "panamenho",
    "paquistanês",
    "paraguaio",
    "peruano",
    "polonês",
    "português",
    "queniano",
    "inglês",
    "centro-africano",
    "dominicano",
    "tcheco",
    "romeno",
    "ruandês",
    "samoano",
    "senegalês",
    "sérvio",
    "sírio",
    "sudanês",
    "suéco",
    "suíço",
    "surinamês",
    "tailandês",
    "tanzaniano",
    "togonês",
    "tunisiano",
    "turco",
]


def nacionalidade_com_genero(nac):
    return f"{nac}(a)"


ESTADO_CIVIL = [
    "SOLTEIRO(a)",
    "CASADO(a)",
    "VIÚVO(a)",
    "SEPARADO(a)",
]

EXPEDICAO = [
    "SSP/UF",
    "Cartório Civil",
    "Polícia Federal",
    "DETRAN",
]

ADMINISTRACAO_NEGOCIOS = {
    "Administração": "Administrador",
    "Administração Pública": "Administrador Público",
    "Agronegócios e Agropecuária": "Agropecuarista",
    "Ciências Aeronáuticas": "Cientista Aeronáutico",
    "Ciências Atuariais": "Cientista Atuarial",
    "Ciências Contábeis": "Cientista Contábil",
    "Ciências Econômicas": "Cientista Econômico",
    "Comércio Exterior": "Profissional de Comércio Exterior",
    "Defesa e Gestão Estratégica Internacional": "Gestor de Estratégia Internacional",
    "Gastronomia": "Profissional em Gatronomia",
    "Gestão Comercial": "Gestor Comercial",
    "Gestão de Recursos Humanos": "Gestor de Recursos Humanos",
    "Gestão de Segurança Privada": "Gestor de Segurança Privada",
    "Gestão de Seguros": "Gestor de Seguros",
    "Gestão de Turismo": "Gestor de Turismo",
    "Gestão Financeira": "Gestor Financeiro",
    "Gestão Pública": "Gestão Pública",
    "Hotelaria": "Hoteleiro",
    "Logística": "Logístico",
    "Marketing": "Profissional de Marketing",
    "Negócios Imobiliários": "Corretor Imobiliário",
    "Pilotagem profissional de aeronaves": "Piloto de Aeronaves",
    "Processos Gerenciais": "Profissional de Processos Gerenciais",
    "Segurança Pública": "Profissional de Segurança Pública",
    "Turismo": "Profissional de Agência de Turismo",
}

ARTES_DESIGN = {
    "Animação": "Projetista de Animações",
    "Arquitetura e Urbanismo": "Arquiteto(a)",
    "Artes Visuais": "Profissional de Artes Visuais",
    "Comunicação das Artes do Corpo": "Comunicador das Artes do Corpo",
    "Conservação e Restauro": "Profissional de Conservação e Restauração",
    "Dança": "Dançarino(a)",
    "Design": "Designer",
    "Design de Games": "Designer de Games",
    "Design de Interiores": "Designer de Interiores",
    "Design de Moda": "Designer de Moda",
    "Fotografia": "Fotógrafo(a)",
    "História da Arte": "Historiador da Arte",
    "Jogos Digitais": "Projetista de Jogos Digitais",
    "Luteria": "Luthier",
    "Música": "Músico(a)",
    "Produção Cênica": "Cinematografista",
    "Produção Fonográfica": "Fonográfico(a)",
    "Teatro": "Ator/Atriz",
}

# 1.4.3 CIÊNCIAS BIOLÓGICAS E DA TERRA
BIOLOGICAS = {
    "Agroecologia": "Agroecologista",
    "Agronomia": "Agrônomo",
    "Alimentos": "Engenheiro de Alimentos",
    "Astronomia": "Astrônomo",
    "Biocombustíveis": "Engenheiro de Biocombustíveis",
    "Biotecnologia": "Biotecnologista",
    "Bioquímica": "Bioquímico",
    "Ciência e Tecnologia de Alimentos": "Cientista de Alimentos",
    "Ciências Agrárias": "Engenheiro Agrícola",
    "Ciências Biológicas": "Biólogo",
    "Ciências Naturais e Exatas": "Cientista da Natureza",
    "Ecologia": "Ecólogo",
    "Geofísica": "Geofísico",
    "Geologia": "Geólogo",
    "Gestão Ambiental": "Gestor Ambiental",
    "Medicina Veterinária": "Veterinário(a)",
    "Meteorologia": "Metereologista",
    "Oceanografia": "Oceanografista",
    "Produção de Bebidas": "Produtor de Bebidas",
    "Produção Sucroalcooleira": "Produtor Sucroalcooleira",
    "Rochas Ornamentais": "Tecnólogo em Rochas Ornamentais",
    "Zootecnia": "Zootecnista",
}

# 1.4.3 ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
SISTEMAS = {
    "Análise e Desenvolvimento de Sistemas": "Analista e Desenvolvedor de Sistemas",
    "Banco de Dados": "Desenvolvedor Back-End",
    "Ciência da Computação": "Cientista da Computação",
    "Ciência e Tecnologia": "Cientista",
    "Computação": "Técnico em Computação",
    "Estatística": "Estatístico",
    "Física": "Físico",
    "Gestão da Tecnologia da Informação": "Gestor da Tecnologia da Informação",
    "Informática": "Técnico em Informática",
    "Informática Biomédica": "Técnico em Informática Biomédica",
    "Matemática": "Matemático",
    "Nanotecnologia": "Técnico em Nanotecnologia",
    "Química": "Químico",
    "Redes de Computadores": "Analista de Rede de Computadores",
    "Segurança da Informação": "Analista de Segurança da Informação",
    "Sistemas de Informação": "Analista de Sistemas da Informação",
    "Sistemas para Internet": "Técnico de Sistemas para Internet",
}

# 1.4.4 CIÊNCIAS SOCIAIS E HUMANAS
SOCIAIS = {
    "Ciências Sociais": "Cientista Social",
    "Arqueologia": "Arqueólogo",
    "Ciências do Consumo": "Cientista de Consumo",
    "Ciências Humanas": "Cientista das Humanidades",
    "Ciências Sociais": "Cientista Social",
    "Cooperativismo": "Cooperativista",
    "Direito": "Advogado(a)",
    "Escrita Criativa": "Escritor Criativo",
    "Estudos de Gênero e Diversidade": "Estudante de Gênero e Diversidade",
    "Filosofia": "Filósofo(a)",
    "Geografia": "Geógrafo(a)",
    "Gestão de Cooperativas": "Gestor(a) de Cooperativas",
    "História": "Historiador(a)",
    "Letras": "Licenciado em Letras",
    "Libras": "Licenciado em Libras",
    "Linguística": "Linguista",
    "Museologia": "Museólogo",
    "Pedagogia": "Pedagogo(a)",
    "Psicopedagogia": "Psicopedagogo(a)",
    "Relações Internacionais": "Internacionalista",
    "Serviço Social": "Assistente Social",
    "Serviços Judiciários e Notariais": "Técnólogo em Serviçoes Judiciários",
    "Tradutor e Intérprete": "Teólogo",
    "Teologia": "Tradutor e Intérprete",
}

# 1.4.5 COMUNICAÇÃO E INFORMAÇÃO
COMUNICACAO = {
    "Comunicação e Informação": "Comunicador(a)",
    "Arquivologia": "Arquivologista",
    "Biblioteconomia": "Bibliotecário",
    "Cinema e Audiovisual": "Cinematografista",
    "Comunicação em Mídias Digitais": "Comunicador em Mídias Digitais",
    "Comunicação Institucional": "Comunicador Institucional",
    "Comunicação Organizacional": "Comunicador Organizacional",
    "Educomunicação": "Educomunicador",
    "Estudos de Mídia": "Estudante de Mídia",
    "Eventos": "Produtor de Eventos",
    "Gestão da Informação": "Gestor da Informação",
    "Jornalismo": "Jornalista",
    "Produção Audiovisual": "Produtor Audiovisual",
    "Produção Cultural": "Produtor Cultural",
    "Produção Editorial": "Produtor Editorial",
    "Produção Multimídia": "Produtor Multimídia",
    "Produção Publicitária": "Produtor Publicitário",
    "Publicidade e Propaganda": "Publicitário",
    "Rádio, TV e Internet": "Profissional Rádio, TV e Internet",
    "Relações Públicas": "Relações-Públicas",
    "Secretariado": "Secretário",
    "Secretariado Executivo": "Secretário Executivo",
}

# 1.4.6 ENGENHARIA E PRODUÇÃO
ENG_PROD = {
    "Engenharia e Produção": "Engenheiro(a) de Produção",
    "Agrimensura": "Técnico em Agrimensura",
    "Aquicultura": "Aquicultor(a)",
    "Automação Industrial": "Técnico em Automação Industrial",
    "Construção Civil": "Construtor(a) Civil",
    "Construção Naval": "Construtor(a) Naval",
    "Eletrônica Industrial": "Técnico em Eletrônica Industrial",
    "Eletrotécnica Industrial": "Técnico em Eletrotécnica Industrial",
    "Energias Renováveis": "Técnico em Energias Renováveis",
    "Engenharia Acústica": "Engenheiro(a) Acústico(a)",
    "Engenharia Aeronáutica": "Engenheiro(a) Aeronáutico(a)",
    "Engenharia Agrícola": "Engenheiro(a) Agrícola",
    "Engenharia Ambiental e Sanitária": "Engenheiro(a) Ambiental",
    "Engenharia Biomédica": "Engenheiro(a) Biomédica",
    "Engenharia Bioquímica, de Bioprocessos e Biotecnologia": "Engenheiro(a) Bioquímico(a) e Biotecnológico(a)",
    "Engenharia Cartográfica e de Agrimensura": "Engenheiro(a) Cartográfico(a) e de Agrimensura",
    "Engenharia Civil": "Engenheiro(a) Civil",
    "Engenharia da Computação": "Engenheiro(a) da Computação",
    "Engenharia de Alimentos": "Engenheiro de Alimentos",
    "Engenharia de Biossistemas": "Engenheiro(a) de Biossistemas",
    "Engenharia de Controle e Automação": "Engenheiro(a) de Controle e Automação",
    "Engenharia de Energia": "Engenheiro(a) de Energia",
    "Engenharia de Inovação": "Engenheiro(a) de Inovação",
    "Engenharia de Materiais": "Engenheiro(a) de Materiais",
    "Engenharia de Minas": "Engenheiro(a) de Minas",
    "Engenharia de Pesca": "Engenheiro(a) de Pesca",
    "Engenharia de Petróleo": "Engenheiro(a) de Petróleo",
    "Engenharia de Produção": "Engenheiro(a) de Produção",
    "Engenharia de Segurança no Trabalho": "Engenheiro(a) de Segurança no Trabalho",
    "Engenharia de Sistemas": "Engenheiro(a) de Sistemas",
    "Engenharia de Software": "Engenheiro(a) de Software",
    "Engenharia de Telecomunicações": "Engenheiro(a) de Telecomunicações",
    "Engenharia de Transporte e da Mobilidade": "Engenheiro(a) de Transporte e de Mobilidade",
    "Engenharia Elétrica": "Engenheiro(a) Elétrico(a)",
    "Engenharia Eletrônica": "Engenheiro(a) Eletrônica(a)",
    "Engenharia Física": "Engenheiro(a) Físico(a)",
    "Engenharia Florestal": "Engenheiro(a) Florestal",
    "Engenharia Hídrica": "Engenheiro(a) Hídrico(a)",
    "Engenharia Industrial Madeireira": "Engenheiro(a) Industrial e Madeireiro(a)",
    "Engenharia Mecânica": "Engenheiro(a) Mecânico(a)",
    "Engenharia Mecatrônica": "Engenheiro(a) Mecatrônico(a)",
    "Engenharia Metalúrgica": "Engenheiro(a) Metalúrgico(a)",
    "Engenharia Naval": "Engenheiro(a) Naval",
    "Engenharia Nuclear": "Engenheiro(a) Nuclear",
    "Engenharia Química": "Engenheiro(a) Químico(a)",
    "Engenharia Têxtil": "Engenheiro(a) Têxtil",
    "Fabricação Mecânica": "Engenheiro(a) Mecânico(a)",
    "Geoprocessamento": "Técnico em Geoprocessamento",
    "Gestão da Produção Industrial": "Gestor(a) de Produção Industrial",
    "Gestão da Qualidade": "Gestor(a) de Qualidade",
    "Irrigação e Drenagem": "Técnico em Irrigação e Drenagem",
    "Manutenção de aeronaves": "Técnico em Manutenção de aeronaves",
    "Manutenção Industrial": "Técnico em Manutenção Industrial",
    "Materiais": "Técnico em Materiais",
    "Mecatrônica Industrial": "Técnico em Mecatrônica Industrial",
    "Mineração": "Técnico em Mineração",
    "Papel e Celulose": "Técnico em Processamento de Papel e Celulose",
    "Petróleo e Gás": "Técnico em Petróleo e Gás",
    "Processos Metalúrgicos": "Técnico em Processos Metalúrgicos",
    "Processos Químicos": "Técnico em Processos Químicos",
    "Produção Têxtil": "Produtor Têxtil",
    "Saneamento Ambiental": "Técnico em Saneamento Ambiental",
    "Segurança no Trabalho": "Técnico em Segurança do Trabalho",
    "Silvicultura": "Técnico em Silvicultura",
    "Sistemas Biomédicos": "Sistemas Biomédicos",
    "Sistemas de Telecomunicações": "Técnico em Sistemas de Telecomunicações",
    "Sistemas Elétricos": "Técnico em Sistemas Elétricos",
    "Sistemas Embarcados": "Técnico em Sistemas Embarcados",
    "Transporte": "Técnico em Transporte",
}

# 1.4.7 SAÚDE
SAUDE = {
    "Biomedicina": "Biomédico(a)",
    "Educação Física": "Educador Físico",
    "Enfermagem": "Enfermeiro(a)",
    "Esporte": "Atleta",
    "Estética e Cosmética": "Esteticista",
    "Farmácia": "Farmacêutico(a)",
    "Fisioterapia": "Fisioterapeuta",
    "Fonoaudiologia": "Fonoaudiólogo(a)",
    "Gerontologia": "Gerontologista",
    "Gestão Desportiva e de Lazer": "Gestor(a) Desportivo e de Lazer",
    "Gestão em Saúde": "Gestor(a) de Saúde",
    "Gestão Hospitalar": "Gestor(a) Hospitalar",
    "Medicina": "Médico(a)",
    "Musicoterapia": "Musicoterapeuta",
    "Naturologia": "Naturologista",
    "Nutrição": "Nutricionista",
    "Obstetrícia": "Obstetra",
    "Odontologia": "Dentista",
    "Oftálmica": "Oftalmologista",
    "Optometria": "Optometrista",
    "Psicologia": "Psicólogo",
    "Quiropraxia": "Quiropraxista",
    "Radiologia": "Radiologista",
    "Saúde Coletiva": "Técnico em Saúde Coletiva",
    "Terapia Ocupacional": "Terapeuta Ocupacional",
}

AREA_ATUACAO = {
    "ADMNISTRAÇÃO, NEGÓCIOS E SERVIÇOS": ADMINISTRACAO_NEGOCIOS,
    "ARTES E DESIGN": ARTES_DESIGN,
    "CIÊNCIAS BIOLÓGICAS E DA TERRA": BIOLOGICAS,
    "ANÁLISE E DESENVOLVIMENTO DE SISTEMAS": SISTEMAS,
    "CIÊNCIAS SOCIAIS E HUMANAS": SOCIAIS,
    "COMUNICAÇÃO E INFORMAÇÃO": COMUNICACAO,
    "ENGENHARIA E PRODUÇÃO": ENG_PROD,
    "SAÚDE": SAUDE,
    "AUTÔNOMO": ["Autônomo(a)"],
    "DESEMPREGADO": ["Desempregado(a)"],
}

import pandas as pd
from dataclasses import dataclass
from enum import Enum
from typing import Union


class Pessoa(Enum):
    FISICA = 1
    JURIDICA = 2


@dataclass
class DadosFisica:
    nome: str
    nacionalidade: str
    estado_civil: str
    profissao: str
    prefixo: str
    telefone: str
    email: str
    rg: str
    expedicao: str
    cpf: str
    rua: str
    numero: str
    bairro: str
    cidade: str

    def imprime(self):
        p = self
        print("PESSOA FÍSICA\n\n")
        print(
            f"Pelo presente instrumento, {p.nome}, {p.nacionalidade}, {p.estado_civil}, "
            f"{p.profissao}, telefone nº {p.prefixo}{p.telefone}, e-mail {p.email}, "
            f"portador(a) do RG inscrito sob nº {p.rg} expedido por {p.expedicao}, "
            f"CPF inscrito sob o número {p.cpf} residente e domiciliado em {p.rua}, "
            f"{p.numero}, {p.bairro}, {p.cidade}.\n"
        )


@dataclass
class DadosJuridica:
    razao_social: str
    denominacao: str
    cnpj: str
    prefixo: str
    telefone: str
    email: str
    rua: str
    numero: str
    bairro: str
    cidade: str
    nome: str
    cpf: str
    rg: str
    expedicao: str

    def imprime(self):
        p = self
        print("PESSOA JURÍDICA\n\n")
        print(
            f"Pelo presente instrumento, {p.razao_social}, também denominada {p.denominacao}, CNPJ nº {p.cnpj}, "
            f"telefone nº {p.prefixo + p.telefone}, e-mail {p.email}, com sede em {p.rua}, "
            f"{p.numero}, {p.bairro}, {p.cidade}, neste ato representado por {p.nome},"
            f"portador do CPF inscrito sob o nº {p.cpf}, RG inscrito sob o número {p.rg}, "
            f"expedido por {p.expedicao}.\n"
        )


def preparar_lista_numerada(opcoes, comeco=1, sep="\n"):
    return sep.join(f"({i}) {opcao}" for i, opcao in enumerate(opcoes, comeco))


def ler_dados_parceiro() -> Union[DadosFisica, DadosJuridica]:
    pessoa_1 = 0
    while pessoa_1 < 1 or pessoa_1 > 2:
        pessoa_1 = int(
            input("\nDIGITE O TIPO DE PESSOA (1) PESSOA FÍSICA (2) PESSOA JURÍDICA\n")
        )

    if pessoa_1 == 1:
        return ler_dados_pessoa_fisica()
    elif pessoa_1 == 2:
        return ler_dados_pessoa_juridica()


def ler_profissao(area):
    profissoes = list(AREA_ATUACAO.keys())[area - 1]
    profissoes = AREA_ATUACAO[profissoes]

    if len(profissoes) == 1:
        return profissoes[0]

    profissao_1 = -1
    while profissao_1 < 0 or profissao_1 >= len(profissoes):
        profissao_1 = int(
            input(
                "\nDIGITE O NÚMERO PARA SUA ÁREA PROFISSIONAL:\n"
                "(0) VOLTAR\n" + preparar_lista_numerada(profissoes.keys()) + "\n"
            )
        )

        if profissao_1 == 0:
            return None

    profissao = list(profissoes.keys())[profissao_1 - 1]
    return profissoes[profissao]


def ler_dados_pessoa_fisica() -> DadosFisica:
    # 1.1. NOME
    nome_1 = str(input("\nNOME COMPLETO: "))

    # 1.2. NACIONALIDADE
    nacionalidade_1 = 0
    while nacionalidade_1 < 1 or nacionalidade_1 >= len(NACIONALIDADE):
        nacionalidade_1 = int(input(preparar_lista_numerada(NACIONALIDADE) + "\n"))
    nacionalidade_1 = NACIONALIDADE[nacionalidade_1 - 1]

    # 1.3. ESTADO CIVIL
    estado_civil_1 = 0
    while estado_civil_1 < 1 or estado_civil_1 >= len(ESTADO_CIVIL):
        estado_civil_1 = int(
            input(
                "\nESTADO CIVIL: "
                + preparar_lista_numerada(ESTADO_CIVIL, sep=" ")
                + "\n"
            )
        )
    estado_civil_1 = ESTADO_CIVIL[estado_civil_1 - 1]

    # 1.4.0 PROFISSÃO
    area_1 = 0
    while area_1 < 1 or area_1 >= len(AREA_ATUACAO):
        area_1 = int(
            input(
                "\nDIGITE A SUA ÁREA DE ATUAÇÃO:\n"
                + preparar_lista_numerada(AREA_ATUACAO)
                + "\n"
            )
        )
        profissao_1 = ler_profissao(area_1)
        if not profissao_1:
            area_1 = 0

    # 1.5 PREFIXO
    prefixo_1 = ""
    while len(prefixo_1) != 2:
        prefixo_1 = str(input("DIGITE O NÚMERO DO PREFIXO BR(+55): "))

    # 1.6 TELEFONE
    telefone_1 = ""
    while len(telefone_1) != 9:
        telefone_1 = str(input("DIGITE O NÚMERO DE TELEFONE: "))

    # 1.7 E-MAIL
    email_1 = ""
    while len(email_1) < 4:
        email_1 = str(input("DIGITE O E-MAIL: "))
    email_1 = ""
    while len(email_1) < 4:
        email_1 = str(input("REPITA O E-MAIL: "))

    # 1.8 RG
    rg_1 = ""
    while len(rg_1) < 1 or len(rg_1) > 10:
        rg_1 = str(input("DIGITE SEU O Nº DO RG: "))

    # 1.9 EXPEDIÇÃO
    expedicao_1 = 0
    while expedicao_1 < 1 or expedicao_1 > 4:
        expedicao_1 = int(
            input(
                "DIGITE O NÚMERO PARA O ÓRGÃO EXPEDIDOR:\n"
                + preparar_lista_numerada(EXPEDICAO)
                + "\n"
            )
        )
    expedicao_1 = EXPEDICAO[expedicao_1 - 1]

    # 1.10 CPF
    cpf_1 = ""
    while len(cpf_1) < 1 or len(cpf_1) > 14:
        cpf_1 = str(input("CPF. Ex(XXX.XXX.XXX-XX): "))

    # 1.11 NÚMERO
    numero_1 = ""
    while len(numero_1) < 1:
        numero_1 = str(input("NÚMERO DA CASA: "))

    # 1.12 RUA
    rua_1 = ""
    while len(rua_1) < 2:
        rua_1 = str(input("DIGITE O NOME DA SUA RUA: "))

    # 1.13 BAIRRO
    bairro_1 = ""
    while len(bairro_1) < 3 or len(bairro_1) > 20:
        bairro_1 = str(input("BAIRRO: "))

    # 1.14 CIDADE
    cidade_1 = ""
    while len(cidade_1) < 1 or len(cidade_1) > 30:
        cidade_1 = str(input("CIDADE: "))

    return DadosFisica(
        nome_1,
        nacionalidade_1,
        estado_civil_1,
        profissao_1,
        prefixo_1,
        telefone_1,
        email_1,
        rg_1,
        expedicao_1,
        cpf_1,
        rua_1,
        numero_1,
        bairro_1,
        cidade_1,
    )


def ler_dados_pessoa_juridica() -> DadosJuridica:
    # 2.1 RAZÃO SOCIAL
    razao_social = str(input("DIGITE A RAZÃO SOCIAL DA EMPRESA:\n"))

    # 2.2 NOME FANTASIA
    denominacao = str(input("DIGITE O NOME FANTASIA DA EMPRESA:\n"))

    # 2.3 CNPJ
    cnpj = ""
    while len(cnpj) != 18:
        cnpj = str(input("DIGITE O CNPJ. Ex.:(XX.XXX.XXX/YYYY-ZZ):\n"))

    # 2.4 PREFIXO
    prefixo_1 = ""
    while len(prefixo_1) != 2:
        prefixo_1 = str(input("DIGITE O NÚMERO DO PREFIXO BR(+55): "))

    # 2.5 TELEFONE
    telefone_1 = ""
    while len(telefone_1) != 9:
        telefone_1 = str(input("DIGITE O NÚMERO DE TELEFONE: "))

    # 2.6 E-MAIL
    email_1 = ""
    while len(email_1) < 4:
        email_1 = str(input("DIGITE O E-MAIL: "))
        email_1 = str(input("REPITA O E-MAIL: "))
    while len(email_1) < 4:
        email_1 = str(input("REPITA O E-MAIL: "))

    # 2.7 NÚMERO
    numero_1 = ""
    while len(numero_1) < 1:
        numero_1 = str(input("NÚMERO DA CASA: "))

    # 2.8 RUA
    rua_1 = ""
    while len(rua_1) < 2:
        rua_1 = str(input("DIGITE O NOME DA SUA RUA: "))

    # 2.9 BAIRRO
    bairro_1 = ""
    while len(bairro_1) < 3 or len(bairro_1) > 20:
        bairro_1 = str(input("BAIRRO: "))

    # 2.10 CIDADE
    cidade_1 = str(input("CIDADE: "))
    while len(cidade_1) < 1 or len(cidade_1) > 30:
        cidade_1 = str(input("CIDADE: "))

    # 2.11 NOME DO REPRESENTANTE
    nome_1 = str(input("NOME COMPLETO DO REPRESENTANTE: "))

    # 2.12 CPF DO REPRESENTANTE
    cpf_1 = ""
    while len(cpf_1) < 1 or len(cpf_1) > 14:
        cpf_1 = str(input("CPF DO REPRESENTANTE. Ex(XXX.XXX.XXX-XX): "))

    # 2.12 RG DO REPRESENTANTE
    rg_1 = ""
    while len(rg_1) < 1 or len(rg_1) > 10:
        rg_1 = str(input("DIGITE SEU O Nº DO RG: "))

    # 2.13 EXPEDIÇÃO
    expedicao_1 = 0
    while expedicao_1 < 1 or expedicao_1 > 4:
        expedicao_1 = int(
            input(
                "DIGITE O NÚMERO PARA O ÓRGÃO EXPEDIDOR:\n"
                + preparar_lista_numerada(EXPEDICAO)
                + "\n"
            )
        )
    expedicao_1 = EXPEDICAO[expedicao_1 - 1]

    return DadosJuridica(
        razao_social,
        denominacao,
        cnpj,
        prefixo_1,
        telefone_1,
        email_1,
        rua_1,
        numero_1,
        bairro_1,
        cidade_1,
        nome_1,
        cpf_1,
        rg_1,
        expedicao_1,
    )


if __name__ == "__main__":
    parceiro_1 = ler_dados_parceiro()
    parceiro_2 = ler_dados_parceiro()
  

    parceiro_1.imprime()
    parceiro_2.imprime()

    print(
        "\ndoravante denominados(as) PARCEIROS(AS),\ncelebram o presente Contrato de "
        "Parceria Empresarial, sob regência do CÓDIGO CIVIL (Lei nº 10.406/02) e "
        "mediante as cláusulas e condições adiante estipuladas que, voluntariamente, "
        "aceitam e outorgam:"
    )