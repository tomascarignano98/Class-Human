from pathlib import Path
from time import ctime
import shutil

source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

# target.write_text(source.read_text())
shutil.copy(source, target)

"""
path.exists()
path.rename("init.txt")
path.unlink()
print(ctime(path.stat().st_ctime))

print(path.read_text())
path.write_text("...")
path.write_bytes()
"""
