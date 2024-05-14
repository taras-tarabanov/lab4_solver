import numpy as np
from scipy.stats import f
# Create a 5x5 matrix of integers
matrix = np.array([
    [48.4, 45.5, 48.9, 45.3],
    [45.2, 47.7, 47.8, 46.5],
    [48.6, 50.3, 49.2, 47.5],
    [47, 51.2, 50.1, 48.1],
    [48.3, 47.8, 47, 48.1]
])
matrix = np.array([
    [200, 140, 170, 145, 165],
    [190, 150, 210, 150, 150],
    [230, 190, 200, 190, 200],
    [150, 170, 150, 170, 180]
])
riven_znachushchosti = 0.01
riven_znachushchosti = 0.05

row_means = np.mean(matrix, axis=1)
#print(row_means)
print(fr"\begin{{align}}")
for i, row in enumerate(matrix):
    latex_code = fr"\bar{{x}}_{i+1}* &= \frac{{1}}{{{matrix.shape[1]}}}({'+'.join(map(str, row))}) = {row_means[i]} \\"
    print(latex_code)

overall_mean = np.mean(row_means)

# Generate LaTeX code for the overall mean
latex_overall_mean = fr"\bar{{x}}^* &= \frac{{1}}{{{matrix.shape[0]}}}({'+'.join(map(lambda x: f'{x:.1f}', row_means))}) = {overall_mean:.1f} \\"


intergroup_ss = matrix.shape[1] * np.sum((row_means - overall_mean) ** 2)

#print(f"Intergroup sum of squares of deviations: {intergroup_ss}")
print(latex_overall_mean)
# Generate LaTeX code for the intergroup sum of squares of deviations

latex_intergroup_ss = fr"Q_1 &= {{{matrix.shape[1]}}}\left({'+'.join(map(lambda x: f'({x:.1f} - {overall_mean:.1f})^2', row_means))}\right) = {intergroup_ss:.2f} \\"
print(latex_intergroup_ss)
intragroup_ss = np.sum((matrix - row_means.reshape(-1, 1)) ** 2)
latex_intragroup_ss = fr"Q_2 &= {'+'.join(map(lambda x: f'({x[0]} - {x[1]:.1f})^2', zip(matrix.flatten(), np.repeat(row_means, matrix.shape[1]))))}"
latex_intragroup_ss += fr" = {intragroup_ss:.2f} \\"
print(latex_intragroup_ss)

s1_squared = intergroup_ss / (matrix.shape[0] - 1)
s2_squared = intragroup_ss / (20 - matrix.shape[0])

latex_s1_squared = fr"s_1^2 &= \frac{{Q_1}}{{4-1}} = \frac{{{intergroup_ss:.0f}}}{{3}} = {s1_squared:.2f}"
latex_s2_squared = fr"s_2^2 &= \frac{{Q_2}}{{20-4}} = \frac{{{intragroup_ss:.0f}}}{{16}} = {s2_squared:.2f}"
print(latex_s1_squared + fr" \\")
print(latex_s2_squared + fr" \\")


F_observed = s1_squared / s2_squared
latex_F_observed = fr"K_{{\text{{cnoc}}}} &= \frac{{s_1^2}}{{s_2^2}} = \frac{{{s1_squared:.2f}}}{{{s2_squared:.2f}}} = {F_observed:.2f} \\"
print(latex_F_observed)

k1 = matrix.shape[0] - 1  # Number of groups minus 1
k2 = 20 - matrix.shape[0] # Total number of observations minus number of groups

# Critical F value (95th percentile)
K_cr = f.ppf(1 - riven_znachushchosti, k1, k2)

# Display results
#print(fr"F_{{\text{{cn}}}} &= {F_observed:.4f} \\")
print(fr"K_{{\text{{kp}}}}&=F_{{0.05; {k1}; {k2}}} = {K_cr:.4f} \\")

# Decision
if F_observed > K_cr:
    print(r"\text{Since } &K_{{\text{{cnoc}}}} > K_{{\text{{kp}}}}, \text{ we reject } H_0.")
    print(r"\text{There is significant difference in the group means.}")
else:
    print(r"\text{Since } &K_{{\text{{cnoc}}}} \leq K_{{\text{{kp}}}}, \text{ we do not reject } H_0.")
    print(r"\text{There is no significant difference in the group means.}")
print(fr"\end{{align}}")
