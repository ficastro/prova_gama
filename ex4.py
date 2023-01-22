def funcao1(text1, text2):
    return (f'{text1}, {text2}')

def funcao2():
    ent1 = str(input("Digite uma entrada qualquer: "))
    ent2 = str(input("Digite outra entrada: "))

    print ("\n"+funcao1(ent1,ent2))

funcao2()