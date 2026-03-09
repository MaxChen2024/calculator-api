from fastapi import FastAPI, status
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
def add(a: float, b: float):
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
def add(a: float, b: float):
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
def add(a: float, b: float):
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
def add(a: float, b: float):
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
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Cannot divide by zero")

    return {"result": a / b}


####################
## Additional Endpoints
####################

@app.get("/power/{a}/{b}", status_code=200)
def add(a: float, b: float):
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

    
    return {"result": a ** b}

@app.get("/sqrt/{a}", status_code=200)
def add(a: float):
    """
    Square root number a.
    
    Parameters:
    - a: First number
    
    Returns:
    - JSON object with the result
    """
    return {"result": math.sqrt(a)}



@app.get("/add-3/{a}/{b}/{c}", status_code=200)
def add(a: float, b: float, c: float):
    """
    Square root number a.
    
    Parameters:
    - a: First number
    
    Returns:
    - JSON object with the result
    """
    return {"result": a + b + c}