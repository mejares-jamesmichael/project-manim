# Manim Practice

A collection of mathematical animations built with [Manim](https://www.manim.community/), the animation engine created by Grant Sanderson (3Blue1Brown).

## Project Overview

This project serves as a sandbox for exploring Manim's capabilities, starting with a 3D visualization of the Lorenz Attractor -- a classic example of deterministic chaos in dynamical systems.

### Current Scenes

| Scene | File | Description |
|-------|------|-------------|
| `LorenzAttractor` | `dev_scene.py` | 3D animated trajectory of the Lorenz system with ambient camera rotation and color gradient. |

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (package manager)
- FFmpeg (required by Manim for rendering)

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd manim-practice
```

### 2. Set Up with uv

This project uses `uv` for dependency management. The Python version and dependencies are pinned in `pyproject.toml` and `uv.lock`.

```bash
# Install dependencies and create the virtual environment
uv sync
```

This will:

- Create a `.venv` directory with Python 3.12
- Install all dependencies from `uv.lock`

### 3. Render a Scene

```bash
uv run manim -ql dev_scene.py LorenzAttractor
```

Output files are written to the `media/` directory.

### 4. Play the Rendered Video

```bash
mpv --loop=inf --keep-open "media\videos\dev_scene\480p15\LorenzAttractor.mp4
```

## Development Workflow

Use `watchmedo` from the `watchdog` package to watch for file changes and re-render automatically:

```bash
uv run watchmedo shell-command --patterns="dev_scene.py" --command="uv run manim -ql --disable_caching dev_scene.py
```

This watches `dev_scene.py` and re-renders the scene on every save. The `--disable_caching` flag ensures Manim regenerates frames from scratch rather than reusing cached outputs.

Combine this with `mpv` in a second terminal for a live preview loop:

```bash
mpv --loop=inf --keep-open "media\videos\dev_scene\480p15\LorenzAttractor.mp4
```

`mpv` will automatically detect the updated file and reload it.

## Project Structure

```
manim-practice/
├── dev_scene.py          # Lorenz attractor scene
├── main.py               # Entry point (placeholder)
├── pyproject.toml        # Project metadata and dependencies
├── uv.lock               # Locked dependency versions
├── .python-version       # Python version pin (3.12)
├── pyrightconfig.json    # Pyright type-checker config
└── media/                # Rendered output (videos, images)
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `manim>=0.20.1` | Mathematical animation engine |
| `scipy>=1.18.0` | ODE solver (`solve_ivp`) for the Lorenz system |
| `watchdog>=6.0.0` | Filesystem monitoring for hot-reload |

## License

This is a personal practice project. No license specified.
