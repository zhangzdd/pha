import json
class setting:
    def __init__(self,searchChannel = 500,channel=500,countTime = 20,eRange = [0,1024],countRange = 10,
                 measureRange = 25,
                 csvDir = "./spectrum",
                 htmlDir = "./html"):
        self.searchChannel = searchChannel
        self.channel = channel
        self.eRange = eRange
        self.countTime = countTime
        self.countRange = countRange
        self.measureRange = measureRange
        self.csvDir = csvDir
        self.htmlDir = htmlDir
        self.default_setting_dir = "settings.json"

    def dumpSetting(self):
        j_dict = {
                  "channel":self.channel,
                  "eRange":self.eRange,
                  "countTime":self.countTime,
                  "countRange":self.countRange,
                  "csvDir":self.csvDir,
                  "htmlDir":self.htmlDir,
                  }
        with open(self.default_setting_dir, 'w') as file:
            json.dump(j_dict, file)
    def importSetting(self):
        with open(self.default_setting_dir, 'r') as file:
            j_dict = json.load(file)
        self.eRange = j_dict["eRange"]
        self.countTime = j_dict["countTime"]
        self.countRange = j_dict["countRange"]
        self.csvDir = j_dict["csvDir"]
        self.htmlDir = j_dict["htmlDir"]
        self.channel = j_dict["channel"]

if __name__ == "__main__":
    set = setting()
    set.dumpSetting()