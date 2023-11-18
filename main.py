#2º Informática Matutino
#Erick Batista, Graziele Olecnhi, Mario Yuri, Iarley Raian

#import da classe

from classe import*


#invocação do metodo login da classe Pessoa
login = Pessoa(None, None)
usuario = login.login()

#na classe tem um RETURN que nos retorna o usuário
if usuario.upper() == 'ALUNO': #caso seja aluno, invocamos o metodo de inscrição do aluno
  
  #invocação do metodo inscrição da classe Aluno
  inscrição = Aluno(None,None, None, None)
  inscrição.inscricao()

elif usuario.upper() == 'LIDER': #caso seja lider, invocamos o metodo de inscrição do aluno e o metodo de exibir informações do lider
  
  #invocação do metodo inscrição da classe Aluno e do metodo de exibir informações da Classe
  inscrição = Aluno(None,None, None, None)
  lider = Lider(None, None, None, None)
  inscrição.inscricao()
  lider.exibirInfoLider()


elif usuario.upper() =='PROFESSOR': #caso seja professor  invocamos o metodo de exibir informações do professor
  torneio2 = input("você deseja criar o torneio?")
  if torneio2 == 'sim':
    print(torneio)
    torneio.run_tournament()
  exibirProfessor = Professor(None,None)
  exibirProfessor.exibirProfessor()
  editarturma = input("Vocde seja editar alguma turma: ")
  if editarturma == 'sim':
    escolha = input("Voce deseja adcionar algum aluno?")
    if escolha == "sim":
      exibirProfessor.adicionar_aluno()

else: 
  print('')