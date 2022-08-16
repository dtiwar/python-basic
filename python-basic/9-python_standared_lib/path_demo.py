from pathlib import Path
#
# path =Path('../../python-basic/ecommerce/shopping/sales.py')
# # path =Path('../../python-basic/')
# # print(path.exists())
# #
# # print(path.cwd())
# #
# #
# # name ="yes" if path.is_dir() else "no"
# # print(name)
#
# print(path.name)
# print(path.stem)
# print(path.parent)
#
# # file_and_folders=[p for p in path.iterdir()]
# # print(file_and_folders)
# #
# # file_and_folders=[p for p in path.iterdir()]
# # print(file_and_folders)
#
# path=path.with_suffix(".csv")
# print(path)


# path =Path('../../python-basic/')
#
# list_of_file = [p for p in path.iterdir() if p.is_file()]
# print(list_of_file)

path =Path('../../python-basic/9-python_standared_lib/path_demo.py')

# path =[p for p in path.rglob("*.py")]
# print(len(path))
from time import ctime
print(ctime(path.stat().st_ctime))

print(path.read_text())

with open('/Users/deep/data/02-projects/python-basic/python-basic/ecommerce/shopping/sales.py') as file:
	test=file.read()
	print(test)
	print("+++++++++")


import shutil

shutil.copy('/Users/deep/data/02-projects/python-basic/python-basic/ecommerce/shopping/sales.py','.')