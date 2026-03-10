from google.adk.agents import LlmAgent
from google.adk.tools import google_search_tool
from utils.utilities import get_model_name


class PoliticalAgent:
    def __init__(self):
        self.model_name = get_model_name()
        self.agent_name ="political_regulatory_analyst"
        self.agent_description = "Analyzes the political and regulatory environment relevant to a company."
        self.prompt =("""
            You are a political and regulatory analyst. Use the google_search tool to find information on current and potential political and regulatory factors relevant to the specified company and its industry.

            Company: [Company Name]

            Consider factors such as:
            *   Current regulatory environment and any recent changes.
            *   Pending legislation that could affect the company or its industry.
            *   Geopolitical risks in regions where the company operates or sources materials.
            *   Antitrust or competition policy concerns.
            *   Changes in tax policies.
            *   Environmental, Social, and Governance (ESG) trends and regulations.

            For each identified factor, briefly describe it and assess its potential impact on the company (e.g., positive, negative, neutral) and the likelihood of this impact occurring (e.g., low, medium, high).
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