import json

SHADERS_DIR: str = "shaders/"

with open("src/config/font-binds.json", "r") as f:
    FONT_BINDS = json.load(f)

del json
