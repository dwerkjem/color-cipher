# Supplementary Algorithms

## Formula for Distributing Points Along a Line

The formula distributes a list of $N$ objects along a line of length $L$ such that each object appears with its specified frequency $N_{\text{subF}}$, and the total number of points along the line equals $L$.

1. **Define the Variables:**
   - $N$: Total number of distinct objects.
   - $N_{\text{subF}}$: A list of frequencies for each object, where $N_{\text{subF}}[i]$ is the frequency of the $i$-th object.
   - $L$: Total length of the line.

2. **Sum of Frequencies:**

   $$\text{SumF} = \sum_{i=1}^{N} N_{\text{subF}}[i]$$

3. **Normalized Length for Each Object:**

   $$L_{\text{subF}}[i] = \left( \frac{N_{\text{subF}}[i]}{\text{SumF}} \right) \times L$$

   This represents the segment of the line $L$ that each object $i$ occupies based on its frequency.

4. **Distribute Points Along the Line:**

   ![equation](eq.png)

### Example of Distributing Points Along a Line

For $N = 3$, $N_{\text{subF}} = [2, 3, 5]$ , and $L = 10$, the output will be a list of length $L$ with the objects distributed more evenly according to their frequencies:

$$\text{SumF} = 2 + 3 + 5 = 10$$

$$L_{\text{subF}}[0] = \left( \frac{2}{10} \right) \times 10 = 2$$

$$L_{\text{subF}}[1] = \left( \frac{3}{10} \right) \times 10 = 3$$

$$L_{\text{subF}}[2] = \left( \frac{5}{10} \right) \times 10 = 5$$

The intervals for placing the objects would be calculated as follows:

$$\text{interval}_0 = \frac{10}{2} = 5$$

$$\text{interval}_1 = \frac{10}{3} \approx 3.33$$

$$\text{interval}_2 = \frac{10}{5} = 2$$

This results in the following distribution:

$$\text{position}_0 = [0, 5]$$

$$\text{position}_1 = [0, 3, 6]$$

$$\text{position}_2 = [0, 2, 4, 6, 8]$$

Mapping these positions onto the line, we get:

$$\text{line} = [0, 2, 1, 2, 2, 0, 1, 2, 2, 1]$$

This method ensures that the points are more evenly spread along the line $L$.

## Formula to decrease the resolution of a dictionary

Given:

- $D$: A dictionary where keys are characters and values are their ratios.
- $\text{maxResolution}$ : The maximum allowed resolution.

1. **Calculate Total Resolution**

    $$\text{totalResolution} = \sum_{k \in D} D[k]$$

2. **Check if Scaling is Needed**

    If $\text{totalResolution} \leq \text{maxResolution}$, return $D$ as is.

3. **Calculate Scaling Factor**

    If $\text{totalResolution} > \text{maxResolution}$:

    $$\text{scalingFactor} = \frac{\text{maxResolution}}{\text{totalResolution}}$$

4. **Create a New Dictionary with a Decreased Resolution**

    $$D' = \{k: D[k] \times \text{scalingFactor} \text{ for each } k \in D\}$$

5. **Normalize the Values**

    Calculate the sum of the new dictionary:

    $$\text{scalingFactorSum} = \sum_{k \in D'} D'[k]$$

    Calculate the normalization factor:

    $$\text{normalizationFactor} = \frac{\text{maxResolution}}{\text{scalingFactorSum}}$$

    Apply the normalization factor:

    $$D'' = \{k: \left\lfloor D'[k] \times \text{normalizationFactor} \right\rfloor \text{ for each } k \in D'\}$$

6. **Adjust to Match maxResolution**

    Calculate the difference:

    $$\text{difference} = \text{maxResolution} - \sum_{k \in D''} D''[k]$$

    Adjust the values to match maxResolution exactly:

    1. Sort the keys in $D''$ by their values in descending order if $\text{difference} > 0$, otherwise in ascending order.
    2. Increment or decrement the values in $D''$ by 1 for the sorted keys until $\text{difference} = 0$.

    The final dictionary $D''$ will have a resolution of $\text{maxResolution}$.
