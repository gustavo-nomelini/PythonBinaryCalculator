#------------------------------------------------------------------------------
# Transformações da base Decimal para as bases Binária, Octal e Hexadecimal
# Calculadora entre números representados na base binária
# e representação de Binários em Complemento de Dois
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# TRANSFORMAÇÃO DECIMAL -> BINÁRIO
#------------------------------------------------------------------------------
def decimalParaBinario (decimalOriginal):
    decimal = decimalOriginal #guardar o valor do decimal original pra imprimir
    binarioNumero = ""

    # números binários até 8 bits, sem sinal: os 8 bits representam o número
    # 2ˆ8 = 256 representações de 00000000 até 11 111111
    # em base decimal representa do 0 ao 255 

    while decimal > 0:
        binarioDigito = decimal % 2
        binarioNumero = str(binarioDigito) + binarioNumero
        decimal = decimal // 2

    if decimalOriginal == 0:
        print("O número",decimalOriginal,", em decimal, na base Binária sem sinal com até 8 bits, vale: 0")
    elif(decimalOriginal<0):
        print("Para números negativos na base decimal utilize a representação em Complemento de Dois")
    elif(decimalOriginal>255):
        print("Número decimal inserido fora do alcance 0-255")
    else:  
        print("O número",decimalOriginal, " ,em decimal, na base Binária sem sinal com até 8 bits, vale: "+binarioNumero)
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# TRANSFORMAÇÃO DECIMAL -> OCTAL
#------------------------------------------------------------------------------
def decimalParaOctal():
    decimalOriginal = int(input("Digite o número na base decimal para ser transformado para a base Octal: "))# converter string do input em número
    decimal = abs(decimalOriginal) #além de guardar pra imprimir aceita converter números negativos como strings
    octalNumero = ""
    while (decimal)>0:
        octalDigito = decimal % 8
        octalNumero = str(octalDigito) + octalNumero
        decimal = decimal // 8

    if decimalOriginal == 0:
        print("O número",decimalOriginal,", em decimal, na base Octal vale 0")
    elif(decimalOriginal<0):
        print("O número",decimalOriginal, " , em decimal, na base Octal vale: -" + octalNumero)
    else:
        print("O número",decimalOriginal, " , em decimal, na base Octal vale: " + octalNumero)

    
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# TRANSFORMAÇÃO DECIMAL -> HEXADECIMAL
#------------------------------------------------------------------------------
def decimalParaHexadecimal():
    decimalOriginal = int(input("Digite o número na base decimal para ser transformado para a base Hexadecimal: "))# converter string do input em número
    decimal = abs(decimalOriginal) #além de guardar pra imprimir aceita converter números negativos como strings
    hexadecimalNumero = ""
    hexadecimalDigito = "0123456789ABCDEF"
    while decimal>0:
        restante = decimal % 16
        hexadecimalNumero = hexadecimalDigito[restante] + hexadecimalNumero
        decimal = decimal // 16


    if decimalOriginal == 0:
        print("O número",decimalOriginal,", em decimal, na base Hexadecimal vale 0")
    elif decimalOriginal < 0:
        print("O número",decimalOriginal,", em decimal, na base Hexadecimal é: -"+hexadecimalNumero)
    else:
        print("O número",decimalOriginal,", em decimal, na base Hexadecimal é: "+hexadecimalNumero)
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# SOMA e SUBTRACAO entre dois números na BASE BINÁRIA
#------------------------------------------------------------------------------
def somaBinarios():
    print("Você deseja entrar com:")
    print("1 - Dois números na base Decimal:")
    print("2 - Dois números na base Binária, até 8bits")
    print("---------------------------------------------------")
    opcao = int(input("Entre com a sua opção: "))
    
    if(opcao == 1):
        x = int(input("Digite o número X na base Decimal: "))
        y = int(input("Digite o número Y na base Decimal: "))
        soma = x + y
        print("A soma de",x,"+",y, "vale:", soma)
        if soma == 0:
            decimalParaBinario(soma)
        else:
            print("O número", x,",na base decimal, representa o número:",bin(x)[2:],"na base binária sem sinal")
            print("O número", y,",na base decimal, representa o número:",bin(y)[2:],"na base binária sem sinal")
            print("O valor somado", soma,",na base decimal, representa o número:",bin(soma)[2:],"na base binária sem sinal")


        print("---------------------------------------------------")
    
    elif(opcao == 2):
        # os números binários serão inseridos como strings
        binario1 = input("Digite o número X na base Binária: ")
        binario2 = input("Digite o número Y na base Binária: ")


        # agora devemos converter as strings em inteiros na base decimal
        x = int(binario1,2)
        y = int(binario2,2)
        print("O número",binario1,"na base Binária, representa",x,"na base Decimal")
        print("O número",binario2,"na base Binária, representa",y,"na base Decimal")

        soma = x + y
        somaBin = bin(soma)[2:]
        print("O número",soma,"na base Binária, representa",soma,"na base Decimal")
        print("A soma",somaBin,"na base Binária, representa",soma,"na base Decimal")

        print("---------------------------------------------------")
    else:
        print("Opcao Inválida")
        print("---------------------------------------------------")
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# MULTIPLICAÇÃO entre dois números na BASE BINÁRIA
#------------------------------------------------------------------------------
def multiplicacaoBinarios():
    print("Você deseja entrar com:")
    print("1 - Dois números na base Decimal")
    print("2 - Dois números na base Binária")
    print("---------------------------------------------------")
    opcao = int(input("Entre com a sua opção: "))
    
    if(opcao == 1):
        x = int(input("Digite o número X na base Decimal: "))
        y = int(input("Digite o número Y na base Decimal: "))
        multiplicacao = x * y
        print("A multiplicação de",x,"*",y, "vale:", multiplicacao)


        if multiplicacao == 0:
            decimalParaBinario(multiplicacao)
        else:
            print("O número", x,",na base decimal, representa o número:",bin(x)[2:],"na base binária sem sinal")
            print("O número", y,",na base decimal, representa o número:",bin(y)[2:],"na base binária sem sinal")
            print("O valor multiplicado", multiplicacao,",na base decimal, representa o número:",bin(multiplicacao)[2:],"na base binária sem sinal")

        print("---------------------------------------------------")
    
    elif(opcao == 2):
        # os números binários serão inseridos como strings
        binario1 = input("Digite o número X na base Binária: ")
        binario2 = input("Digite o número Y na base Binária: ")


        # agora devemos converter as strings em inteiros na base decimal
        x = int(binario1,2)
        y = int(binario2,2)
        
        print("O número",binario1,"na base Binária, representa",x,"na base Decimal")
        print("O número",binario2,"na base Binária, representa",y,"na base Decimal")

        multiplicacao = x * y
        multiplicacaoBin = bin(multiplicacao)[2:]

        print("O número multiplicado na base decimal vale: ",multiplicacao)
        print("A multiplicação na base binária é representada por: ",multiplicacaoBin)

        print("---------------------------------------------------")
    else:
        print("Opcao Inválida")
        print("---------------------------------------------------")
    
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# DIVISÃO entre dois números na BASE BINÁRIA
#------------------------------------------------------------------------------
def divisaoBinarios():
    print("Você deseja entrar com:")
    print("1 - Dois números na base Decimal")
    print("2 - Dois números na base Binária")
    print("---------------------------------------------------")
    opcao = int(input("Entre com a sua opção: "))
    
    if(opcao == 1):
        x = int(input("Digite o número X na base Decimal: "))
        y = int(input("Digite o número Y na base Decimal: "))
        divisao = int(x / y)
        print("A divisão de",x,"/",y, "vale:", divisao)
        
        if divisao == 0:
            decimalParaBinario(multiplicacao)
        else:
            print("O número", x,",na base decimal, representa o número:",bin(x)[2:],"na base binária sem sinal")
            print("O número", y,",na base decimal, representa o número:",bin(y)[2:],"na base binária sem sinal")
            print("O valor dividido", divisao,",na base decimal, representa o número:",bin(divisao)[2:],"na base binária sem sinal")

        print("---------------------------------------------------")
    
    elif(opcao == 2):
        # os números binários serão inseridos como strings
        binario1 = input("Digite o número X na base Binária: ")
        binario2 = input("Digite o número Y na base Binária: ")


        # agora devemos converter as strings em inteiros na base decimal
        x = int(binario1,2)
        y = int(binario2,2)
        
        print("O número",binario1,"na base Binária, representa",x,"na base Decimal")
        print("O número",binario2,"na base Binária, representa",y,"na base Decimal")

        divisao = x / y
        divisaoBin = bin(divisao[2:])

        print("O número dividido na base decimal vale: ",divisao)
        print("A multiplicação na base binária é representada por: ",divisaoBin)

        print("---------------------------------------------------")
    else:
        print("Opcao Inválida")
        print("---------------------------------------------------")

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# BINÁRIO com SINAL: representação de COMPLEMENTO DE DOIS
#------------------------------------------------------------------------------

