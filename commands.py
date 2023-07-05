from googletrans import Translator


async def check_language(message: str) -> str | None:
    """Defines the language of the message

    Args:
        message: str
    Returns:
        language code: str or None
    """
    translator = Translator()
    input_language = translator.detect(message)
    return input_language.lang


async def translate(message: str) -> str:
    """Translate the message from RU into EN

    Args:
        message(ru): str
    Returns:
        message(en): str
    """

    translator = Translator()
    result = translator.translate(message, dest="en")
    return result.text
