import requests
import json

daemon = "daemonhost to be written"
d = "http://" + daemon

def Balance(publicKey) {
    res = requests.get(d + "/balance/" + publicKey)
    return res.json()
}

def GetTxById(idd) {
    res = requests.get(d + "/gettx/" + str(idd))
    return res.json()
}

def ReceivedTx(publicKey) {
    res = requests.get(d + "/receivedtx/" + publicKey)
    return res.json()
}

def SentTx(publicKey) {
    res = requests.get(d + "/senttx/" + publicKey)
    return res.json()
}

def CreateWallet() {
    res = requests.get(d + "/createwallet")
    return res.json()
}

def SendTx(privateKey,amount,receiver) {
    dicti = {
        "privateKey" : privateKey,
        "amount" : amount,
        "receiver" : receiver
    }
    res = requests.post(d + "/sendtx",json.dumps(dicti))
    return res.json()
}
