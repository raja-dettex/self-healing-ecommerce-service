# 🛠️ Self-Healing E-commerce Service

A minimal microservices-based e-commerce backend with gRPC communication and a central API Gateway that supports self-healing capabilities.

## 🔧 Architecture

- **API Gateway**: Single entry point for client requests. Routes requests to appropriate gRPC services based on `service_name`.
- **User Service**: Handles user-related logic via gRPC.
- **Order Service**: Manages order placement and tracking via gRPC.
- **Recovery Logic**: Built-in anomaly detection and auto-recovery features.

## 📦 Microservices

- `user_service/`: gRPC service for user creation, authentication, and info.
- `order_service/`: gRPC service for order creation, status, and history.
- `api_gateway/`: RESTful interface for external clients. Internally routes to gRPC endpoints.

## 🚀 API Gateway Endpoints

### `POST /route`

Routes a JSON payload to the appropriate gRPC service.

**Request Body:**
```json
{
  "service_name": "user" | "order",
  "payload": {
    // JSON payload to be forwarded to the service
  }
}
```

### `GET /anomalies`

Returns a list of detected service anomalies for debugging or observability.

## 📦 Running the Services

1. **Clone the repo:**
   ```bash
   git clone https://github.com/raja-dettex/self-healing-ecommerce-service.git
   cd self-healing-ecommerce-service
   ```

2. **Run using Docker Compose:**
   ```bash
   docker-compose up --build
   ```
   
## 📈 Monitoring

- Prometheus is configured for basic service monitoring.
- Access Prometheus UI at: `http://localhost:9090`



