import json
import requests

res = requests.get("https://myarad.primariaarad.ro/dm_arad/ext_services.nsf/xsp/.jaxrs/myCity/getAll")
data = json.loads(res.text)
entries = data["entries"]

total = len(entries)
solutionate = 0

for entry in entries:
	if entry["status"] == "Solutionata":
		solutionate += 1

procent = round(solutionate * 100 / total)
print("{0}% au fost rezolvate".format(procent))
print("{0} din {1} au fost rezolvate".format(solutionate, total))
