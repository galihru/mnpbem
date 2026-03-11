"""Task registry compatible with MNPBEM bembase.find selection logic."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class Registration:
    task_name: str
    needs: tuple[str | dict[str, Any], ...]
    cls: type[Any]


class BEMRegistry:
    """Registry that matches option dictionaries against `needs` constraints."""

    def __init__(self) -> None:
        self._entries: list[Registration] = []

    def register(self, task_name: str, cls: type[Any], needs: tuple[str | dict[str, Any], ...] = ()) -> None:
        self._entries.append(Registration(task_name=task_name, needs=tuple(needs), cls=cls))

    def find_class(self, task_name: str, options: dict[str, Any], **property_pairs: Any) -> type[Any] | None:
        merged = dict(options)
        merged.update(property_pairs)

        best_match: tuple[int, type[Any] | None] = (0, None)
        for entry in self._entries:
            if entry.task_name != task_name:
                continue

            score = 0
            ok = True
            for need in entry.needs:
                if isinstance(need, str):
                    if need in merged and merged[need] is not None:
                        score += 1
                    else:
                        ok = False
                        break
                else:
                    if len(need) != 1:
                        ok = False
                        break
                    key, expected = next(iter(need.items()))
                    if merged.get(key) == expected:
                        score += 1
                    else:
                        ok = False
                        break

            if ok and score >= best_match[0]:
                best_match = (score, entry.cls)

        return best_match[1]


def register(
    task_name: str,
    *,
    needs: tuple[str | dict[str, Any], ...] = (),
    registry: BEMRegistry | None = None,
) -> Callable[[type[Any]], type[Any]]:
    """Decorator for registering classes into the default or custom registry."""

    target_registry = default_registry if registry is None else registry

    def decorator(cls: type[Any]) -> type[Any]:
        target_registry.register(task_name=task_name, cls=cls, needs=needs)
        return cls

    return decorator


default_registry = BEMRegistry()
