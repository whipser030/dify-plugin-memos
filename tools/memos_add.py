from collections.abc import Generator
from typing import Any
import requests
import json
import random
import os
from datetime import datetime, timezone

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage



class MemosAdd(Tool):
    
    def _get_conversation_id(self) -> str:

        session_date = datetime.now(timezone.utc)
        date_format = "%I:%M %p on %d %B, %Y UTC"
        formatted_date = session_date.strftime(date_format)
        iso_date = session_date.isoformat()


        timestamp_str = str(int(session_date.timestamp()))[-8:]
        random_part = str(random.randint(1000, 9999))
        conversation_id = timestamp_str + random_part
        return iso_date, conversation_id

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        
        user_id= tool_parameters["user_id"]
        conversation_id= tool_parameters.get("conversation_id", None)
        iso_date, conversation_id_new = self._get_conversation_id()
        if conversation_id is None:
            conversation_id = conversation_id_new
            
        messages = [
          {"role": "user", "content": str(tool_parameters.get("user_messages", ""))},
          {"role": "assistant", "content": str(tool_parameters.get("ai_messages", ""))}
        ]

        for item in messages:
            if "chat_time" not in item:
                messages = [{**item, "chat_time": iso_date} for item in messages]
                break

        headers = {
            "Authorization": self.runtime.credentials["memos_api_key"]  
        }

        data = {
                "user_id":user_id,
                "conversation_id":conversation_id,
                "source": "Dify",
                "messages": messages
                }

        MemOS_url = os.path.join(self.runtime.credentials["memos_url"], "add/message") 
        response = requests.post(url=MemOS_url, json=data, headers=headers, timeout=5)
        
        response.raise_for_status()
        valuable_res = response.json()
        yield self.create_json_message(valuable_res)