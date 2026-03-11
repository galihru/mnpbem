from mnpbem_base import bemsolver, register


@register("bemsolver", needs=({"mode": "stat"},))
class StaticSolver:
    def __init__(self, matrix, *, options=None, **kwargs):
        self.matrix = matrix
        self.options = options or {}

    def info(self) -> str:
        return f"Static solver with shape {self.matrix.shape}"


solver = bemsolver({"mode": "stat"}, [[1.0, 0.0], [0.0, 1.0]])
print(solver.info())
