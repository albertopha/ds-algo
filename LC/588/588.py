"""
Test cases:
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile","ls","ls"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"],["/a/b"],["/a/b/c"]]
["FileSystem","mkdir","ls","ls","mkdir","ls","ls","addContentToFile","readContentFromFile","ls","readContentFromFile"]
[[],["/zijzllb"],["/"],["/zijzllb"],["/r"],["/"],["/r"],["/zijzllb/hfktg","d"],["/zijzllb/hfktg"],["/"],["/zijzllb/hfktg"]]
["FileSystem","mkdir","ls","mkdir","ls","ls","ls","addContentToFile","ls","ls","ls"]
[[],["/m"],["/m"],["/w"],["/"],["/w"],["/"],["/dycete","emer"],["/w"],["/"],["/dycete"]]
"""
class File(object):
    def __init__(self, name, content):
        self.name = name
        self.content = content
        
class Directory(object):
    def _init__(self, name):
        self.name = name
        self.files = dict()
        self.directories = dict()

class FileSystem(object):

    def __init__(self):
        self.home = Directory("")

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        if not path:
            return []
        
        p = path.split("/")
        
        # File from the /home
        if p[0]:
            return p
        
        current_directory = self.home
        for i in range(1, len(p) - 1):
            directory = p[i]
            current_directory = current_directory.directories[directory]
            
        if p[-1] in current_directory.files:
            return [p[-1]]
        
        if p[-1] in current_directory.directories:
            current_directory = current_directory.directories[p[-1]]
        lists = list(current_directory.files.keys()) + list(current_directory.directories.keys())
        return sorted(lists)
        

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        if not path:
            return
        
        p = path.split("/")
        
        # mkdir("/") -> not valid
        if not p[1]:
            return
        
        current_directory = self.home
        for directory in p:
            if not directory:
                continue

            if directory not in current_directory.directories:
                current_directory.directories[directory] = Directory(directory)

            current_directory = current_directory.directories[directory]
        

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        if not filePath:
            return
        
        p = filePath.split("/")
        current_directory = self.home
        for i in range(1, len(p) - 1):
            directory = p[i]
            current_directory = current_directory.directories[directory]
        
        file_name = p[-1]
        if file_name not in current_directory.files:
            current_directory.files[file_name] = File(file_name, "")
        
        current_directory.files[file_name].content += content
        

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        if not filePath:
            return ""
        
        p = filePath.split("/")
        current_directory = self.home
        for i in range(1, len(p) - 1):
            directory = p[i]
            current_directory = current_directory.directories[directory]
        
        file_name = p[-1]
        return current_directory.files[file_name].content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
