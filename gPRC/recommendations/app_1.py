import grpc
from product_recommendations_pb2 import Category, RRequest
from product_recommendations_pb2_grpc import RecommendationsStub

channel = grpc.insecure_channel('localhost:5050')

client = RecommendationsStub(channel)

req = RRequest(
    user_id=1,
    category=Category.CAR,
    result_limit=12,
)

recommendationsResults = client.Recommend(
    req,

)
print(recommendationsResults)
