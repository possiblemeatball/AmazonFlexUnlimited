from datetime import datetime
from lib.Log import Log
import json
from locale import currency
from lib.FlexUnlimited import FlexUnlimited


class Offer:

    def __init__(self, flex_unlimited: FlexUnlimited, offerResponseObject: object) -> None:
        self.id = offerResponseObject.get("offerId")
        self.serviceAreaId = offerResponseObject.get('serviceAreaId')
        self.serviceAreaName = flex_unlimited.service_areas_map[self.serviceAreaId]
        self.hidden = offerResponseObject.get("hidden")
        self.expirationDate = datetime.fromtimestamp(offerResponseObject.get("expirationDate"))
        self.startTime = datetime.fromtimestamp(offerResponseObject.get("startTime"))
        self.endTime = datetime.fromtimestamp(offerResponseObject.get('endTime'))
        self.weekday = self.startTime.weekday()
        self.duration = self.endTime - self.startTime
        self.rateInfo = {
            'priceAmount': float(offerResponseObject.get('rateInfo').get('priceAmount')),
            'isSurge': bool(offerResponseObject.get('rateInfo').get('isSurge')),
            'surgeMultiplier': offerResponseObject.get('rateInfo').get('surgeMultiplier'),
        }   
        self.payRate = self.rateInfo['priceAmount'] / (self.duration.seconds / 3600)

    def __str__(self) -> str:
        dict_copy = self.__dict__.copy()
        dict_copy.pop('id')
        dict_copy.pop('serviceAreaId')
        return f"Offer{json.dumps(dict_copy, default=str)}"
    
    def strPretty(self) -> str:
        body = f'{self.serviceAreaName}\n'
        body += f'Pay: {currency(self.rateInfo["priceAmount"])} ({currency(self.payRate)}/hr) ({self.rateInfo["surgeMultiplier"] if self.rateInfo["surgeMultiplier"] is not None else "NO"} SURGE)\n'
        body += f'Date: {self.startTime.strftime("%a %b %d %Y (%m/%d/%y)")}\n'
        body += f'Time: {self.startTime.strftime("%I:%M %p")} - {self.endTime.strftime("%I:%M %p")} ({str(self.duration.seconds / 3600)} {"hour" if (self.duration.seconds / 3600) == 1 else "hours"})'

        return body
