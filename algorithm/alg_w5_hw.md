# 算法设计作业
- 2019-10-16
- 苏锦华
- 2017201620
## 2-1 Insertion sort on small arrays in merge sort
### Qestion a 
> Show that insertion sort can sort the n=k sublists, each of length k,in $\Theta(nk)$ worst-case time

The python code of insertion is shown in the following.

```py
for sublist in sublists:
    for i in range(1,len(sublist)):
        j = i
        while sublist[i] < sublist[j-1]:
            j -= 1  # base operation
        sublist = sublist[:j] + sublist[i] + sublist[j:i] + sublist[i+1:]
```

The exterior loop will run $n/k$ times and $k$ times for medium part. In worst case, the interior loop will run $(i - 1)$ times, thus $\frac{n}{k}\times\frac{k\times(k-1)}{2}=\Theta(nk)$.
### Question b
> Show how to merge the sublists in $\Theta(n\lg(n/k))$ worst-case time.

The python code of merge-sort is shown in the following.

```py
while len(sublists) > 1:
    sublist_1, sublist_2 = sublists.pop(), sublists.pop()
    i,j = 0,0
    sublist = []
    while i < len(sublist_1) and j < len(sublist_2):
        #base operation
        if sublist_1[i] <= sublist_2[j]:
            sublist.append(sublist_1[i])
            i += 1
        else:
            sublist.append(sublist_2[j])
            j += 1
    if i < len(sublist_1):
        sublist += sublist_1[i:]
    else:
        sublist += sublist_2[j:]
    sublists.insert(0,sublist)
```

For this specific method, we merge 2 every time, so we get $\log_{2}(n/k)$ rounds. For each round, we merge $n$ number in order, thus operating $n\log_{2}(n/k)=\Theta(n\lg(n/k))$ times.

### Question c
> Given that the modified algorithm runs in $\Theta(nk+n\lg(n/k))$ worst-case time, what is the largest value of k as a function of n for which the modified algorithm has the same running time as standard merge sort, in terms of $\Theta$-notation?

In terms of $\Theta$-notation, $\Theta(nk)$ < $\Theta(n^{2})$ when $k << n$. For the same reason, two method have the same time complexity when $k < n^{p}$ as long as $p>0$, which means $\Theta(nk)$ <= $\Theta(n\lg(n))$.

### Question d
> How should we choose k in practice?

Assume that constant factors of insert sort and merge sort are $\beta_{0}$ and $\beta_{1}$. There is an equation $\beta_{0}nk+\beta_{1}n\lg(n/k)=\beta_{1}n\lg(n)$, thus $\frac{\lg(k)}{k}=\frac{\beta_{0}}{\beta_{1}}$.

## 2-3 Correctness of Horner's rule
### Question a

> In terms of $\Theta$-notation, what is the running time of this code fragment for Horner's rule?

The mainly cost of time is the operation of multiplication, so the Horner's method operate n times of multiplication, thus $\Theta(n)$.

### Question b

> Write pseudocode to implement the naive polynomial-evaluation algorithm that computes each term of the polynomial from scratch. What is the running time of this algorithm? How does it compare to Horner’s rule?

The pseudocode of naive method is shown in the following.

```py
y = 0
for i = 0 upto n
     temp = a[i]
    for j = 1 upto i
         temp = temp * x
     y += temp
```

The time complexity of naive method is $\Theta(\frac{n\times(n-1)}{2})=\Theta(n^{2})$.

### Question c

> Following the iteration invariant proof presented in this chapter, proof this question.

With the loop iterating, the coefficients keep constant while p keeps increasing, thus $x^{p}$ finally fit the $a_{p}$.

### Question d

> Conclude by arguing that the given code fragment correctly evaluates a polynomial characterized by the coefficients a0;a1;...; an.

The polynomial can be evaluated as n loop, where coefficients are distributed in each loop, which indicates the different importance of each coefficient.

## 2-4 Inversions
### Question a

> List the five inversions of the array (2,3,8,6,1).

Pairs:(1,5),(2,5),(3,4),(3,5),(4,5).

### Question b

> What array with elements from the set $\{1, 2,...,n\}$ has the most inversions? How many does it have?

The array $\{n, n-1,...,1\}$ has the most inversions, whose total number is $\frac{n\times(n-1)}{2}$.

### Question c

> What is the relationship between the running time of insertion sort and the number of inversions in the input array? Justify your answer.

Insertion sort has a base operation to compare each pair as shown in 2-3, and every comparation means a new inversion pair found. For the worst case, the base operation of the insertion sort also runs $\frac{n\times(n-1)}{2}$ times.

### Question d

> Give an algorithm that determines the number of inversions in any permutation on n elements in $\Theta(n\lg(n))$ worst-case time. (Hint: Modify merge sort.)

The modified merge sort code is shown in the following.

```py
sublists = permutation_array
inversions_count = 0
while len(sublists) > 1:
    sublist_, _sublist = sublists.pop(), sublists.pop()
    #_sublist is in the front of sublist_
    i,j = 0,0
    sublist = []
    while i < len(_sublist) and j < len(sublist_):
        #base operation
        if _sublist[i] <= sublist_[j]:
            sublist.append(_sublist[i])
            i += 1
        else:
            sublist.append(sublist_[j])
            j += 1
            inversions_count += 1
    if i < len(_sublist):
        sublist += _sublist[i:]
        inversions_count +=1
    else:
        sublist += sublist_[j:]
    sublists.insert(0,sublist)
print('Total inversion count is %s' %inversions_count)
```

