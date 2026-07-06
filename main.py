def numberplate(number):
    """
    This function takes a number as input and returns a formatted number plate string.
    
    Args:
    number (int): The number to be formatted into a number plate.
    
    Returns:
    str: A formatted number plate string.
    """
    # Ensure the number is a positive integer
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a positive integer.")
    
    # Format the number into a number plate format (e.g., "ABC-1234")
    formatted_number = f"ABC-{number:0}"
    
    return formatted_number

number = 123
formatted_plate = numberplate(number)
print(f"The formatted number plate is: {formatted_plate}")  
