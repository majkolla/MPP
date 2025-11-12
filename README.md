# Parallel Python implementation 

## Runtime & Scheduler

- Work-stealing thread pool
- Keeps all cores busy under irregular workloads (e.g., divide-and-conquer sort, graph).

- Tasks & futures with cancellation, timeouts, priority:

Foundation for all higher-level APIs.

Safety defaults:

Warn (or copy) when mutables cross threads; prefer functional patterns.
    1
CPU awareness:

Pool size = os.cpu_count() by default

## Data-parallel primtives 

- parallel_for(range, fun, chunk)
- parallel_map
- parallel_reduce 


## Algorthims 

### Sorting Algs
- parallel_mergesort()
- parallel_samplesort(type_buffer, ...)
- nth_element

## Pipeline 

- MPMC queues
