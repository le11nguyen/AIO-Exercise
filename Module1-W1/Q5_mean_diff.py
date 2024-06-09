# -------------Question 5: Mean Difference of nth Root Error: -----------------


# Mean Difference of nth Root Error function
def md_nre_single(y,y_hat,n,p):
    result = (y ** (1/n) - y_hat ** (1/n))**p
    return result

# Test output
if __name__ == "__main__":
    print(md_nre_single(y =50 , y_hat =49.5 , n =2 , p =1))