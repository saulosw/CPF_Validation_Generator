import random
import random

geral_question = input("Pressione [G] para Gerar um CPF aleatório \n"
                       "Pressione [V] para Validar um CPF\n"
                       ": ")
#Validação-------------------------------------------**
if geral_question == "V":
    CPF_total = input("Digite seu CPF: ") \
        .replace(" ","") \
        .replace(".","") \
        .replace("-","")

    print(f"Seu CPF é {CPF_total}")
    CPF_first_digit = CPF_total[:9]

    resultado_digito_1 = 0
    resultado_digito_2 = 0
    count = 10

    for digit in CPF_first_digit:
        resultado_digito_1 += int(digit) * count
        count -= 1

    #Resultado1
    digit = (resultado_digito_1 * 10) % 11
    digit = digit if digit <= 9 else 0

    CPF_first_digit_two = CPF_first_digit + str(digit)
    count_two = 11

    for digit_2 in CPF_first_digit_two:
        resultado_digito_2 += int(digit_2) * count_two
        count_two -= 1

    #Resultado2
    digit_2 = (resultado_digito_2 * 10) % 11
    digit_2 = digit_2 if digit_2 <= 9 else 0

    print(f"O resultado do primeiro digito é: {digit}")
    print(f"O resultado do segundo digito é: {digit_2}")

    calculo_cpf = f"{CPF_first_digit}{digit}{digit_2}"

    if calculo_cpf == CPF_total:
        print(f"O CPF {CPF_total} é válido!!")
    else:
        print("CPF enviado é inválido!!")

#Geração de Valor-------------------------------------------**
if geral_question == "G":
    nine_digit = ""
    for value in range(11):
        nine_digit += str(random.randint(0, 9))

    CPF_first_digit = nine_digit[:9]

    resultado_digito_1 = 0
    resultado_digito_2 = 0
    count = 10

    for digit in CPF_first_digit:
        resultado_digito_1 += int(digit) * count
        count -= 1

    #Calculo1
    digit = (resultado_digito_1 * 10) % 11
    digit = digit if digit <= 9 else 0

    CPF_first_digit_two = CPF_first_digit + str(digit)
    count_two = 11

    for digit_2 in CPF_first_digit_two:
        resultado_digito_2 += int(digit_2) * count_two
        count_two -= 1

    #Calculo2
    digit_2 = (resultado_digito_2 * 10) % 11
    digit_2 = digit_2 if digit_2 <= 9 else 0

    calculo_cpf = f"{CPF_first_digit}{digit}{digit_2}"

    print(calculo_cpf)
