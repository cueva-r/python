import psutil

cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
cpu_freq = psutil.cpu_freq(percpu=True)

print("Uso de CPU por núcleo: ")
for i, (percent, freq) in enumerate(zip(cpu_percent, cpu_freq), start=1):
    print(f"Núcleo {i}: {percent}% Frecuencia: {freq.current}MHz")

virtual_mem = psutil.virtual_memory()
swap = psutil.swap_memory()

print("\nMemoria virtual: ")
print(f"Total: {virtual_mem.total / (1024 ** 3):.2f} GB")
print(f"Usado: {virtual_mem.used / (1024 ** 3):.2f} GB")
print(f"total del intercambio: {swap.total / (1024 ** 3):.2f} GB")
print(f"intercambio usado: {swap.used / (1024 ** 3):.2f} GB")

network = psutil.net_io_counters()
print("\ninformación de red: ")
print(f"Bytes recibidos: {network.bytes_recv}")
print(f"Bytes enviados: {network.bytes_sent}")

try:
    temperatures = psutil.sensors_temperatures()
    if temperatures:
        print("\nTemperaturas: ")
        for name, entries in temperatures.items():
            for entry in entries:
                print(f"{name}: {entry.current}°C")
    else:
        print("\nInformación de temperatura no disponible")
except AttributeError:
    print("\nInformación de temperatura no disponible")

#información de la batería
battery = psutil.sensors_battery()
if battery:
    plugged = "Conectado" if battery.power_plugged else "No conectado"
    print(f"\nEstado de batería: {plugged}, {battery.percent}%")
else:
    print("\nInformación de la batería no disponible")

disk = psutil.disk_usage('/')
print("\ninformación de disco: ")
print(f"Espacio de disco: {disk.total / (1024 ** 3):.2f} GB")
print(f"Espacio de disco usado: {disk.used / (1024 ** 3):.2f} GB")
print(f"Espacio libre en disco: {swap.free / (1024 ** 3):.2f} GB")