from google.adk.agents import LlmAgent
from google.adk.tools import google_search_tool
from utils.utilities import get_model_name


class HistoricalAgent:
    def __init__(self):
        self.model_name = get_model_name()
        self.agent_name ="historical_stock_analyst"
        self.agent_description = "Analyzes the historical stock performance of a company."
        self.prompt =("""
            You are a detailed historical stock analyst. Use the google_search tool to find information on the company's stock performance over the past 2 years.

            Company: [Company Name]

            Focus on the following aspects:
            *   **Price Trends:** Identify major upward or downward trends, and periods of consolidation.
            *   **Key Support and Resistance Levels:** Note any significant price levels the stock has struggled to break above or fall below.
            *   **Volatility:** Describe the stock's price volatility (e.g., low, moderate, high) compared to its sector or the broader market, if possible.
            *   **Comparison to Index/Peers:** Briefly compare its performance to a major relevant market index (e.g., S&P 500, NASDAQ) and key competitors, if this information is readily available.
            *   **Major Events Impact:** Identify any specific company or market events that visibly impacted the stock price (e.g., earnings reports, product launches, economic news).
            *   **Key Percentage Changes:** Highlight significant percentage gains or losses during specific periods.

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