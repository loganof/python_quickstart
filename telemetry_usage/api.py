from fastapi import FastAPI, Depends
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.prometheus import PrometheusMetricsExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from functools import wraps
import time

app = FastAPI()

# 配置资源信息
resource = Resource(attributes={"service.name": "my-fastapi-service"})

# 设置TracerProvider
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# 设置Prometheus导出器
exporter = PrometheusMetricsExporter(port=8001)
span_processor = BatchSpanProcessor(exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# 初始化FastAPI Instrumentor
FastAPIInstrumentor.instrument_app(app, tracer_provider=trace.get_tracer_provider())


# 使用 lifespan 上下文管理器来替代 on_event
@app.on_event("startup")
async def startup_event():
    import prometheus_client
    from starlette_exporter import PrometheusMiddleware, handle_metrics

    app.add_middleware(PrometheusMiddleware)
    app.add_route("/metrics", handle_metrics)


# 监控函数调用的耗时
def trace_function(tracer, name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with tracer.start_as_current_span(name) as span:
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                span.set_attribute("execution_time", end_time - start_time)
                return result

        return wrapper

    return decorator


# 示例函数
@trace_function(tracer, "read_root")
@app.get("/")
def read_root():
    time.sleep(0.5)  # 模拟延迟
    return {"Hello": "World"}


@trace_function(tracer, "read_item")
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    time.sleep(0.5)  # 模拟延迟
    return {"item_id": item_id, "q": q}


# 启动应用
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
