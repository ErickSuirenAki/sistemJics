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
      
class Aluno (Pessoa):

  def __init__(self, nome, matricula, turma, genero):
    super().__init__(nome, matricula)
    self.turma = None
    self.genero = None

  def inscricao(self):
    listaParticipantes = []
    with open(r"lista_feminino.txt", 'r') as fp:
        linesFeminino = len(fp.readlines()) 
    with open(r"lista_feminino.txt", 'r') as fp:
        linesMasculino = len(fp.readlines()) 
    with open(r"lista_feminino.txt", 'r') as fp:
        lines = len(fp.readlines()) 
    
    with open(r"lista_feminino.txt", 'r') as fp:
      linesFeminino = len(fp.readlines())
    with open(r"lista_masculino.txt", 'r') as fp:
      linesMasculino = len(fp.readlines())
    with open(r"lista.txt", 'r') as fp:
      lines = len(fp.readlines())
   
    self.turma = input('Digite sua turma:')
    #GRAZI
    self.genero = input('Qual o seu gênero, masculino ou feminino?')
    
    if self.genero == 'feminino':
      if linesFeminino < 6:
        self.matricula = input('Digite sua matrícula:')
        if self.matricula in info_2_M:
          nome1 = info_2_M[self.matricula]
          string = str(nome1)
          nome2 = string.replace("{", "").replace("}", "")
          self.nome = nome2.replace('"', '').replace("'", '')
          if self.turma=='2':
                    
            self.nome = repr(self.nome)
            self.nome = self.nome.replace("'", "")
            with open("lista_feminino.txt","a") as file:
              file.write("1\n")
            with open("participantes_feminino.txt", "a") as file:
              file.write(self.nome + ", "+ self.matricula + "\n")
              print('Seu nome é:', self.nome)
            with open("participantes_feminino.txt", "r") as arquivo:
                        # Lê cada linha do arquivo
              for linha in arquivo:
                self.nome = linha.strip()  # Remove espaços em branco extras
                listaParticipantes.append(self.nome)  # Adiciona o nome à lista "nomes"
            print("Você foi adicionado a lista de participantes", self.genero)

                    
  
  
          else:
            print('turma x')
                
        else:
            print('invalido')  
           
        
         
    elif self.genero == 'masculino':
      if linesMasculino < 6:
          self.matricula = input('Digite sua matrícula:')
          if self.matricula in info_2_M:
            nome1 = info_2_M[self.matricula]
            string = str(nome1)
            nome2 = string.replace("{", "").replace("}", "")
            self.nome = nome2.replace('"', '').replace("'", '')
            
            if self.turma=='2':
              
               self.nome = repr(self.nome)
               self.nome = self.nome.replace("'", "")
               with open("lista_masculino.txt","a") as file:
                 file.write("1\n")
               with open("participantes_masculino.txt", "a") as file:
                 file.write(self.nome + ", "+ self.matricula + "\n")
               print('Seu nome é:', self.nome)
               with open("participantes_masculino.txt", "r") as arquivo:
                # Lê cada linha do arquivo
                for linha in arquivo:
                  self.nome = linha.strip()  # Remove espaços em branco extras
                  listaParticipantes.append(self.nome)  # Adiciona o nome à lista "nomes"
               print("Você foi adicionado a lista de participantes", self.genero)
                      
  
            else:
             print('turma x')
                
          else:
             print('invalido')  
      
    if lines > 5 :
      print("Limite de participantes atingido")
    
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




  


  

