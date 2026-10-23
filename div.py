from add import add
from sub  import sub

def div(a, b):
    """Return the division of a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b    
if __name__ == "__main__":
    # Example usage
    result = div(20, 4)
    print(f"The division of 20 by 4 is: {result}")
    
    diff_result = sub(20, 4)
    print(f"The difference of 20 and 4 is: {diff_result}")
    
    sum_result = add(20, 4)
    print(f"The sum of 20 and 4 is: {sum_result}")