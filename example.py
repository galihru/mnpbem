"""Interactive 3D electric-field visualization around a spherical nanoparticle.

This example uses the published mnpbem submodules:
- mnpbem-material: dielectric response models
- mnpbem-mie: Rayleigh-limit polarizability
- mnpbem-particles: geometric sphere primitive

Usage:
    python interactive_3d_field.py

Headless test (save one frame):
    python interactive_3d_field.py --no-gui --save field.png
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


def _bootstrap_local_modules() -> None:
    """Allow running from monorepo source without pip install."""
    repo_root = Path(__file__).resolve().parents[2]
    for package_dir in repo_root.glob("mnpbem*"):
        src_dir = package_dir / "src"
        if src_dir.is_dir():
            src_str = str(src_dir)
            if src_str not in sys.path:
                sys.path.insert(0, src_str)


_bootstrap_local_modules()

from mnpbem_material import EpsConst, EpsDrude  # noqa: E402
from mnpbem_mie import rayleigh_polarizability  # noqa: E402
from mnpbem_particles import Sphere  # noqa: E402


def build_sphere_mesh(radius_nm: float, n_theta: int = 28, n_phi: int = 56) -> tuple[np.ndarray, np.ndarray]:
    """Return vertices (N, 3) and triangular faces (M, 3) for a sphere."""
    theta = np.linspace(1e-3, np.pi - 1e-3, n_theta)
    phi = np.linspace(0.0, 2.0 * np.pi, n_phi, endpoint=False)
    tt, pp = np.meshgrid(theta, phi, indexing="ij")

    x = np.sin(tt) * np.cos(pp)
    y = np.sin(tt) * np.sin(pp)
    z = np.cos(tt)
    vertices = radius_nm * np.column_stack((x.ravel(), y.ravel(), z.ravel()))

    faces: list[tuple[int, int, int]] = []
    for i in range(n_theta - 1):
        for j in range(n_phi):
            jn = (j + 1) % n_phi
            a = i * n_phi + j
            b = (i + 1) * n_phi + j
            c = i * n_phi + jn
            d = (i + 1) * n_phi + jn
            faces.append((a, b, c))
            faces.append((c, b, d))
    return vertices, np.asarray(faces, dtype=int)


def compute_surface_field(
    wavelength_nm: float,
    radius_nm: float,
    material_name: str,
    medium_n: float,
    vertices: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute quasi-static total field on/near the sphere surface.

    Returns:
        scalar_face: field magnitude per triangular face
        arrow_start: arrow origins
        arrow_dir: arrow directions
    """
    eps_particle, _ = EpsDrude(material_name)(np.array([wavelength_nm], dtype=float))
    eps_medium, _ = EpsConst(medium_n**2)(np.array([wavelength_nm], dtype=float))
    alpha = rayleigh_polarizability(radius_nm, eps_particle[0], eps_medium[0])

    normals = vertices / np.linalg.norm(vertices, axis=1, keepdims=True)
    sample_points = 1.02 * vertices
    r = np.linalg.norm(sample_points, axis=1, keepdims=True)
    rhat = sample_points / r

    # Incident field polarized along +x
    e0 = np.array([1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j], dtype=complex)
    p_dip = alpha * e0

    dot = np.sum(rhat * p_dip, axis=1, keepdims=True)
    e_dip = (3.0 * rhat * dot - p_dip) / np.maximum(r**3, 1e-12)
    e_total = e0 + e_dip

    # Magnitude of near field for color map.
    e_mag = np.linalg.norm(e_total, axis=1).real

    # Quiver arrows on illuminated side (x > 0).
    illum_idx = np.flatnonzero(vertices[:, 0] > 0.72 * radius_nm)[::5]
    arrow_start = 1.05 * vertices[illum_idx]
    e_real = np.real(e_total[illum_idx])
    e_norm = np.linalg.norm(e_real, axis=1, keepdims=True)
    arrow_dir = np.divide(e_real, np.maximum(e_norm, 1e-12))

    # Project vertex magnitudes to face magnitudes.
    return e_mag, arrow_start, arrow_dir


