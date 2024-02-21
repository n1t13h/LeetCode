class Solution:
    def gcdOfStrings(self,str1: str, str2: str) -> str:
        """
        Finds the greatest common divisor (GCD) of two strings.

        Args:
            str1: The first string.
            str2: The second string.

        Returns:
            The GCD of the strings, or an empty string if no GCD exists.
        """

        if str1 + str2 != str2 + str1:
            return ""

        GCD_length = gcd(len(str1), len(str2))
        return str1[:GCD_length] if str1[:GCD_length] == str2[:GCD_length] else ""
