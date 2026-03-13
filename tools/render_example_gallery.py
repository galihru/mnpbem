from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "docs" / "example-data"
IMAGE_DIR = ROOT / "docs" / "example-images"
README_PATH = ROOT / "README.md"

MODULE_META = {
    "python": {"title": "Python", "package": "mnpbem-material + mnpbem-mie", "registry": "PyPI"},
    "javascript": {"title": "JavaScript", "package": "@galihru/mnp", "registry": "npm"},
    "csharp": {"title": "C#", "package": "MnpPlasmon", "registry": "NuGet"},
    "rust": {"title": "Rust", "package": "mnp-plasmon", "registry": "Crates.io"},
    "r": {"title": "R", "package": "mnpPlasmonR", "registry": "CRAN-ready"},
    "julia": {"title": "Julia", "package": "MnpPlasmon", "registry": "General Registry"},
    "ruby": {"title": "Ruby", "package": "mnp_plasmon", "registry": "RubyGems + GitHub Packages"},
    "c": {"title": "C", "package": "mnp-plasmon", "registry": "vcpkg / source"},
    "cpp": {"title": "C++", "package": "mnp-plasmon", "registry": "vcpkg / source"},
}

ORDER = ["python", "javascript", "csharp", "rust", "r", "julia", "ruby", "c", "cpp"]
BEGIN = "<!-- BEGIN AUTO EXAMPLE GALLERY -->"
END = "<!-- END AUTO EXAMPLE GALLERY -->"


def read_spectrum(path: Path) -> tuple[list[float], list[float], list[float], list[float]]:
    wavelengths: list[float] = []
    c_ext: list[float] = []
    c_sca: list[float] = []
    c_abs: list[float] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            wavelengths.append(float(row["wavelength_nm"]))
            c_ext.append(float(row["c_ext"]))
            c_sca.append(float(row["c_sca"]))
            c_abs.append(float(row["c_abs"]))
    return wavelengths, c_ext, c_sca, c_abs


def render_plot(module_key: str, csv_path: Path) -> None:
    wavelengths, c_ext, c_sca, c_abs = read_spectrum(csv_path)
    meta = MODULE_META[module_key]

    plt.figure(figsize=(7.8, 4.8))
    plt.plot(wavelengths, c_ext, label="Cext", linewidth=2.2, color="#0f766e")
    plt.plot(wavelengths, c_sca, label="Csca", linewidth=2.0, color="#2563eb")
    plt.plot(wavelengths, c_abs, label="Cabs", linewidth=2.0, color="#dc2626")
    plt.title(f"{meta['title']} example: Au sphere spectral response")
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Cross-section (nm^2)")
    plt.grid(alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(IMAGE_DIR / f"{module_key}.png", dpi=160)
    plt.close()


def build_gallery_block() -> str:
    lines = [BEGIN, ""]
    for module_key in ORDER:
        csv_path = DATA_DIR / f"{module_key}.csv"
        if not csv_path.exists():
            continue
        meta = MODULE_META[module_key]
        image_rel = f"docs/example-images/{module_key}.png"
        lines.extend(
            [
                f"### {meta['title']}",
                "",
                f"Package: {meta['package']}  ",
                f"Registry: {meta['registry']}",
                "",
                f"![{module_key} example]({image_rel})",
                "",
            ]
        )
    lines.append(END)
    return "\n".join(lines)


def update_readme() -> None:
    content = README_PATH.read_text(encoding="utf-8")
    gallery = build_gallery_block()
    if BEGIN in content and END in content:
        start = content.index(BEGIN)
        finish = content.index(END) + len(END)
        updated = content[:start]
        head = updated.rstrip()
        tail = content[finish:]
        README_PATH.write_text(head + "\n\n" + gallery + tail, encoding="utf-8")
        return

    section = "\n".join([
        "## Development",
        "",
        "The example gallery below is generated automatically from module-level simulation scripts.",
        "Each image keeps the same filename and is overwritten on every workflow run, so the repository does not accumulate duplicate images.",
        "",
        gallery,
    ])
    README_PATH.write_text(content.rstrip() + "\n\n" + section + "\n", encoding="utf-8")


def main() -> None:
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    for module_key in ORDER:
        csv_path = DATA_DIR / f"{module_key}.csv"
        if csv_path.exists():
            render_plot(module_key, csv_path)
    update_readme()


if __name__ == "__main__":
    main()
