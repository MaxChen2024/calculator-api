from fastapi import FastAPI, status

app = FastAPI()

## Health Check
@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}

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
    return {"result": a / b}



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
    return {"result": a / b}