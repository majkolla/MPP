import sys 
import sysconfig 
from dataclasses import dataclass 


@dataclass
class FreeThreadingInfo:
    build_supports_free_threading: bool 
    gil_enabled: bool | None
    
    @property
    def is_free_threaded(self) -> bool: 
        """
        True if this build is free threaded and GIL is disabled
        """
        return self.build_supports_free_threading and (not self.gil_enabed)
    



def _build_supports_free_threading() -> bool:
    """
    Return True if this Python build supports free-threading: 
    Py_GIL_DISABLED. 
    """
    return bool(sysconfig.get_config_var("Py_GIL_DISABLED"))


def _gil_enabled_runtime() -> bool | None:
    """
    Return True if the GIL is enabled at runtime, False if disabled, or None
    if we can't tell on this interpreter.
    """
    checker = getattr(sys, "_is_gil_enabled", None)
    if checker is None:
        return None
    else: 
        return checker

def get_free_threading_info() -> FreeThreadingInfo:
    """
    Collect structured info about free-threading support.
    """
    return FreeThreadingInfo(
        build_supports_free_threading=_build_supports_free_threading(),
        gil_enabled=_gil_enabled_runtime(),
    )


def is_free_threaded() -> bool:
    """
    Convenience wrapper used by the rest of the library.

    Returns True only when:
    * this is a free-threaded Python build (GIL optional), and
    * the GIL is currently disabled for this process.
    """

    return get_free_threading_info().is_free_threaded

"""5. Process fallback stub
Later you’ll implement actual process-based backends (multiprocessing,
concurrent.futures.ProcessPoolExecutor, etc). For Phase 0, we just provide a
clear stub.

Create src/pyparallel/compat/process_fallback.py:

python
Kopiera kod"""

from __future__ import annotations

from typing import Callable, Iterable, TypeVar, Sequence

T = TypeVar("T")
U = TypeVar("U")


def parallel_map_process_fallback(
    func: Callable[[T], U],
    items: Iterable[T],
    *,
    workers: int | None = None,
) -> Sequence[U]:
    """
    Placeholder process-based parallel map.

    Intended to be used on non-free-threaded Pythons as a safer alternative
    to threads for CPU-bound work.

    Phase 0: this is just a stub so the API exists. We'll fill in a
    multiprocessing-based implementation in a later phase.
    """
    raise NotImplementedError(
        "process fallback not implemented yet; "
        "this is a Phase 0 compatibility stub."
    )