import json
import os

from verify import *

verified = verify(False)

if verified:
    packagedJson = json.load(open('./package.json'))
    print("Tagging %s" % (packagedJson['version']))
    os.system("git tag %s; git push --tags" % (packagedJson['version']))
else:
    print(verified)
