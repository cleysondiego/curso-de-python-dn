def le_arquivo(arquivo):
    try:
        abrir = open(f'{arquivo}')
    except FileNotFoundError:
        print('Arquivo não existe!')
    else:
        print(abrir.read())
        abrir.close()
    finally:
        print('Vou executar com erro ou sem')


le_arquivo("exercicio09.txt")
