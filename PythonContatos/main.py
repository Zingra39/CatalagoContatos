import re

#VARIAVIES GLOBAIS
lista_contatos = []

contato_teste = {}
contato_teste['nome'] = "Teste"
contato_teste['telefone'] = "19972677343"
contato_teste['email'] = "teste@gmail.com.br"
contato_teste['favorito'] = False

lista_contatos.append(contato_teste)


#FUNÇÕES DE VERIFICAÇÃO
def verifica_email():
  cond = True
  while cond:
    email = input("Conta de e-mail: ").strip()
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(regex_email, email):
        cond == False
        return email
    else:
      print("\n[E-MAIL INAVLIDO] Este e-mail apresenta formato invalido")

def verifica_nome():
  cond = True
  
  while cond:
    nome = input("Nome do Contato: ").strip()
    regex_nome = r'[0-9._%+-@]'
    if re.search(regex_nome,nome):
      print("\n[NOME INVALIDO] Evite usar simbolos e numeros")
    else:
      cond == False
      return nome
 
def verifica_telefone():
  cond = True
  while cond:
    telefone = input("Numero do telefone: ").strip()
    regex_telefone = r'[a-zA-Z._%+]'
    if len(telefone) == 11 and not re.search(regex_telefone, telefone):
      return telefone
    else:
      print("\n[TELEFONE INVALIDO] Telefone apresenta formato errado")

def verifica_id():
  while True:
    try:
      indice = int(input("Informe o ID do contato: "))
      return lista_contatos[indice-1]
    except:
      print("\n[ERROR] Contato não existe na lista, tente outro ID")


#FUNÇÕES DE OPERAÇÕES DO SISTEMA
def tela_inicial():
    print("Lista de Contatos")
    print("==================================")
    print("ESCOLHA UM OPÇÃO:")
    print("""
          [1] Cadastrar contato\n
          [2] Listar contatos\n
          [3] Atualizar contato\n
          [4] Favoritar contato\n
          [5] Deletar contato\n
          [6] Listar Favoritos\n\n
          
          [0] Sair
          """)

def inserir_contato():
  print("\n\nCadastrar contato")
  print("====================================")
  
  contato = {}
  contato['favorito'] = False
  contato['nome'] = verifica_nome()
  contato['email'] = verifica_email()
  contato['telefone'] = verifica_telefone()
  
  lista_contatos.append(contato)
  print("Contato cadatrado com sucesso")
  
  print("\n\n")
  input("Pressione enter para continuar")
  
def listar_contatos(favoritos):
  
  title = "Listar Favoritos" if favoritos else "Listar Contatos"
  
  print(f"\n\n{title}")
  print("====================================")
  
  if favoritos:
    for i in lista_contatos:
      if i['favorito'] == True:
        print(f'{lista_contatos.index(i) + 1}.Nome: {i['nome']} \n Telefone: {i['telefone']} \n E-mail: {i['email']} \n Favorito: [{"Sim" if i['favorito'] else "Não"}] \n\n')
  else:
    for i in lista_contatos:
      print(f'{lista_contatos.index(i) + 1}.Nome: {i['nome']} \n Telefone: {i['telefone']} \n E-mail: {i['email']} \n Favorito: [{"Sim" if i['favorito'] else "Não"}] \n\n')

  input("Pressione enter para continuar")
  
def favoritar_contato():
  listar_contatos(False)
  print("\n\nQual contato deseja favoritar")
  print("====================================")
  
  contato = verifica_id()
  contato['favorito'] = True
  
  print("Contato favoritado com sucesso\n\n")
  input("Pressione enter para continuar")
  
def atualizar_contato():
  listar_contatos(False)
  
  contato = verifica_id()
  
  contato['nome'] = verifica_nome()
  contato['telefone'] = verifica_telefone()
  contato['email'] = verifica_email()
  
  print("Contato foi alterada com sucesso\n\n")
  input("Pressione enter para continuar")
  
def deletar_contato():
  listar_contatos(False)
  
  contato = verifica_id()
  indiceContato = lista_contatos.index(contato)
  
  lista_contatos.pop(indiceContato)
  
  print("Contato deletado com sucesso\n\n")
  input("Pressione enter para continuar")


#LAÇO DE REPETIÇÃO WHILE, QUE IRÁ MANTER O SISTEMA FUNCIONANDO ATÉ O VALOR SER 0
#SWITCH COM AS OPERAÇÕES DESEJAVEIS
while True:
  tela_inicial()
  opcao = input("Escolha uma opção: ")
  if opcao == '1':
    inserir_contato()
  elif opcao == '2':
    listar_contatos(False)
  elif opcao == '3':
    atualizar_contato()
  elif opcao == '4':
    favoritar_contato()
  elif opcao == '5':
    deletar_contato()
  elif opcao == '6':
    listar_contatos(True)
  elif opcao == '0':
    break
  else:
    print("Opção Invalida\n\n")
    input("Pressione enter para continuar")
