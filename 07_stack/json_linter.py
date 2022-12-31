def validate_format(chars: str) -> bool:
    lookup = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for char in chars:
        if char in lookup:  # keys
            stack.append(lookup[char])
        if char in lookup.values():
            if not stack:
                return False
            if char != stack.pop():
                return False
    if stack:
        return False

    return True


if __name__ == "__main__":
    j_normal = "{'key1': 'value', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}"
    print(validate_format(j_normal))
    j_missing = "{'key1': 'value', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}}"
    print(validate_format(j_missing))
    j_mismatch = "{'key1': ['value', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}"
    print(validate_format(j_mismatch))
    j_left = "{'key1': 'value', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}{"
    print(validate_format(j_left))
