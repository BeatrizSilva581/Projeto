
cadastrodelivro=[]

def cadastrar_livro():
    print('-' * 30)
    print(' ' * 5 + '📚Cadastro de Livro ')
    print('-' * 30)
    titulo =str(input(Funcoes.cor_texto('🔖| Coloque o titulo do livro: ', "azul")))
    genero=str(input(Funcoes.cor_texto('📖| Digite o gênero: ', "azul")))
    autor=str(input(Funcoes.cor_texto('📝| Qual é o autor: ', "azul")))
    mesdaleitura=str(input(Funcoes.cor_texto('🗓️| Qual foi o mês da leitura do livro: ', "azul")))
    cadastro={
        'titulo': titulo,
        'genero': genero,
        'autor': autor,
        'mesdaleitura': mesdaleitura,
        'realizada':False
    }
    cadastrodelivro.append(cadastro)
    print('😎 === Livro cadastrado com sucesso!! === 😎 \n')

def consultar_livro():
    if len(cadastrodelivro)==0:
        print(Funcoes.cor_texto(' 😓 Nenhum livro cadastrado..! \n', "amarelo"))
        return
    numero = 1
    for livro in cadastrodelivro:
        status = ' '
        if livro['realizada']==True:
            status= '✅ Discutido'
        else:
            status= '❌ Não discutido'

        print(f'[{numero}] titulo: {livro['titulo']} | genero: {livro['genero']} | '
              f'Autor: {livro['autor']} | Mês da leitura: {livro['mesdaleitura']} | Status: {status}')
        numero+=1
    print()

def buscar_livro():
    tema=str(input('Buscar por titulo ou gênero: ')).lower()
    encontrados=[]
    for livro in cadastrodelivro:
        if (tema in livro ['titulo'].lower()) or (tema in livro['genero'].lower()):
            encontrados.append(livro)

    if len(encontrados) == 0:
        print(Funcoes.cor_texto('🤔 Nenhum cadastro encontrado. \n', "amarelo"))
        return
    numero = 1
    for livro in encontrados:
        status = ' '
        if livro['realizada'] == True:
            status = '✅ Discutido'
        else:
            status = '❌ Não discutido'

        print(
            f'[{numero}] Titulo: {livro['titulo']} | Gênero: {livro['genero']} | Autor: {livro['autor']} | Status: {status}')
        numero += 1
    print()

def status_atualizar():
     consultar_livro()
     if len(cadastrodelivro) == 0:
         return
     try:
        numero = int(input('Digite o número do livro para marcar como realizado:'))
        indice = numero - 1


        if numero <= len(cadastrodelivro):
             cadastrodelivro[indice]['realizada'] = True
             print(Funcoes.cor_texto('✅ Livro marcado como discutido ✅\n', "verde"))
        else:
             print(Funcoes.cor_texto('🛹 Número inválido 🛹\n', "vermelho"))
     except ValueError:
         print(Funcoes.cor_texto('🛹Entrada invalida. Digite um número🛹\n', "vermelho"))

def exibir_menu():
    while True:
        print(Funcoes.cor_texto("✨✨✨📚  === 📖 Clube do Livro ===  📚✨✨✨", "roxo"))
        print(Funcoes.cor_texto("1. ✍️📖💾 Cadastrar de Livro", "verde"))
        print(Funcoes.cor_texto("2. 🔎 Visualização de Livros", "verde"))
        print(Funcoes.cor_texto("3. 📅📚 Busca de Livro", "verde"))
        print(Funcoes.cor_texto("4. 🔄 Atualizar Status", "verde"))
        escolha=str(input("❓ Escolha uma opção: "))
        if escolha =="1":
            cadastrar_livro()
        elif escolha=="2":
            consultar_livro()
        elif escolha=="3":
            buscar_livro()
        elif escolha=="4":
            status_atualizar()
        else:
            print(Funcoes.cor_texto("⚠️❌❗ Opção Inválida. Tente novamente. \n", "vermelho"))

import Funcoes
exibir_menu()