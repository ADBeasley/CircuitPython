# import os
# import ipaddress
import wifi
import socketpool
import mdns

print()
print("Connecting to WiFi")


mdns_server = mdns.Server(wifi.radio)
mdns_server.hostname = "mypico"

#  connect to your SSID
wifi.radio.connect('SSID', 'password')

print("Connected to WiFi")


# pool = socketpool.SocketPool(wifi.radio)

#  prints MAC address to REPL
print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

#  prints IP address to REPL
print("My IP address is", wifi.radio.ipv4_address)
