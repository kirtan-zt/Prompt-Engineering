from utils.config import get_gemini_client, DEFAULT_MODEL, handle_api_error
from loguru import logger
from google.genai import types
import os

client = get_gemini_client()

def generate_model_code(user_request: str, component: str, example_code: str) -> str:
    """
    Sends a request to Gemini, including a one-shot example, to generate 
    a specific Django component.
    """
    
    # Define the SYSTEM INSTRUCTION 
    system_instruction = f"""
    You are an expert Django developer and a Python code generator.
    Your task is to generate complete, clean, and idiomatic Python code for the requested Django component.
    
    You will be given a one-shot example to demonstrate the required output style, structure, and syntax.

    CONSTRAINTS:
    1. The output MUST contain ONLY the final Python code.
    2. DO NOT include any explanatory text, comments outside of standard docstrings, or markdown code fences.
    3. The code must be self-contained and ready to be pasted directly into a Django file.
    4. The requested component is a Django {component}.
    5. The new code MUST strictly follow the style and syntax of the provided example.
    """
    
    # 2. Constructing the Multi-Part Conversation (One-Shot Example)
    # We structure the prompt as a conversation: User provides the generic prompt and example, Model provides the correct code.
    
    # Part 1: Initial User Prompt (Requesting the style/example)
    example_prompt = f"""
    Here is a one-shot example of a Django Model:

    --- EXAMPLE TASK ---
    Create a model for a product with name, price, stock, and category fields.

    --- EXAMPLE CODE ---
    {example_code}
    """
    
    # Part 2: The model "responds" with the correct code for the example
    model_response_example = f"""
    {example_code}
    """
    
    # Part 3: The FINAL User Prompt (The actual task you want completed)
    final_user_prompt = f"Now, generate the necessary Python code for the following Django {component}:\n\nTASK: {user_request}"

    for attempt in range(3):
        try:
            response = client.models.generate_content(
            model=DEFAULT_MODEL,
            # We pass the history of the "conversation" to the model
            contents=[
                # System Instruction
                types.Content(
                    role="user", 
                    parts=[types.Part(text=example_prompt)] 
                ), 
                # 1. The One-Shot Example Turn (Model's simulated response)
                types.Content(
                    role="model", 
                    parts=[types.Part(text=model_response_example)] 
                ), 
                
                # 2. The Final Generation Turn (User)
                types.Content(
                    role="user", 
                    parts=[types.Part(text=final_user_prompt)] 
                ), 
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
    
if __name__ == "__main__":
    
    # The One-Shot Example Code (Used for style/format)
    one_shot_example = """
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.CharField(max_length=100)
"""
    model_request = (
        "Generate a single Django model named 'Product' for the 'ecommerce_app'. "
        "It must include the following fields: "
        "name (CharField, max 100), price (DecimalField with 10 digits and 2 decimal places), "
        "stock (IntegerField) and category of the product (CharField, max 100). "
        "Implement RegexValidator in name and category so that user can input special character or number"
        "Implement MinValueValidator in price and stock such that the value should be more than 0"
        "The model must include the required imports and a basic __str__ method."
    )
    
    logger.info("--- GENERATING SINGLE DJANGO MODEL CODE WITH ONE-SHOT EXAMPLE ---")
    
    generated_model_code = generate_model_code(
        user_request=model_request,
        component="models",
        example_code=one_shot_example  # Pass the example here
    )
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    if generate_model_code:
        logger.info("--- GENERATED CODE ---")
        models_file_path = os.path.abspath(os.path.join(
        current_script_dir, 
        '../../ecommerce_project/ecommerce_app/models.py'
    ))
        with open(models_file_path, 'w') as f:
            f.write(generated_model_code)
        logger.success(f"Code successfully written to: {models_file_path}")
    else:
        logger.error("Failed to generate code.")