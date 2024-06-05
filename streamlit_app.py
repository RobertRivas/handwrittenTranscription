from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


import streamlit as st
from PIL import Image
import pandas as pd

import utils.ocr.ocr as tr

# import utils.llm.llm as lm
def ocr_transcription(file):
    # Authenticate with Azure Cognitive Services.
    computervision_client = ComputerVisionClient(st.secrets["endpoint"], CognitiveServicesCredentials(st.secrets["key"]))

    read_image = file
    print(type(read_image))

    # Call API with URL and raw response (allows you to get the operation location). Call Azure using computervision_client with the URL.
    read_response = computervision_client.read_in_stream(read_image, pages=['1,2,3,4,5,6,7,8'], raw=True)

    # # <snippet_read_response>
    # # Get the operation location (URL with an ID at the end) from the response
    read_operation_location = read_response.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = read_operation_location.split("/")[-1]

    # Call the "GET" API and wait for it to retrieve the results
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
            time.sleep(1)

    # Print the detected text, line by line
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                print(line.text)
                st.write(line.text)
                print(line.bounding_box)
    print()

    print(computervision_client)
    print(read_image)

    return read_result



st.write('Upload a pdf handwritten or text.')

# lm.llm_function()

file_upload = st.file_uploader('Choose your file', type="pdf")

# if file_upload is not None:
#     print(file_upload)

img_data = file_upload
    


ocr_transcription(img_data)
    


# st.write(file_upload)







