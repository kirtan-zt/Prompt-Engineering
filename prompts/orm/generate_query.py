from utils.config import get_gemini_client, DEFAULT_MODEL, handle_api_error
from loguru import logger
import os
from google.genai import types

client = get_gemini_client()

def generate_query_code(user_request: str, component: str):
    """
    Sends a request to Gemini to generate ORM query to fetch objects from database.
    """

    # SYSTEM INSTRUCTION
    system_instruction=f"""
        You are an experienced Django developer.
        Your task is to generate raw ORM query for the requested filters for products component.

        After defining models, views, urls, we are done with crud functionality. 
        Our next task is to generate ORM query for performing database operations. 

        CONSTRAINTS:
        1. The output MUST contain ONLY the final ORM query that returns Queryset.
        2. DO NOT include any explanatory text, comments outside of standard docstrings, or markdown code fences.
        3. The code must be self-contained and ready to be pasted directly into a python manage.py shell window.
        4. The requested component is an query filter to be fetched by an ORM object {component}.
        """
    
    user_prompt=f"Generate the necessary query for the following conditional object {component}:\n\nTASK: {user_request}"

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
    query_request=(
        "Write an ORM query to generate a queryset, the query set should return:"
        "Fetch all products with stock > 0 and price < 100."
        "Sort results by price ascending."
        "Return only query code without explanation." \
        "Proceed by creating an object of the Product model and then apply conditional parameters"
    )
    logger.info("--- GENERATING DJANGO ORM QUERY CODE ---")
    
    generated_code = generate_query_code(
        user_request=query_request,
        component="querysets",
    )
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    if generated_code:
        logger.info("--- GENERATED CODE ---")
        models_file_path = os.path.abspath(os.path.join(
        current_script_dir,'../../orm-querysets/raw_query.txt'))
        with open(models_file_path, 'w') as f:
            f.write(generated_code)
        logger.success(f"Code successfully written to: {models_file_path}")
    else:
        logger.error("Failed to generate code.")