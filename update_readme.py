import os
import json
import re
import requests

folders_to_scan = ["indexes", "Cloud"]

total_data = 0
total_indexes = 0

for folder in folders_to_scan:
    for root, _, files in os.walk(folder):
        for filename in files:
            if filename.endswith(".json"):
                total_indexes += 1
                filepath = os.path.join(root, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                        total_data += len(data)
                    except Exception as e:
                        print(f"Failed to load {filepath}: {e}")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

pattern = r"(<!-- BloraCloud-Stats-Start -->)(.*?)(<!-- BloraCloud-Stats-End -->)"
replacement = (
    f"<!-- BloraCloud-Stats-Start -->\n"
    f"Indexes : {total_indexes}\n"
    f"Indexed Data : {total_data}\n"
    f"<!-- BloraCloud-Stats-End -->"
)
readme = re.sub(pattern, replacement, readme, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print(f"README updated: {total_indexes} indexes, {total_data} data points")

webhook_url = os.getenv("DISCORD_WH")
if webhook_url:
    payload = {
        "content": f"📊 **BloraCloud Stats Updated!**\nIndexes: {total_indexes}\nData Points: {total_data}"
    }
    try:
        r = requests.post(webhook_url, json=payload, timeout=5)
        r.raise_for_status()
        print("✅ Sent update to Discord")
    except Exception as e:
        print(f"❌ Failed to send webhook: {e}")
else:
    print("⚠️ No DISCORD_WH secret found, skipping Discord notification.")
