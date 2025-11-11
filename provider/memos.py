from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from tools.memos_add import MemosAdd
from tools.memos_search import MemosSearch


class MemosProvider(ToolProvider):
    
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            MEMOS_URL = credentials.get("memos_url","")
            MEMOS_API_KEY = credentials.get("memos_api_key","")

            if not MEMOS_URL or not MEMOS_API_KEY:
                raise ToolProviderCredentialValidationError("MEMOS URL and API key are required.")

        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
