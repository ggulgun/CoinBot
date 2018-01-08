import os, requests, json
from errbot import BotPlugin, botcmd, arg_botcmd

class ethereum(BotPlugin):

    @botcmd # Ethereum price in TR
    def ethereum(self, msg, args):
        urlKoineks = "https://koineks.com/ticker"
        response = requests.get(urlKoineks)
        data = response.json()
        currentAmountETHKoineks = data["ETH"]["current"]


        urlBTCTurk = "https://www.btcturk.com/api/ticker"
        response = requests.get(urlBTCTurk)
        data = response.json()
        currentAmountBTCTurk = data[2]["last"]


        return "Koineks : " + str(currentAmountETHKoineks) + " TL \n" +  "BtcTurk : "  + str(currentAmountBTCTurk) + " TL"
