'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês; 
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal. 
IMPORTANTE: 
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média; 
'''
import json

def analise_faturamento(faturamento_diario):
  '''
  Analisa dados de faturamento diário e retorna informações sobre o menor, maior valor e dias acima da média.
  '''
  valores_faturamento = list(faturamento_diario.values())
  menor_valor = min(valores_faturamento)
  maior_valor = max(valores_faturamento)

  media_mensal = sum(valores_faturamento) / len([v for v in valores_faturamento if v > 0])

  dias_acima_media = sum(1 for valor in valores_faturamento if valor > media_mensal)

  return {
    'menor_valor': menor_valor,
    'maior_valor': maior_valor,
    'dias_acima_media': dias_acima_media
  }

with open('ex_3/faturamento_diario.json') as f:
  faturamento_diario = json.load(f)

resultados = analise_faturamento(faturamento_diario)
print(f'Menor valor de faturamento: {resultados['menor_valor']}')
print(f'Maior valor de faturamento: {resultados['maior_valor']}')
print(f'Dias com faturamento acima da média: {resultados['dias_acima_media']}')