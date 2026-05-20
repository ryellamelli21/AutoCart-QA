import os
from openai import OpenAI
from dotenv import load_dotenv
from ai.prompt_templates import FAILURE_ANALYSIS_PROMPT

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_failure(failure_log):
    prompt = FAILURE_ANALYSIS_PROMPT.format(failure_log = failure_log)

    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role":"system", "content":"You are an expert QA Automation Engineer."},
            {"role":"user", "content":"prompt"}
        ]
    )

    return response.choices[0].message.content