from collections.abc import Generator
from typing import Any
import requests
import os

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage



class MemosSearch(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:

        user_id = tool_parameters["user_id"]
        query = tool_parameters["query"]
            
        memory_limit_number = int(tool_parameters.get("memory_limit_number", 6))

        data = {
                "user_id":user_id,
                "query":query,
                "memory_limit_number": memory_limit_number,
                "source":"Dify"
                }
        headers = {
            "Authorization": self.runtime.credentials["memos_api_key"]  
        }
        MemOS_url = os.path.join(self.runtime.credentials["memos_url"], "search/memory") 

        response = requests.post(url=MemOS_url, json=data, headers=headers,timeout=5)
        response.raise_for_status()
        valuable_res = response.json()
        
        yield self.create_json_message(valuable_res)