# Exercise OLS (version without functions

# Load the data
x = [9.55, 9.36, 0.2, 2.06, 5.89, 9.3, 4.74, 2.43, 6.5, 4.77]
y = [15.28, 16.16, 1.2, 5.14, 9.82, 13.88, 6.3, 3.71, 9.96, 9]

def promedio(l):
    sum = 0
    for i in l:
        sum +=i
    return sum/len(l)

# Let us compute the average of x

mean_x = promedio(x)

# Let us compute the average of y
mean_y = promedio(y)

# Let us compute the numerator and the denominator of the beta estimator: 
numerator = 0
denominator = 0
for i in range(0,len(x)): # here I use the index for-loop to be able to use both x and y
    numerator += (y[i]-mean_y)*(x[i]-mean_x)
    denominator += (x[i]-mean_x)**2
    
beta = numerator / denominator

# Now get the intercept
alpha = mean_y - beta * mean_x


# Print the output
print("Regression analysis y = alpha + beta*x + u")
print("------------------------------------------")
print("x\t%10.5f" % beta)
print("const\t%10.5f" % alpha)
print("------------------------------------------")


