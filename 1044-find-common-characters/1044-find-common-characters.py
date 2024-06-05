class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        cnt = Counter(words[0])

        for w in words:
            cur_count = Counter(w)
            for char in cnt:
                cnt[char]=min(cnt[char],cur_count[char])
        
        res = []
        for c in cnt:
            for i in range(cnt[c]):
                res.append(c)
        return res

        