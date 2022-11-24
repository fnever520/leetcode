import os
from importlib import import_module
from pathlib import Path

modules_dir = "./modules"
modules_namespace = "modules"

def load_and_run(file_name):
    class_name = Path(file_name).stem
    
    m = import_module(f"{modules_namespace}.{class_name}")
    c = dir(m)[0]
    obj = getattr(m, c)

    print(f"GOT {obj} from {m}")
    print(f"Tests is {obj.tests}")
    print(f"Types is {obj.types}")
    obj.run()

for file in os.scandir(modules_dir):
    if file.name.endswith(".py"):
        load_and_run(file.name)
        print("===========")