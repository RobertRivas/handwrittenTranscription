import streamlit as st
from PIL import Image
import pandas as pd

import utils.ocr.ocr as tr

# import utils.llm.llm as lm

st.write('Upload a pdf handwritten or text.')

# lm.llm_function()

file_upload = st.file_uploader('Choose your file', type="pdf")

# if file_upload is not None:
#     print(file_upload)

img_data = file_upload
    


print(tr.ocr_transcription(img_data))
    


# st.write(file_upload)







