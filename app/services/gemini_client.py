def analyze_images_with_gemini(image_urls: list[str]) -> dict:
    """
    MOCK Gemini Vision Adapter.

    NOTE:
    Gemini Vision Python SDK is currently unstable / deprecated.
    This adapter simulates a vision-capable model response
    while preserving the full system architecture.

    In production, this adapter can be replaced with
    REST-based Gemini Vision or another multimodal provider.
    """

    # Deterministic, schema-compliant output
    return {
        "visual_dimensions": {
            "gender_expression": 0.0,
            "visual_weight": -1.5,
            "embellishment": -2.5,
            "unconventionality": -0.5,
            "formality": -1.0
        },
        "attributes": {
            "wirecore_visible": None,
            "frame_geometry": "rectangular",
            "transparency": "opaque",
            "dominant_colors": ["white", "gray"],
            "textures": ["smooth"],
            "suitable_for_kids": None
        },
        "confidence": 0.85
    }
