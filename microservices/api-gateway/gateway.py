import json

from fastapi import FastAPI, Request, HTTPException
import uvicorn
import grpc
from concurrent import futures
import api_gateway_pb2, api_gateway_pb2_grpc
from service import APIGatewayService
from prometheus_client import generate_latest, Histogram, Counter, CONTENT_TYPE_LATEST
import time
from fastapi.responses import Response
from recovery.anomaly.anomaly_detector import get_anomalies

REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency in seconds")
ERROR_COUNTER = Counter("request_errors_total", "Total request errors")

app = FastAPI()


@app.get("/metrics")
def get_metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/")
def welcome():
    return "running , welcome"

@app.get("/anomalies")
def anomalies():
    anomalies_data = get_anomalies()
    if len(anomalies_data) == 0:
        return { 'status': 'normal'}
    return {'status': 'anomaly detected', 'anomalies': anomalies_data}
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    api_gateway_pb2_grpc.add_APIGatewayServiceServicer_to_server(APIGatewayService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("server started on port 50051")
    server.wait_for_termination()

@app.post("/route")
async def route(request: Request):
    start = time.time()
    data = await request.json()
    if "service_name" not in data or "payload" not in data:
        raise HTTPException(status_code=400, detail="Missing required fields: service_name or payload")
    try:
        service_name = data["service_name"]
        payload = json.dumps(data["payload"])
        channel = grpc.insecure_channel("localhost:50051")
        stub = api_gateway_pb2_grpc.APIGatewayServiceStub(channel)
        response: api_gateway_pb2.RouteResponseMessage = stub.RouteRequest(api_gateway_pb2.RouteRequestMessage(service_name=service_name, payload=payload))
        REQUEST_LATENCY.observe(time.time() - start)
        return { "response" : response.response}
    except Exception as e:
        ERROR_COUNTER.inc()
        return { "response": str(e)}
    


if __name__ == '__main__':
    print(api_gateway_pb2.RouteResponseMessage(response="request routed"))
    import threading
    threading.Thread(target=serve, daemon=True).start()
    uvicorn.run(app, host='0.0.0.0', port=8000)
