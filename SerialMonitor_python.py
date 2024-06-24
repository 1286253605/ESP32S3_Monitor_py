import wmi

hwmon = wmi.WMI(namespace="root\LibreHardwareMonitor")
sensors = hwmon.Sensor(SensorType="Control")

for s in sensors:
	print(s)
 