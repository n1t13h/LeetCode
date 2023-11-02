class Solution:
    def findWords(self, words):
        keyboard_rows = [
            set('qwertyuiop'),
            set('asdfghjkl'),
            set('zxcvbnm')
        ]

        result = []
        for word in words:
            word_set = set(word.lower())
            for row in keyboard_rows:
                if word_set.issubset(row):
                    result.append(word)
                    break

        return result
