# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

path_home = pathlib.Path.home()
path_code = path_home / "Documents" / "CodingNomads"

try:
    for item in path_code.iterdir():
        print(item.name)
        if "." not in item.suffix:
            path_code_lv1 = path_code / item.name
            for item_lv1 in path_code_lv1.iterdir():
                print("|----" + item_lv1.name)
                if "." not in item_lv1.suffix:
                    path_code_lv2 = path_code_lv1 / item_lv1.name
                    for item_lv2 in path_code_lv2.iterdir():
                        print("|----|----" + item_lv2.name)
except Exception:
    pass