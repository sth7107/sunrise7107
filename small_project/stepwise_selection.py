import numpy as np
import pandas as pd
import statsmodels.api as sm

def stepwise_selection(X, y, start_list, threshold_in, \
						threshold_out) -> list:
    """
    Perform a stepwise selection procedure with forward and 
    backward steps based on p-values
    
    Parameters
    ----------
    X: a DataFrame with all the candidate variables
    y: a Series for target variable
    start_list: the starting point of the stepwise, blank (start_list=[]),
                or some predetermined variables
    threshold_in: add a new variable if its p-value is less than threshold_in,
                in the process of forward step
    threshold_out: drop a variable if its p-value is greater than threshold_out,
                in the process of backward step
                
    Returns
    -------
    incl_list: the final list of the selected variables
    
    prints
    ------
    print(1): each step of forward and p-values
    print(2): if adding a variable, print the variable with its pvalues
    print(3): if dropping a variable, print the variable with its pvalues
       
    """
    incl_list = list(start_list)
    
    i = 0
    
    while True:
        loop_break = True
        
        # forward step
        # a list of variables not included so far
        excl_list = list(set(X.columns) - set(incl_list))
        new_pval = pd.Series(index = excl_list)
        
        # start a for loop to run regression each with included variables
        for new_var in excl_list:
            reg_temp = sm.OLS(y, sm.add_constant(X[incl_list+[new_var]],
                                has_constant='add')).fit()
            new_pval[new_var] = reg_temp.pvalues[new_var]
            
        # select the new variables with the lowest p-values
        lowest_pval = new_pval.min()
        if lowest_pval < threshold_in:
            i += 1
            loop_break = False
            
            add_var = new_pval.idxmin()
            incl_list.append(add_var)
            reg_temp = sm.OLS(y, sm.add_constant(X[incl_list],
                                has_constant='add')).fit()
		
        # print(1)
        print(f'\n Forward step round {i} \n', reg_temp.pvalues)
        
        # print(2)
        print(f'\n Add {add_var} with p-value {lowest_pval}.\n')
        
        # backward step
        reg_temp = sm.OLS(y, sm.add_constant(X[incl_list],
                                has_constant='add')).fit()
        # get all variables' p-values
        pvalues = reg_temp.pvalues.iloc[1:] # excluding intercept's p-values
        highest_pval = pvalues.max()
        
        if highest_pval > threshold_out:
            loop_break = False
            drop_var = pvalues.idxmax()
            
            # exclude this variable whose p-value is beyond the threshold_out
            incl_list.remove(drop_var)
            # print(3)
            print(f'\n Drop {drop_var} with p-value {highest_pval}. \n')
        
        if loop_break: # when loop_break is True, break the loop.
            break
        
    return incl_list
            
        
        
