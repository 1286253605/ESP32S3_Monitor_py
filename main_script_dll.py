import json, requests
import time
import serial
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
from Ui_untitled import Ui_MainWindow
import serial.tools.list_ports
# ---------------------系统托盘---------------------
from PyQt5.QtWidgets import QSystemTrayIcon, QAction
from PyQt5.QtWidgets import QMenu
from PyQt5.QtGui import QIcon
# ---------------------DLL---------------------
import clr
import os, sys
clr.AddReference('./LibreHardwareMonitorLib') # 这里不需要加后缀.dll 内部会自动拼接
from LibreHardwareMonitor.Hardware import Computer


# -----------------------Sensor--------------------------------
url = 'http://127.0.0.1:8085'

params = dict()

computer_tmp = Computer()

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

def computer_init():
    # computer_tmp = Computer()
    computer_tmp.IsCpuEnabled = True  # 获取CPU时用
    computer_tmp.IsGpuEnabled = True  # 获取GPU时用
    computer_tmp.IsMemoryEnabled = True  # 获取内存时用
    # self.computer_tmp.IsNetworkEnabled = True  # 获取网卡数据时使用
    computer_tmp.Open()
    

    
def get_value_dll(sensor_id):
    for computer in computer_tmp.Hardware:
        computer.Update()
        for s in computer.Sensors:
            if( str(s.Identifier) == sensor_id ):
                if( s.Value == None ):
                    return 0
                return s.Value

    

def print_data():
    try:
        while 1:
            cpuLoad = get_value_dll("/intelcpu/0/load/0");
            cpuTemp = get_value_dll("/intelcpu/0/temperature/14")
            gpuLoad = get_value_dll("/gpu-nvidia/0/load/0");
            gpuTemp = getValue("/gpu-nvidia/0/temperature/0")
            ramLoad = getValue("/ram/load/0")
            
            print("CPU Load:\t"+str(cpuLoad))
            print("CPU temp:\t"+str(cpuTemp))
            print("GPU Load:\t"+str(gpuLoad))

            time.sleep(1)
    except:
        raise



# -----------------------UI--------------------------------
class MyWindow( QMainWindow ):
    # 有QMainWindow QWidget 要和Ui保持一致 
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.init_timer()
        self.serial_now     = []
        self.send_gap_time  = 0
        
        self.combo_box_init()
        self.connect_signal_slot()
        

    def combo_box_init(self):
        # Baud Rate
        self.ui.comboBox_baud.addItem("9600")
        self.ui.comboBox_baud.addItem("19200")
        self.ui.comboBox_baud.addItem("38400")
        self.ui.comboBox_baud.addItem("57600")
        self.ui.comboBox_baud.addItem("115200")


    def connect_signal_slot(self):
        self.ui.pushButton_flush.clicked.connect(self.slot_btn_flush_serial)
        self.ui.pushButton_open_serial.clicked.connect(self.slot_btn_open_serial)
        self.ui.pushButton_monitor_stop.clicked.connect(self.timer_stop_send)
        self.ui.pushButton_monitor_start.clicked.connect(self.timer_start_send)

# ---------------------系统托盘---------------------


            
# -----------------------TIMER--------------------------------
    def init_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_send_data)
        # self.timer.start(1000)          # 间隔1000ms
        # self.timer.stop()
        pass

    def timer_send_data(self):
        
        cpuLoad = int(get_value_dll("/intelcpu/0/load/0"))
        cpuTemp = int(get_value_dll("/intelcpu/0/temperature/14"))
        gpuLoad = int(get_value_dll("/gpu-nvidia/0/load/0"))
        gpuTemp = int(get_value_dll("/gpu-nvidia/0/temperature/0"))
        ramLoad = int(get_value_dll("/ram/load/0"))
        print("CPU Load:\t"+str(cpuLoad))
        print("GPU Load:\t"+str(gpuLoad))
        print("CPU temp:\t"+str(cpuTemp))
        
        # self.serial_class.write((str(cpuLoad)+",").encode("utf-8"))
        # self.serial_class.write((str(cpuTemp)+",").encode("utf-8"))
        # self.serial_class.write((str(gpuLoad)+",").encode("utf-8"))
        # self.serial_class.write((str(gpuTemp)+",").encode("utf-8"))
        # self.serial_class.write((str(ramLoad)+",").encode("utf-8"))
        str_temp = str(cpuLoad) + "," + str(cpuTemp) + "," + str(gpuLoad) + "," + str(gpuTemp) + "," + str(ramLoad) + ",end,"
        self.serial_class.write( str_temp.encode("utf-8") )
        
        # serial.Serial.write(serial, gpuLoad)
        pass

    def timer_start_send(self):
        self.send_gap_time = int(self.ui.comboBox_gap_time.currentText())
        self.timer.start(self.send_gap_time)
        pass

    def timer_stop_send(self):
        self.timer.stop()
        


# -----------------------Serial--------------------------------
    def slot_btn_open_serial(self):
        port_from_combo         = self.ui.comboBox_com_select.currentText()
        baud_rate_from_combo    = int(self.ui.comboBox_baud.currentText())
        
        # PARITY_NONE, PARITY_EVEN, PARITY_ODD, PARITY_MARK, PARITY_SPACE = 'N', 'E', 'O', 'M', 'S'
        SELECT_PARITY = { "NONE":'N', "EVEN":'E', "ODD":'O'}
        
        self.serial_class = serial.Serial( port=port_from_combo, 
                                        baudrate=baud_rate_from_combo, 
                                        parity=serial.PARITY_NONE,
                                        stopbits=serial.STOPBITS_ONE,
                                        bytesize=8)
        try:
            serial.Serial.open()
        except Exception as exc:
            # print error
            print(str(exc))
        time.sleep(1)


    #按下刷新按钮 更新当前串口
    def slot_btn_flush_serial( self ):
        #获取当前可用COM口
        port_list = list( serial.tools.list_ports.comports() )
        if( len( port_list ) == 0 ):
            print( "No serial" )
        else:
            for i in range( 0, len( port_list ) ):
                self.serial_now.append( port_list[ i ].name )
        #更新到UI中
        for i in self.serial_now:
            self.ui.comboBox_com_select.addItem( i )


# -----------------------Main--------------------------------
if __name__ == "__main__":
        # -----DLL-----
    computer_init()
    # print_data()
    # -----DLL-----
    app = QApplication([])              # 传入空参数列表
    window = MyWindow()
    window.show()
    # -----系统托盘-----
    app.setQuitOnLastWindowClosed(False)
    icon = QIcon("./monitor.png")
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    menu = QMenu()
    option1 = QAction("ShowMainWindow")
    option1.triggered.connect(window.show)
    option2 = QAction("Exit")
    option2.triggered.connect(app.quit)
    menu.addAction(option1)
    menu.addAction(option2)
    tray.setContextMenu(menu)
    
    # -----系统托盘-----

    app.exec()

