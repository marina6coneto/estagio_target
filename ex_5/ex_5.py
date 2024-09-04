'''
 5) Escreva um programa que inverta os caracteres de um string. 
 IMPORTANTE: 
 a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
 b) Evite usar funções prontas, como, por exemplo, reverse; 
'''
def inverter_string(texto):
  '''
  Inverte os caracteres de uma string.
  '''

  texto_invertido = ''
  for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]
  return texto_invertido

# Opção 1: String definida no código
texto = 'Olá, mundo!'
texto_invertido = inverter_string(texto)
print(f'String original: {texto}')
print(f'String invertida: {texto_invertido}')

# Opção 2: Entrada do usuário
texto = input('Digite uma string: ')
texto_invertido = inverter_string(texto)
print(f'String original: {texto}')
print(f'String invertida: {texto_invertido}')