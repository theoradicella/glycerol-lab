# Glycerol Lab

## Setup

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Measurements

We measured the length in milliliters using black tape marking on the tube.

| Volume | Height |
|--------|--------|
| 100 mL | 9.25 cm |
| 220 mL | 20.35 cm |

## Material Properties

- **Ball Density**: ~7.7 g/cm³ (±0.1 error)
- **Glycerol Viscosity**: 0.8 Pa·s (at room temperature)
- **Room Temperature**: 25°C

## Tasks

1. **Check Stokes' Law** from the videos
2. **Check limit velocity** of falling balls
3. **ML algorithm** to predict velocity
4. **ML algorithm** to reconstruct trajectory

## Notes

The viscosity of the glycerol depends on temperature, which is maintained at 26.5°C.

## Video Structure

Videos are organized by volume and trial:
```
videos/
├── 100ml/
│   ├── trial1-5/
│   │   └── 2mm, 3mm, 4mm, 5mm, 6mm.mp4v
└── 220ml/
    ├── trial1-5/
        └── 2mm, 3mm, 4mm, 5mm, 6mm.mp4v
```
