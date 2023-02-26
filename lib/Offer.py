from datetime import datetime
from lib.Log import Log
from locale import currency


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

        body = f'{self.locationName} ({self.locationId})\n'
        body += f'Pay: {currency(self.blockRate)} ({currency(self.ratePerHour)}/hr)\n'
        body += f'Date: {self.expirationDate.strftime("%a %b %d %Y (%m/%d/%y)")}\n'
        body += f'Time: {self.expirationDate.strftime("%I:%M %p")} - {self.endTime.strftime("%I:%M %p")} ({str(blockDuration)} {"hour" if blockDuration == 1 else "hours"})'

        return body
