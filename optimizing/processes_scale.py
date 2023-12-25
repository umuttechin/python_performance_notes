"""
Scaling
    Threading and asyncio on a CPU core
    Multiprocessing on more CPU cores
    Use more machines

Celery(open source library)
    Task queue
    Data processing
    Run on many worker machines

Dask
    Integrates with Numpy and Pandas
    Data science
    Scaling from notebook to cluster

Ray
    Framework for scaling Python applications
    Scaling from notebook to cluster
    Designate to be general purpose
    Machine learning workloads

Kubernetes
    General purpose
    Autoscaling
    Cloud manages service

"""
from dask.distributed import Client


def clean_order(order_id):
    for _ in range(500_000_000):
        pass
    print(f"finished thread {order_id}.")




if __name__ == '__main__':
    client = Client()
    orders = [i * 10 for i in range(5)]
    client.map(clean_order, orders)

