import matplotlib.pyplot as plt
import json
import dateutil.parser

### IPv4 Emotet (TA542)
save_json = json.load(open("plot_ips.json"))
for e in save_json:
	plt.plot(dateutil.parser.parse(e[0]), e[1], e[2])
plt.ylabel("Amount of IPs added to AlienVault from TU Delft dataset (459 IPs)")
plt.xlabel("x = added by an API, o = added manually\nred = epoch1, green = epoch2, blue = epoch3, black = partner01")
plt.title("IPv4 Emotet (TA542)")
plt.show()

### SHA256 Emotet (TA542)
save_json = json.load(open("plot_sha256.json"))
for e in save_json:
	plt.plot(dateutil.parser.parse(e[0]), e[1], e[2])
plt.ylabel("Amount of SHA256 checksums added to AlienVault from TU Delft dataset (54 SHA256 checksums)")
plt.xlabel("x = added by an API, o = added manually")
plt.title("SHA256 Emotet (TA542)")
plt.show()

### URL Emotet (TA542)
save_json = json.load(open("plot_url.json"))
for e in save_json:
	plt.plot(dateutil.parser.parse(e[0]), e[1], e[2])
plt.ylabel("Amount of URLs added to AlienVault from TU Delft dataset (50 URLs)")
plt.xlabel("x = added by an API, o = added manually")
plt.title("URL Emotet (TA542)")
plt.show()

### email Emotet (TA542)
save_json = json.load(open("plot_email.json"))
for e in save_json:
	plt.plot(dateutil.parser.parse(e[0]), e[1], e[2])
plt.ylabel("Amount of email addresses added to AlienVault from TU Delft dataset (116 addresses)")
plt.xlabel("x = added by an API, o = added manually")
plt.title("Email addresses Emotet (TA542)")
plt.show()

### hostname Emotet (TA542)
save_json = json.load(open("plot_host.json"))
for e in save_json:
	plt.plot(dateutil.parser.parse(e[0]), e[1], e[2])
plt.ylabel("Amount of hostnames added to AlienVault from TU Delft dataset (107 hostnames)")
plt.xlabel("x = added by an API, o = added manually\ngreen = from URL, blue = from email address, black = from both")
plt.title("Hostnames Emotet (TA542)")
plt.show()
