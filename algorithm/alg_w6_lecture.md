# 算法设计第六周课堂笔记
## 矩阵相乘算法
### difficulty: high running time
### method: Strassen's trick

Grade-school method: $\Theta(n^{3})$

Base thought: divide and conquer

Naive try: block matrix method, while using master method, it is still $\Theta(n^{3})$ running time.

In 1969, Strassen put forward a method like divide and conquer for multiplication. In short, he found 8 multiplication can be reduced to 7, using matrix multiplication interior quality.

Relative linear algebra problems: matrix inversion, least square.

## Convolution and FFT

### Fourier analysis
Any periodic function can be expressed as the sum of a series of sinusoids.

Mainly contribution: make the media signals be easily stored.

$y(t)=\frac{2}{\pi}\sum_{k=1}^{n} \frac{\sinkt}{k}$

### Euler's identity
Sum of sine and cosines = sum of complex exponentials.

### Time domain vs. frequency domain
sampling based on time or frequency, which FFT is used as a dimension reduction method.

### Similiar polynomial: coefficient representation

Multilication (linear convolution). $\Theta(n^{2})$ using brute force.

However, the transformation between two representations cost in $\Theta(n^{2})$ running time.

coefficient representation -FFT-> point value representation -point value multiplication-> point value representation -FFT-> coefficient representation 

FFT only costs $\Theta(n\lg(n))$, where FFT is short for fast fourier transformation.

### Divide and conquer method
Divide into even and odd degree terms.

Divide into low and high-degree terms.

- $A(1) = A_{even}(1) + 1A_{odd}(1)$
- $A(-1) = A_{even}(1) - 1A_{odd}(1)$
- $A(i) = A_{even}(1) + iA_{odd}(1)$
- $A(-i) = A_{even}(1) - iA_{odd}(1)$

