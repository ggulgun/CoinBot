import os, requests, json
from errbot import BotPlugin, botcmd, arg_botcmd

class bitcoin(BotPlugin):

    @botcmd # Bitcoin price in TR
    def bitcoin(self, msg, args):
        urlKoineks = "https://koineks.com/ticker"
        response = requests.get(urlKoineks)
        data = response.json()
        currentAmountBTCKoineks = data["BTC"]["current"]


        urlBTCTurk = "https://www.btcturk.com/api/ticker"
        response = requests.get(urlBTCTurk)
        data = response.json()
        currentAmountBTCTurk = data[0]["last"]

        urlParibu = "https://www.paribu.com/ticker"
        response = requests.get(urlParibu)
        data = response.json()
        currentAmountParibu = data["BTC_TL"]["last"]

        return "Koineks : " + str(currentAmountBTCKoineks) + " TL \n" +  "BtcTurk : "  + str(currentAmountBTCTurk) + " TL \n" + "Paribu : " + str(currentAmountParibu) + " TL"
