# tridiagonal-symmetric-system-of-linear-equations

This script solves systems of linear equations with tridiagonal symmetric matrices. Therefore insert your diagonal (__a__), upper diagonal (__u__) and RHS (__b__) vectors in the first few lines of the code and execute it.
The equation should look something like this:

$$ \begin{bmatrix}
    a_{0} & u_{0} & 0 &  \dots & 0 \\
    u_{0} & a_{1} & u_{1} & \ddots & \vdots  \\
    0     & u_{1} & a_{2} & u_{2}  & 0 \\
    \vdots & \ddots & \ddots & \ddots & \ddots \\
    0 & \dots & 0  & u_{n-2}  & a_{n-1}
   \end{bmatrix}
   \cdot
   \begin{bmatrix}
    c_{0} \\
    c_{1}  \\
    \\
    \vdots \\
    c_{n-1}
  \end{bmatrix}
  =\begin{bmatrix}
    b_{0} \\
    b_{1}  \\
    \\
    \vdots \\
    b_{n-1}
  \end{bmatrix} \in \mathbb{R}^{n}$$
  
Since using Gaussian eliminiation would lead to $\mathcal{O}(n^3)$ this algorithm is much faster with $\mathcal{O}(n)$ and explictly $8n-6$  operations.
