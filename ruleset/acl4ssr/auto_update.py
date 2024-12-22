import os
import requests

# Define file paths
url = "https://raw.githubusercontent.com/217heidai/adblockfilters/refs/heads/main/rules/china.txt"
downloaded_file = os.path.join("/Users/unit117/Dev/clashConverter/ruleset/acl4ssr", "china_downloaded.txt")
modified_file = os.path.join("/Users/unit117/Dev/clashConverter/ruleset/acl4ssr", "china_modified.txt")
check_file = os.path.join("/Users/unit117/Dev/clashConverter/ruleset/acl4ssr", "check.txt")
combined_file = os.path.join("/Users/unit117/Dev/clashConverter/ruleset/acl4ssr", "combined_output.txt")

# Download the file
response = requests.get(url)
if response.status_code == 200:
    with open(downloaded_file, "w", encoding="utf-8") as file:
        file.write(response.text)
    print(f"File downloaded and saved to {downloaded_file}")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
    exit()

# Modify the file by adding DOMAIN-SUFFIX to each line
with open(downloaded_file, "r", encoding="utf-8") as infile, open(modified_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("#"):
            outfile.write(f"DOMAIN-SUFFIX,{stripped_line}\n")

print(f"Modified file written to {modified_file}")

# Combine china_modified with check.txt and remove duplicates
unique_lines = set()

with open(modified_file, "r", encoding="utf-8") as modfile, \
     open(check_file, "r", encoding="utf-8") as chkfile, \
     open(combined_file, "w", encoding="utf-8") as combfile:
    for line in modfile:
        stripped_line = line.strip()
        if stripped_line:
            unique_lines.add(stripped_line)
    for line in chkfile:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("#"):
            unique_lines.add(stripped_line)
    for line in sorted(unique_lines):
        combfile.write(line + "\n")

print(f"Combined file written to {combined_file}")
