def center_text(ch_limit, text, text_len):
    """
    Return the text centered according to the space limit

    param: text_len
    """
    if ch_limit == text_len:
        return text

    center = int(ch_limit / 2 + 0.5)
    sep = center - int(text_len / 2 + 0.5)
    if text_len % 2 == 0:
        return sep * ' ' + text + (sep - 1) * ' '
    return sep * ' ' + text + sep * ' '
