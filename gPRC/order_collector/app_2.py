import random
import time
import grpc
from order_collector_pb2 import FirstRequest, Order
import order_collector_pb2_grpc
from concurrent import futures


class OrderCollectorService(order_collector_pb2_grpc.OrderCollectorServicer):
    def randomOrderGenerator(self):
        return Order(
            user_id=random.randint(1, 1_000_000),
            price=random.randint(1_000, 5_000_000),
            dateTime=int(time.time()),
        )

    def Collect(self, request, context):
        while(True):
            yield self.randomOrderGenerator()


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

order_collector_pb2_grpc.add_OrderCollectorServicer_to_server(
    servicer=OrderCollectorService(),
    server=server
)
port = 5051
server.add_insecure_port("[::]:" + str(port))
server.start()
print("Server started on port: " + str(port))
server.wait_for_termination()
