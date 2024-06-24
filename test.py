################################################################
# Install:
# * python -m pip install colorama
# * python -m pip install requests
#
# Usage:
# * MAKE SURE YOU READ THE WARNING
# * python LiquidCool.py
#
# Description:
# This script implements a simple load based control of two fans
# It first saves the original Fan settings, then starts 
# monitoring the CPU and GPU load. It integrates those values
# to dampen the value changes somewhat. It then uses the maximum
# of the two values to set the fan speeds.
#
# Warning: This script is written as an example and may or may 
# not kill your PC! Use at your own risk!
################################################################

import colorama
import json, requests
import time
import math

url = 'http://127.0.0.1:8085'

params = dict()

pos = lambda x, y: '\x1b[%d;%dH' % (y, x)
clear = lambda : "\033[2J\033[1;1f"

def getValue(sensorId):
	params=dict(id=sensorId, action="Get")
	resp = requests.post(url=url + "/Sensor", params = params, timeout=10);
	result = json.loads(resp.text);

	if result["result"] != "ok":
		raise Exception("Server returned error:\n " + result["message"].replace("\\n", "\n").replace("\\r", ""))
	if result["value"] == None:
		return None;
	else:
		return float(result["value"])

# def setValue(sensorId, sensorValue):
# 	if sensorValue == None:
# 		sensorValue = "null"
# 	params=dict(id=sensorId, action="Set", value=sensorValue)
# 	resp = requests.post(url=url + "/Sensor", params = params, timeout=10);
# 	result = json.loads(resp.text)
# 	if result["result"] != "ok":
# 		raise Exception("Server returned error:\n " + result["message"].replace("\\n", "\n").replace("\\r", ""))

def draw_progressbar(x, y, description, progress):
	p = '#'*math.floor(progress/5)
	p1 = '-'*math.ceil((100-progress)/5)
	print('{0}{1}[{2}{3}] {4}%   '.format(pos(x,y), description, p, p1, math.floor(progress*100)/100), end='')

def integrate(oldval, newval):
	return float(oldval)*0.8 + float(newval) * 0.2

def main():
	colorama.init()

	print(clear())

	try:
		integratedCPU = getValue("/intelcpu/0/load/0");
		integratedGPU = getValue("/gpu-nvidia/0/load/0");


		while 1:
			cpuLoad = getValue("/intelcpu/0/load/0");
			gpuLoad = getValue("/gpu-nvidia/0/load/0");

			integratedCPU = integrate(integratedCPU, cpuLoad)
			integratedGPU = integrate(integratedGPU, gpuLoad)

			draw_progressbar(1, 1, "CPU:  ", cpuLoad)
			draw_progressbar(1, 2, "GPU:  ", gpuLoad)

			draw_progressbar(1, 3, "IGPU: ", integratedCPU)
			draw_progressbar(1, 4, "IGPU: ", integratedGPU)
			
			print(pos(1, 1))
			time.sleep(1)
	except:
		print(clear())

		raise



if __name__ == '__main__':
    main()