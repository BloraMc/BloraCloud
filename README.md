# BloraCloud

BloraCloud is a community-driven project hosting **editable cloud JSON/TXT indexes**. It’s designed so anyone can contribute data, such as Minecraft servers, game stats, or other cloud resources.

Now, it has multiple JSON/TXT files like `mcjavasrv.json`, which stores **Minecraft Java server info**. Users can create **pull requests** to add more data to expand cloud info.

---
**Stats :**

<!-- BloraCloud-Stats-Start -->
Indexes :
Indexed Data :
<!-- BloraCloud-Stats-End -->

---

## Features

* **Community editable:** Everyone can contribute via GitHub.
* **Multiple cloud indexes:** Each JSON file can store different types of data.
* **Easy to parse:** JSON format is simple for developers to integrate.
* **Example:** `mcjavasrv.json` stores servers with:

  * `name`
  * `ip` & `port`
  * `version`
  * `description`
  * `location`

---

## How to Contribute

1. **Fork the repository**.
2. **Edit an existing JSON** or **add a new one**.
3. Make sure the JSON is **valid and properly formatted**.
4. Submit a **pull request** with your changes.

---

## Example: Adding a Minecraft Server

```json
{
  "name": "Cool Minecraft Server",
  "ip": "play.exemple.org",
  "port": 25565,
  "version": "1.19+",
  "description": "Fun server!",
  "location": "Asia/HongKong"
}
```

---

## Usage

Devs can fetch any JSON file directly via its **raw GitHub URL** and use it in their apps, scripts, or even Bots. Example:

```python
import requests

JSON_URL = "https://raw.githubusercontent.com/BloraMc/BloraCloud/main/indexes/mcjavasrv.json"

def fetch_servers():
    try:
        response = requests.get(JSON_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching server list: {e}")
        return []

def search_servers(servers, query):
    results = []
    query_lower = query.lower()
    for server in servers:
        if (query_lower in server["name"].lower() or
            query_lower in server["location"].lower() or
            query_lower in server["version"].lower()):
            results.append(server)
    return results

def display_server(server):
    print(f"Name: {server['name']}")
    print(f"IP: {server['ip']}:{server['port']}")
    print(f"Version: {server['version']}")
    print(f"Description: {server['description']}")
    print(f"Location: {server['location']}")
    print("-" * 40)

def main():
    servers = fetch_servers()
    if not servers:
        return

    print("Welcome to BloraMc Minecraft Server Finder!")
    while True:
        query = input("Enter search term (or 'exit' to quit): ").strip()
        if query.lower() == "exit":
            break

        matches = search_servers(servers, query)
        if matches:
            print(f"\nFound {len(matches)} server(s):\n")
            for server in matches:
                display_server(server)
        else:
            print("This server isnt there! Consider adding it to the Index https://github.com/BloraMc/BloraCloud/\n")

if __name__ == "__main__":
    main()
```

---

## Join the Community

* Share your servers or cloud data
* Help keep the indexes up-to-date
* Make Minecraft server discovery or cloud apps easier for everyone

---

BloraCloud is **community collaboration**, feel free to contribute ah!

---

# Rules

* Do **not** add Minecraft servers labeled **Private** or **Apply Only**.
* Do **not** submit any **private or sensitive information**.
* Do **not** add index data that could lead to **harmful or dangerous content**.
