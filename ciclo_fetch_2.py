import os
import textwrap

FuncionBinario = {
    "AND": "100100",
    "NOP": "000000",
    "ADD": "100000",
    "OR":  "100101",
    "SUB": "100010",
    "SLT": "101010",
    "SW":  "101011",
    "LW":  "100011",
    "J":   "000010",
}

tipoInstruccion = {
    "AND": "R",
    "NOP": "R",
    "ADD": "R",
    "OR":  "R",
    "SUB": "R",
    "SLT": "R",
    "SW":  "I",
    "LW":  "I",
    "J":   "J",
}

def instruccion_a_binario(numero):
    return f"{int(numero):05b}"

def mostrar_contenido(archivo):
    """ Muestra el contenido del archivo en la consola """
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
        print("\nContenido del archivo:")
        print(contenido)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def convertir_a_binario(archivo):
    """ Convierte el archivo ASM a binario """
    if not archivo:
        print("¡Atención! Selecciona un archivo primero.")
        return

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        
        resultados = []
        for linea in lineas:
            partes = linea.split()
            instruccion = partes[0]
            if instruccion in tipoInstruccion:
                mnemonico = tipoInstruccion[instruccion]
                instruct = FuncionBinario[instruccion]
                if "R" in mnemonico:
                    if "000000" in instruct:
                        cadena = "00000000000000000000000000000000"
                    else:
                        Rd          = partes[1].replace("$", "").strip()
                        Rs          = partes[2].replace("$", "").strip()
                        Rt          = partes[3].replace("$", "").strip()
                        op =    "000000"
                        shamt = "00000"
                        RD = instruccion_a_binario(Rd)
                        RS = instruccion_a_binario(Rs)
                        RT = instruccion_a_binario(Rt)
                        cadena = op +  RS + RT + RD + shamt + instruct
                        
                
                if "I" in mnemonico:
                    op = instruct
                    Rs = partes[1].replace("$", "").strip()
                    Rt = partes[2].replace("$", "").strip()
                    ofset = partes[3].replace("#", "").strip()
                    Offset = f"{int(ofset):016b}"
                    RS = instruccion_a_binario(Rs)
                    RT = instruccion_a_binario(Rt)
                    cadena = op + RS + RT + Offset

                if "J" in mnemonico:
                    op = instruct
                    index = partes[1].replace("#", "").strip()
                    Index = f"{int(index):026b}"
                    cadena = op + Index

                palabra = [cadena[i:i+8] for i in range(0, len(cadena), 8)]
                resultados.append(palabra)

        ruta_salida = archivo.replace(".asm", "_binario.txt")
        with open(ruta_salida, "w", encoding="utf-8") as f:
            for palabra in resultados:
                for bytes in palabra:
                    f.write(bytes + "\n")
        
        print(f"\nArchivo binario guardado en: {ruta_salida}")

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

def menu():
    """ Muestra el menú interactivo en consola """
    while True:
        print("\n============================")
        print("|Conversor ASM a Binario")
        print("|============================")
        print("|1. Seleccionar archivo ASM")
        print("|2. Ver contenido del archivo")
        print("|3. Convertir archivo a Binario")
        print("|4. Salir")
        print("============================")
        
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            archivo = input("Introduce la ruta del archivo ASM: ")
            if os.path.exists(archivo) and archivo.endswith(".asm"):
                print(f"Archivo {archivo} seleccionado correctamente.")
            else:
                print("¡Error! El archivo no existe o no es un archivo .asm.")
                archivo = None

        elif opcion == "2":
            if archivo:
                mostrar_contenido(archivo)
            else:
                print("Primero selecciona un archivo.")

        elif opcion == "3":
            if archivo:
                convertir_a_binario(archivo)
                
            else:
                print("Primero selecciona un archivo.")
        
        elif opcion == "4":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 4.")

if __name__ == "__main__":
    archivo = None  # Inicialmente no hay archivo seleccionado
    menu()
