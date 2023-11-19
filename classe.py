from dict import *
import random

class Pessoa:
  def __init__(self, nome, matricula):
    self.nome = None
    self.matricula = None

  def login(self):
      
            usuario = input('Você é aluno, líder ou professor?')
            return usuario
       
            
      
class Aluno(Pessoa):
    def __init__(self, nome, matricula, turma, genero):
        super().__init__(nome, matricula)
        self.turma = turma
        self.genero = genero

    def inscricao(self):
        try:
            listaParticipantes = []

            self.genero = input('Qual o seu gênero, masculino ou feminino?').lower()
            self.turma = input('Digite sua turma:').lower()
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
               raise ValueError('Combinação de gênero e turma não suportada')
            
        except Exception as e:
            print(f"Ocorreu um erro durante a inscrição: {e}")
    
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
        super().__init__(nome, matricula)

        self.nome = None
        self.matricula = None

    def logarProf(self):
        self.nome = input('Digite seu nome:')
        self.matricula = input('Digite sua matricula:')
      
    def adicionar_aluno(self):
        try:
            listaParticipantes = []
            genero = input('Digite o gênero do aluno (masculino/feminino): ').lower()
            turma = input('Digite a turma do aluno: ').lower()
            
            if (genero, turma) in turma_dict:
                    lista_file, info_file, participantes_file = turma_dict[(genero, turma)]
                    with open(lista_file, 'r') as fp:
                        lines = len(fp.readlines())

                    self.matricula = input('Digite a matrícula do aluno:')
                    if self.matricula in globals()[info_file]:
                        nome1 = globals()[info_file][self.matricula]
                        nome2 = str(nome1).replace("{", "").replace("}", "")
                        self.nome = nome2.replace('"', '').replace("'", '')
                        if turma == turma:
                            self.nome = repr(self.nome).replace("'", "")
                            with open(lista_file, "a") as file:
                                file.write("1\n")
                            with open(participantes_file, "a") as file:
                                file.write(self.nome + ", " + self.matricula + "\n")
                            print('O aluno é:', self.nome)

                            with open(participantes_file, "r") as arquivo:
                                for linha in arquivo:
                                    self.nome = linha.strip()
                                    listaParticipantes.append(self.nome)
                            print("Você adicionou à lista de participantes", genero)
                        else:
                            print('Turma inválida')
                    else:
                        print('Matrícula inválida')
            else:
                raise ValueError('Combinação de gênero e turma não suportada')
        except Exception as e:
            print(f"Ocorreu um erro ao adicionar o aluno: {e}")
    

    def remover_aluno(self):
        try:
            genero = input('Digite o gênero do aluno (masculino/feminino): ').lower()
            turma = input('Digite a turma do aluno: ').lower()
            matricula = input('Digite a matrícula do aluno: ')

            chave_turma = (genero, turma)
            if chave_turma in turmas_dict:
                arquivo_participantes, _ = turmas_dict[chave_turma]
                with open(arquivo_participantes, "r") as arquivo_inscricoes:
                    linhas = arquivo_inscricoes.readlines()
                with open(arquivo_participantes, "w") as arquivo_inscricoes:
                    for linha in linhas:
                        if matricula not in linha:
                            arquivo_inscricoes.write(linha)
                print(f'O aluno com a matrícula {matricula} foi removido da turma {turma}.')
            else:
                raise ValueError('Essa turma não está cadastrada.')
            
        except Exception as e:
            print(f"Ocorreu um erro ao remover o aluno: {e}")

    def exibirProfessor(self):
        try:
            print('Você deseja ver o andamento das inscrições de todas as turmas ou escolher uma turma específica? (TODAS/ESPECIFICA)')
            escolha = input().upper()

            
            if escolha == 'TODAS':
                for (genero, turma), (arquivo_participantes, info_file) in turmas_dict.items():
                    print(f'INSCRIÇÕES {genero.upper()} - {turma.upper()}')
                    nomes = []
                    with open(arquivo_participantes, "r") as arquivo_inscricoes:
                        for linha in arquivo_inscricoes:
                            nome = linha.strip()
                            nomes.append(nome)
                    print(*nomes, sep=", ")
                    print('\n')

            elif escolha == 'ESPECIFICA':
                print('Você deseja ver o andamento das inscrições de qual turma?')
            
                # Lista de todas as turmas
                lista_turmas = [
                    '2 info matutino',
                    '2 info vespertino',
                    '3 info matutino',
                    '3 info vespertino',
                    '1 edifica a',
                    '1 edifica b',
                    '2 edifica matutino',
                    '2 edifica vespertino',
                    '3 edifica matutino',
                    '3 edifica vespertino',
                    '1 quimica a',
                    '1 quimica b',
                    '2 quimica matutino',
                    '2 quimica vespertino',
                    '3 quimica matutino',
                    '3 quimica vespertino',
                    '1 eletro a',
                    '1 eletro b',
                    '2 eletro matutino',
                    '2 eletro vespertino',
                    '3 eletro matutino',
                    '3 eletro vespertino',
                ]

                print('\n'.join([f'{i + 1}- {turma.capitalize()}' for i, turma in enumerate(lista_turmas)]))
                
                ver_inscricoes = input()
                if ver_inscricoes.isdigit() and 1 <= int(ver_inscricoes) <= len(lista_turmas):
                    
                    turma_selecionada = lista_turmas[int(ver_inscricoes) - 1]
                    mas_or_fem = input('Masculino ou Feminino?')

                    
                    turma_key = (mas_or_fem.lower(), turma_selecionada.lower())

                    if turma_key in turmas_dict:
                        arquivo_participantes, _ = turmas_dict[turma_key]
                        nomes = []
                        with open(arquivo_participantes, "r") as arquivo_inscricoes:
                            for linha in arquivo_inscricoes:
                                nome = linha.strip()
                                nomes.append(nome)
                        print(f'INSCRIÇÕES {mas_or_fem.upper()} - {turma_selecionada.upper()}')
                        print(*nomes, sep=", ")
                    else:
                        print('Essa turma não está cadastrada.')
                else:
                    print('Opção inválida. Selecione um número de turma válido.')

            else:
                raise ValueError('Escolha inválida.')
        
        except Exception as e:
            print(f"Ocorreu um erro ao remover o aluno: {e}")

