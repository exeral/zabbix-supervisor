#!/usr/bin/python3
# author: exeral@gmail.com

import json
import subprocess
import re

# Data to be written
dictionary ={
  "data": []
}
regex = r'.+no\ssuch\sfile'

supervisor_output = subprocess.check_output(['/usr/bin/supervisorctl', 'status'])
for line in supervisor_output.splitlines():
    process_state = line.decode('UTF-8')
    if not re.match(regex, process_state):
        process_details=process_state.split()
        name=process_details[0]
        status=process_details[1]
        process_dict= {
          "{#PROCESS_NAME}": name
        }
        dictionary['data'].append(process_dict)


json_object = json.dumps(dictionary, indent = 4)
# Serializing json
print(json_object)
