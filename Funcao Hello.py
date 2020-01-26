def funcao_hello(nome):
    print('Hello {}!'.format(nome))

def gravar_dados(dados):

    arquivo = open('usuarios.txt', 'r')

    conteudo = arquivo.readlines()
    conteudo.append('\nNovo Usuário\n')
    conteudo.append('Nome: {}\n'.format(dados['nome']))
    conteudo.append('Idade: {}\n'.format(dados['idade']))

    arquivo = open('usuarios.txt', 'w')

    arquivo.writelines(conteudo)

    arquivo.close()

def ler_dados():
    arquivo = open('usuarios.txt', 'r')
    unica_string = arquivo.read()
    arquivo.close()
    return unica_string

funcao_hello('Visual Studio Code')

funcao_hello('GitHub')

funcao_hello('Testando um pool request')

nome = input('Qual o seu nome? ')
idade = input('Qual sua idade? ')
funcao_hello(nome)

dados = {'nome': nome, 'idade': idade}

print('Seu nome é {} e você tem {} anos.'.format(dados['nome'], dados['idade']))

if input('Gravar os dados? (s/n): ') == 's':
    gravar_dados(dados)

if input('Ver registros? (s/n): ') == 's':
    print(ler_dados())
