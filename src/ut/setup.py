import json


def toJsonFile(data, savePath):
    with open(savePath, "w", encoding="utf-8") as f:
        f.write(json.dumps(data))
