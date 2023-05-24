def capitalize(text):
    if text == '':
        return ''
    first_element = text[0]
    other_elements = text[1:]
    return f'{first_element.upper()}{other_elements}'
