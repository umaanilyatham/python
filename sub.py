from add import add

def sub(a, b):
    """Return the difference of a and b."""
    return a - b    
if __name__ == "__main__":
    # Example usage
    result = sub(10, 4)
    print(f"The difference of 10 and 4 is: {result}")
    
    sum_result = add(10, 4)
    print(f"The sum of 10 and 4 is: {sum_result}")