from fastapi import APIRouter, HTTPException

from app.schemas.input import AnalyzeRequest
from app.schemas.output import VisualMeasurementResponse
from app.utils.image_validator import is_valid_image_url
from app.services.gemini_client import analyze_images_with_gemini

router = APIRouter()


@router.post("/analyze", response_model=VisualMeasurementResponse)
def analyze_product(request: AnalyzeRequest):
    """
    FINAL ANALYZE ENDPOINT:
    - Validates image URLs
    - Sends images to Gemini Vision
    - Parses strict JSON
    - Returns schema-validated output
    """

    # Step 1: Validate image URLs
    valid_images = [
    str(url) for url in request.image_urls
    if is_valid_image_url(str(url))
]


    if not valid_images:
        raise HTTPException(
            status_code=400,
            detail="No valid image URLs provided"
        )

    # Step 2: Call Gemini Vision (returns dict)
    try:
        gemini_result = analyze_images_with_gemini(valid_images)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Gemini Vision error: {str(e)}"
        )

    # Step 3: Validate against schema (CRITICAL)
    try:
        return VisualMeasurementResponse(**gemini_result)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Invalid AI response structure: {str(e)}"
        )
