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
    is_correct_string = 'Yes' if output == correct_output else 'No'
    outs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string)

print('...')



# In[4]: Print the output
num_wrong = len([output[4] for output in outputs if output[4] == 'no'])
output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', ' Linear Combination', '  Activation Output', '   Is Correct'])
if not num_wrong:
    print('Nice! You got it all correct.\n')
else:
    print('You got {} wrong.  Keep Trying!\n'.format(num_wrong))
    print(output_frame.to_string(index=False))
