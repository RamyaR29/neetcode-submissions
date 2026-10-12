class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        wordlist = []
        for each in strs:
            word = ""
            num = len(each)
            word = str(num)+"#"+each
            wordlist.append(word)
        return "".join(wordlist)


    def decode(self, s: str) -> List[str]:
        print (s)
        print (len(s))
        if len(s) == 0:
            return []
        i = 0
        ans = []
        while i < len(s):
            print(f"{i} in {s[i]}")

            numA = []
            while s[i]!= "#":
                numA.append(s[i])
                i = i+1

            num = int("".join(numA))

            each = []

            if num == 0:
                ans.append("")
                i = i+1
                continue

            j = 0
            for j in range(i+1, i+num+1):
                each.append(s[j])

            ans.append("".join(each))
            j = j+1
            i = j
        print(ans)
        return ans

