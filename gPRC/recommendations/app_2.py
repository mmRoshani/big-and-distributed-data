import grpc
from matplotlib.pyplot import title
from product_recommendations_pb2 import Category, RRequest, Ad, Ads
import product_recommendations_pb2_grpc
from concurrent import futures

booster = {
    Category.MELK: [
        Ad(id=1, title='Cool', price=10.40),
        Ad(id=2, title='Best', price=100.40),
        Ad(id=3, title='Excellent', price=1000.40),
    ],
    Category.CAR: [
        Ad(id=1, title='Cool', price=1.40),
        Ad(id=2, title='Best', price=2.40),
        Ad(id=3, title='Excellent', price=3.40),
        Ad(id=4, title='Perfect', price=4.40),
    ],
    Category.DIGITAL: [
        Ad(id=1, title='Cool', price=0.400),
        Ad(id=2, title='Best', price=0.50),
        Ad(id=3, title='Excellent', price=0.60),
        Ad(id=4, title='Perfect', price=0.70),
    ]
}


class RecommendationService(product_recommendations_pb2_grpc.RecommendationsServicer):
    def Recommend(self, request, context):
        ads = booster[request.category]
        return Ads(ad=ads)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

product_recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
    servicer=RecommendationService(),
    server=server
)
port = 5050
server.add_insecure_port("[::]:" + str(port))
server.start()
print("Server started on port: " + str(port))
server.wait_for_termination()
