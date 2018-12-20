# format for making IBM Watson API call

from watson_machine_learning_client import WatsonMachineLearningAPIClient

wml_credentials = {
                   "url": "https://us-south.ml.cloud.ibm.com",
                   "username": "*****",
                   "password": "*****",
                   "instance_id": "*****"
                  }

client = WatsonMachineLearningAPIClient(wml_credentials)

# actual details

from watson_machine_learning_client import WatsonMachineLearningAPIClient

wml_credentials = {
				   "url": "https://jp-tok.ml.cloud.ibm.com",
				   "username": "ecf736ef-6dc5-423e-b811-7b6f4b7c81fe", 
				   "password": "b690cf53-0af7-4afa-aa02-2dff24638a55",
                   "instance_id": "326eab92-7d79-4c04-ae11-17a1caf0610b"
                   }

client = WatsonMachineLearningAPIClient(wml_credentials)