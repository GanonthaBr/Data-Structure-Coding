# LEVEL 1
class FileSystem:
    def __init__(self):
        self.root = {}
        self.admin_user = ['admin']

    def mkdir(self, path):
        
        self.root[path] = {}


    def ls(self, path, create_missing= False):
        parts = [p for p in path.split('/')]
        curr = parts[-1]
        print(f"Current dir to list: {curr}")

        # Create missing dir
        if create_missing:
            for part in parts:
                if part not in self.root:
                    self.root[part] = {}

        if curr in self.root:
            return sorted(self.root.get(curr, {}).keys())
        else:
            return []

    


    # LEVEL 2
    def create_file(self, path, content, user='normal'):

        if user not in self.admin_user:
            return "Permission Denied"
        parts = [p for p in path.split('/')]
        if len(parts) == 0:
            return None
        curr_dir = parts[-2]
        file_name = parts[-1]

        self.root[curr_dir][file_name] = content

        return True

    def read_file(self,path, user='normal'):
        if user not in self.admin_user:
            return "Permission Denied"
        parts = [p for p in path.split('/')]
        if len(parts) == 0:
            return None
        curr_dir = parts[-2]
        file_name = parts[-1]
        print(f"Reading file: {file_name} from dir: {curr_dir}")
        if curr_dir not in self.root.keys():
            return "Directory does not exist"
        return self.root[curr_dir].get(file_name, "File does not exist")

    def find(self, target_name, user='normal'):
        if user not in self.admin_user:
            return "Permission Denied"
        result = []
        def search(directory, path):
            for name, content in directory.items():
                current_path = f"{path}/{name}"
                if name == target_name:
                    result.append(current_path.replace('//','/'))
                if isinstance(content, dict):
                    search(content, current_path)
        search(self.root, "/")
        return sorted(result)
              

if __name__ == "__main__":
    file_system = FileSystem()

    file_system.mkdir('/root/users/docs')

    ls = file_system.ls('/root/users/docs',True)

    print(ls)

    file_system.create_file('/root/users/docs/file1.txt', 'Hello, World!', 'admin')
    file_system.create_file('/root/users/docs/file2.txt', 'This is a test file.')
    content = file_system.read_file('/root/users/docs/file1.txt', 'admin')
    print(content)
    ls = file_system.ls('/root/users/docs', True)

    print(file_system.root)
    print(ls)

    found_paths = file_system.find('file1.txt','admin')
    print(found_paths)