from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat

email_classification_agent = Agent(
    name="email classification agent",
    model=OpenAIChat(id="gpt-4o"),
    role="you are a email classification agent, who can classify the email to the given categories.",
    instructions=dedent(f"""\
        Classify the following customer email into exactly one of these categories:
        - Subscription
        - Dissatisfaction  
        - MoneyRefund
        Respond with only the category name, nothing else.\
    """)
)

email_content_extractor_agent = Agent(
    name="email content extractor agent",
    model=OpenAIChat(id="gpt-4o"),
    role="",
    instructions=dedent(f"""
        Scenario-1
        Extract the following information from the given subscription email:
        - transaction_number: The transaction number (e.g., "PAY-2024-001")
        - amount: The total amount mentioned (without $ or ₹ sign, e.g., "299.99")
            
        Respond with valid JSON only, like:
        {{"transaction_number": "PAY-2024-001", "amount": "299.99"}}
        
        Scenario-2:
        Extract the following information from the given subscription email:
        - transaction_number: The transaction number (e.g., "PAY-2024-001")
        - amount: The total amount mentioned (without $ or ₹ sign, e.g., "299.99")
            
        Respond with valid JSON only, like:
        {{"transaction_number": "PAY-2024-001", "amount": "299.99"}}
        
        Scenario-3:
        Extract the following information from the given subscription email:
        - transaction_number: The transaction number (e.g., "PAY-2024-001")
        - amount: The total amount mentioned (without $ or ₹ sign, e.g., "299.99")
            
        Respond with valid JSON only, like:
        {{"transaction_number": "PAY-2024-001", "amount": "299.99"}}
        
        If a field is not found, use null.
        """)
)

email_response_generation_agent = Agent(
    name="email response generation agent",
    model=OpenAIChat(id="gpt-4o"),
    role="",
    instructions=dedent(f"""\ """)
)