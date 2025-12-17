from utils.config import get_gemini_client, DEFAULT_MODEL, handle_api_error
from loguru import logger
from google.genai import types
import os

client = get_gemini_client()

def generate_views_code(user_request: str, component: str):
    """
    Sends a request to Gemini to generate class based views Django component.
    """

    # SYSTEM INSTRUCTION
    system_instruction=f"""
        You are an experienced Django developer.
        Your task is to generate complete, clean, and idiomatic Python code for the requested Django component.

        You have already defined models.py, serializers.py now it's time you make use of these and create class based views.

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
    views_request=(
        "Generate a ModelViewSet for the Product model, which is defined in models.py."
        "Use serializer_class named ProductSerializer, which is defined in serializers.py,"
        "Define a class for this viewset named ProductViewSet with necessary queryset and serializer_class arguments"
        "Implement basic CRUD functionality in this viewset for Product model"
    )
    logger.info("--- GENERATING DJANGO VIEWS.PY CODE ---")
    
    generated_code = generate_views_code(
        user_request=views_request,
        component="viewsets",
    )
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    if generated_code:
        logger.info("--- GENERATED CODE ---")
        models_file_path = os.path.abspath(os.path.join(
        current_script_dir,'../../ecommerce_project/ecommerce_app/views.py'))
        with open(models_file_path, 'w') as f:
            f.write(generated_code)
        logger.success(f"Code successfully written to: {models_file_path}")
    else:
        logger.error("Failed to generate code.")