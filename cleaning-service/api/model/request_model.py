from typing import Optional
from pydantic import BaseModel


class RequestContent(BaseModel):
    text: Optional[str] = ""
    constraction: Optional[bool] = True
    stopword: Optional[bool] = False