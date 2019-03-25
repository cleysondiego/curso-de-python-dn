# language:pt
Funcionalidade: Jokenpo
    Dados 2 capitães de times de futebol
    Eles devem jogar jokenpo
    Para decidir quem escolherá o primeiro jogador

Cenário: Capt. A e Capt. B empatam
    Quando C.A jogadr "papel" e C.B jogar "papel"
    Então gera empate

Cenário: Capt. A ganha de Capt. B
    Quando C.A jogar "papel" e C.B jogar "pedra"
    Então "papel" ganha de "pedra"
    então C.A ganha