class Torneio:
    def __init__(self, teams):
        self.teams = teams
        self.chaves_do_torneio = self.criar_chaves()
        self.vencedores_primeira_rodada = []

    def criar_chaves(self):
        random.shuffle(self.teams)
        return [self.teams[i:i + 4] for i in range(0, len(self.teams), 4)]

    def simular_jogos(self, brackets):
        winners = []
        for i, match in enumerate(brackets):
            print(f"\nChave {i + 1}: {match}")
            winner = random.choice(match)
            winners.append(winner)
            print(f"Jogo {i + 1}: Vencedor - {winner}")
        return winners

    def criar_chave_de_um_jogo(self):
        while len(self.vencedores_primeira_rodada) > 1:
            self.vencedores_primeira_rodada = [self.vencedores_primeira_rodada[i:i + 2] for i in range(0, len(self.vencedores_primeira_rodada), 2)]
            self.vencedores_primeira_rodada = self.simular_jogos(self.vencedores_primeira_rodada)
        return self.vencedores_primeira_rodada[0]

    def comecar_torneio(self):
        print("Chaves do Torneio:")
        

        self.vencedores_primeira_rodada = self.simular_jogos(self.chaves_do_torneio)
        print("\nVencedores da Primeira Rodada:")
        print(self.vencedores_primeira_rodada)

        vencedor = self.criar_chave_de_um_jogo()
        print("\nVencedor do Torneio:")
        print(vencedor)

torneio = Torneio(teams)





  


  

