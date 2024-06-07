class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        rootSet = set(dictionary)

        def findRoot(word):
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in rootSet:
                    return prefix
            return word
        
        words = sentence.split()
        replacedWords = [findRoot(word) for word in words]

        return ' '.join(replacedWords)