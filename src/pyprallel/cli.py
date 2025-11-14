from __future__ import annotations
import argparse
from .examples.hello_cores import run_hello_cores



def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="pyparallel-bench",
        description="Tiny benchmark/demo CLI for pyparallel.",
    )
    parser.add_argument(
        "-n",
        "--threads",
        type=int,
        default=None,
        help="Number of threads to spawn (default: CPU count).",
    )
    parser.add_argument(
        "-i",
        "--iterations",
        type=int,
        default=200_000,
        help="Iterations per thread.",
    )
    args = parser.parse_args(argv)

    result = run_hello_cores(
        n_threads=args.threads,
        iterations_per_thread=args.iterations,
    )

    print(
        f"Ran {len(result.per_thread)} threads, "
        f"{result.total_iterations} total iterations "
        f"in {result.wall_time_s:.3f}s"
    )
