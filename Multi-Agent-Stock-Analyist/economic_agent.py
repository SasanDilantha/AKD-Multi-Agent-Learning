from google.adk.agents import LlmAgent
from google.adk.tools import google_search_tool
from utils.utilities import get_model_name


class EconomicAgent:
    def __init__(self):
        self.model_name = get_model_name()
        self.agent_name ="economic_analyst"
        self.agent_description = "Analyzes the macroeconomic environment relevant to a company."
        self.prompt =("""
            You are an economic analyst. Use the google_search tool to find information on current macroeconomic factors relevant to the specified company and its industry.

            Company: [Company Name]

            Consider factors such as:
            *   Interest rate trends and their potential impact on borrowing costs and investment.
            *   Inflation rates and their effect on costs and consumer purchasing power.
            *   GDP growth (or contraction) and its relation to overall market demand.
            *   Supply chain conditions affecting the company's operations.
            *   Consumer spending patterns relevant to the company's products/services.
            *   Currency exchange rate fluctuations if the company has international operations.
            *   Key industry-specific economic indicators.

            For each identified factor, briefly explain its current state and specifically how it might positively or negatively impact the company.
            Present the findings as a concise summary report. Output ONLY the report content.
        """).strip()
        

    def create_agent(self) -> LlmAgent:
        return LlmAgent(
            name=self.agent_name,
            model=self.model_name,
            description=self.agent_description,
            instruction=self.prompt,
            tools=[google_search_tool]
        )