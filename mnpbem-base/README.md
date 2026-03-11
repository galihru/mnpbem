# mnpbem-base

`mnpbem-base` provides registry and factory primitives for selecting solver classes from option constraints.
The release notes are generated directly from this scientific README for traceable package documentation.

## Implemented Formulation
Given a requirement set for a candidate class, the selection score is:

```text
\hat{c}=\arg\max_c\sum_j\mathbf{1}[\text{need}_{c,j}\ \text{is satisfied}]
```

This mirrors rule-based class dispatch used in MNPBEM-style solver construction.

## Implementation
- Registry logic: `src/mnpbem_base/registry.py`
- Factory entry points: `src/mnpbem_base/factory.py`

## Dependencies
- `numpy>=1.24`

## Installation
```bash
pip install mnpbem-base
```

## Example
Runnable example:
- `examples/basic_usage.py`

Run:
```bash
python examples/basic_usage.py
```

## Author
- GALIH RIDHO UTOMO
- g4lihru@students.unnes.ac.id