def set_axes_equal(ax: plt.Axes) -> None:
    """Set equal 3D scaling for x, y, z."""
    xlim = ax.get_xlim3d()
    ylim = ax.get_ylim3d()
    zlim = ax.get_zlim3d()

    xmid = 0.5 * (xlim[0] + xlim[1])
    ymid = 0.5 * (ylim[0] + ylim[1])
    zmid = 0.5 * (zlim[0] + zlim[1])
    radius = 0.5 * max(xlim[1] - xlim[0], ylim[1] - ylim[0], zlim[1] - zlim[0])

    ax.set_xlim3d(xmid - radius, xmid + radius)
    ax.set_ylim3d(ymid - radius, ymid + radius)
    ax.set_zlim3d(zmid - radius, zmid + radius)


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Interactive 3D MNPBEM-style sphere field demo.")
    parser.add_argument("--wavelength", type=float, default=548.1, help="Wavelength in nm.")
    parser.add_argument("--radius", type=float, default=50.0, help="Sphere radius in nm.")
    parser.add_argument("--material", type=str, default="Au", help="Drude material name: Au, Ag, or Al.")
    parser.add_argument("--medium-n", type=float, default=1.33, help="Refractive index of surrounding medium.")
    parser.add_argument("--no-gui", action="store_true", help="Render one frame only (no interactive window).")
    parser.add_argument("--save", type=str, default="", help="Optional path to save PNG.")
    return parser


def main() -> None:
    args = make_parser().parse_args()

    sphere = Sphere(radius_nm=float(args.radius))
    vertices, faces = build_sphere_mesh(sphere.radius_nm)

    fig = plt.figure(figsize=(8.2, 6.5))
    ax = fig.add_subplot(111, projection="3d")
    plt.subplots_adjust(bottom=0.18)

    e_mag, arrow_start, arrow_dir = compute_surface_field(
        wavelength_nm=float(args.wavelength),
        radius_nm=sphere.radius_nm,
        material_name=args.material,
        medium_n=float(args.medium_n),
        vertices=vertices,
    )

    face_values = e_mag[faces].mean(axis=1)
    surf = ax.plot_trisurf(
        vertices[:, 0],
        vertices[:, 1],
        vertices[:, 2],
        triangles=faces,
        linewidth=0.55,
        edgecolor="#1f4fb2",
        antialiased=True,
        shade=False,
        cmap="plasma",
    )
    surf.set_array(face_values)
    surf.set_clim(np.percentile(face_values, 5), np.percentile(face_values, 95))

    quiver = ax.quiver(
        arrow_start[:, 0],
        arrow_start[:, 1],
        arrow_start[:, 2],
        arrow_dir[:, 0],
        arrow_dir[:, 1],
        arrow_dir[:, 2],
        length=0.22 * sphere.radius_nm,
        normalize=True,
        color="crimson",
        linewidth=0.9,
    )

    ax.set_title(f"Electric field at {args.wavelength:.4f} nm", pad=18)
    ax.set_xlabel("x (nm)")
    ax.set_ylabel("y (nm)")
    ax.set_zlabel("z (nm)")
    ax.view_init(elev=18, azim=42)
    set_axes_equal(ax)

    cbar = fig.colorbar(surf, ax=ax, shrink=0.72, pad=0.03)
    cbar.set_label("|E_total| (arb. unit)")

    slider_ax = fig.add_axes([0.16, 0.06, 0.68, 0.03])
    wl_slider = Slider(slider_ax, "Wavelength (nm)", 430.0, 750.0, valinit=float(args.wavelength))

    def update(val: float) -> None:
        nonlocal quiver
        wavelength = float(val)
        e_mag_new, arrow_start_new, arrow_dir_new = compute_surface_field(
            wavelength_nm=wavelength,
            radius_nm=sphere.radius_nm,
            material_name=args.material,
            medium_n=float(args.medium_n),
            vertices=vertices,
        )
        face_values_new = e_mag_new[faces].mean(axis=1)
        surf.set_array(face_values_new)
        surf.set_clim(np.percentile(face_values_new, 5), np.percentile(face_values_new, 95))
        quiver.remove()
        quiver = ax.quiver(
            arrow_start_new[:, 0],
            arrow_start_new[:, 1],
            arrow_start_new[:, 2],
            arrow_dir_new[:, 0],
            arrow_dir_new[:, 1],
            arrow_dir_new[:, 2],
            length=0.22 * sphere.radius_nm,
            normalize=True,
            color="crimson",
            linewidth=0.9,
        )
        ax.set_title(f"Electric field at {wavelength:.4f} nm", pad=18)
        fig.canvas.draw_idle()

    wl_slider.on_changed(update)

    if args.save:
        fig.savefig(args.save, dpi=170, bbox_inches="tight")

    if args.no_gui:
        plt.close(fig)
    else:
        plt.show()


if __name__ == "__main__":
    main()
