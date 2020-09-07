import subprocess 
from win10toast import ToastNotifier

notifier = ToastNotifier()

ips = []

IP_DEVICE = '192.168.0.100'

proc = subprocess.Popen("arp -a",stdout=subprocess.PIPE) #opens the cmd and returns the ARP table

F = True
while F:
      line = proc.stdout.readline() #read cmd lines
      if not line:
          break
      try:
        connected_ip = line.decode('utf-8').split()
        ips.append(connected_ip)
        for i in ips:
            try:
                connected_ip = i[0]
                if connected_ip == IP_DEVICE:
                    notifier.show_toast("!!!","Device Connected") #send a windows notification
                    F=False
            except IndexError:
                pass
        
        
      except UnicodeDecodeError:
            pass

