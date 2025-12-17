from utils.config import get_gemini_client, DEFAULT_MODEL, handle_api_error
from loguru import logger
from google.genai import types
import os

client = get_gemini_client()

def generate_readme_code(user_request: str, component: str, example_code: str=""):
    """
    Sends a request to Gemini to generate documentation for Django component.
    """

    # SYSTEM INSTRUCTION
    system_instruction=f"""
        You are an experienced Django developer.
        Your task is to generate a complete, clean, and professional README.md for an E-commerce project.

        Create a README.md file for detailed explanation on Django project.

        CONSTRAINTS:
        1. Output ONLY the raw Markdown content.
        2. DO NOT wrap the output in markdown code fences like ```markdown.
        3. DO NOT include any introductory or concluding remarks (e.g., "Here is your file").
        4. Use professional technical writing style.
        """
    full_prompt = f"""
    TECHNICAL CONTEXT:
    Schema: Name(CharField), Price(DecimalField), Stock(IntegerField), Category(CharField)
    Repo: https://github.com/kirtan-zt/Prompt-Engineering.git
    CRUD: Fetch all, Create/Categorize, Update Stock, Delete.
    API: DefaultRouter, r'products' registered at path('api/').

    INSTRUCTIONS FOR README:
    {user_request}
    {f"REFERENCE EXAMPLE STYLE: {example_code}" if example_code else ""}
    """
    user_prompt=f"Generate the necessary README.md code for the following Django project {component}:\n\nTASK: {user_request}"

    for attempt in range(3):
        try:
            response=client.models.generate_content(
            model=DEFAULT_MODEL,
            contents=[
                types.Content(role="user", parts=[types.Part(text=full_prompt)]),
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
    docs_request=(
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
    )
    logger.info("--- GENERATING DOCUMENTATION FOR DJANGO APPLICATION ---")
    
    generated_code = generate_readme_code(
        user_request=docs_request,
        component="README",
    )
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    if generated_code:
        logger.info("--- GENERATED CODE ---")
        models_file_path = os.path.abspath(os.path.join(
        current_script_dir,'../../README.md'))
        with open(models_file_path, 'w') as f:
            f.write(generated_code)
        logger.success(f"Code successfully written to: {models_file_path}")
    else:
        logger.error("Failed to generate code.")