from dict import *


class Pessoa:
  def __init__(self, nome, matricula):
    self.nome = None
    self.matricula = None

  def login(self):
    
    usuario = input('Você é aluno, líder ou professor?')
    
    if usuario.upper() == 'ALUNO': 
      print('INSCRIÇÃO JICS VOLEIBOL')
      
      
    elif usuario.upper() == 'PROFESSOR':
      self.nome = input("Digite seu nomee:")
      self.matricula= int(input('Digite sua matricula'))
      
    return usuario
      
class Aluno(Pessoa):
    def __init__(self, nome, matricula, turma, genero):
        super().__init__(nome, matricula)
        self.turma = turma
        self.genero = genero

    def inscricao(self):
        listaParticipantes = []

        self.genero = input('Qual o seu gênero, masculino ou feminino?').lower()
        self.turma = input('Digite sua turma:').lower()

        turma_dict = {
            ("feminino", "2 info matutino"): ("lista_feminino.txt", "info_2_M", "participantes_feminino.txt"),
            ("feminino", "2 info vespertino"): ("listafeminino_info_2_vesp.txt", "info_2_V", "participantes_feminino_2_info_vesp.txt"),
            ("feminino", "3 info matutino"): ("listafeminino_info_3_M.txt", "info_3_M", "participantes_feminino_3_info_M.txt"),
            ("feminino", "3 info vespertino"): ("lista_feminino_3_info_V.txt", "info_3_V", "participantes_feminino_3_info_V.txt"),
            ("feminino", "1 info a"): ("lista_feminino_1_info_A.txt", "info_1_A", "participantes_feminino_1_info_A.txt"),
            ("feminino", "1 info b"): ("lista_feminino_1_info_B.txt", "info_1_B", "participantes_feminino_1_info_B.txt"),
            ("feminino", "1 edifica a"): ("lista_feminino_1_edifica_A.txt", "edif_1_A", "participantes_feminino_1_edifica_A.txt"),
            ("feminino", "1 edifica a"): ("lista_feminino_1_edifica_B.txt", "edif_1_B", "participantes_feminino_1_edifica_B.txt"),
            ("feminino", "2 edifica matutino"): ("lista_feminino_2 edifica_M.txt", "edif_2_M", "particpantes_feminino_2_edifica_M.txt"),
            ("feminino", "2 edifica vespertino"): ("lista_feminino_2_edifica_V.txt", "edfi_2_V", "participantes_feminino_2_edfiica_V.txt"),
            ("feminino", "3 edifica matutino"): ("lista_feminino_3_edifica_M.txt", "edif_3_M", "participantes_feminino_3_edifica_M.txt"),
            ("feminino", "3 edifica vespertino"): ("lista_feminino_3_edifica_V.txt", "edif_3_V", "participantes_feminino_3_edifica_V.txt"),
            ("feminino", "1 quimica a"): ("lista_feminino_1_quim_A.txt", "quim_1_A", "participantes_feminino_1_quim_A.txt"),
            ("feminino", "1 quimica b"): ("lista_feminino_1_quim_B.txt", "quim_1_B", "participantes_feminino_1_quim_B.txt"),
            ("feminino", "2 quimica matutino"): ("lista_feminino_2_quim_M.txt", "quim_2_M", "participantes_feminino_2_quim_M.txt"),
            ("feminino", "2 quimica vespertino"): ("lista_feminino_2_quim_V.txt", "quim_2_V", "participantes_feminino_2_quim_V.txt"),
            ("feminino", "3 quimica matutino"): ("lista_feminino_3_quim_M.txt", "quim_3_M", "participantes_feminino_3_quim_M.txt"),
            ("feminino", "3 quimica vespertino"): ("lista_feminino_3_quim_V.txt", "quim_3_V", "participantes_feminino_3_quim_V.txt"),
            ("feminino", "1 eletro a"): ("lista_feminino_1_eletro_A.txt", "elet_1_A", "participantes_feminino_1_eletro_A.txt"),
            ("feminino", "1 eletro b"): ("lista_feminino_1_eletro_B.txt", "elet_1_B", "participantes_feminino_1_eletro_B.txt"),
            ("feminino", "2 eletro matutino"): ("lista_feminino_2_eletro_M.txt", "elet_2_M", "participantes_feminino_2_eletro_M.txt"),
            ("feminino", "2 eletro vespertino"): ("lista_feminino_2_eletro_V.txt", "elet_2_V", "participantes_feminino_2_eletro_V.txt"),
            ("feminino", "3 eletro matutino"): ("lista_feminino_3_eletro_M.txt", "elet_3_M", "participantes_feminino_3_eletro_M.txt"),
            ("feminino", "3 eletro vespertino"): ("lista_feminino_3_eletro_V.txt", "elet_3_V", "participantes_feminino_3_eletro_V.txt"),
            ("masculino", "2 info vespertino"): ("lista_masculino_2_info_V.txt", "info_2_V", "participantes_masculino_2_info_V.txt"),
            ("masculino", "2 info matutino"): ("lista_masculino.txt", "info_2_M", "participantes_masculino.txt"),
            ("masculino", "3 info matutino"): ("lista_masculino_3_info_M.txt", "info_3_M", "participantes_masculino_3_info_M.txt"),
            ("masculino", "3 info vespertino"): ("lista_masculino_3_info_V.txt", "info_3_V", "participantes_masculino_3_info_V.txt"),
            ("masculino", "1 info a"): ("lista_masculino_1_info_A.txt", "info_1_A", "participantes_masculino_1_info_A.txt"),
            ("masculino", "1 info b"): ("lista_masculino_1_info_B.txt", "info_1_B", "participantes_masculino_1_info_B.txt"),
            ("masculino", "1 edifica a"):("lista_masculino_1_edifica_A.txt", "edif_1_A", "participantes_masculino_1_edifica_A.txt"),
            ("masculino", "1 edifica b"): ("lista_masculino_1_edifica_B.txt", "edif_1_B", "participantes_masculino_1_edifica_B.txt"),
            ("masculino", "2 edifica matutino"): ("lista_masculino_2_edifica_M.txt", "edif_2_M", "participantes_masculino_2_edifica_M.txt"),
            ("masculino", "2 edifica vespertino"): ("lista_masculino_2_edifica_V.txt", "edfi_2_V", "participantes_masculino_2_edifica_V.txt"),
            ("masculino", "3 edifica matutino"): ("lista_masculino_3_edifica_M.txt", "edif_3_M", "participantes_masculino_3_edifica_M.txt"),
            ("masculino", "3 edifica vespertino"): ("lista_masculino_3_edifica_V.txt", "edif_3_V", "participantes_masculino_3_edifica_V.txt"),
            ("masculino", "1 quimica a"): ("lista_masculino_1_quim_A.txt", "quim_1_A", "participantes_masculino_1_quim_A.txt"),
            ("masculino", "1 quimica b"): ("lista_masculino_1_quim_B.txt", "quim_1_B", "participantes_masculino_1_quim_B.txt"),
            ("masculino", "2 quimica matutino"): ("lista_masculino_2_quim_M.txt", "quim_2_M", "participantes_masculino_2_quim_M.txt"),
            ("masculino", "2 quimica vespertino"): ("lista_masculino_2_quim_V.txt", "quim_2_V", "participantes_masculino_2_quim_V.txt"),
            ("masculino", "3 quimica matutino"): ("lista_masculino_3_quim_M.txt", "quim_3_M", "participantes_masculino_3_quim_M.txt"),
            ("masculino", "3 quimica vespertino"): ("lista_masculino_3_quim_V.txt", "quim_3_V", "participantes_masculino_3_quim_V.txt"),
            ("masculino", "1 eletro a"): ("lista_masculino_1_eletro_A.txt", "elet_1_A", "participantes_masculino_1_eletro_A.txt"),
            ("masculino", "1 eletro b"): ("lista_masculino_1_eletro_B.txt", "elet_1_B", "participantes_masculino_1_eletro_B.txt"),
            ("masculino", "2 eletro matutino"): ("lista_masculino_2_eletro_M.txt", "elet_2_M", "participantes_masculino_2_eletro_M.txt"),
            ("masculino", "2 eletro vespertino"): ("lista_masculino_2_eletro_V.txt", "elet_2_V", "participantes_masculino_2_eletro_V.txt"),
            ("masculino", "3 eletro matutino"): ("lista_masculino_3_eletro_M.txt", "elet_3_M", "participantes_masculino_3_eletro_M.txt"),
            ("masculino", "3 eletro vespertino"): ("lista_masculino_3_eletro_V.txt", "elet_3_V", "participantes_masculino_3_eletro_V.txt")

            
        }

        genero = self.genero
        turma = self.turma

        if (genero, turma) in turma_dict:
            lista_file, info_file, participantes_file = turma_dict[(genero, turma)]

            with open(lista_file, 'r') as fp:
                lines = len(fp.readlines())

            self.matricula = input('Digite sua matrícula:')
            if self.matricula in globals()[info_file]:
                nome1 = globals()[info_file][self.matricula]
                nome2 = str(nome1).replace("{", "").replace("}", "")
                self.nome = nome2.replace('"', '').replace("'", '')

                if self.turma == turma:
                    self.nome = repr(self.nome).replace("'", "")
                    with open(lista_file, "a") as file:
                        file.write("1\n")
                    with open(participantes_file, "a") as file:
                        file.write(self.nome + ", " + self.matricula + "\n")
                    print('Seu nome é:', self.nome)

                    with open(participantes_file, "r") as arquivo:
                        for linha in arquivo:
                            self.nome = linha.strip()
                            listaParticipantes.append(self.nome)
                    print("Você foi adicionado à lista de participantes", self.genero)
                else:
                    print('Turma inválida')
            else:
                print('Matrícula inválida')
        else:
            print('Combinação de gênero e turma não suportada')


  
    
    #grazi
  

