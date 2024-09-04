# Análise de Faturamento Diário de uma Distribuidora

Este programa em Python analisa os dados de faturamento diário de uma distribuidora e calcula:

- O menor valor de faturamento ocorrido em um dia do mês.
- O maior valor de faturamento ocorrido em um dia do mês.
- O número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

## Descrição

O programa utiliza um arquivo JSON que contém o faturamento diário da distribuidora. Ele lê os dados, calcula o menor e o maior valor de faturamento, a média mensal (ignorando dias sem faturamento) e conta quantos dias o faturamento diário superou a média.

## Fonte de Dados

Os dados de faturamento estão armazenados em um arquivo `JSON` chamado `faturamento_diario.json`. O arquivo deve estar no mesmo diretório do script Python ou em um diretório especificado no caminho.