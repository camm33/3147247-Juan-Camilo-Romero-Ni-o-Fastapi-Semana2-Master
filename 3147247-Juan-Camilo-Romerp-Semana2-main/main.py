
#!/usr/bin/env python3
"""
Mi Primera API FastAPI - Verificación de Setup
Desarrollador: [Tu nombre se llenará automáticamente]
"""

from fastapi import FastAPI
import os
import sys
from datetime import datetime

# Crear instancia de FastAPI
app = FastAPI(
    title="Mi Primera API FastAPI",
    description="API de verificación para setup del bootcamp",
    version="1.0.0"
)

@app.get("/")
def home():
    """Endpoint principal de verificación"""
    return {
        "message": "¡Setup completado correctamente!",
        "project": "FastAPI Bootcamp - Semana 1",
        "timestamp": datetime.now().isoformat(),
        "status": "✅ Working perfectly"
    }

@app.get("/info/setup")
def info_setup():
    """Información del entorno de desarrollo"""
    return {
        "python_version": sys.version,
        "python_path": sys.executable,
        "working_directory": os.getcwd(),
        "virtual_env": os.environ.get("VIRTUAL_ENV", "No detectado"),
        "user": os.environ.get("USER", "No detectado"),
        "hostname": os.environ.get("HOSTNAME", "No detectado")
    }

