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
    instructions=dedent(f"""\ """)
)

email_response_generation_agent = Agent(
    name="email response generation agent",
    model=OpenAIChat(id="gpt-4o"),
    role="",
    instructions=dedent(f"""\ """)
)