class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return path

        pathList = path.split("/")
        stack = []

        for dir in pathList:
            if dir == "..":
                if stack:
                    stack.pop()
            elif dir != "" and dir != ".":
                stack.append(dir)
            

        return "/" + "/".join(stack)
        