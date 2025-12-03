import tornado.ioloop
import tornado.web
from dask.distributed import Client, LocalCluster

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

class FastHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, fast response!")

class FibHandler(tornado.web.RequestHandler):
    async def get(self, n):
        n = int(n)
        future = self.application.dask_client.submit(fib, n)
        result = await future  # tunggu hasil dari Dask
        self.write(str(result))

def make_app(dask_client):
    app = tornado.web.Application([
        (r"/fast", FastHandler),
        (r"/fib/(\d+)", FibHandler),
    ])
    app.dask_client = dask_client
    return app

def main():
    # setup Dask cluster
    cluster = LocalCluster(n_workers=2, threads_per_worker=1)
    client = Client(cluster)

    app = make_app(client)
    app.listen(8000)
    print("Server running at http://localhost:8000")
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
