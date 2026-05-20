FAILURE_ANALYSIS_PROMPT = """
You are a senior QA Automation Engineer.

Analyze the following Selenium/Pytest failure log:

{failure_log}

Provide:
1. Root Cause
2. Likely Reason
3. Suggested Fix
4. Severity Level
5. Whether this is likely flaky or genuine
"""


def analyze_failure(failure_log):
    """
    Placeholder AI analysis function.
    Later this can be connected to Gemini or Claude API.
    """
    
    formatted_prompt = FAILURE_ANALYSIS_PROMPT.format(
        failure_log=failure_log
    )

    return f"""
AI Failure Analysis Report
--------------------------
Prompt Sent To AI:
{formatted_prompt}

Temporary Local Analysis:
- Root Cause: Possible locator issue / timeout / stale element
- Likely Reason: UI change, synchronization issue, or browser inconsistency
- Suggested Fix: Review locators, waits, and page transitions
- Severity Level: Medium
- Type: Could be flaky depending on reproducibility
"""