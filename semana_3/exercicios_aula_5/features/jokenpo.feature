# language:pt
Funcionalidade: Jokenpo
    Dados 2 capitães de times de futebol
    Eles devem jogar jokenpo
    Para decidir quem escolherá o primeiro jogador

Cenário: Capt. A e Capt. B empatam
    Quando C.A jogar "papel" e C.B jogar "papel"
    Então gera empate

Cenário: Capt. A ganha de Capt. B
    Quando C.A jogar "Papel" e C.B jogar "Pedra"
    Então "Papel" ganha

#To run: behave (Caminho do .feature) ou python3 -m behave (caminho do .feature)
