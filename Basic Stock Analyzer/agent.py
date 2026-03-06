from google.adk.agents import Agent
from google.adk.tools import google_search
import threading


class AgentDriver:
    __instance = None
    __lock = threading.Lock()

    __name : str = "basic_stock_analyzer"
    __description : str = "A comprehensive stock analysis agent that provides investment recommendations"
    __model : str = "gemini-2.5-flash"

    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super(AgentDriver, cls).__new__(cls)

        return cls.__instance
    
    def __create_root_prompt(self):
        return ("""
            You are a comprehensive stock analysis agent. When asked about a company, provide a detailed investment analysis that covers:

            1. RECENT NEWS: Use google_search to find 5 recent news headlines about the company with publication dates.
            2. HISTORICAL ANALYSIS: Analyze stock performance, trends, technicals, events, and valuation.
            3. ECONOMIC ANALYSIS: Assess rates, inflation, GDP, supply chain, consumer trends, and more.
            4. POLITICAL/REGULATORY ANALYSIS: Review regulations, policy, risks, and ESG factors.
            5. INVESTMENT RECOMMENDATION: Provide Buy/Hold/Sell, risk level, target price, and rationale.

            Always start your analysis with a clear statement of which company you're analyzing.
        """).strip()
    
    def get_root_agent(self):
        if not hasattr(AgentDriver, "__root_agent"):
            AgentDriver.__root_agent = Agent(
                model=self.__model,
                name=self.__name,
                description=self.__description,
                instruction=self.__create_root_prompt(),
                tools=[google_search],
            )
        return AgentDriver.__root_agent
    
    def get_agent_info(self)->dict:
        return {
            "name": self.__name,
            "description": self.__description,
            "model": self.__model,
        }
    
