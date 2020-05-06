# -*- coding: utf-8 -*-
"""
@author: Felix
Example module that contains information on how to work with the JSON dataformat
"""

import json


########################### JSON EXAMPLE ######################################

#JSON String
example_string = '{"array_name":[{"key1":"value1","key1.1":"value1.1"},{"key2":"value2"},{"key_n":"value_n"}]}'

#Content of JSON String
json_example = {
	"array_name": [
		{
		          "key1": "value1",
		          "key1.1": "value1.1"
		},
		{
		          "key2": "value2"
		},
		{
		          "key_n": "value_n"
		}
	]
}


#Changing JSON-String to a Python object
array = json.loads(example_string)



###############################################################################
#################################Task##########################################
###############################################################################
'''
1. Save the material information in a JSON-String and automatically load that
information when restarting your UI
'''