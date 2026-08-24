import re

html_path = '/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Tailwind config
old_config_start = 'tailwind.config = {\n            darkMode: "class",\n            theme: {\n                extend: {\n                    "colors": {'
new_config_start = """tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                        serif: ['"Outfit"', 'sans-serif'],
                    },
                    animation: {
                        'infinite-scroll': 'scroll 25s linear infinite',
                    },
                    keyframes: {
                        scroll: {
                            '0%': { transform: 'translateX(0)' },
                            '100%': { transform: 'translateX(-50%)' },
                        }
                    },
                    "colors": {"""
html = html.replace(old_config_start, new_config_start)

# 2. Fix the HTML to use Tailwind animation
html = html.replace('<div class="animate-scroll gap-4">', '<div class="animate-infinite-scroll flex w-max gap-4 hover:[animation-play-state:paused]">')

# 3. Clean up the janky duplicate CSS blocks
html = re.sub(r'<style>.*?\.animate-scroll.*?</style>', '', html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Tailwind updated successfully!")
