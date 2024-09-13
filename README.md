# Generalización de algoritmos de búsqueda estocástica local por medio de métodos de representación conjunta de soluciones

## Contenido

En la carpeta `/source` hay tres _notebooks_ con el código final utilzado en todos los experimentos.
En `/source/medias_ponderadas.ipynb` se encuentra la implementación del algoritmo evolutivo por medias ponderadas (AEMP). Por su parte, `/source/GA.ipynb` y `/source/PSO.ipynb` contienen el código utilzado para ejecutar los algoritmos genéticos y de enjambre de partículas clásicos, mediante las librerías PyGAD y PySwarm.

Se ha medido el rendimiento de los seis algoritmos al enfrentarse a conjuntos de instancias del problema de la cobertura de vérticles (`/vertex_cover_benchmarks`) y del de la mochila (`/knapsack_benchmarks`).

El directorio `/results` contiene los resultados obtenidos, organizados por instancia y algoritmo. Cada fichero contiene los resultados correspondientes a las 20 ejecuciones en formato "elemento de mayor _fitness_", "valor de _fitness_ máximo"

### Carpetas auxiliares

En `/results_latex` hay un archivo para cada instancia con los resultados de todas las ejecuciones de todos los algoritmos en formato `CSV`, para facilitar su comparación y conversión en tabla de `LaTeX`. El `/results_test_no_param` es similar, pero con todos los valores cambiados de signo, pues las herramientas empleadas para realizar _tests_ no paramétricos requerían que los problemas fueran de minimización.

Finalmente, en `/intentos` se pueden ver una serie de intentos auxiliares que finalmente no forman parte del trabajo. Fueron descartados o refactorizados.

## Referencias

