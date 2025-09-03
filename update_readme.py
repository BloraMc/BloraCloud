import os
import json
import re

indexes_folder = "indexes"
total_data = 0
total_indexes = 0

for root, _, files in os.walk(indexes_folder):
    for filename in files:
        if filename.endswith(".json"):
            total_indexes += 1
            filepath = os.path.join(root, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                total_data += len(data)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

pattern = r"(<!-- BloraCloud-Stats-Start -->)(.*?)(<!-- BloraCloud-Stats-End -->)"
replacement = f"<!-- BloraCloud-Stats-Start -->\nIndexes : {total_indexes}\nIndexed Data : {total_data}\n<!-- BloraCloud-Stats-End -->"
readme = re.sub(pattern, replacement, readme, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print(f"README updated: {total_indexes} indexes, {total_data} data points")