class Lider(Aluno):

  def __init__(self, turma, idade, nome, matricula):
    super().__init__(turma, idade, nome, matricula)


  def exibirInfoLider(self):
    self.matricula = input('Digite sua matricula: ')
    if self.matricula in ListaLider: 
      exibirlider= input("Você deseja ver o andamento das inscricoes da sua turma?")
      if exibirlider.upper() == 'SIM':
        print('INSCRIÇÕES MASCULINAS')
        nomes_masculinos = []
        with open("participantes_masculino.txt", "r") as arquivo:
          for linha in arquivo:
            nome = linha.strip()  
            nomes_masculinos.append(nome)  
            print(nomes_masculinos)
        
        print('\n')
        print('INSCRIÇÕES FEMININAS')
        print('\n')
        nomes_femininos = []
        with open("participantes_feminino.txt", "r") as arquivo:
       
          for linha in arquivo:
            nome = linha.strip()  
            nomes_femininos.append(nome)
            print(*nomes_femininos, sep=", ")
    else: print("Você não é um líder de turma.")

class Professor(Pessoa):
  def __init__(self, nome, matricula):
   super().__init__( nome, matricula)

  def exibirProfessor(self):
    print('Você deseja ver o andamento das inscrições de qual turma?')
    lista= ['''1- 2º INFORMÁTICA MATUTINO''']
    print(' '.join(lista))
    ver_inscricoes = input()
    if ver_inscricoes == '1':
      mas_or_fem = input('Masculino ou Feminino?')
      if mas_or_fem.upper() == 'MASCULINO':
        nomes_masculinos = []
        with open("participantes_masculino.txt", "r") as arquivo:
        # Lê cada linha do arquivo
          for linha in arquivo:
            nome = linha.strip()  # Remove espaços em branco extras
            nomes_masculinos.append(nome)  # Adiciona o nome à lista "nomes"
          print(nomes_masculinos)

      elif mas_or_fem.upper() == "FEMININO":
        nomes_femininos = []
        with open("participantes_feminino.txt", "r") as arquivo:
        # Lê cada linha do arquivo
          for linha in arquivo:
            nome = linha.strip()  # Remove espaços em branco extras
            nomes_femininos.append(nome)  # Adiciona o nome à lista "nomes"
          print(*nomes_femininos, sep=", ")

    else:
      print('essa turma não esta cadastrada.')




  


  

