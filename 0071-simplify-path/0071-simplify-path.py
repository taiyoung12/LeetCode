class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directorys = path.split("/")
        while '' in directorys:
            directorys.remove('')
        
        for directory in directorys :
            if directory == '.': 
                continue
            if directory == '..' and len(stack) > 0:
                stack.pop(-1)
            if directory != '..': 
                stack.append(directory)
        answer = '/' + '/'.join(stack)

        return "/" if answer == "/.." else answer