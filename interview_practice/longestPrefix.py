

def longestPrefix(strsList: list) -> str:
    """
        args: list of strings
        return: string
    """
    str_list = [word.lower() for word in strsList]
    prefix = str_list[0]
    for word in strsList[1 : ]:
        if not word.startswith(prefix):
            prefix = prefix[ : -1]
            if not prefix:
                return ""
    return prefix

strs = ["apple", "appa", "appu"]
res = longestPrefix(strs)
print(res)

