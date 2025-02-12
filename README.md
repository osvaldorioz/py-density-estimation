El **Kernel Density Estimation (KDE)** es una técnica no paramétrica para estimar la función de densidad de probabilidad (PDF) de una variable aleatoria a partir de una muestra de datos. A diferencia de los histogramas, KDE produce una estimación suave y continua de la densidad, lo que facilita la visualización de la distribución de los datos.

### Cómo funciona:
1. Cada punto de datos se trata como el centro de una función de kernel (normalmente una gaussiana).
2. La densidad estimada en un punto se calcula sumando las contribuciones de los kernels de todos los puntos vecinos, ponderadas según su distancia.

### Usos principales:
- **Detección de anomalías:** Identificar puntos con baja densidad que podrían considerarse atípicos.
- **Visualización de distribuciones:** Entender mejor la distribución subyacente de los datos en análisis exploratorios.
- **Estimación de probabilidades:** Calcular la probabilidad de observar ciertos valores o rangos en los datos.

En resumen, KDE es una herramienta poderosa para el análisis y la visualización de datos cuando se desea evitar suposiciones fuertes sobre la distribución subyacente.
