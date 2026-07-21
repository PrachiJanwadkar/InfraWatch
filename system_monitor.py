import psutil
import socket
import platform
import time

def get_system_info():

    vm = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    swap = psutil.swap_memory()
    network = psutil.net_io_counters()

    cpu_freq = psutil.cpu_freq()

    cpu = psutil.cpu_percent(interval=1)

    processes = []

    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status']):
     try:
        info = p.info

        # Skip the Windows idle process
        if info['name'] == "System Idle Process":
            continue

        processes.append(info)

     except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

    top_cpu = sorted(
    processes,
    key=lambda x: x['cpu_percent'],
    reverse=True
    )[:10]

    return {

        "hostname": socket.gethostname(),

        "ip": socket.gethostbyname(socket.gethostname()),

        "os": platform.system(),

        "kernel": platform.release(),
        "architecture": platform.machine(),

        "processor": platform.processor(),


        "boot": time.ctime(psutil.boot_time()),

        "cpu": cpu,

        "physical_cores": psutil.cpu_count(False),

        "logical_cores": psutil.cpu_count(True),

        "cpu_freq": round(cpu_freq.current,2),

        "memory": vm.percent,

        "memory_total": round(vm.total/(1024**3),2),

        "memory_available": round(vm.available/(1024**3),2),

        "swap": swap.percent,

        "disk": disk.percent,

        "disk_total": round(disk.total/(1024**3),2),

        "disk_free": round(disk.free/(1024**3),2),

        "bytes_sent": round(network.bytes_sent/(1024**2),2),

        "bytes_recv": round(network.bytes_recv/(1024**2),2),

        "packets_sent": network.packets_sent,

        "packets_recv": network.packets_recv,

        "processes": top_cpu

    }