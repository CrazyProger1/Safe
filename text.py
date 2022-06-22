def reduce_text(text: str, length: int = 20):
    if len(text) > length:
        text = "".join(text[:length]) + "..."

    return text
