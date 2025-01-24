# Handwritten Transcription with Streamlit and Azure Cognitive Services

Welcome to the **Handwritten Transcription** repository! This project leverages the power of **Streamlit**, **Azure Cognitive Services**, and **Computer Vision** to accurately transcribe handwritten text into digital form. Designed for simplicity and efficiency, it provides a user-friendly interface to process and analyze handwritten documents. I created this project to speed up hand written data entry in a school administration working environment.

---

## 🚀 Features

- **Handwritten Text Recognition**: Upload handwritten documents, and get accurate transcription using Azure Cognitive Services' OCR capabilities.
- **Streamlit Integration**: A sleek, interactive web application for real-time transcription.
- **PDF-Only Support**: Accepts PDF files for transcription.
- **Customizable Workflows**: Flexible to integrate additional preprocessing or postprocessing steps.
- **Seamless Deployment**: Easily deployable on local machines or cloud environments.

---

## 📋 Prerequisites

1. **Azure Cognitive Services Key**:
   - Sign up for Azure Cognitive Services [here](https://azure.microsoft.com/en-us/products/cognitive-services/).
   - Create an account and obtain your API key and endpoint. Refer to the [Azure Cognitive Services documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/) for detailed guidance.

2. **Python Dependencies**:
   - Python 3.8 or above
   - Install dependencies using:
     ```bash
     pip install -r requirements.txt
     ```

3. **Streamlit**:
   - Ensure Streamlit is installed by running:
     ```bash
     pip install streamlit
     ```

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RobertRivas/handwrittenTranscription.git
   cd handwrittenTranscription
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Azure Cognitive Services credentials:
   - Create a `.env` file in the root directory and add:
     ```env
     AZURE_OCR_ENDPOINT=<your_azure_endpoint>
     AZURE_OCR_KEY=<your_azure_key>
     ```

---

## 🖥️ Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

3. Upload a PDF document, and let the app transcribe it for you!

---

## 🧩 Repository Structure

```plaintext
handwrittenTranscription/
├── app.py               # Streamlit application
├── azure_ocr.py         # Handles Azure OCR API calls
├── utils.py             # Utility functions for preprocessing
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment file
└── README.md            # Project documentation
```

---

## 🌟 Demo

Check out the live demo hosted [here](#) (add link if available).

---

## 📚 References

- [Azure Cognitive Services Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/)
- [Programming Historian Tutorials](https://programminghistorian.org/) for additional resources on digital transcription and data handling workflows.

---

## 🛡️ Security

Ensure your Azure API keys and other sensitive data are not exposed. Use `.env` files and avoid committing them to your repository.

---

## 🤝 Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/RobertRivas/handwrittenTranscription/issues).

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 📧 Contact

For any inquiries or feedback, reach out at:
- **Email**: robertrivas@example.com (replace with your contact info)
- **GitHub**: [RobertRivas](https://github.com/RobertRivas)

---

Happy transcribing! ✍️

