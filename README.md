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

## Project Structure

- `solucao.py`: Main source code with all required functions and classes.
- `README.md`: Project documentation and team information.


 ## Results for initial state “2_3541687”
| Algorithm           | Time (s)  | Expanded Nodes | Cost             |
| ------------------- | --------- | -------------- | ---------------- |
| A\* Hamming         | 0.1141    | 13.506         | 23               |
| A\* Manhattan       | 0.0194    | 1.830          | 23               |
| A\* New Heuristic   | 0.0197    | 1.830          | 23               |
| BFS                 | 1.2399    | 117.263        | 23               |
| DFS                 | 0.0682    | 14.626         | 14.571           |

