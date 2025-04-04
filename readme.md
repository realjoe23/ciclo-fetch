# Ciclo Fetch - Descripción del Proyecto

Este proyecto implementa un **ciclo Fetch** básico como parte de una arquitectura simplificada de computadora. El sistema se compone de los siguientes módulos:

- **Program Counter (PC)**  
- **Memoria de Instrucciones**  
- **ALU (Unidad Aritmética Lógica)**  

##Descripción del Ciclo Fetch

El **ciclo Fetch** es el primer paso en la ejecución de una instrucción. En esta etapa, el sistema recupera la instrucción ubicada en la dirección señalada por el *Program Counter* desde la memoria de instrucciones, y luego actualiza el PC para apuntar a la siguiente instrucción.

### Componentes

#### 🧠 Program Counter (PC)
- Registra la dirección de la próxima instrucción a ejecutar.
- Se inicializa en 0.
- Se incrementa en pasos de **4 en 4** (para simular instrucciones de 4 bytes).
- Su salida se conecta a la **memoria de instrucciones** y a una **ALU** especial.

#### 💾 Memoria de Instrucciones
- Memoria con capacidad para **1000 bytes**.
- Cada celda de memoria almacena **1 byte**.
- Se accede mediante la dirección que entrega el **PC**.
- Durante el ciclo Fetch, se leen **4 bytes consecutivos** para formar una instrucción completa (simulando una instrucción de 32 bits).

#### ➕ ALU (Unidad Aritmética Lógica)
- Encargada de sumar **4** a la salida del **PC**.
- Su salida se retroalimenta al **PC** para actualizar su valor en cada ciclo.

## 📋 Ejecución del Ciclo

1. **Lectura de dirección desde el PC**:  
   Se obtiene la dirección actual donde se encuentra la próxima instrucción.

2. **Lectura de instrucción desde memoria**:  
   Se leen 4 bytes a partir de la dirección indicada por el PC desde la memoria de instrucciones.

3. **Incremento del PC**:  
   La ALU suma 4 al valor actual del PC.

4. **Actualización del PC**:  
   El nuevo valor del PC se guarda para apuntar a la siguiente instrucción.

Este ciclo se repite continuamente, instrucción por instrucción.
