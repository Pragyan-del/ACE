virtual_files = {}


def write_file(filename, content):
    virtual_files[filename] = content
    return f"{filename} written successfully"


def read_file(filename):
    return virtual_files.get(filename, "File not found")


def ls():
    return list(virtual_files.keys())


def edit_file(filename, new_content):
    if filename in virtual_files:
        virtual_files[filename] = new_content
        return f"{filename} updated successfully"
    return "File not found"