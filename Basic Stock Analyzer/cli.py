import asyncio
import sys
import time
from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from agent import AgentDriver
from utils.utilities import get_google_api_key, mask_api_key


class CLIOrchestrator:
    def __init__(self):
        self.agent_driver = AgentDriver()
        self.root_agent = self.agent_driver.get_root_agent()
        self.app_name = self.agent_driver.get_agent_info()["name"]
        
        self.google_api_key = get_google_api_key()
        if not self.google_api_key:
            print("[__error__] Error: GOOGLE_API_KEY environment variable not set.")
            sys.exit(1)

        print(f" [__info__] Using Google API Key: {mask_api_key(self.google_api_key)}")

    async def analyze_stock(self, company: str):
        session_service = InMemorySessionService()
        session = await session_service.create_session(
            app_name=self.app_name,
            user_id="cli_user",
        )
        runner = Runner(
            agent=self.root_agent,
            session_service=session_service,
            app_name=self.app_name,
        )

        query = f"Analyze {company} stock. Should I invest in it? Provide a comprehensive analysis."
        content = types.Content(
            role="user",
            parts=[types.Part(text=query)],
        )

        print(f"\n[__query__] Analyzing {company}...\n")
        print("[__query__] This may take a few minutes as we gather and analyze data.")

        result = ""
        search_count = 0

        async for event in runner.run_async(
            session_id=session.id,
            user_id="cli_user",
            new_message=content,
        ):
            if hasattr(event, 'content') and hasattr(event.content, 'parts'):
                for part in event.content.parts:
                    function_call = getattr(part, "function_call", None)
                    function_response = getattr(part, "function_response", None)

                    if function_call and hasattr(function_call, "name"):
                        if function_call.name == "google_search":
                            search_count += 1
                            print(f"\n[__info__] Performing Google Search #{search_count}: Finding information......\n")
                        elif function_response:
                            print(f"\n[__info__] Received response from {function_call.name}......\n")

                    if hasattr(part, 'text') and part.text and not getattr(event, 'partial', False):
                        result = part.text

        return result

    async def run_cli(self):
        print("\n============================================")
        print("[|__|] BASIC STOCK ANALYZER - CLI INTERFACE [|__|]")
        print("============================================")

        if len(sys.argv) > 1:
            company = sys.argv[1]
        else:
            company = input("\nEnter a company name to analyze (or press Enter for Microsoft): ").strip()
            if not company:
                company = "Microsoft"

        try:
            start_time = time.time()
            result = await self.analyze_stock(company=company)
            end_time = time.time()
            print("\n============================================")
            print(f"ANALYSIS COMPLETED IN {round(end_time - start_time, 1)} SECONDS")
            print("============================================")
            print(result)
        except Exception as e:
            print(f"\n[__error__] An error occurred: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(CLIOrchestrator().run_cli())

