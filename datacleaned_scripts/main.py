import csv

input_file = 'dataset.csv'
output_file = 'dataset_p1.csv'

# Define el patrón de fila que deseas eliminar
pattern = ',,,,,,,,,,,,,,,,'

# Abre el archivo de entrada y el archivo de salida con el encoding adecuado
with open(input_file, 'r', encoding='utf-8', errors='ignore', newline='') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Itera sobre cada fila en el archivo de entrada
    for row in reader:
        # Convierte la fila en una cadena y verifica si contiene el patrón
        row_str = ','.join(row)
        if pattern not in row_str:
            writer.writerow(row)

print(f'Filas con "{pattern}" eliminadas y guardadas en {output_file}')
