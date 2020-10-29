import matplotlib.pyplot as plt
import json
import dateutil.parser

### IPv4 Emotet (TA542)
save_json = json.load(open("plot_ips.json"))
fig, ax = plt.subplots(1, 1, figsize=(9.5, 7))
for e in save_json:
	ax.plot(dateutil.parser.parse(e[0]), e[1], e[2])
plt.ylabel("Amount of IPs added to AlienVault from TU Delft dataset (459 IPs)")
plt.xlabel("x = added by an API, o = added manually\nred = epoch1, green = epoch2, blue = epoch3, black = partner01")
plt.title("IPv4 Emotet (TA542)")
plt.show()
fig.savefig("IPv4_TA542.pdf")

### SHA256 Emotet (TA542)
save_json = json.load(open("plot_sha256.json"))
fig, ax = plt.subplots(1, 1, figsize=(9.5, 7))
for e in save_json:
	ax.plot(dateutil.parser.parse(e[0]), e[1], e[2])
plt.ylabel("Amount of SHA256 checksums added to AlienVault from TU Delft dataset (54 SHA256 checksums)")
plt.xlabel("x = added by an API, o = added manually")
plt.title("SHA256 Emotet (TA542)")
plt.show()
fig.savefig("SHA256_TA542.pdf")

### URL Emotet (TA542)
save_json = json.load(open("plot_url.json"))
fig, ax = plt.subplots(1, 1, figsize=(9.5, 7))
for e in save_json:
	ax.plot(dateutil.parser.parse(e[0]), e[1], e[2])
plt.ylabel("Amount of URLs added to AlienVault from TU Delft dataset (50 URLs)")
plt.xlabel("x = added by an API, o = added manually")
plt.title("URL Emotet (TA542)")
plt.show()
fig.savefig("URL_TA542.pdf")

### email Emotet (TA542)
save_json = json.load(open("plot_email.json"))
fig, ax = plt.subplots(1, 1, figsize=(9.5, 7))
for e in save_json:
	ax.plot(dateutil.parser.parse(e[0]), e[1], e[2])
plt.ylabel("Amount of email addresses added to AlienVault from TU Delft dataset (116 addresses)")
plt.xlabel("x = added by an API, o = added manually")
plt.title("Email addresses Emotet (TA542)")
plt.show()
fig.savefig("email_TA542.pdf")

### hostname Emotet (TA542)
save_json = json.load(open("plot_host.json"))
fig, ax = plt.subplots(1, 1, figsize=(9.5, 7))
for e in save_json:
	ax.plot(dateutil.parser.parse(e[0]), e[1], e[2])
plt.ylabel("Amount of hostnames added to AlienVault from TU Delft dataset (107 hostnames)")
plt.xlabel("x = added by an API, o = added manually\ngreen = from URL, blue = from email address, black = from both")
plt.title("Hostnames Emotet (TA542)")
plt.show()
fig.savefig("host_TA542.pdf")
