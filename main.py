import shutil
from pathlib import Path

config = {"site-packages": r"D:\Program Files\Python311\Lib\site-packages"}

src = Path(Path.cwd()) / "src"

shutil.copytree(src, config["site-packages"], dirs_exist_ok=True)
