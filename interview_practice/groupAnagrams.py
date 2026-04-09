from collections import defaultdict

def groupAnagrams(strsList: list) -> list:
    """
        args : list of strings
        return : nested list
    """
    defDict = defaultdict(list)
    for word in strsList:
        defDict["".join(sorted(word))].append(word)
        print(defDict)
    return defDict

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])  

    
def groupingOfAnagrams(strList):
    d = defaultdict(list)
    for word in strList:
        d["".join(sorted(word))].append(word)    
    return d

groupingOfAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])