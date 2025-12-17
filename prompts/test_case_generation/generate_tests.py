from utils.config import get_gemini_client, DEFAULT_MODEL, handle_api_error
from loguru import logger
import os
from google.genai import types

client = get_gemini_client()

def generate_tests_code(user_request: str, component: str):
    """
    Sends a request to Gemini to generate test cases for Django component.
    """

    # SYSTEM INSTRUCTION
    system_instruction=f"""
        You are an experienced QA Engineer, having expertise in testing Django applications.
        Your task is to generate unit test cases using TestCase module with failure and success scenarios.

        IMPORTANT: Django model validators are NOT triggered on save() or create(). 
        For all failure test scenarios involving field validation, you MUST:
        1. Instantiate the model without saving it to the database.
        2. Wrap the `model_instance.full_clean()` call within `self.assertRaises(ValidationError)`.

        CONSTRAINTS:
        1. The output MUST contain ONLY the final Python code.
        2. DO NOT include any explanatory text, comments outside of standard docstrings, or markdown code fences.
        3. The code must be self-contained and ready to be pasted directly into a Django file.
        4. The requested component is a Django {component}.
    """
    
    user_prompt=f"Generate the necessary Python code for the following Django {component}:\n\nTASK: {user_request}"

    for attempt in range(3):
        try:
            response=client.models.generate_content(
            model=DEFAULT_MODEL,
            contents=[
                types.Content(role="user", parts=[types.Part(text=user_prompt)]),
            ],
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.1
            ) 
        )
            return response.text.strip()
        except Exception as e:
            if not handle_api_error(e, attempt):
                raise e
    
if __name__=='__main__':
    test_request=(
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
    )
    logger.info("--- GENERATING DJANGO TEST CASES CODE ---")
    
    generated_code = generate_tests_code(
        user_request=test_request,
        component="testcases",
    )
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    if generated_code:
        logger.info("--- GENERATED CODE ---")
        models_file_path = os.path.abspath(os.path.join(
        current_script_dir,'../../ecommerce_project/ecommerce_app/tests.py'))
        with open(models_file_path, 'w') as f:
            f.write(generated_code)
        logger.success(f"Code successfully written to: {models_file_path}")
    else:
        logger.error("Failed to generate code.")