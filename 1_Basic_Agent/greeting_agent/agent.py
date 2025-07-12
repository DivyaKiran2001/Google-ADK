from google.adk.agents import Agent

root_agent =  Agent(
    name="Greeting_Agent",
    description="A simple agent that greets the user.",
    model="gemini-1.5-pro",
    instruction="""
        You are a helpful assistant that greets the user.Ask for the user's name and greet them by name.
    """
)