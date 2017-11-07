
## TCown

TCown is a collection of python scripts that will take [ThreatConnect](https://www.threatconnect.com) export spreadsheet files (`.xlsx`) and utilize them for scanning packet capture files (`.pcap`) or file systems. Currently just hacked together for the basic idea, will finish later. Pushed cause c9 is sketch.

Dependencies: `sudo pip install openpyxl scapy`

Usage for tcown-pcap.py:
```
> python tcown-pcap.py example/ThreatConnectExport.xlsx example/Traffic.pcap
Scanning Traffic.pcap for signatures from ThreatConnectExport-badsites.xlsx...
! 4 - Host - windowslayer.in - <country> - <description> - Packet 1234
```

Usage for tcown-files.py:
```
> python tcown-files.py ThreatConnectExport-badfiles.xlsx /path/to/scan/
Scanning /path/to/scan/ for signatures from ThreatConnectExport-badfiles.xlsx...
! 27 - Host - 442c98598c1ca91a0541764e95ccd05e - <country> - <description> - /path/to/scan/evilfile
```
