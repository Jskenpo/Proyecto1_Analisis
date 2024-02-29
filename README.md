# Proyecto de Máquina de Turing para la Sucesión de Fibonacci

Este proyecto consiste en la implementación de una Máquina de Turing que simula el cálculo de la sucesión de Fibonacci. La Máquina de Turing es una abstracción teórica de un modelo computacional que puede simular la lógica de cualquier algoritmo computacionalizable.

## Archivos Utilizados

- **FileReader.py**: Este archivo contiene funciones para leer y parsear archivos YAML que representan la configuración de una Máquina de Turing.
- **TMachine.py**: Aquí se define la clase `TuringMachine`, que implementa la lógica de la Máquina de Turing. Además, contiene la implementación de la cinta (`Tape`) y las funciones de transición de la máquina.
- **TTape.py**: Define la clase `Tape`, que representa la cinta de la Máquina de Turing. También contiene códigos de colores para resaltar la posición actual de la cabeza de lectura/escritura.
- **Main.py**: El archivo principal que utiliza las funciones definidas en los otros archivos para ejecutar la Máquina de Turing y calcular la sucesión de Fibonacci.
- **fibonacci_machine.yaml**: Contiene las funciones de transición de la Máquina de Turing para calcular la sucesión de Fibonacci.

## Estructura del Proyecto

- **FileReader.py**: Se encarga de leer un archivo YAML que contiene la configuración de la Máquina de Turing, incluyendo estados, función de transición, etc.
- **TMachine.py**: Define la clase `TuringMachine`, que representa la Máquina de Turing. Contiene métodos para ejecutar la máquina y evaluar cadenas.
- **TTape.py**: Define la clase `Tape` que representa la cinta de la Máquina de Turing. También incluye códigos de colores para resaltar la posición actual de la cabeza de lectura/escritura.
- **Main.py**: Es el punto de entrada del programa. Lee el número de Fibonacci a calcular, crea una instancia de la Máquina de Turing y ejecuta la simulación.
- **fibonacci_machine.yaml**: Contiene las funciones de transición de la Máquina de Turing para calcular la sucesión de Fibonacci.

## Dependencias del proyecto

Antes de ejecutar el proyecto asegúrate de tener instaladas las siguientes dependencias:

1. **Graphviz**: Librería que permite graficar los estados y transiciones de la máquina de turing.
2. **YAML**: Librería de python que opermite la lectura de archivos YAML.

## Ejecución del Proyecto

Para ejecutar el proyecto, sigue estos pasos:

1. Asegúrate de tener instalado Python en tu sistema.
2. Ejecuta el archivo `Main.py`.
3. Ingresa el número de Fibonacci que deseas calcular cuando se solicite.
4. El programa mostrará el resultado tanto en formato decimal como en segundos, además de imprimir la sucesión de Fibonacci en la cinta de la Máquina de Turing.


## Análisis empírico 

En el siguiente documento se detalla el funcionamiento de la máquina de Turing en relación con la sucesión de Fibonacci. Además, se incluye el diagrama de la máquina y se analiza la regresión lineal de la máquina de Turing con diferentes entradas.

<a href= './Proyecto 1.pdf'> Informe de proyecto </a>
