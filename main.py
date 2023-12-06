from classe import *
login = Pessoa(None, None)

while True:
    usuario = login.login()

    try:
        if usuario.upper() == 'ALUNO':
            inscricao = Aluno(None, None, None, None)
            inscricao.inscricao()

        elif usuario.upper() == 'LIDER':
            lider = Lider(None, None, None, None)
            lider.exibirInfoLider()

        elif usuario.upper() == 'PROFESSOR':
            exibirProfessor = Professor(None, None)
            logar = Professor(None, None)
            logar.logarProf()
            decisao_professor = input("Você deseja ver o andamento das turmas [1], editar as turmas [2], ou gerar boletim[3]")

            if decisao_professor == '1':
                exibirProfessor.exibirProfessor()
            elif decisao_professor == '2':
                escolha = input("Você deseja adicionar algum aluno?")
                if escolha.lower() == "sim":
                    exibirProfessor.adicionar_aluno()
            elif decisao_professor == '3':
                print(torneio)
                torneio.comecar_torneio()

        else:
            raise ValueError('Você não escolheu uma das alternativas existentes. Digite de novo.')

        
        break

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
