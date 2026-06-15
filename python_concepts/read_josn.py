import json
from stat import filemode

filepath="C:\\Playwright_python\\June2026_APITesting_practice\\test_data.json"
with open(filepath, "r") as f:
    data = json.load(f)
print(data)
 

print(data["cName"])
print(data["empid"])

data["empName1"] = "Srinivas Narayan"
#write data to json file
with open(filepath, "w") as f:
    json.dump(data, f, indent=4)

