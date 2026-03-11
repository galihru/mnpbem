# mnpbem-material

`mnpbem-material` mengimplementasikan model fungsi dielektrik utama pada domain plasmonik.

## Formulasi yang Diimplementasikan
1. **Konstanta dielektrik**

\[
\varepsilon(\lambda)=\varepsilon_0,\qquad
k(\lambda)=\frac{2\pi}{\lambda}\sqrt{\varepsilon}
\]

2. **Model Drude**

\[
\varepsilon(\omega)=\varepsilon_\infty-\frac{\omega_p^2}{\omega(\omega+i\gamma)}
\]

dengan transformasi energi-panjang gelombang:

\[
\omega_{\mathrm{eV}} = \frac{\mathrm{EV\_TO\_NM}}{\lambda_{\mathrm{nm}}}
\]

Parameter `Au`, `Ag`, `Al` mengikuti formulasi pada file MATLAB `Material/@epsdrude/init.m`.

3. **Model tabulasi**

Dari data `(E, n, k)`, didapat:

\[
\varepsilon = (n + i k)^2
\]

Interpolasi dilakukan pada domain panjang gelombang hasil konversi dari energi.

Implementasi:
- `src/mnpbem_material/models.py`
- data material: `src/mnpbem_material/data/*.dat`

## Dependensi
Dependensi runtime dipasang otomatis saat instalasi paket:
- `numpy>=1.24`

## Contoh Penggunaan
Contoh siap jalan tersedia di:
- `examples/basic_usage.py`

Jalankan:

```bash
python examples/basic_usage.py
```

## Author
- GALIH RIDHO UTOMO
- g4lihru@students.unnes.ac.id
