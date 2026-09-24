# === Stage 61: Add performance timing for core list and search operations ===
# Project: GearLocker
import time

def benchmark_list_operations(locker):
    """Benchmark core list and search operations of the locker."""
    start = time.perf_counter()
    _ = list(locker.items.values())
    _ = list(locker.borrowers.values())
    elapsed_list = time.perf_counter() - start
    print(f"List operations: {elapsed_list:.4f}s")

    start = time.perf_counter()
    _ = locker.search_items("gloves")
    _ = locker.search_items("helmet")
    _ = locker.search_items("unknown_item")
    elapsed_search = time.perf_counter() - start
    print(f"Search operations: {elapsed_search:.4f}s")
