# Simulador del Campo Eléctrico

Este proyecto permite visualizar el campo eléctrico resultante debido a distintas distribuciones de carga: anillo, disco y línea finita. La interfaz gráfica permite al usuario configurar parámetros como el radio de la distribución y la posición en el eje \(x\) de un punto \(P\). El resultado se muestra gráficamente y se proporciona el valor del campo eléctrico en \(N/C\).

## Requisitos

- Python 3.8 o superior.
- Bibliotecas externas: `numpy`, `matplotlib`, `scipy`, `tkinter`. Puedes instalar todas con:
  ```bash
  pip install numpy matplotlib scipy tk

## Inicialización

1. Clona este repositorio en tu computadora local o descarga los archivos fuente.
2. Asegúrate de tener todas las bibliotecas mencionadas en "Requisitos" instaladas.
3. Navega hasta la carpeta del proyecto en tu terminal o línea de comandos.

## Correr el Proyecto

Desde la línea de comandos o terminal, simplemente ejecuta:
   
   ```bash
   python [nombre-del-archivo-principal].py
   ```


Por supuesto, reemplaza `[nombre-del-archivo-principal]` con el nombre del archivo Python principal que contiene la interfaz gráfica y las funciones de cálculo.

## Uso

1. **Selección de Distribución de Carga**: Elige entre "Anillo", "Disco", o "Línea finita" como tu distribución de carga.
2. **Configuración de Parámetros**:
   - **Radio**: Ajusta el radio de la distribución de carga utilizando el slider.
   - **Distancia en X**: Ajusta la posición del punto \(P\) en el eje \(x\) usando el slider.
3. **Visualización**:
   - Haz clic en el botón "Graficar" para visualizar la distribución de carga, el punto \(P\), y la dirección y magnitud del campo eléctrico en ese punto.
   - Observa el título del gráfico para ver el valor del campo eléctrico en \(N/C\).

