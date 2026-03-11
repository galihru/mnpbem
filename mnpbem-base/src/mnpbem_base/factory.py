"""Factory functions mirroring MATLAB entry points in Base/*.m."""

from __future__ import annotations

from typing import Any

from .registry import default_registry


def _extract_options(args: tuple[Any, ...]) -> tuple[dict[str, Any], tuple[Any, ...], dict[str, Any]]:
    options = {}
    positionals = list(args)
    property_pairs: dict[str, Any] = {}

    # First dict argument is treated as options structure, following MATLAB style.
    for idx, item in enumerate(positionals):
        if isinstance(item, dict):
            options = dict(item)
            positionals.pop(idx)
            break

    # Remaining trailing string/value pairs are property pairs.
    i = 0
    while i + 1 < len(positionals):
        key = positionals[i]
        if isinstance(key, str):
            property_pairs[key] = positionals[i + 1]
            del positionals[i : i + 2]
        else:
            i += 1

    return options, tuple(positionals), property_pairs


def _factory(task_name: str, *args: Any) -> Any:
    options, positionals, property_pairs = _extract_options(args)
    cls = default_registry.find_class(task_name, options, **property_pairs)
    if cls is None:
        raise ValueError(f"no class for task '{task_name}' and provided options")
    return cls(*positionals, options=options, **property_pairs)


def bemsolver(*args: Any) -> Any:
    return _factory("bemsolver", *args)


def dipole(*args: Any) -> Any:
    return _factory("dipole", *args)


def electronbeam(*args: Any) -> Any:
    return _factory("eels", *args)


def greenfunction(*args: Any) -> Any:
    return _factory("greenfunction", *args)


def planewave(*args: Any) -> Any:
    return _factory("planewave", *args)


def spectrum(*args: Any) -> Any:
    return _factory("spectrum", *args)
