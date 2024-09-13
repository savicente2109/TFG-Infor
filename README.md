# Generalización de algoritmos de búsqueda estocástica local por medio de métodos de representación conjunta de soluciones

## Contenido

En la carpeta `/source` hay tres _notebooks_ con el código final utilzado en todos los experimentos.
En `/source/medias_ponderadas.ipynb` se encuentra la implementación del algoritmo evolutivo por medias ponderadas (AEMP). Por su parte, `/source/GA.ipynb` y `/source/PSO.ipynb` contienen el código utilzado para ejecutar los algoritmos genéticos y de enjambre de partículas clásicos, mediante las librerías PyGAD [[1]](#1) y PySwarms [[2]](#2).

Se ha medido el rendimiento de los seis algoritmos al enfrentarse a conjuntos de instancias del problema de la cobertura de vérticles (`/vertex_cover_benchmarks`) [[3]](#3) y del de la mochila (`/knapsack_benchmarks`) [[4]](#4).

El directorio `/results` contiene los resultados obtenidos, organizados por instancia y algoritmo. Cada fichero contiene los resultados correspondientes a las 20 ejecuciones en formato "elemento de mayor _fitness_", "valor de _fitness_ máximo".

### Carpetas auxiliares

En `/results_latex` hay un archivo para cada instancia con los resultados de todas las ejecuciones de todos los algoritmos en formato `CSV`, para facilitar su comparación y conversión en tabla de `LaTeX`. El `/results_test_no_param` es similar, pero con todos los valores cambiados de signo, pues las herramientas empleadas para realizar _tests_ no paramétricos requerían que los problemas fueran de minimización.

Finalmente, en `/intentos` se pueden ver una serie de intentos auxiliares que finalmente no forman parte del trabajo. Fueron descartados o refactorizados.

## Referencias

<a id="1">[1]</a>
Gad, A. F. Pygad: An intuitive genetic algorithm python library. _Multimedia Tools and Applications_, páginas 1–14, 2023.

<a id="2">[2]</a>
Miranda, L. J. V. PySwarms, a research-toolkit for Particle Swarm Optimization in Python. _Journal of Open Source Software_, vol. 3(21), 2018.

<a id="3">[3]</a>
Rossi, R. A. y Ahmed, N. K. The Network Data Repository with Interactive Graph Analytics and Visualization. En _Proceedings of the Twenty-Ninth AAAI Conference on Artificial Intelligence_. 2015.

<a id="4">[4]</a>
Onoue, Y. Repositorio de la librería kplib. 2013. Disponible en [https://github.com/likr/kplib](https://github.com/likr/kplib) (último acceso, 2024).
