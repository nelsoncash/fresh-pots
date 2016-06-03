from scapy.all import *
import requests
SLACK_API_URL = 'https://slack.com/api/chat.postMessage'

def send_message():
  data = {
    "token": "<TOKEN_HERE>",
    "channel" : "<CHANNEL_ID_HERE>",
    "icon_url" : "http://i.imgur.com/4tPGRDP.gif",
    "text": ":coffee: Fresh Pots :coffee:"
  }
  requests.post(SLACK_API_URL, data)

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)i
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == '<DASH_MAC_ADDRESS_HERE>':
        send_message()

print sniff(prn=arp_display, filter="arp", store=0)