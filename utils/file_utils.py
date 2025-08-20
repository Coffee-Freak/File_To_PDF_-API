VALID_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif', '.tiff')

def is_valid_image(filename: str) -> bool:
    """
    Check if the file has a valid image extension
    """
    return filename.lower().endswith(VALID_EXTENSIONS)
