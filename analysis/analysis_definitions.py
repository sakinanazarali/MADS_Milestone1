import scipy.stats as stats

def t_test(group1, group2):
    # Perform the t-test
    t_statistic, p_value = stats.ttest_ind(group1, group2)

    # Print the results
    print("T-statistic:", t_statistic)
    print("P-value:", p_value)

    # Interpret the results
    alpha = 0.05  # Significance level
    if p_value < alpha:
        print("Reject the null hypothesis: There is a significant difference between the groups.")
    else:
        print("Fail to reject the null hypothesis: There is no significant difference between the groups.")

    return(t_statistic, p_value)