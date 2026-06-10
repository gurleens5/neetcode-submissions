class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "😄"

        else:
            return "😀".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "😄":
            return []
        elif s == "":
            return [""]
        else:
            return s.split("😀")
