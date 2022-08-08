```sh

pip install grpcio-tools


pip install grpcio

first: cd recommendations 

python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/product_recommendations.proto

```