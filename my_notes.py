# Escritura de archivo de texto
with open("my_notes.txt", "w") as file:
    # Escribir notas personales en el archivo
    file.write("Nota 1: Estoy feliz de ser estudiante de la UEA.\n")
    file.write("Nota 2: Ha sido muy bonita la experiencia de aprender a programar.\n")
    file.write("Nota 3: Seguire adquiriendo conocimientos en progrmacion.\n")

# Cierra el archivo después de escribir
file.close()

# Lectura de archivo de texto
with open("my_notes.txt", "r") as file:
    # Leer el contenido del archivo línea por línea
    for line in file:
        # Mostrar cada línea leída en la consola
        print(line.strip())  # .strip() elimina los caracteres de nueva línea al final

