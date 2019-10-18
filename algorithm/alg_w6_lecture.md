# 算法设计第六周课堂笔记
## 矩阵相乘算法
### difficulty: high running time
### method: Strassen's trick

Grade-school method: $\Theta(n^{3})$

Base thought: divide and conquer

Naive try: block matrix method, while using master method, it is still $\Theta(n^{3})$ running time.

In 1969, Strassen put forward a method like divide and conquer for multiplication. In short, he found 8 multiplication can be reduced to 7, using matrix multiplication interior quality.

Relative linear algebra problems: matrix inversion, least square.