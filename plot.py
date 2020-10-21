import matplotlib.pyplot as plt
import json
import dateutil.parser

save_json = json.load(open("plot_ips.json"))
for e in save_json:
	plt.plot(dateutil.parser.parse(e[0]), e[1], e[2])
plt.ylabel("Amount of IPs added to AlienVault from TU Delft dataset (459 IPs)")
plt.xlabel("x = added by an API, o = added manually\nred = epoch1, green = epoch2, blue = epoch3, black = partner01")
plt.show()
