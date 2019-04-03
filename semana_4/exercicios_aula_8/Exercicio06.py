class TV:
    def __init__(self, canal: int, volume: int):
        self.canal = canal
        self.volume = volume

    def alterar_volume(self, novo_volume):
        if novo_volume > 100 or novo_volume < 0:
            print('Não é possivel alterar para o volume desejado.')
        else:
            self.volume = novo_volume

    def alterar_canal(self, novo_canal):
        if novo_canal > 30 or novo_canal < 0:
            print('Canal inexistente!')
        else:
            self.canal = novo_canal


if __name__ == '__main__':
    minha_tv = TV(3, 60)
    print(f'A televisão está no canal {minha_tv.canal}')
    print(f'A televisão está com o volume {minha_tv.volume}')
    minha_tv.alterar_volume(30)
    minha_tv.alterar_canal(30)
    print(f'A televisão está no canal {minha_tv.canal}')
    print(f'A televisão está com o volume {minha_tv.volume}')
