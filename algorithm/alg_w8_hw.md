# algorithm homework week 8
- SuJinhua 2017201620
## Question 4
### requirements
> There a setup work needed to be optimized so that physicists can quickly calculate the force on each particle.

The naive psedocode whose running time is $\Theta(n^{2})$ is on the following.

```
For j = 1, 2, ..., n
    Initialize Fj to 0
    For i = 1, 2, ..., n
        If i < j then
            Add C*qi*qj/(j-i)**2 to Fj
        Else if i > j then
            Add -C*qi*qj/(j-i)**2 to  Fj
        Endif
    Endfor
    Output Fj
Endfor
```
### Solution

Formula shows that the total force on particle j can be split into two parts, force caused by left particles and force caused by right particle j, which are of symmetry. To make arguments brief, only second part force will be discussed in the following. With property of symmetry, the similar method can also be applied in the first part and it makes no difference on time complexity in the worst case for it just makes the time cost double.
I will take a simple example to demonstrate my main idea. Suppose that there are five particles 1, 2, 3, 4, 5.

| particle no. | total force caused by particles in the right |
| :-- | :--: |
| 1 | $Cq_{1}\times(\frac{q_{2}}{1}+\frac{q_{3}}{4}+\frac{q_{4}}{9}+\frac{q_{5}}{16})$ |
| 2 | $Cq_{2}\times(\frac{q_{3}}{1}+\frac{q_{4}}{4}+\frac{q_{5}}{9})$ |
| 3 | $Cq_{3}\times(\frac{q_{4}}{1}+\frac{q_{5}}{4})$ |
| 4 | $Cq_{4}\times(\frac{q_{5}}{1})$ |

It can be found that in each force term the distance and right part particle number has a stable bias, equalling to force bearing particle number. It is a bit like the convolution. It reminds me to construct polynomial product f(x). 

$f(x) = (\sum_{i = 1}^{n}q_{i}x^{i})\times (\sum_{i = 1}^{n}\frac{x^{i}}{(n+1-i)^{2}}) = g(x)h(x)$

Where the coefficients of the f(x) have an amazing results. The coefficients of $x^{n+2},..,x^{2n}$ respectively equals to force from right part on particle 1, 2, 3, ...

So the problem can be converted into below several subproblems.

- to calculate initial coefficient with coef-represetation with time complexity of $\Theta(n)$
- to get product ceofficient
    + using FFT to get coordinate representation of two polyminal g(x) and h(x)
    + directly get product of h(x_n) and g(x_n) to get the f(x_2n) on coordinate representation
    + we need to change coordinate representation into coefficient representation again. With DFT it is equivalent to the process of changing coefficient representation into coordinate representation, then we could use FFT with time complexity of $\Theta(n\log(n))$

## Question 5 
### requirements
> solving a spefic hidden surface removal problem about finding 'visible' lines of n lines in $\Theta(n\log(n))$.

### Solution

Since all of lines are represented in y = ax + b format and there is no vertical line. It can be easily figured out that when x -> infinite only a will effect the visibility of lines.

First, we use buble-sort for two times to get the biggest a and smallest a and move these two line into visible list V, so other lines are still in L - V. Two round buble-sort only take 2n time cost.

Second, calculate the meeting point of above two lines, (x0,y0) , and calculate y = a * x0 + b for each line in L - V. Use buble-sort for one round and label the biggest y as y_m, we mark this line's parameter like a_m, b_m. Of course we add this line into V.

- when y <= y0, move the line into unvisible list U.
- when y > y0
    + if a > a_m, move the line into right_list R_l.
    + if a < a_m, move the line into left_list L_l.
    + if a = a_m, move the line into U.

Third, repectively find out the meeting point of new line and above two line and we get left meeting point and right meeting point. Then we find out we could repeat the similar procedure of second part. That is to say, we divide it into two seperate subprocess, left part and right part. When dealing with left part, we only check lines in left_list.

Theoratically, we build a recursion algorithm and for each subproblem we can break it into 2 sub-subproblems. So the number of recursion layers is less than $\log_{2}(n)$ and basic operation is to calculate y(x0) and compare it with y_m and a_m. Thankfully, every sublist has no intersect part so in each recursion layer we at most do basic operation for n times. That means the time complexity of my algorithm is $\Theta(n\log(n))$.
