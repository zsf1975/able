from typing import Any, Union


def force_convertible_to_java_array(
        value: Any
) -> Union[list, tuple, bytes, bytearray]:
    """Construct a value that is convertible to a Java array.

    >>> force_convertible_to_java_array(['314'])
    ['314']
    >>> force_convertible_to_java_array('314')
    ['3', '1', '4']
    >>> force_convertible_to_java_array(314)
    [314]
    >>> force_convertible_to_java_array(0)
    [0]
    >>> force_convertible_to_java_array('')
    []
    >>> force_convertible_to_java_array(None)
    []
    """
    if isinstance(value, (list, tuple, bytes, bytearray)):
        return value
    try:
        return list(value)
    except TypeError:
        if value is None:
            return []
    return [value]
