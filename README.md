# E-commerce Product API

This project provides a RESTful API for managing e-commerce products using Django and Django REST Framework. It allows for basic CRUD (Create, Read, Update, Delete) operations on product data.

## Features

*   **Product Management:**
    *   Create new products with name, price, stock, and category.
    *   Fetch all products.
    *   Update the stock quantity of existing products.
    *   Delete products.
*   **Categorization:** Products can be assigned to categories.
*   **RESTful API:** All functionalities are exposed through a clean and intuitive API.

## Setup and Installation

### Prerequisites

*   Python 3.6+
*   `pip` (Python package installer)

### Cloning the Repository

```bash
git clone https://github.com/kirtan-zt/Prompt-Engineering.git
cd Prompt-Engineering
```

### Setting up a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
# .\venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate
```

### Installing Dependencies

Once the virtual environment is activated, install the required packages:

```bash
pip install django djangorestframework
```

## Running the Application

### Starting the Development Server

To start the Django development server, navigate to the project's root directory (where `manage.py` is located) and run:

```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/`.

### Running Tests

The project includes tests to verify the functionality of the API. To run the tests, execute:

```bash
python manage.py test
```

## API Reference

The API is built using Django REST Framework's `DefaultRouter` and is accessible under the `/api/` path.

### Products Endpoint

Base URL: `/api/products/`

#### 1. Fetch All Products

*   **Method:** `GET`
*   **URL:** `/api/products/`
*   **Description:** Retrieves a list of all available products.
*   **Request Parameters:** None
*   **Sample Response (200 OK):**

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
        "price": "25.50",
        "stock": 200,
        "category": "Apparel"
    }
]
```

#### 2. Create a New Product

*   **Method:** `POST`
*   **URL:** `/api/products/`
*   **Description:** Creates a new product.
*   **Request Body (JSON):**

```json
{
    "name": "Smartphone",
    "price": "800.00",
    "stock": 150,
    "category": "Electronics"
}
```

*   **Sample Response (201 Created):**

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

*   **Method:** `GET`
*   **URL:** `/api/products/{id}/` (Replace `{id}` with the product's ID)
*   **Description:** Retrieves details of a specific product.
*   **Request Parameters:**
    *   `id` (integer, path parameter): The unique identifier of the product.
*   **Sample Response (200 OK):**

```json
{
    "id": 1,
    "name": "Laptop",
    "price": "1200.00",
    "stock": 50,
    "category": "Electronics"
}
```

*   **Sample Response (404 Not Found):**

```json
{
    "detail": "Not found."
}
```

#### 4. Update Product Stock

*   **Method:** `PATCH` or `PUT`
*   **URL:** `/api/products/{id}/` (Replace `{id}` with the product's ID)
*   **Description:** Updates the stock quantity of an existing product. `PATCH` is recommended for partial updates.
*   **Request Body (JSON):**

```json
{
    "stock": 45
}
```

*   **Sample Response (200 OK):**

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

*   **Method:** `DELETE`
*   **URL:** `/api/products/{id}/` (Replace `{id}` with the product's ID)
*   **Description:** Deletes a specific product.
*   **Request Parameters:**
    *   `id` (integer, path parameter): The unique identifier of the product to delete.
*   **Sample Response (204 No Content):** (No response body)
*   **Sample Response (404 Not Found):**

```json
{
    "detail": "Not found."
}
```