from datetime import datetime
from lib.Log import Log
from locale import currency


class Offer:

    def __init__(self, offerResponseObject: object) -> None:
        self.id = offerResponseObject.get("offerId")
        self.serviceAreaId = offerResponseObject.get('serviceAreaId')
        self.expirationDate = datetime.fromtimestamp(offerResponseObject.get("expirationDate"))
        self.startTime = datetime.fromtimestamp(offerResponseObject.get("startTime"))
        self.endTime = datetime.fromtimestamp(offerResponseObject.get('endTime'))
        self.rateInfo = {
            'priceAmount': float(offerResponseObject.get('rateInfo').get('priceAmount')),
            'isSurge': bool(offerResponseObject.get('rateInfo').get('isSurge')),
            'surgeMultiplier': offerResponseObject.get('rateInfo').get('surgeMultiplier'),
        }   
        self.hidden = offerResponseObject.get("hidden")
        self.duration = self.endTime - self.startTime
        self.payRate = self.rateInfo['priceAmount'] / (self.duration.seconds / 3600)
        self.weekday = self.startTime.weekday()
    
    def toString(self) -> str:
        body = f'{self.serviceAreaId}\n'
        body += f'Pay: {currency(self.rateInfo["priceAmount"])} ({currency(self.payRate)}/hr)\n'
        body += f'Date: {self.startTime.strftime("%a %b %d %Y (%m/%d/%y)")}\n'
        body += f'Time: {self.startTime.strftime("%I:%M %p")} - {self.endTime.strftime("%I:%M %p")} ({str(self.duration.seconds / 3600)} {"hour" if (self.duration.seconds / 3600) == 1 else "hours"})'

        return body
