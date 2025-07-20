class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        answer = []

        for file in folder:
            if not answer or not file.startswith(answer[-1] + "/"):
                answer.append(file)
       
        return answer