import grpc
import api_gateway_pb2, api_gateway_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = api_gateway_pb2_grpc.APIGatewayServiceStub(channel=channel)

request = api_gateway_pb2.RouteRequestMessage(
    service_name="demo",
    payload="demo request"
)
responses = []

for i in range(10):
    response = stub.RouteRequest(request)
    responses.append(response)

print([{'resp': resp.response} for resp in responses])
