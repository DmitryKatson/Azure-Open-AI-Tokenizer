import tiktoken

def _get_token_ids(text):
    """Return the ordered ids of the tokens in a text.

    Args:
        text: The string input to tokenize.

    Returns:
        A list of ids corresponding to the tokens in the text, in order they occur
            in the text.
    """
    tokenizer = _get_tokenizer()

    # tokenize the text using the cl100k_base tokenizer
    return tokenizer.encode(text)

def _get_tokenizer():
    return tiktoken.get_encoding("cl100k_base")

def get_num_tokens(text):
    # """Returns the number of tokens in a text string."""
    return len(_get_token_ids(text))

def get_tokens(text):
    """Returns the tokens in a text string."""
    tokenizer = _get_tokenizer()

    tokens_bytes = tokenizer.decode_tokens_bytes(_get_token_ids(text))

    # decode each byte string into a regular string
    tokens_str = [token.decode('utf-8') for token in tokens_bytes]

    return tokens_str
