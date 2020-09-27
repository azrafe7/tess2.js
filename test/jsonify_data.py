import json
from pathlib import Path, PurePath

DATA_DIR = "data"
PATTERN = "**/*.dat"
OUTPUT_FILE = "data.json"

path = Path(DATA_DIR)

json_data = {}

for i, f in enumerate(path.glob(PATTERN)):
  #if i > 1: break  # for testing
  p = Path(f)
  parent = p.relative_to(DATA_DIR).parent
  print(p, p.name, p.relative_to(DATA_DIR).parent)
  item = {}
  path = str(p).replace("\\", "/")
  value = p.read_text()
  json_data[path] = value

json_options = {'sort_keys':True, 'indent':2, 'separators':(',', ': ')}

json_str = json.dumps(json_data, **json_options)
print(json_str[:1000] + " ...")

with open(OUTPUT_FILE, "w") as out:
  json.dump(json_data, out, **json_options)