# a representação de um binário em complemento de dois 
# serve para representar números com sinal, ou seja, inteiros negativos

# em um sistema de 8bits com sinal podemos representar 256 opções
# assim como a representação binária sem sinal
# entretanto dos 8 bits, o primeiro representa o sinal do número(0 positivo / 1 negativo)
# enquanto os outros 7 bits restantes representam o valor
# das 256 opções temos -128 -> +127 (com o 0 dão 256 opções)
def complementoDeDois():
    bits = 8 #definido na especificação do trabalho
    decimalOriginal = int(input("Digite o número na base decimal para ser transformado para a base Binária com sinal, \n utilizando complemento de dois até um número de 8bits (-128 a +127): "))
    decimal = decimalOriginal
    if(decimal<-128 or decimal>127):
        print("Número inserido fora do alcance -128 a +127, 8bits de sinais!")
    elif decimal >= 0:
        # Convertendo um número positivo diretamente
        binario = bin(decimal)[2:]
        # Preenchendo com zeros à esquerda para completar o número de bits
        binarioPositivoCorrigido = binario.zfill(bits)
        print("O número",decimal,"em complemento de dois vale",binarioPositivoCorrigido)
    else:
        # Convertendo o valor absoluto do número negativo
        positivo_binario = bin(abs(decimal))[2:]
        # Preenchendo com zeros à esquerda para completar o número de bits
        positivo_binario = positivo_binario.zfill(bits)
        # Invertendo os bits para calcular o complemento de um
        complemento_de_um = ''.join('1' if bit == '0' else '0' for bit in positivo_binario)
        # Convertendo o complemento de um para um número inteiro
        complemento_de_um_int = int(complemento_de_um, 2)
        # Adicionando um para calcular o complemento de dois
        complemento_de_dois_int = complemento_de_um_int + 1
        # Convertendo de volta para binário
        complemento_de_dois_binario = bin(complemento_de_dois_int)[2:]
        # Preenchendo com zeros à esquerda para completar o número de bits
        binarioNegativoCorrigido = complemento_de_dois_binario.zfill(bits)
        print("O número",decimal,"em complemento de dois vale",binarioNegativoCorrigido)
        
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# MENU DE OPÇÕES DO PROGRAMA 
# SELEÇÃO DA OPÇÃO DO MENU
#------------------------------------------------------------------------------
def selecaoMenu():
    while True:
        print("---------------------------------------------------")
        print("Escolha qual operação entre bases numéricas você deseja realizar:")
        print("1 - Decimal para Binário")
        print("2 - Decimal para Octal")
        print("3 - Decimal para Hexadecimal")
        print("4 - Soma e Subtração entre 2 valores binários")
        print("5 - Multiplicação entre 2 valores binários")
        print("6 - Divisão entre 2 valores binários")
        print("7 - Conversão de Binários para Complemento de Dois")
        print("8 - Interromper execução do programa")
        print("---------------------------------------------------")
        
        try:
            option = int(input("Selecione a opção do menu: "))
        except ValueError:
            print("Opção Inválida!")
            continue

        
        if option == 8:
            print("Encerrando execução do programa!")
            break
        elif option == 1:
            decimalOriginal = int(input("Digite o número na base decimal para ser transformado para a base Binária: "))# converter string do input em número
            decimalParaBinario(decimalOriginal)
        elif option == 2:
            decimalParaOctal()
        elif option == 3:
            decimalParaHexadecimal()
        elif option == 4:
            somaBinarios()
        elif option == 5:
            multiplicacaoBinarios()
        elif option == 6:
            divisaoBinarios()
        elif option == 7:
            complementoDeDois()
        else:
            print("Opção Inválida! Por favor, escolha uma opção entre 1 e 8.")
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# FUNÇÃO PRINCIPAL(MAIN)
#------------------------------------------------------------------------------
selecaoMenu()