from datetime import datetime

from lib.Log import Log


class Offer:

    def __init__(self, offerResponseObject: object) -> None:
        self.id = offerResponseObject.get("offerId")
        self.expirationDate = datetime.fromtimestamp(offerResponseObject.get("expirationDate"))
        self.locationId = offerResponseObject.get('serviceAreaId')
        self.locationName = offerResponseObject.get('serviceAreaName')
        self.blockRate = float(offerResponseObject.get('rateInfo').get('priceAmount'))
        self.endTime = datetime.fromtimestamp(offerResponseObject.get('endTime'))
        self.hidden = offerResponseObject.get("hidden")
        self.ratePerHour = self.blockRate / ((self.endTime - self.expirationDate).seconds / 3600)
        self.weekday = self.expirationDate.weekday()
    
    def toString(self) -> str:
        blockDuration = (self.endTime - self.expirationDate).seconds / 3600

        body = 'Location: ' + self.locationName + '\n'
        body += 'Date: ' + str(self.expirationDate.month) + '/' + str(self.expirationDate.day) + '\n'
        body += 'Pay: $' + str(self.blockRate) + ' ($' + str(self.ratePerHour) + '/hr)\n'
        body += 'Block Duration: ' + str(blockDuration) + f' {"hour" if blockDuration == 1 else "hours"}\n'

        if not self.expirationDate.minute:
            body += f'Start time: {str(self.expirationDate.hour)}:00\n'
        elif self.expirationDate.minute < 10:
            body += f'Start time: {str(self.expirationDate.hour)}:0{str(self.expirationDate.minute)}\n'
        else:
            body += f'Start time: {str(self.expirationDate.hour)}:{str(self.expirationDate.minute)}\n'

        if not self.endTime.minute:
            body += f'End time: {str(self.endTime.hour)}:00\n'
        elif self.endTime.minute < 10:
            body += f'End time: {str(self.endTime.hour)}:0{str(self.endTime.minute)}\n'
        else:
            body += f'End time: {str(self.endTime.hour)}:{str(self.endTime.minute)}\n'

        return body
