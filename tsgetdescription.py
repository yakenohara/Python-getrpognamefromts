import sys
import json

from TSInfoExtractor import TSInformation

tsobj = TSInformation(sys.argv[1])

# for str_key, key in tsobj.extract().items():
#     print(json.dumps(tsobj.extract().items(), indent=4))

obj = tsobj.extract()

print(obj['program']['description'])
