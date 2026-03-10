from google.adk.agents import LlmAgent
from google.adk.tools import google_search_tool
from utils.utilities import get_model_name

class NewsAgent:
    def __init__(self):
        self.model_name = get_model_name()
        self.agent_name ="news_reporter"
        self.agent_description = "Gathers recent news headlines for a company."
        self.prompt =("""
            You are a financial news reporter. Use the google_search tool to find 5 recent news headlines about the specified company that are relevant to its financial performance or stock valuation. Include publication dates if available.

            Company: [Company Name]

            For each headline, provide a brief (1-2 sentence) summary and indicate the likely sentiment (Positive, Negative, Neutral) towards the company's stock.
            Present the information as a numbered list. Output ONLY the numbered list of headlines, summaries, and sentiments.
            Provide a concise overall summary of the news sentiment if possible.
        """).strip()
        

    def create_agent(self) -> LlmAgent:
        return LlmAgent(
            name=self.agent_name,
            model=self.model_name,
            description=self.agent_description,
            instruction=self.prompt,
            tools=[google_search_tool]
        )