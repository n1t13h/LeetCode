class Solution:
    def reformat(self, s: str) -> str:
        digits = []
        letters = []

        for char in s:
            if char.isdigit():
                digits.append(char)
            elif char.isalpha():
                letters.append(char)

        if abs(len(digits) - len(letters)) not in [0, 1]:
            return ""

        output = ""
        if len(digits) > len(letters):
            for i in range(len(letters)):
                output += digits[i] + letters[i]
            output += digits[-1]
        else:
            for i in range(len(digits)):
                output += letters[i] + digits[i]
            if len(letters) > len(digits):
                output += letters[-1]

        return output
