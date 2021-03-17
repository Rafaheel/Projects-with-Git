km = float(input('Informe a kilometragem utilizada: '))
dias_uso = float(input('Informe a quantidade de dias utilizados: '))
custo_diaria = 60 * dias_uso
custo_km = 0.15 * km
total_pagar = custo_diaria + custo_km
print(f'O total a pagar pelo serviço é de R$ {total_pagar}')