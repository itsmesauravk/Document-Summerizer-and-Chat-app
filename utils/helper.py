import os

def clean_text(text: str) -> str:
    """
    Clean text by removing extra whitespace and non-printable characters.
    
    Args:
        text: The text to clean
        
    Returns:
        The cleaned text
    """
    # Remove extra whitespace
    text = " ".join(text.split())
    
    # Remove non-printable characters
    text = "".join(char for char in text if char.isprintable() or char in ['\n', '\t'])
    
    return text

def get_file_extension(file_path: str) -> str:
    """
    Get the file extension from a file path.
    
    Args:
        file_path: The file path
        
    Returns:
        The file extension
    """
    _, extension = os.path.splitext(file_path)
    return extension.lower()