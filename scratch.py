import re

with open('tienda.html', 'r', encoding='utf-8') as f:
    tienda = f.read()

# Extract script block
script_match = re.search(r'<script>(.*?)</script>', tienda, re.DOTALL)
if not script_match:
    print("Script not found")
    exit(1)
script_content = script_match.group(1)

with open('nueva_web_pruebas/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

# Remove any existing script before </body> just in case
index = re.sub(r'<script>.*?</script>\s*</body>', '</body>', index, flags=re.DOTALL)

# Insert the script block before </body>
script_tag = f"\n<script>{script_content}</script>\n"
index = index.replace('</body>', f'{script_tag}</body>')

with open('nueva_web_pruebas/index.html', 'w', encoding='utf-8') as f:
    f.write(index)

print("JS copied successfully")
