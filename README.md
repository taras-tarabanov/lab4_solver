# One-way ANOVA Calculator
![image](https://github.com/taras-tarabanov/lab4_solver/assets/146372529/981f1cd9-7fd4-449a-9c8a-4a5bed716f00)

## Input

* `matrix`: a 5x5 NumPy array of integers
* `riven_znachushchosti`: the significance level (default: 0.05)

## Output

* Calculated values printed to the console in LaTeX format
  
Example output:
```
\begin{align}
\bar{x}_1* &= \frac{1}{5}(200+140+170+145+165) = 164.0 \\
\bar{x}_2* &= \frac{1}{5}(190+150+210+150+150) = 170.0 \\
\bar{x}_3* &= \frac{1}{5}(230+190+200+190+200) = 202.0 \\
\bar{x}_4* &= \frac{1}{5}(150+170+150+170+180) = 164.0 \\
\bar{x}^* &= \frac{1}{4}(164.0+170.0+202.0+164.0) = 175.0 \\
Q_1 &= 5\left((164.0 - 175.0)^2+(170.0 - 175.0)^2+(202.0 - 175.0)^2+(164.0 - 175.0)^2\right) = 4980.00 \\
Q_2 &= (200 - 164.0)^2+(140 - 164.0)^2+(170 - 164.0)^2+(145 - 164.0)^2+(165 - 164.0)^2+(190 - 170.0)^2+(150 - 170.0)^2+(210 - 170.0)^2+(150 - 170.0)^2+(150 - 170.0)^2+(230 - 202.0)^2+(190 - 202.0)^2+(200 - 202.0)^2+(190 - 202.0)^2+(200 - 202.0)^2+(150 - 164.0)^2+(170 - 164.0)^2+(150 - 164.0)^2+(170 - 164.0)^2+(180 - 164.0)^2 = 7270.00 \\
s_1^2 &= \frac{Q_1}{4-1} = \frac{4980}{3} = 1660.00 \\
s_2^2 &= \frac{Q_2}{20-4} = \frac{7270}{16} = 454.38 \\
K_{\text{cnoc}} &= \frac{s_1^2}{s_2^2} = \frac{1660.00}{454.38} = 3.65 \\
F_{\text{observed}} &= 3.6534 \\
F_{0.05; 3; 16} &= 3.2389 \\
\text{Since } &F_{\text{observed}} > F_{\text{critical}}, \text{ we reject } H_0.
\text{There is &significant difference in the group means.}
\end{align}
```
## Code

* Written in Python using SciPy library

## Usage

1. Run the script using Python: `python anova.py`
2. Copy console output like in example
3. View the output in LaTeX format using [www.texrendr.com](http://www.texrendr.com/)
