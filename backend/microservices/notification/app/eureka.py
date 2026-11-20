"""Eureka registration helpers for the notification microservice."""
import os
import socket

import py_eureka_client.eureka_client as eureka_client


def resolve_ip() -> str:
    env_ip = os.getenv("IP_ADDR")
    if env_ip:
        return env_ip
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]
    except OSError:
        return "127.0.0.1"


async def start_eureka(port: int) -> None:
    ip_addr = resolve_ip()
    eureka_server = os.getenv("EUREKA_SERVER", "http://localhost:8761/eureka/")
    await eureka_client.init_async(
        eureka_server=eureka_server,
        app_name="NOTIFICATION",
        instance_port=port,
        instance_host=ip_addr,
        instance_ip=ip_addr,
        health_check_url=f"http://{ip_addr}:{port}/health",
        status_page_url=f"http://{ip_addr}:{port}/info",
        home_page_url=f"http://{ip_addr}:{port}/",
    )


async def stop_eureka() -> None:
    try:
        await eureka_client.stop_async()
    except Exception:
        pass
