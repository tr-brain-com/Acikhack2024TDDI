from typing import List, Optional
from pydantic import BaseModel


class ResponseContent(BaseModel):
    text: Optional[str] = ""