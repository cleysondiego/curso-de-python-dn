from behave import when





@when('C.A jogadr "{mao_1}" e C.B jogar "{mao_2}"')
def jogada_igual(context, mao_1, mao_2):
    context.resultado_jogada = jogo_jokenpo(mao_1, mao_2)

@then('gera empate')
def assertiva_jogada_igual(context):
    assert context.resultado_jogada == 'Empate'