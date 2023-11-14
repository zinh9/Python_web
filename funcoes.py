def ler_arquivo():
  with open('arquivo_tarefas.txt', 'r') as arquivo:
    return arquivo.readlines()

def salvar_arquivo(tasks):
  with open('arquivo_tarefas', 'w') as arquivo:
    for tarefa in tasks:
      arquivo.write(f'{tarefa}\n')

def excluir_tarefa(tasks):
  with open('arquivo_tarefas.txt', 'w') as arquivo:
    for tarefa in tasks:
      arquivo.write(f'{tarefa}\n')
