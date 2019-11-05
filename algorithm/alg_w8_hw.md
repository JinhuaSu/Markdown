# algorithms homework week 8
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