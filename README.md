# E-commerce Product Management API

This project implements a simple E-commerce Product Management API using Django and Django REST Framework. It provides a robust backend for managing product information, including creation, retrieval, updating, and deletion of product records.

## Introduction

The E-commerce Product Management API is designed to offer a straightforward interface for handling product data. It allows users to manage product inventory efficiently through a set of RESTful endpoints. The API focuses on core product attributes such as name, price, stock quantity, and category, making it suitable for integration into various e-commerce platforms or inventory management systems.

## Main Features

- **Product Listing**: Retrieve a comprehensive list of all available products.
- **Product Creation**: Add new products to the inventory with details like name, price, stock, and category.
- **Product Categorization**: Assign categories to products during creation for better organization.
- **Stock Management**: Update the stock quantity for existing products.
- **Product Details**: Fetch specific product information using its unique identifier.
- **Product Deletion**: Remove products from the inventory.

## Setup

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository

First, clone the project repository from GitHub:

```bash
git clone https://github.com/kirtan-zt/Prompt-Engineering.git
cd Prompt-Engineering/ecommerce_project # Navigate into the project directory
```

### 2. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

Install Django and Django REST Framework along with any other required packages:

```bash
pip install django djangorestframework
```

### 4. Run Migrations

Apply the database migrations to create the necessary tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Running the Application

### Start the Local Server

Once the setup is complete, you can start the Django development server:

```bash
python manage.py runserver
```

The API will now be accessible at `http://127.0.0.1:8000/`.

### Run Tests

To ensure all components are working as expected, run the project's test suite:

```bash
python manage.py test
```

## API Reference

The API endpoints are accessible under the `/api/` path. All endpoints return JSON responses.

### Base URL

`http://127.0.0.1:8000/api/products/`

---

### 1. List all Products

Retrieves a list of all products in the inventory.

- **URL**: `/api/products/`
- **Method**: `GET`
- **Request Parameters**: None
- **Sample Response (200 OK)**:

  ```json
  [
    {
      "id": 1,
      "name": "Laptop Pro",
      "price": "1200.00",
      "stock": 50,
      "category": "Electronics"
    },
    {
      "id": 2,
      "name": "Wireless Mouse",
      "price": "25.50",
      "stock": 200,
      "category": "Accessories"
    }
  ]
  ```

---

### 2. Create a Product

Adds a new product to the inventory.

- **URL**: `/api/products/`
- **Method**: `POST`
- **Request Body**:

  ```json
  {
    "name": "Mechanical Keyboard",
    "price": "75.00",
    "stock": 150,
    "category": "Accessories"
  }
  ```

- **Sample Response (201 Created)**:

  ```json
  {
    "id": 3,
    "name": "Mechanical Keyboard",
    "price": "75.00",
    "stock": 150,
    "category": "Accessories"
  }
  ```

---

### 3. Retrieve a Single Product

Fetches details for a specific product by its ID.

- **URL**: `/api/products/{id}/`
- **Method**: `GET`
- **Request Parameters**: None
- **Sample Response (200 OK)**:

  ```json
  {
    "id": 1,
    "name": "Laptop Pro",
    "price": "1200.00",
    "stock": 50,
    "category": "Electronics"
  }
  ```

---

### 4. Update Product Stock

Updates the stock quantity (or any other field) for an existing product.
For partial updates (e.g., only stock), use `PATCH`. For full replacement, use `PUT`.

- **URL**: `/api/products/{id}/`
- **Method**: `PATCH`
- **Request Body (for updating stock)**:

  ```json
  {
    "stock": 45
  }
  ```

- **Sample Response (200 OK)**:

  ```json
  {
    "id": 1,
    "name": "Laptop Pro",
    "price": "1200.00",
    "stock": 45,
    "category": "Electronics"
  }
  ```

---

### 5. Delete a Product

Removes a product from the inventory.

- **URL**: `/api/products/{id}/`
- **Method**: `DELETE`
- **Request Parameters**: None
- **Sample Response (204 No Content)**:
  (No content is returned upon successful deletion)
# Prompt-Engineering
