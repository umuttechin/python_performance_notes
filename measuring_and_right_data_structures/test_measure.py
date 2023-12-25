from ..measure import heavy_work

def test_benchmark_heavy_work(benchmark):
    benchmark(heavy_work)