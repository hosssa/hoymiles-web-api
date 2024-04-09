/**
 * Sample script to collect hoymiles DTU data with ioBroker 
 * webApiHost and dtuSerialNo need to be configured accordingly.
 */

const webApiHost = "http://<hostname>:<port>"
const dtuSerialNo = "<xxx>"

const states = {
    dtuPower: `hoymiles.DTUBI-${dtuSerialNo}.dtuPower`,
    dtuDailyEnergy: `hoymiles.DTUBI-${dtuSerialNo}.dtuDailyEnergy`,
    totalEnergy: `hoymiles.DTUBI-${dtuSerialNo}.totalEnergy`
} 

// init states
for (const state of Object.values(states)) {
    if(!existsState(state)) createState(state)
}

// log totalEnergy every 10 minutes 
schedule('*/10 * * * *', () => {
    get('appGetHistPower')
    .then(({totalEnergy}) => setState(states.totalEnergy, totalEnergy))
    .catch(error => log(error, 'error'));
});

// log dtuPower every 5 seconds 
schedule('*/5 * * * * *', () => {
    get('getRealDataNew')
    .then(({dtuPower, dtuDailyEnergy}) => {
        setState(states.dtuPower, dtuPower);
        setState(states.dtuDailyEnergy, dtuDailyEnergy); })
    .catch(error => log(error, 'error'));
});

// promisified httpGet function
const get = (endpoint) => {
    return new Promise((resolve, reject) => {
        httpGet(webApiHost + "/" + endpoint + "/DTUBI-" + dtuSerialNo, { timeout: 1000 }, (error, response) => {
            if(error) reject(error)
            else if(response.statusCode !== 200) reject(response.data)
            else resolve(JSON.parse(response.data))
        })
    });
}