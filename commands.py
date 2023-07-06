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

    # Используя Deepl код стоило бы заменить на следующий: 
    # auth_key = "api key here"  # Replace with your key
    # translator = deepl.Translator(auth_key)
    # input_language = translator.detected_source_lang(message)

async def translate(message: str) -> str:
    """Translate the message from EN into RU

    Args:
        message(ru): str
    Returns:
        message(en): str
    """

    translator = Translator()
    result = translator.translate(message, dest="ru")
    return result.text

    # Используя Deepl код стоило бы заменить на следующий: 
    # auth_key = "api key here"  # Replace with your key
    # translator = deepl.Translator(auth_key)
    # result = translator.translate_text(message, target_lang="EN")