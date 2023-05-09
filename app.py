import sys
from prettytable import PrettyTable
from lib.FlexUnlimited import FlexUnlimited

if __name__ == "__main__":
  print("Amazon Flex Unlimited\n")
  
  flexUnlimited = FlexUnlimited()
  if (len(sys.argv) > 1):
    arg1 = sys.argv[1]
    if (arg1 == "getAllServiceAreas" or arg1 == "--w"):
      print("\n Your service area options:")
      serviceAreasTable = PrettyTable()
      serviceAreasTable.field_names = ["Service Area ID", "Service Area Name"]
      for service_area_key in flexUnlimited.service_areas_map.keys() :
        serviceAreasTable.add_row(service_area_key, flexUnlimited.service_areas_map[service_area_key])
      print(serviceAreasTable)
    else:
      print("Invalid argument provided.")
  else:
    flexUnlimited.run()