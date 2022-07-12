import pathlib

path = pathlib.Path().cwd()

path_target = pathlib.Path("/Users/byu/Documents/CodingNomads/python-101-main/")
path_new = pathlib.Path("/Users/byu/Documents/CodingNomads/python-101-main/13_modules-and-automation/resource")
path_remove = pathlib.Path("/Users/byu/Documents/CodingNomads/python-101-main/13_modules-and-automation/resource_new")
path_remove.rmdir()
path_new.mkdir(exist_ok=True)
path_new.replace("/Users/byu/Documents/CodingNomads/python-101-main/resource")

for file in path_target.iterdir():
    if file.suffix == ".md":
        print(file)