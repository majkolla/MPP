from dataclasses import dataclass 
import os
import threading
import time
from typing import List


@dataclass
class ThreadStats:
    thread_index: int
    iterations: int
    duration_s: float


@dataclass
class HelloCoresResult:
    total_iterations: int
    per_thread: List[ThreadStats]
    wall_time_s: float


def run_hello_cores(n_threads: int | None = None, iterations_per_thread: int = 200_000,) -> HelloCoresResult:
    """
    Start N threads, each increments a counter iterations_per_thread times,
    and return some basic stats.

    This is intentionally simple and CPU-bound to create a simple benchmark
    and compare the GIL vs free threaded programs.  
    """
    
    if n_threads is None or n_threads <= 0:
        n_threads = os.cpu_count() or 4 

    threads: list[threading.Thread] = []
    stats: list[ThreadStats] = []
    stats_lock = threading.Lock()

    def worker(idx: int) -> None:
        counter = 0
        start = time.perf_counter()
        for _ in range(iterations_per_thread):
            counter += 1 # is this okey? no racing problem or lock issues here?
        end = time.perf_counter()
        # store stats safely
        with stats_lock:
            stats.append(
                ThreadStats(
                    thread_index=idx,
                    iterations=counter,
                    duration_s=end - start,
                )
            )

    start_wall = time.perf_counter()
    for i in range(n_threads):
        t = threading.Thread(target=worker, args=(i,), name=f"worker-{i}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end_wall = time.perf_counter()

    total_iterations = sum(s.iterations for s in stats)
    # sort by index for stable output
    stats.sort(key=lambda s: s.thread_index)

    return HelloCoresResult(
        total_iterations=total_iterations,
        per_thread=stats,
        wall_time_s=end_wall - start_wall,
    )



# I should compare 
def main() -> None:
    """
    Small CLI entrypoint, wired up as `pyparallel-hello`.
    """
    result = run_hello_cores()
    print(f"Total iterations: {result.total_iterations}")
    print(f"Wall time: {result.wall_time_s:.3f}s")
    print("Per-thread:")
    total_time_thread = 0 
    for s in result.per_thread: 
        total_time_thread += s.duration_s
    for s in result.per_thread:
        print(
            f"  thread {s.thread_index:2d}: "
            f"{s.iterations} iters in {s.duration_s:.3f}s"
        )
     
     
    print(f"total time with threads: {total_time_thread}")
    
    
    print("------------------------Sequental part-----------------------------")
    counter_seq: int = 0
    start= time.perf_counter()
    for i in range(200_000 * 22): 
       counter_seq += 1 
    end = time.perf_counter()
    print(end - start)

if __name__ == "__main__": 
    main()






















