from streamlit.testing.v1 import AppTest

def test_upload_file_type():
    f = open("/Users/robertrivas/PycharmProjects/handwrittenTranscription/emiya_barbie_tis.pdf", "r")
    at = AppTest.from_file("streamlit_app.py").run()
    return
