# tools/search_tools.py
import json
import os
import requests
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class SearchInternetInput(BaseModel):
    """Input schema for SearchInternetTool."""
    query: str = Field(..., description="Search query for finding relevant information")

class SearchInternetTool(BaseTool):
    name: str = "search_internet"
    description: str = "Search the internet for a topic and return results"
    args_schema: Type[BaseModel] = SearchInternetInput

    def _run(self, query: str) -> str:
        """Search the internet for a topic and return results"""
        top_result_to_return = 5
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query, "num": top_result_to_return, "tbm": "nws"})
        headers = {'X-API-KEY': os.environ.get('SERPER_API_KEY', ''), 'content-type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        data = response.json()
        if 'organic' not in data:
            return "No results found or API key problem."
        results = data['organic']
        output = []
        for result in results[:top_result_to_return]:
            date = result.get('date', 'Date not available')
            output.append(f"Title: {result['title']}\nLink: {result['link']}\nDate: {date}\nSnippet: {result['snippet']}\n---")
        return "\n".join(output)

# Create an instance of the tool
search_internet = SearchInternetTool()
