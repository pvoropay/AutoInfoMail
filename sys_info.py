#!/usr/bin/env python3
import psutil
import socket

def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        print("Error getting IP address:", e)
        return None

def get_system_info():
    try:
        battery_percent = psutil.sensors_battery().percent
        memory_free = psutil.virtual_memory().available / (1024 * 1024)
        cpu_load = psutil.cpu_percent(interval=5)
        return battery_percent, memory_free, cpu_load
    except Exception as e:
        print("Error getting system info:", e)
        return None

ip_address = get_ip_address()
battery, memory, cpu = get_system_info()
