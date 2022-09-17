import grpc
from order_collector_pb2 import FirstRequest
from order_collector_pb2_grpc import OrderCollectorStub

channel = grpc.insecure_channel('localhost:5051')

client = OrderCollectorStub(channel)

req = FirstRequest(
    token="AAbbCCddEEff"
)

for result in client.Collect(req):
    print(result)
