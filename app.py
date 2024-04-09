from flask import Flask, render_template
from google.protobuf.json_format import MessageToJson
from hoymiles_wifi.dtu import DTU

app = Flask(__name__)

@app.route("/")
@app.route("/<hostname>")
def index(hostname="<hostname>"):
	return render_template("index.html", hostname=hostname)

@app.route("/getRealDataNew/<hostname>")
async def get_real_data_new(hostname):
	dtu = DTU(hostname)
	response = await dtu.async_get_real_data_new()
	if response:
		return MessageToJson(response)
	else:
		return error()

@app.route("/getRealDataHms/<hostname>")
async def get_real_data_hms(hostname):
	dtu = DTU(hostname)
	response = await dtu.async_get_real_data_hms()
	if response:
		return MessageToJson(response)
	else:
		return error()

@app.route("/getRealData/<hostname>")
async def get_real_data(hostname):
	dtu = DTU(hostname)
	response = await dtu.async_get_real_data()
	if response:
		return MessageToJson(response)
	else:
		return error()

@app.route("/getConfig/<hostname>")
async def get_config(hostname):
	dtu = DTU(hostname)
	response = await dtu.async_get_config()
	if response:
		return MessageToJson(response)
	else:
		return error()
  
@app.route("/networkInfo/<hostname>")
async def network_info(hostname):
	dtu = DTU(hostname)
	response = await dtu.async_network_info()
	if response:
		return MessageToJson(response)
	else:
		return error()

@app.route("/appInformationData/<hostname>")
async def app_information_data(hostname):
	dtu = DTU(hostname)
	response = await dtu.async_app_information_data()
	if response:
		return MessageToJson(response)
	else:
		return error()

@app.route("/appGetHistPower/<hostname>")
async def app_get_hist_power(hostname):
	dtu = DTU(hostname)
	response = await dtu.async_app_get_hist_power()
	if response:
		return MessageToJson(response)
	else:
		return error()

@app.route("/getInformationData/<hostname>")
async def get_information_data(hostname):
	dtu = DTU(hostname)
	response = await dtu.async_get_information_data()
	if response:
		return MessageToJson(response)
	else:
		return error()

@app.route("/heartbeat/<hostname>")
async def heartbeat(hostname):
	dtu = DTU(hostname)
	response = await dtu.async_heartbeat()
	if response:
		return MessageToJson(response)
	else:
		return error()

@app.post("/restartDtu/<hostname>")
async def restart_dtu(hostname):
	dtu = DTU(hostname)
	response = await dtu.async_restart_dtu()
	if response:
		return MessageToJson(response)
	else:
		return error()

@app.post("/turnOnInverter/<hostname>")
async def turn_on_inverter(hostname):
	dtu = DTU(hostname)
	response = await dtu.async_turn_on_inverter()
	if response:
		return MessageToJson(response)
	else:
		return error()

@app.post("/turnOffInverter/<hostname>")
async def turn_off_inverter(hostname):
	dtu = DTU(hostname)
	response = await dtu.async_turn_off_inverter()
	if response:
		return MessageToJson(response)
	else:
		return error()

def error():
	return "Unable to get response from DTU!", 500

if __name__ == "__main__":
    app.run(debug=True)
