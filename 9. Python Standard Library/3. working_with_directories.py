from pathlib import Path

path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

paths = [p for p in path.iterdir() if p.is_dir()]
py_fiels = [p for p in path.rglob(pattern="*.py")]
print(py_fiels)
