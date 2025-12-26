from urllib.parse import urlparse


def is_valid_image_url(url: str) -> bool:
    """
    Validates whether a URL is likely to be an image URL
    based purely on its structure (no network calls).

    Accepts common image extensions appearing anywhere
    in the URL path (CDN-safe).
    """

    # Basic type and empty check
    if not url or not isinstance(url, str):
        return False

    parsed = urlparse(url)

    # Must be a web URL
    if parsed.scheme not in ("http", "https"):
        return False

    # Common image extensions
    image_extensions = (
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".gif"
    )

    path_lower = parsed.path.lower()

    # Allow extensions anywhere in path (important for CDNs)
    return any(ext in path_lower for ext in image_extensions)
