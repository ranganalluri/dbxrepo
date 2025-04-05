from mathone.utils.math_op import MathOperations

if __name__ == "__main__":
    # Sample data
    data = 10
    value = 5
    # Initialize MathOperations class
    math_operations = MathOperations(data)

    # Perform operations
    result_add = math_operations.add( value)
    result_subtract = math_operations.subtract( value)

    # Print results
    print(f"Addition Result: {result_add}")
    print(f"Subtraction Result: {result_subtract}")