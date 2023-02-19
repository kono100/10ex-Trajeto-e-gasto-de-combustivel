
''' Construa uma função que receba 2 parâmetros, sendo: a distância percorrida por um veículo 
em uma viagem e o consumo de combustível (em litros) gastos nesse trajeto. Calcule e 
retorne o consumo médio de combustível desta viagem. '''


dist = float(input('Digite a distância total: '))
litros = float(input('Quantos litros foram gastos no percurso: '))

media = dist/litros
print(f'A média gasta no percurso foi de {media:.2f} litros')

