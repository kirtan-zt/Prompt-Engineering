# Submission Documentation for Prompt Engineering course

To create automated code for crud operations, query generation, test case generation, documentation generation, Google's [gemini-2.5-flash-lite](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash-lite) was used.

## Prompts for crud automation:

### 1. Generate models.py:

```bash
"Generate a single Django model named 'Product' for the 'ecommerce_app'. "
"It must include the following fields: "
"name (CharField, max 100), price (DecimalField with 10 digits and 2 decimal places), "
"stock (IntegerField) and category of the product (CharField, max 100). "
"Implement RegexValidator in name and category so that user can input special character or number"
"Implement MinValueValidator in price and stock such that the value should be more than 0"
"The model must include the required imports and a basic __str__ method."
```

**Reflections**

- In order to generate Django models with all constraints, I have used one-shot-prompting approach in the example response which will exactly tell the AI model to keep the schema accordingly.
- Ensures consistent output formatting

### 2. Generate serializers.py:

```bash
"Generate a ModelSerializer for the Product model, which is defined in models.py."
"The serializer must be named ProductSerializer, inherit from serializers.ModelSerializer,"
"and include all fields ('__all__')."
```

**Reflections**

- In order to generate Django serializers, I have used structured prompting approach which will exactly tell the AI model to import existing model and create serializer accordingly
- Ensures consistent output formatting

### 3. Generate views.py:

```bash
"Generate a ModelViewSet for the Product model, which is defined in models.py."
"Use serializer_class named ProductSerializer, which is defined in serializers.py,"
"Define a class for this viewset named ProductViewSet with necessary queryset and serializer_class arguments"
"Implement basic CRUD functionality in this viewset for Product model"
```

**Reflections**

- In order to generate Django views, I have used Chain-of-Thought prompting approach which will exactly tell the AI model to first go with Viewset method and then map the serializer.
- Improves code reliability

### 4. Generate urls.py

```bash
"Generate project-level urls.py to link the viewsets declared in ecommerce_app, which is defined in views.py."
"Make use of router object that uses DefaultRouter() module to generate URLs, register with r'products'"
```

**Reflections**

- In order to generate Django's project level urls, I have used structured prompting approach which will provide context to AI model to use router from DefaultRouter class

## Prompt for generating ORM query:

```bash
"Write an ORM query to generate a queryset, the query set should return:"
"Fetch all products with stock > 0 and price < 100."
"Sort results by price ascending."
"Return only query code without explanation." \
"Proceed by creating an object of the Product model and then apply conditional parameters"
```

**Reflections**

- In order to generate a ORM query in shell window terminal, I have used structured prompting approach with all the conditions to apply before doing final filter in the objects
- Ensures correct output formatting

## Prompt for generating test cases:

```bash
"Write unit test cases for the Product model using the Django TestCase class. "
"Strictly follow these rules to ensure 100% pass rate:"
"1. VALIDATION STRATEGY:"
"- For all FAILURE scenarios, you MUST instantiate the model (Product(...)) and call `instance.full_clean()` "
"inside a `self.assertRaises(ValidationError)` block. Do not use Product.objects.create() for failures."

"2. SUCCESS SCENARIOS (Ensure these pass):"
"- Name/Category: Use only alphanumeric, spaces, or hyphens (e.g., 'Laptop-Pro 123')."
"- Price: Use a value clearly above the minimum, like 10.99 (The min is 0.01)."
"- Stock: Use a value clearly above the minimum, like 5 (The min is 1)."
"- Assertions: When checking prices, use `self.assertEqual(float(product.price), 10.99)` or `Decimal('10.99')`."

"3. FAILURE SCENARIOS (Ensure these raise ValidationError):"
"- Regex: Test names with symbols like '@', '#', or '$' (Forbidden by r'^[a-zA-Z0-9\s-]+$')."
"- Price: Test with 0.00 and -1.00 (Forbidden by MinValueValidator 0.01)."
"- Stock: Test with 0 and -5 (Forbidden by MinValueValidator 1)."
"- Length: Test name/category longer than 100 characters."

"4. IMPORTS:"
"- from decimal import Decimal"
"- from django.core.exceptions import ValidationError"
"- from .models import Product"
"- DO NOT redefine the Product model."
```

**Reflections**

- In order to generate a ORM query in shell window terminal, I have used Chain-of-Thought prompting approach to provide each and every context, scenario, constraints, etc.
- Reduces hallucination

## Prompt for generating documentation

```bash
"Create a README file for ecommerce_project."
"The README must contain following modules for better understanding:"
"Create an introduction section to brief about the project."
"Main features section to highlight functionality in bullet points."
"There is no user authentication for this Django project, so do not mention that in features"
"Start from setup, cloning the git repo, activating virtual env and installation of django, django-restframework"
"Guide on how to start local server, run tests."
"Create API Reference section for endpoints description for CRUD operations"
"In API reference, include request parameters and sample JSON responses"
"Return the output in Markdown format only."
```

**Reflections**

- In order to generate a ORM query in shell window terminal, I have used Chain-of-Thought prompting approach to provide series of steps to be followed, output format, etc.
- Ensures sequential code generation and structured response
