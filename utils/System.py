import os
import sys
import wmi
import requests
import subprocess



def getSystem():

    def get_hwid():
        try:
            hwid = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True,
                                        stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
        except:
            hwid = "None"
        return hwid

    cpu = wmi.WMI().Win32_Processor()[0].Name
    gpu = wmi.WMI().Win32_VideoController()[0].Name
    ram = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576, 0)
    hwid = get_hwid()

    return { 
            "hostname ": os.getenv('COMPUTERNAME'),
            "username" : os.getenv('USERNAME'),
            "CPU":cpu,
            "GPU":gpu,
            "RAM":ram,
            "HWID":hwid
        }