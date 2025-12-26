from pydantic import BaseModel, Field
from typing import List, Optional


class VisualDimensions(BaseModel):
    gender_expression: float = Field(..., ge=-5.0, le=5.0)
    visual_weight: float = Field(..., ge=-5.0, le=5.0)
    embellishment: float = Field(..., ge=-5.0, le=5.0)
    unconventionality: float = Field(..., ge=-5.0, le=5.0)
    formality: float = Field(..., ge=-5.0, le=5.0)


class VisualAttributes(BaseModel):
    wirecore_visible: Optional[bool] = None
    frame_geometry: Optional[str] = None
    transparency: Optional[str] = None
    dominant_colors: List[str] = Field(default_factory=list)
    textures: List[str] = Field(default_factory=list)
    suitable_for_kids: Optional[bool] = None


class VisualMeasurementResponse(BaseModel):
    visual_dimensions: VisualDimensions
    attributes: VisualAttributes
    confidence: float = Field(..., ge=0.0, le=1.0)
