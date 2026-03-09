from fastapi import FastAPI, status, HTTPException
import math

app = FastAPI()

## Health Check
@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


#####################
## Default Endpoints
#####################


## Addition
@app.get("/add/{a}/{b}", status_code=200)
def add(a: str, b: str):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers")


    return {"result": a + b}



@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: str, b: str):
    """
    Subtract number a by b.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers")

    return {"result": a - b}


@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: str, b: str):
    """
    Multiply two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers")

    return {"result": a * b}


@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: str, b: str):
    """
    Divide number a by b.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers")

    try:
        result = a / b
    except ZeroDivisionError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Cannot divide by zero, second input (b) cannot be zero")

    return {"result": result}


####################
## Additional Endpoints
####################

@app.get("/power/{a}/{b}", status_code=200)
def power(a: str, b: str):
    """
    Calculate a to the power of b
    
    Parameters:
    - a: Base number
    - b: Exponent power
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers")

    
    return {"result": a ** b}

@app.get("/sqrt/{a}", status_code=200)
def sqrt(a: str):
    """
    Calculates the square root of a number
    
    Parameters:
    - a: First number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Input must be a valid number")

    try:
        sqrt_a = math.sqrt(a)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Cannot take the square root of a negative number")



    return {"result": sqrt_a}



@app.get("/add_3/{a}/{b}/{c}", status_code=200)
def add_3(a: str, b: str, c: str):
    """
    Adds 3 numbers together
    
    Parameters:
    - a: First number
    
    Returns:
    - JSON object with the result
    """

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="'a', 'b', and 'c' must all be valid numbers")

    return {"result": a + b + c}