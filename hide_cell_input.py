import os.path
import nbformat as nbf
from glob import glob

notebooks = glob(os.path.join('./', "*.ipynb"))

for ipath in notebooks:
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        cell_tags = cell.get("metadata", {}).get("tags", [])
        if len(cell_tags) == 0:
            cell_tags.append("hide-input")
        cell["metadata"]["tags"] = cell_tags

    nbf.write(ntbk, os.path.join('./', os.path.splitext(os.path.basename(ipath))[0]+".ipynb"))