@app.get("/health")
def health_check():
    """Endpoint de verificación de salud"""
    return {
        "status": "healthy",
        "message": "API running correctly",
        "environment": "development"
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Iniciando servidor de verificación...")
    print("🌐 Acceder a: http://localhost:8000")
    print("📄 Documentación: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
from fastapi import FastAPI

app = FastAPI(title="Mi Primera API")

@app.get("/")
def hello_world():
    return {"message": "¡Mi primera API FastAPI!"}

@app.get("/info")
def info():
    return {"api": "FastAPI", "week": 1, "status": "running"}

@app.get("/greeting/{name}")
def greet_user(name: str):
    return {"greeting": f"¡Hola {name}!"}

# Sin type hints (como en Semana 1)
def greet(name):
    return f"Hello {name}!"

# Con type hints (lo que aprenderemos hoy)
def greet(name: str) -> str:
    return f"Hello {name}!"

# Tipos simples para APIs
def create_user(name: str, age: int, active: bool) -> dict:
    return {"name": name, "age": age, "active": active}

def get_numbers() -> list:
    return [1, 2, 3, 4, 5]

def get_config() -> dict:
    return {"debug": True, "version": "1.0"}

# Tipos simples para APIs
def create_user(name: str, age: int, active: bool) -> dict:
    return {"name": name, "age": age, "active": active}

def get_numbers() -> list:
    return [1, 2, 3, 4, 5]

def get_config() -> dict:
    return {"debug": True, "version": "1.0"}

from fastapi import FastAPI

app = FastAPI(title="My First API")

# ANTES (Semana 1)
@app.get("/")
def hello_world():
    return {"message": "My first FastAPI!"}

# DESPUÉS (con type hints)
@app.get("/")
def hello_world() -> dict:
    return {"message": "My first FastAPI!"}

# Si tenías endpoint con parámetro
@app.get("/greeting/{name}")
def greet_user(name: str) -> dict:
    return {"greeting": f"Hello {name}!"}

# Endpoint con múltiples parámetros
@app.get("/calculate/{num1}/{num2}")
def calculate(num1: int, num2: int) -> dict:
    result = num1 + num2
    return {"result": result, "operation": "sum"}

from typing import List, Dict

# Lista de strings
@app.get("/fruits")
def get_fruits() -> List[str]:
    return ["apple", "banana", "orange"]

# Lista de números
@app.get("/numbers")
def get_numbers() -> List[int]:
    return [1, 2, 3, 4, 5]

# Diccionario con estructura conocida
@app.get("/user/{user_id}")
def get_user(user_id: int) -> Dict[str, str]:
    return {
        "id": str(user_id),
        "name": "Demo User",
        "email": "demo@example.com"
    }
    
from typing import List, Dict

# Lista de strings
@app.get("/fruits")
def get_fruits() -> List[str]:
    return ["apple", "banana", "orange"]

# Lista de números
@app.get("/numbers")
def get_numbers() -> List[int]:
    return [1, 2, 3, 4, 5]

# Diccionario con estructura conocida
@app.get("/user/{user_id}")
def get_user(user_id: int) -> Dict[str, str]:
    return {
        "id": str(user_id),
        "name": "Demo User",
        "email": "demo@example.com"
    }
    
# Alguien envía datos incorrectos a tu API
# Tu API se rompe o da resultados raros
@app.post("/users")
def create_user(data):
    # ¿Qué pasa si data no tiene 'name'?
    # ¿Qué pasa si 'age' es texto en lugar de número?
    return {"user": data}

from pydantic import BaseModel

# Definir QUÉ datos esperas
class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/users")
def create_user(user: User):
    # Pydantic garantiza que los datos son correctos
    return {"user": user.dict()}

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My API with Pydantic")

# Tu primer modelo de datos
class Product(BaseModel):
    name: str
    price: int  # en centavos para evitar decimales
    available: bool = True  # valor por defecto

# Lista temporal para guardar productos
products = []

# Endpoint GET (como antes)
@app.get("/")
def hello_world() -> dict:
    return {"message": "API with Pydantic!"}

# NUEVO: Endpoint POST con Pydantic
@app.post("/products")
def create_product(product: Product) -> dict:
    product_dict = product.dict()
    product_dict["id"] = len(products) + 1
    products.append(product_dict)
    return {"message": "Product created", "product": product_dict}

# Endpoint para ver todos los productos
@app.get("/products")
def get_products() -> dict:
    return {"products": products, "total": len(products)}

from typing import Optional

class CompleteUser(BaseModel):
    name: str
    age: int
    email: str
    phone: Optional[str] = None  # campo opcional
    active: bool = True

@app.post("/users")
def create_user(user: CompleteUser) -> dict:
    return {"user": user.dict(), "valid": True}

# Agregar a tu main.py existente

# Parámetro de ruta simple
@app.get("/products/{product_id}")
def get_product(product_id: int) -> dict:
    for product in products:
        if product["id"] == product_id:
            return {"product": product}
    return {"error": "Product not found"}

# Múltiples parámetros de ruta
@app.get("/categories/{category}/products/{product_id}")
def product_by_category(category: str, product_id: int) -> dict:
    return {
        "category": category,
        "product_id": product_id,
        "message": f"Searching product {product_id} in {category}"
    }
from typing import Optional

# Query parameters opcionales
@app.get("/search")
def search_products(
    name: Optional[str] = None,
    max_price: Optional[int] = None,
    available: Optional[bool] = None
) -> dict:
    results = products.copy()

    if name:
        results = [p for p in results if name.lower() in p["name"].lower()]
    if max_price:
        results = [p for p in results if p["price"] <= max_price]
    if available is not None:
        results = [p for p in results if p["available"] == available]

    return {"results": results, "total": len(results)}

# Agregar estos modelos después de tu modelo Product

class ProductResponse(BaseModel):
    id: int
    name: str
    price: int
    available: bool
    message: str = "Product retrieved successfully"

class ProductListResponse(BaseModel):
    products: list
    total: int
    message: str = "List retrieved successfully"

# Actualizar endpoints para usar response models
@app.get("/products", response_model=ProductListResponse)
def get_products() -> ProductListResponse:
    return ProductListResponse(
        products=products,
        total=len(products)
    )

@app.post("/products", response_model=ProductResponse)
def create_product(product: Product) -> ProductResponse:
    product_dict = product.dict()
    product_dict["id"] = len(products) + 1
    products.append(product_dict)

    return ProductResponse(
        id=product_dict["id"],
        name=product_dict["name"],
        price=product_dict["price"],
        available=product_dict["available"],
        message="Product created successfully"
    )

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="My Enhanced API - Week 2")

# Modelos de datos
class Product(BaseModel):
    name: str
    price: int
    available: bool = True

class ProductResponse(BaseModel):
    id: int
    name: str
    price: int
    available: bool
    message: str = "Successful operation"

class ProductListResponse(BaseModel):
    products: List[dict]
    total: int
    message: str = "List retrieved"

# Almacenamiento temporal
products = []

# Endpoints básicos
@app.get("/")
def hello_world() -> dict:
    return {"message": "Week 2 API with Pydantic and Type Hints!"}

@app.get("/products", response_model=ProductListResponse)
def get_products() -> ProductListResponse:
    return ProductListResponse(
        products=products,
        total=len(products)
    )

@app.post("/products", response_model=ProductResponse)
def create_product(product: Product) -> ProductResponse:
    product_dict = product.dict()
    product_dict["id"] = len(products) + 1
    products.append(product_dict)

    return ProductResponse(**product_dict, message="Product created")

@app.get("/products/{product_id}")
def get_product(product_id: int) -> dict:
    for product in products:
        if product["id"] == product_id:
            return {"product": product}
    raise HTTPException(status_code=404, detail="Product not found")

@app.get("/search")
def search_products(
    name: Optional[str] = None,
    max_price: Optional[int] = None
) -> dict:
    results = products.copy()

    if name:
        results = [p for p in results if name.lower() in p["name"].lower()]
    if max_price:
        results = [p for p in results if p["price"] <= max_price]

    return {"results": results, "total": len(results)}