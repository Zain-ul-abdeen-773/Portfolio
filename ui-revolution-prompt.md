# UI Revolution Prompt — IDE Agent
> Sci-Fi Neural Interface Design System | 3D + Heavy Animation

---

## Design Direction: Sci-Fi Neural Interface

The aesthetic: a living, breathing AI operating system. Think less "website", more "command center from 2077." Dark void backgrounds, glowing geometry, depth layers, and motion that feels alive. Every element should feel like it exists in 3D space.

You are a senior creative frontend engineer tasked with completely revolutionizing this application's UI. Do NOT preserve the old design in any way — treat this as a ground-up rebuild with the same functionality but an entirely new visual identity.

---

## Visual Identity

### Color Palette
Use these CSS variables everywhere — no hardcoded values:

```css
--void: #020408;
--deep: #060d18;
--surface: #0a1628;
--glass: rgba(10, 22, 48, 0.6);
--border-glow: rgba(0, 212, 255, 0.15);
--primary: #00d4ff;
--primary-dim: rgba(0, 212, 255, 0.08);
--accent: #7b2ff7;
--accent-glow: rgba(123, 47, 247, 0.4);
--hot: #ff3d71;
--warm: #ffaa00;
--text-primary: #e8f4ff;
--text-secondary: rgba(232, 244, 255, 0.5);
--text-dim: rgba(232, 244, 255, 0.2);
```

### Typography
- **Display / Headings:** `'Orbitron'` (Google Fonts) — geometric, futuristic
- **Body / Data:** `'JetBrains Mono'` (Google Fonts) — technical, readable
- No Inter, Roboto, or system fonts anywhere

---

## 3D & Depth System

Every major UI surface must have depth. Implement all three:

**1. Layered Glassmorphism**  
Panels use `backdrop-filter: blur(20px)` with subtle border glow, not flat cards. Stack multiple transparent layers for depth.

**2. Perspective Tilt on Hover**
```javascript
element.addEventListener('mousemove', (e) => {
  const rect = element.getBoundingClientRect();
  const x = (e.clientX - rect.left) / rect.width - 0.5;
  const y = (e.clientY - rect.top) / rect.height - 0.5;
  element.style.transform =
    `perspective(1000px) rotateY(${x * 12}deg) rotateX(${-y * 12}deg) translateZ(20px)`;
});
element.addEventListener('mouseleave', () => {
  element.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg) translateZ(0)';
});
```

**3. Floating Z-Layers**  
Use `transform: translateZ()` within `transform-style: preserve-3d` containers to create genuine depth stacking.

**4. Parallax Background**  
Background elements move at different speeds on scroll/mouse move.

---

## Animation System

### Page Load Sequence (staggered — do not skip)
| Element | Delay | Animation |
|---|---|---|
| Background grid | 0ms | Fade in |
| Main container | 200ms | Slide up + fade |
| Header elements | 400ms / 500ms / 600ms | Cascade left-to-right |
| Cards / panels | 600ms, 750ms, 900ms... | Upward drift + fade |
| Scan line | Once | Sweeps across screen |

### Continuous Ambient Animations (always running, subtle)
- Floating particles in background — 15–20 CSS pseudo-elements, randomized position/size/duration
- Pulsing glow on primary accent elements — `2–3s ease-in-out infinite`
- Slowly rotating geometric shapes in background at `0.05` opacity
- Border glow breathes — `opacity: 0.1 → 0.3 → 0.1`, 4s cycle

### Interaction Animations
- **Buttons:** `scale(0.97)` on press + ripple effect + sound-wave glow outward
- **Nav items:** Underline draws from left on hover via `scaleX` transform
- **Data values:** Count up from 0 on first viewport entry (IntersectionObserver)
- **Cards:** `translateY(-8px)` + shadow bloom on hover
- **Page transitions:** Current content blurs + fades, new content sharpens in

### Loading States
- Skeleton screens with animated shimmer — never spinners
- Progress bars use `--primary` cyan with trailing glow

---

## Component Specifications

### Navigation
- Floating pill-shaped top bar, centered, NOT full-width
- Glass background with `backdrop-filter`
- Logo left, nav center, status indicator right (green pulse dot = connected)
- Active nav link: subtle cyan glow underline

### Hero / Dashboard Header
- Full-width, min `40vh`
- Large Orbitron headline with gradient: `--primary` → `--accent`
- Subtitle in monospace with typewriter animation (character by character)
- Background: animated mesh gradient that slowly shifts colors
- Floating stat chips that drift upward on hover

### Data Cards / Panels
- Glass panels with `--border-glow` border
- Top-left corner: 20×20px glowing bracket accent (CSS only)
- Inner content: subtle dot grid pattern at `3%` opacity
- Numbers: `JetBrains Mono`, count up on viewport entry
- Hover: 3D tilt + cyan border brightens

### Buttons

| Type | Default | Hover |
|---|---|---|
| Primary | Cyan fill | Transparent + glowing border |
| Secondary | Transparent + border | Fills with glow |
| Destructive | `--hot` red + pulse | Brighter red + shadow |

All buttons: `letter-spacing: 0.1em`, uppercase, monospace font.

### Charts / Visualizations
- Dark background, glowing line strokes in `--primary`
- Grid lines at `5%` opacity only
- Data points pulse softly
- Tooltips: glass panel with sharp drop shadow

### Tables / Lists
- No harsh borders — subtle bottom borders at `--text-dim` opacity
- Row hover: full-row glass highlight slides in from left
- Status badges: pill-shaped with matching glow color per status

---

## Background System

Build five stacked layers:

| Layer | Content |
|---|---|
| 1 (deepest) | Solid `--void` |
| 2 | Radial gradient from `--accent-glow` at center-top |
| 3 | CSS perspective grid — fine lines (1px, 3% opacity) converging to horizon |
| 4 | 20 floating particles — randomized via CSS custom properties |
| 5 | Diagonal scan line sweeping top-to-bottom every 8 seconds |

---

## Technical Rules

- CSS custom properties for every color, spacing, and timing value — no hardcoded values
- `will-change: transform, opacity` on all animated elements
- Respect reduced motion preference:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

- No Bootstrap, Material UI, or Tailwind component classes — pure custom CSS
- Glass effects degrade gracefully: fallback `background: var(--surface)` if `backdrop-filter` unsupported
- All fonts loaded via Google Fonts with `display=swap`
- `scroll-behavior: smooth` on `:root`

---

## Rebuild Instructions

1. Start with the layout shell: nav + background system + base typography + CSS variables
2. Rebuild each component one by one following specs above
3. Do not skip the animation system — it is the soul of this design
4. Keep all existing functionality, data props, and routing logic intact
5. Only the visual layer changes

**Paste your component/page list below, then run:**

```
[YOUR COMPONENT / PAGE LIST HERE]
[YOUR FRAMEWORK — React / Next.js / Vue / etc.]
```
