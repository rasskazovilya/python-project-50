from pathlib import Path


def get_contents_suffix(file_path):
    file_path = Path(file_path)
    with open(file_path) as file:
        file_suffix = file_path.suffix.lstrip('.')
        file_content = file.read()
    return file_content, file_suffix
