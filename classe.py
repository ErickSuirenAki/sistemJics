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

        turma_dict = {
            ("feminino", "2 info matutino"): ("lista_feminino.txt", "info_2_M", "participantes_feminino.txt"),
            ("feminino", "2 info vespertino"): ("listafeminino_info_2_vesp.txt", "info_2_V", "participantes_feminino_2_info_vesp.txt"),
            ("feminino", "3 info matutino"): ("listafeminino_info_3_M.txt", "info_3_M", "participantes_feminino_3_info_M.txt"),
            ("feminino", "3 info vespertino"): ("lista_feminino_3_info_V.txt", "info_3_V", "participantes_feminino_3_info_V.txt"),
            ("masculino", "2 info vespertino"): ("lista_masculino_2_info_V.txt", "info_2_V", "participantes_masculino_2_info_V.txt"),
            ("masculino", "2 info matutino"): ("lista_masculino.txt", "info_2_M", "participantes_masculino.txt"),
            ("masculino", "3 info matutino"): ("lista_masculino_3_info_M.txt", "info_3_M", "participantes_masculino_3_info_M.txt"),
            ("masculino", "3 info vespertino"): ("lista_masculino_3_info_V.txt", "info_3_V", "participantes_masculino_3_info_V.txt")
            
        }

        genero = self.genero.lower()
        turma = self.turma.lower()

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




  


  

