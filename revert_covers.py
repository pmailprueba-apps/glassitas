import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Reverse mapping
mapping = {
    'baby_shower': '031d1e47-9588-46e2-b91e-6e3f4ba6817f.jpg',
    'bautizo': '14396917-52d9-4685-8103-2a31c5021a75.jpg',
    'comunion': '1909b3fb-431a-43d7-bdcd-7b6213712a26.jpg',
    'boda': '23d74606-4762-4574-b9d2-deb56b51ef1c.jpg',
    'cumpleanos': '254d1177-ee18-4db0-8807-a42c1e5ce8b3.jpg',
    'xv': '309f1bda-0663-4031-bcf8-39b74de860c0.jpg',
    'corporativo': '363e760c-2270-40cc-8746-7cfa50e9d480.jpg',
    'institucion': '434841ae-ba2e-4e71-8964-62698cd3f332.jpg',
    'graduacion': '5909b07e-8bc3-4116-84bf-1f41329ba18c.jpg'
}

for cat, img in mapping.items():
    new_str = f"foto: '../assets/productos/con_marco_blanco/galerias_con_marco/{cat}/img_1.jpg'"
    old_str = f"foto: '../assets/productos/con_marco_blanco/1_1_Cuadrado_1080x1080/{img}'"
    html = html.replace(old_str, new_str)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Covers reverted!")
