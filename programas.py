from .lp_classes import Retangulo as ret, Ponto


#Questao 3c

def obra ():
    comprimento = input('Insira o comprimento do local em metros: ')
    largura = input('Insira a largura do local em metros: ')

    local = ret(comprimento, largura)

    areaLocal = local.area()
    perimetroLocal = local.perimetro()

    ladoPiso  = float(input('Insira o comprimento do piso em metros: '))
    areaPiso = pow(ladoPiso, 2)

    quantidade_pisos = areaLocal / areaPiso
    quantidadeRodape = perimetroLocal / ladoPiso 


    print (f'serão necessários {quantidade_pisos} pisos e {quantidadeRodape} rodapés para suprir o local')
