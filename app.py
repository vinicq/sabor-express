
import os

restaurantes = [{'nome': 'Lasanha', 'categoria': 'Italiana', 'ativo': True}, 
                {'nome': 'Pizza', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Praça', 'categoria': 'Brsileira', 'ativo': False}]

def exibir_nome_do_programa():
      """
      Exibe o nome do programa com formatação estilizada no terminal.

      Outputs:
      - Mostra uma representação gráfica do nome do programa usando caracteres ASCII.
      """
      print("""
            
      ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
      ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
      ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
      ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
      ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
      ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
            """)

def exibir_opcoes():
      """
      Exibe as opções disponíveis no menu principal.

      Outputs:
      - Mostra uma lista numerada com as seguintes opções no terminal:
            1. Cadastrar restaurante
            2. Listar restaurante
            3. Alternar estado do restaurante
            4. Sair
      """
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Alternar estado do restaurante')
      print('4. Sair\n')

def finalizar_app():
      """
      Finaliza o aplicativo exibindo uma mensagem de saída.

      Outputs:
      - Exibe o subtítulo "Saindo do sistema..." formatado no terminal.
      """
      exibir_subtitulo('Saindo do sistema...')
      
def opcao_invalida():
      """
      Notifica o usuário sobre uma opção inválida e retorna ao menu principal.

      Inputs:
      - Nenhum input direto, mas aguarda o usuário pressionar qualquer tecla para continuar.

      Outputs:
      - Exibe uma mensagem indicando que a opção selecionada é inválida.
      - Pausa a execução até o usuário pressionar uma tecla.
      - Chama a função `main()` para retornar ao menu principal.
      """
      print('Opção inválida!\n')
      input('Digite uma tecla para voltar ao menu principal')
      main()

def voltar_ao_menu_principal():
      """
      Retorna ao menu principal após uma pausa.

      Inputs:
      - Aguarda o usuário pressionar qualquer tecla para continuar.

      Outputs:
      - Chama a função `main()` para retornar ao menu principal.
      """
      input('\nDigite uma tecla para voltar ao menu principal ')
      main()

def exibir_subtitulo(texto):
      """
      Exibe um subtítulo formatado no terminal.

      Inputs:
      - `texto`: Uma string que será exibida como subtítulo.

      Outputs:
      - Limpa o terminal.
      - Exibe o texto fornecido entre linhas de asteriscos, com espaço adicional ao redor.
      - Adiciona uma linha em branco após o subtítulo.
      """
      os.system('cls')
      linha = '*' * (len(texto) + 4) 
      print(linha)
      print(texto)
      print(linha)
      print()
      
def cadastrar_novo_restaurante():
    """
    Essa função é responsável por Cadastra um novo restaurante.

    Inputs:
    - Solicita ao usuário o nome do restaurante.
    - Solicita ao usuário a categoria do restaurante.

    Outputs:
    - Adiciona o restaurante à lista global `restaurantes` com as seguintes informações:
        - nome: Nome do restaurante fornecido pelo usuário.
        - categoria: Categoria do restaurante fornecida pelo usuário.
        - ativo: Estado inicial definido como `False`.
    - Exibe uma mensagem confirmando o cadastro.
    """
    exibir_subtitulo('Cadastro de novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input('Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    """
    Essa função é responsável por Lista os restaurantes cadastrados.

    Inputs:
    - Utiliza a lista global `restaurantes`, que contém dicionários com informações dos restaurantes.

    Outputs:
    - Exibe uma tabela com os seguintes campos:
        - Nome do restaurante.
        - Categoria do restaurante.
        - Estado (Ativo ou Inativo).
    - Retorna ao menu principal após a exibição.
    """
    exibir_subtitulo('Listagem de restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Estado'.ljust(20)}')
    for restaurante in restaurantes:
          nome_restaurante = restaurante['nome']
          categoria = restaurante['categoria']
          ativo = 'Ativo' if restaurante['ativo'] else 'Inativo' 
          print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') 
          
    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    """
    Essa função é responsável por Alterna o estado (ativo/inativo) de um restaurante cadastrado.

    Inputs:
    - Solicita ao usuário o nome do restaurante que deseja alterar.

    Outputs:
    - Se o restaurante for encontrado:
        - Altera o estado do campo `ativo` (de True para False ou vice-versa).
        - Exibe uma mensagem confirmando a alteração.
    - Se o restaurante não for encontrado:
        - Exibe uma mensagem informando que o restaurante não foi localizado.
    - Retorna ao menu principal após a execução.
    """
    exibir_subtitulo('Alterar estado do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
          if restaurante['nome'] == nome_do_restaurante:
                restaurante_encontrado = True
                restaurante['ativo'] = not restaurante['ativo']
                print(f'O restaurante {nome_do_restaurante} foi alterado com sucesso!')
                break
    if not restaurante_encontrado:
          print(f'O restaurante {nome_do_restaurante} nao foi encontrado!')
    voltar_ao_menu_principal()

def escolher_opcao():
      """
      Gerencia a escolha do usuário no menu principal.

      Inputs:
      - Solicita ao usuário que insira um número correspondente à opção desejada no menu.

      Outputs:
      - Executa a função correspondente à opção escolhida:
            1. `cadastrar_novo_restaurante`: Cadastra um novo restaurante.
            2. `listar_restaurantes`: Lista os restaurantes cadastrados.
            3. `alternar_estado_do_restaurante`: Alterna o estado de um restaurante.
            4. Finaliza o aplicativo (exibe "Finalizar app").
      - Caso a entrada seja inválida:
            - Exibe uma mensagem de erro.
            - Retorna ao menu principal após o erro.
      """
      try:
            
            opcao_escolhida = int(input('Escolha uma opção: '))
            match opcao_escolhida:
                  case 1:
                        cadastrar_novo_restaurante()
                  case 2:
                        listar_restaurantes()
                  case 3:
                        alternar_estado_do_restaurante()
                  case 4:
                        print('Finalizar app')
                  case _:
                        opcao_invalida()
                        print('Opção inválida!')
      except:
            print('Opção inválida!')
            input('Digite uma tecla para voltar ao menu principal')
            main()



def main():
      """
      Função principal do programa que controla o fluxo inicial.

      Outputs:
      - Limpa o terminal.
      - Exibe o nome do programa.
      - Mostra as opções do menu principal.
      - Aguarda o usuário selecionar uma opção através da função `escolher_opcao`.
      """
      os.system('cls')
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()

if __name__ == '__main__':
      main()
