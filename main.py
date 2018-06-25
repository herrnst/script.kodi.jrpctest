# executeJSONRPC debug addon

import json
import xbmc

def log(str):
    xbmc.log("[script.kodi.jrpctest] %s" % (str), level=xbmc.LOGDEBUG)

def jrpcget(method, params):
    jsondata = {
        "jsonrpc": "2.0",
        "method": method,
        "id": method}

    if params:
        jsondata["params"] = params

    try:
        rpccmd = json.dumps(jsondata)
        log("JSONRPC enter: " + rpccmd)

        rpcreply = xbmc.executeJSONRPC(rpccmd)

        log("JSONRPC return: " + rpcreply)

        rpcdata = json.loads(rpcreply)

        if rpcdata["id"] == method and rpcdata.has_key("result"):
            return rpcdata["result"]
    except Exception as e:
        log("Caught JSONRPC exception: %s" % (str(e)))

    return False


def pymain():
    labels = [
        "MusicPlayer.Channels",
        "Player.Duration",
        "Player.Time",
        "System.CurrentWindow",
        "System.CurrentControl",
        "System.ScreenHeight",
        "System.Time(hh:mm:ss)",
        "VideoPlayer.AudioChannels",
    ]

    mon = xbmc.Monitor()

    log("Addon start")
    while not mon.waitForAbort(0.1):
        jrpcget("XBMC.GetInfoLabels", {"labels": labels})

    log("Addon end")

if __name__ == "__main__":
    pymain()
