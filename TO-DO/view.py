from controller import *
import os

sair = 0
while sair == 0:
    os.system("cls")
    print("SOFTWARE DE TO-DO\n1 - Adicionar tarefa \n2 - Listar tarefas \n3 - Alterar tarefa \n4 - Concluir tarefa\n5 - Listar tarefas concluídas\n6 - Excluir tarefas\n7 - Sair")
    opcao = input("Digite a opção desejada.\n-> ")
    match opcao:
        case "1":
            os.system("cls")
            tarefa = input("Digite a tarefa -> ")
            addTarefa = ControllerAdicionarTarefa(tarefa)
            os.system("pause")
        case "2":
            os.system("cls")
            print("Estes são os itens presentes na lista de tarefas: ")
            listarTarefa = ControllerListarTarefa()
            os.system("pause")
        case "3":
            os.system("cls")
            print("Estes são os itens presentes na lista de tarefas:")
            listarTarefa = ControllerListarTarefa()
            indiceAlterar = input("Qual número da tarefa que deseja alterar? ")
            novaDesc = input("Qual a nova descrição da tarefa? ")
            alterarTarefa = ControllerAlterarTarefa(indiceAlterar, novaDesc)
            os.system("pause")
            
        case "4":
            os.system("cls")
            #listarTarefasA = #listar tarefas ativas
            concluirTarefa = input("Qual o número da tarefa que deseja concluir? ")
        case "5":
            os.system("cls")
            print("As tarefas atualmente concluídas são:")
            concluidas = ControllerConcluirTarefa()
            #listarTarefasC = #listar tarefas concluidas
        case "6":
            os.system("cls")
            listarTarefa = ControllerListarTarefa()
            idexcluir = input("Digite o número da tarefa que deseja excluir -> ")
            excluirTarefa = ControllerExcluirTarefa(idexcluir)
            os.system("pause")
        case "7":
            os.system("cls")
            sair = 1
        case _:
            os.system("cls")
            print("Opção inválida")