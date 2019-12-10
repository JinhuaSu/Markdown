# algorithm homework 3

**info**

SuJinhua 2017201620

**analysis on the problem**

It is an analogy question of cal-subquence. However there are 6 operations which relate with previous sub-problem, especially the twiddle operation and kill operation. As for different cost combination of above operation, the specific recurrence formulation may differ a bit, ignoring some extremely costful operation combinations to save time. For example, when the cost of delete is extremely bigger than the cost of delete, we will think about using delete to repalce the kill for most time.

**recurrence formulation**

Note: the slice operation appears in the following is based on python.

We use ED(i,j) to represent the sub-problem of editting distance on a[:i+1] and b[:j+1] without OPT(KILL), and ED(i,j) is a tuple like (total cost, a list of operation series). So our final goal is to get the ED(x,n), where x ranges from 0 to m and is for updating OPT(KILL) in the termination, and we use bottom-top method to get close to ED(x,n) using ED(i,j) and recursive formulation. There is pseudo code to describe the precoss how to get ED(i,j).

```py
if j == 0:
    E(i,j) = (i*cost_DELETE, ['DELETE']*i)
elif i == 0:
    ED(i,j) = (j*cost_INSERT, ['INSERT']*j)
else:
    opt_l = []
    if a[i] == b[j]:
        opt1 = (ED(i-1,j-1)[0] + cost_COPY, ED(i-1,j-1)[1] + ['COPY']))
        opt_l.append(opt1)
    if ED(i-1,j)[1][-1] == 'INSERT':
        if a[i] == b[j]:
            opt2 = (ED(i-1,j)[0] + cost_COPY - cost_INSERT, ED(i-1,j)[1][:-1] + ['COPY'])
        else:
            opt2 = (ED(i-1,j)[0]+ cost_REPLACE - cost_INSERT, ED(i-1,j)[1][:-1] + ['REPLACE'])
    else:
        opt2 = (ED(i-1,j)[0] + cost_DELETE, ED(i-1,j)[1] + ['DELETE'])
    opt_l.append(opt2)
    if ED(i,j-1)[1][-1] == 'DELETE':
        if a[i] == b[j]:
            opt3 = (ED(i,j-1)[0]+ cost_COPY - cost_DELETE, ED(i-1,j)[1][:-1] + ['COPY'])
        else:
            opt3 = (ED(i,j-1)[0]+ cost_REPLACE - cost_DELETE, ED(i-1,j)[1][:-1] + ['REPLACE'])
    else:
        opt3 = (ED(i-1,j)[0] + cost_INSERT, ED(i-1,j)[1] + ['INSERT'])
    opt_l.append(opt3)
    if a[i] == b[j-1] and a[i-1] == b[j]:
        opt4 = (ED(i-2,j-2)[0] + cost_TWIDDLE, ED(i-2,j-2)[1] + ['TWIDDLE'])
        opt_l.append(opt4)    
sorted('ascending',opt_l,lambda x:x[0])
ED(i,j) = opt_l[0]
```
**Naive algorithm**

Generate a (m+1) * (n+1) matrix to save the intermediate result. Calculating ED(i,j) is an elementary operation, so the time complexity and space complexity are both $\Theta(m \times n)$.

**Hirschberg’s algorithm for saving space**

To make the space usage more efficient, use following pseudo-code to save space and give one way to consider the KILL operation.

```py
row1 = [ED(0,j) for j in range(n+1)]
row2 = [ED(1,j) for j in range(n+1)]
column1 = [ED(i,0) for i in range(m+1)]
column2 = [ED(i,1) for i in range(m+1)]
for j in range(2,n+1):
    for i in range(2,m+1):
        edit_distance(ED(i,j),row1,row2,column1,column2)
        save(ED(i,j),column1)
    column1,column2 = column2,column1
num = check_delete_num(ED(m,n))
if num * cost_DELETE >= cost_KILL:
    use_KILL(ED(m,n))
```

Since we only use less space, the space complexity will be $\Theta(m+n)$.

**optimal alignment**

Optimal alignment is a specific application of editting distance, corresponding cost value is in the following.

| operation | cost |
| :--: | :--: |
| COPY | -1 |
| REPLACE | 1 |
| INSERT | 2 |
| DELETE | 2 |
| TWIDDLE | infinite |
| KILL | infinite |