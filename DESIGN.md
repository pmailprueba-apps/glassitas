# Design System: Glassitas Boutique Bakery

## 1. Visual Theme & Atmosphere
A warm, elegant, and appetizing boutique bakery interface with clean asymmetric layouts and fluid spring-physics motion. The atmosphere is sweet yet premium—like a modern, high-end patisserie in a cosmopolitan city. It balances the playfulness of custom cookies with the trust and quality of a luxury brand.

## 2. Color Palette & Roles
- **Peach Cream** (#F8DCD1) — Primary background surface. Replaces standard white to give a warm, inviting, "creamy" feel.
- **Pure Canvas** (#FFFFFF) — Card backgrounds and container fills. Used sparingly to create high-contrast clean zones for photos.
- **Deep Teal** (#1E6367) — Primary text, display headings, and main CTAs. High contrast against the peach background. (Replaces pure black).
- **Terracotta Coral** (#D88B79) — Single accent color for secondary buttons, active states, focus rings, and decorative frames around the cookies.
- **Muted Teal** (rgba(30,99,103,0.7)) — Secondary text, descriptions, metadata.
- **Whisper Border** (rgba(216,139,121,0.2)) — Card borders, 1px structural lines.

## 3. Typography Rules
- **Display:** `Outfit` or `Playfair Display` — Track-tight, controlled scale, weight-driven hierarchy. Used for the Hero title and section headers to give a boutique, editorial feel.
- **Body:** `Geist` or `Outfit` — Relaxed leading, 65ch max-width, Deep Teal color. Clean, modern, highly legible.
- **Banned:** Inter, generic system fonts (Times New Roman, Arial). No neon typography.

## 4. Component Stylings
* **Buttons:** Flat, pill-shaped or generously rounded. No outer glow. Tactile -2px translate on hover/active. Deep Teal fill for primary, Terracotta ghost/outline for secondary.
* **Cards:** Generously rounded corners (1.5rem). Diffused Terracotta-tinted whisper shadow. Used to showcase cookies (Fondant, Impresión, Muffins). 
* **Images:** All gallery images must have a subtle Terracotta inner border ("marco de glassitas") and an absolute-positioned badge with an ID Code (e.g., "GL-001") in Deep Teal.
* **Inputs:** Label above, error below. Focus ring in Terracotta accent color. No floating labels.

## 5. Layout Principles
- Grid-first responsive architecture. 
- Wide, asymmetrical Hero section with a beautiful offset image. (No generic centered heroes).
- Strict single-column collapse below 768px. Max-width containment (1200px).
- Generous internal padding (whitespace) to let the products breathe. No overlapping text on images.
- Section 1: Hero
- Section 2: Galletas Diseño Personalizado con Fondant
- Section 3: Galletas con Impresión
- Section 4: Muffins y Pasteles con Impresión

## 6. Motion & Interaction
- Spring physics for all interactive elements (buttons, cards).
- Hovering a cookie card slightly scales the image up (1.03x) and lifts the card.
- Smooth staggered cascade reveals for the cookie galleries.

## 7. Anti-Patterns (Banned)
- No emojis.
- No `Inter` font.
- No pure black (`#000000`).
- No neon glows or drop shadows with high opacity.
- No 3-column equal grids for the hero.
- No filler UI text: "Scroll to explore", bouncing chevrons.
- No overlapping elements — clean spatial separation always.
