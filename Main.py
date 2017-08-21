# In[0]: <- for Hydrogen (to use jupyter kernels in Atom)
# import statements
import pandas as pd

print('...')


# In[1]: set weight1, weight2, and bias
weight1 = 0.0
weight2 = 0.0
bias    = 0.0

print('...')


# In[2] Inputs and Outputs
test_inputs = [(0,0,), (0,1), (1, 0), (1, 1)]
correct_outputs = [False, False, False, True]
outputs = []

print('...')


# In[3]:  Generate and check output
for test_input, correct_output in zip(test_inputs, correct_outputs):
    linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
    output = int(linear_combination >= 0)
    
