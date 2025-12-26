from pydantic import BaseModel, HttpUrl, Field
from typing import List


class AnalyzeRequest(BaseModel):
    image_urls: List[HttpUrl] = Field(..., min_items=1)
