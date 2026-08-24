import re
import os

files = [
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/nueva_web_pruebas/index.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/tienda.html",
    "/Volumes/MiDisco1TB/Proyectos/44-glassitas/preguntas-frecuentes.html"
]

full_style_block = """<style>
        .tactile-btn {
            transition: transform 0.15s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), color 0.15s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            will-change: transform;
        }
        .tactile-btn:hover {
            transform: translate(-2px, -2px);
            box-shadow: 3px 3px 0px 0px #C46231;
        }
        .tactile-btn:active {
            transform: scale(0.97) translate(0px, 0px) !important;
            box-shadow: 0px 0px 0px 0px #C46231 !important;
        }
        
        .product-card {
            transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: transform;
        }
        .product-card:hover {
            transform: scale(1.02);
        }
        .product-card:active {
            transform: scale(0.98);
        }
        
        .lightbox-anim {
            transition: opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }
        
        a, button {
            transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1) !important;
            transition-duration: 0.2s !important;
        }
        
        .active-scale:active {
            transform: scale(0.97) !important;
        }

        .inner-border {
            position: absolute;
            inset: 8px;
            border: 1px solid rgba(196, 98, 49, 0.4);
            pointer-events: none;
            z-index: 10;
        }
        .product-img {
            transition: transform 0.5s ease;
        }
        .ambient-shadow {
            box-shadow: 0 10px 40px -10px rgba(0, 75, 77, 0.08);
        }

        .btn-premium {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            background-color: #004B4D;
            color: #ffffff;
            padding: 0.875rem 2.25rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            box-shadow: 0 10px 20px -5px rgba(0, 75, 77, 0.25);
            transition: transform 0.15s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: transform;
            text-decoration: none;
        }
        .btn-premium:hover {
            background-color: #00383a;
            box-shadow: 0 15px 25px -5px rgba(0, 75, 77, 0.35);
            transform: translateY(-2px);
        }
        .btn-premium:active {
            transform: scale(0.97) translateY(0);
            box-shadow: 0 4px 6px -1px rgba(0, 75, 77, 0.2);
        }

        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        .animate-scroll {
            animation: scroll 30s linear infinite;
            display: inline-flex;
            width: max-content;
        }
        .animate-scroll:hover {
            animation-play-state: paused;
        }
</style>
"""

for filepath in files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Clean any duplicate or broken style blocks
    content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
    
    # Inject full clean style block before </head>
    head_end = content.find('</head>')
    if head_end != -1:
        content = content[:head_end] + full_style_block + "\n" + content[head_end:]

    # Format grey texts (Hero subtitle and others) to match the preview (text-xl font-light tracking-wide)
    content = content.replace(
        '<p class="text-lg font-medium text-on-surface-variant mb-10">Diseños únicos para tus momentos especiales.</p>',
        '<p class="text-xl md:text-2xl font-light text-[#3f4849] tracking-wide mb-8 leading-relaxed">Diseños únicos para tus momentos especiales.</p>'
    )

    # Format subtitles in sections (like Mayoreo / Galería description)
    content = content.replace(
        'Artesanía en cada detalle. Perfectas para bodas, bautizos y celebraciones únicas.',
        'Artesanía en cada detalle. Diseños exclusivos para bodas, bautizos y celebraciones únicas.'
    )
    content = re.sub(
        r'<p class="([^"]*text-on-surface-variant[^"]*)">([^<]+)</p>',
        lambda m: f'<p class="text-base md:text-lg font-light text-[#3f4849] tracking-wide leading-relaxed">{m.group(2)}</p>' if 'mb-' in m.group(1) or 'max-w' in m.group(1) else m.group(0),
        content
    )

    with open(filepath, 'w') as f:
        f.write(content)

print("Estilos y formato visual aplicados con éxito.")
