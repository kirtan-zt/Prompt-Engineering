# E-commerce Project

This project is a simple e-commerce backend built using Django and Django REST framework. It provides a basic API for managing product information, including creating, retrieving, updating, and deleting products.

## Features

- **Product Management:**
  - Create new products with name, price, stock, and category.
  - Fetch all products.
  - Update the stock quantity of existing products.
  - Delete products.
- **Categorization:** Products can be assigned to categories.
- **RESTful API:** All functionalities are exposed through a RESTful API.

## Setup and Installation

### Prerequisites

- Python 3.6+
- pip

### Cloning the Repository

```bash
git clone https://github.com/kirtan-zt/Prompt-Engineering.git
cd Prompt-Engineering
```

### Setting up the Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
# .\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Installing Dependencies

Install Django and Django REST framework using pip.

```bash
pip install django djangorestframework
```

## Running the Application

### Starting the Development Server

Once the dependencies are installed and the virtual environment is activated, you can start the Django development server.

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

### Running Tests

To run the project's tests, execute the following command:

```bash
python manage.py test
```

## API Reference

The project exposes a RESTful API for product management. The base URL for the API is `http://127.0.0.1:8000/api/`.

### Products Endpoint

The `/api/products/` endpoint handles CRUD operations for products.

#### 1. Fetch All Products

- **Method:** `GET`
- **URL:** `/api/products/`
- **Description:** Retrieves a list of all products.
- **Request Parameters:** None
- **Sample Response (JSON):**

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": "1200.00",
    "stock": 50,
    "category": "Electronics"
  },
  {
    "id": 2,
    "name": "T-Shirt",
    "price": "25.00",
    "stock": 200,
    "category": "Apparel"
  }
]
```

#### 2. Create a New Product

- **Method:** `POST`
- **URL:** `/api/products/`
- **Description:** Creates a new product.
- **Request Body (JSON):**

```json
{
  "name": "Smartphone",
  "price": "800.00",
  "stock": 150,
  "category": "Electronics"
}
```

- **Sample Response (JSON - on successful creation):**

```json
{
  "id": 3,
  "name": "Smartphone",
  "price": "800.00",
  "stock": 150,
  "category": "Electronics"
}
```

#### 3. Retrieve a Specific Product

- **Method:** `GET`
- **URL:** `/api/products/<int:pk>/`
- **Description:** Retrieves details of a specific product by its ID.
- **URL Parameters:**
  - `pk` (integer): The unique identifier of the product.
- **Sample Response (JSON):**

```json
{
  "id": 1,
  "name": "Laptop",
  "price": "1200.00",
  "stock": 50,
  "category": "Electronics"
}
```

#### 4. Update Product Stock

- **Method:** `PUT` or `PATCH`
- **URL:** `/api/products/<int:pk>/`
- **Description:** Updates the stock quantity of a specific product. You can send the entire product object with `PUT` or just the fields you want to update with `PATCH`.
- **URL Parameters:**
  - `pk` (integer): The unique identifier of the product.
- **Request Body (JSON - example for PATCH):**

```json
{
  "stock": 45
}
```

- **Sample Response (JSON - on successful update):**

```json
{
  "id": 1,
  "name": "Laptop",
  "price": "1200.00",
  "stock": 45,
  "category": "Electronics"
}
```

#### 5. Delete a Product

- **Method:** `DELETE`
- **URL:** `/api/products/<int:pk>/`
- **Description:** Deletes a specific product by its ID.
- **URL Parameters:**
  - `pk` (integer): The unique identifier of the product.
- **Sample Response (JSON - on successful deletion):**

An empty response with a `204 No Content` status code is typically returned on successful deletion.
