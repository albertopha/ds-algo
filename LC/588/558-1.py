"""
File
{
    name
}

Directory
{
    name: Directory
}
"""
from typing import Optional, Union 

class File:
    
    def __init__(self, name):
        self.name = name
        self.content = ""

class Directory:
    
    def __init__(self, name):
        self.name = name
        self.directories = dict()
        self.files = dict()
    
class FileSystem:

    def __init__(self):
        self.root = Directory("root")

    def ls(self, path: str) -> List[str]:
        navigated = self.navigate(path)
        
        if not navigated:
            return []
        
        if isinstance(navigated, File):
            return [navigated.name]
        
        return sorted(list(navigated.directories.keys()) + list(navigated.files.keys()))

    def mkdir(self, path: str) -> None:
        self.navigateCreate(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        paths = filePath.split("/")
        directory_paths = paths[0:-1]
        file_name = paths[-1]
        navigated = self.navigateCreate(directory_paths)
        
        if not isinstance(navigated, Directory):
            return
        
        if file_name not in navigated.files:
            navigated.files[file_name] = File(file_name)
        
        navigated.files[file_name].content += content

    def readContentFromFile(self, filePath: str) -> str:
        navigated = self.navigate(filePath)
        
        if not isinstance(navigated, File):
            return ""
        
        return navigated.content
    
    def navigate(self, path) -> Optional[Union[Directory, File]]:
        if path == "/":
            return self.root
        
        tmp = self.root
        paths = path.split("/") if isinstance(path, str) else path
        
        for i in range(1, len(paths)):
            if not isinstance(tmp, Directory):
                return None
            
            if paths[i] in tmp.directories:
                tmp = tmp.directories[paths[i]]
            elif paths[i] in tmp.files:
                tmp = tmp.files[paths[i]]
            else: # Doesn't exist
                return None
        return tmp
    
    def navigateCreate(self, path) -> Optional[Directory]:
        if path == "/":
            return self.root
        
        tmp = self.root
        paths = path.split("/") if isinstance(path, str) else path
        
        for i in range(1, len(paths)):
            if isinstance(paths[i], File):
                return None
            
            if paths[i] not in tmp.directories:
                tmp.directories[paths[i]] = Directory(paths[i])
            
            tmp = tmp.directories[paths[i]]
        return tmp

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
