from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    flow.response.content = flow.response.content.decode().replace("Simple messenger", "<<YOUR TEXT>>").encode()
    flow.response.content = flow.response.content.decode().replace("Send message", "<<YOUR TEXT>>").encode()