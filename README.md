# 8-Puzzle A* Solver

This project is a Python implementation of A* search algorithms for solving the 8-puzzle problem. Developed as part of the Artificial Intelligence course at the Federal University of Rio Grande do Sul (UFRGS), it includes two A* variants using the Hamming and Manhattan heuristics.

## University Information

**Course**: Artificial Intelligence  
**Professor**: Joel Luís Carbonera  
**Institution**: Universidade Federal do Rio Grande do Sul (UFRGS)  
**Department**: Departamento de Informática Aplicada

## Contributors

- João Francisco Hirtenkauf Munhoz – 00275634
- Luís Antônio Mikhail Dawa - 00313853
- Mario Augusto Brum da Silveira - 00322868

> Replace the names above with your actual team information.

## Project Structure

- `solucao.py`: Main source code with all required functions and classes.
- `prepara.sh`: Optional script to install additional dependencies.
- `README.md`: Project documentation and team information.

## Dependencies

This project uses **Python 3.12** and the following libraries:

- `numpy`
- `pandas`
- `numba`

To install them using `pip`:

```bash
pip install numpy pandas numba
```

 ## Results
| Algoritmo           | Tempo (s) | Nós Expandidos | Custo da Solução |
| ------------------- | --------- | -------------- | ---------------- |
| A\* Hamming         | 0.1141    | 13.506         | 23               |
| A\* Manhattan       | 0.0194    | 1.830          | 23               |
| A\* Heurística nova | 0.0197    | 1.830          | 23               |
| BFS                 | 1.2399    | 117.263        | 23               |
| DFS                 | 0.0682    | 14.626         | 14.571           |

