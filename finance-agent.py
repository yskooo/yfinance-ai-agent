from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv
load_dotenv(override=True)

web_search_agent = Agent(
    name="web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources of references."],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(
            stock_price=True,
            stock_fundamentals=True,
            analyst_recommendations=True,
            company_news=True,
            company_info=True
        )
    ],
    instructions=["Always use tables to display the data."],
    show_tools_calls=True,
    markdown=True
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Always provide the news along with its source.",
        "Always provide tables to show the data."
    ],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response(
    "Summarize analyst recommendation and share the latest news for Meta",
    stream=True
)
