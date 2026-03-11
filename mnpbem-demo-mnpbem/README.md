# mnpbem-demo-mnpbem

[![PyPI version](https://img.shields.io/pypi/v/mnpbem-demo-mnpbem.svg)](https://pypi.org/project/mnpbem-demo-mnpbem/)
[![Python versions](https://img.shields.io/pypi/pyversions/mnpbem-demo-mnpbem.svg)](https://pypi.org/project/mnpbem-demo-mnpbem/)

`mnpbem-demo-mnpbem` adds a thin orchestration layer for scripted demo pipelines.

## Scientific Context
The module acts as a deterministic controller for reproducible simulation sequences:

`D = {(lambda_i, configuration_i) | i = 1, 2, ..., N}`

In equivalent Unicode notation:
`D = {(λ_i, configuration_i) | i = 1, 2, ..., N}`

## Implementation
- Demo pipeline summary: `src/mnpbem_demo_mnpbem/runner.py`

## Installation
```bash
pip install mnpbem-demo-mnpbem
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
