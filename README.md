# Shiksha Sampadan

Shiksha Sampadan is a GenAI-powered content generator designed to create and translate educational content into 22 different Indian languages. The project simplifies learning by categorizing content into three levels, catering to users with varying degrees of understanding.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Customization](#customization)
- [Future Enhancements](#future-enhancements)

## Project Overview

Shiksha Sampadan helps generate educational content using books, PDFs, or other learning materials as its knowledge base. It incorporates multi-lingual text-to-speech functionality and translation into 22 Indian regional languages, making learning accessible and diverse.

## Features
- **Content Generation:** Create educational content based on the user's chosen topic and subtopics.
- **Multi-Lingual Support:** Translate content into 22 Indian languages.
- **Text-to-Speech:** Convert translated text into speech for a more engaging learning experience.
- **Categorized Learning Levels:** Content is categorized into three levels to match the learner's understanding:
  - **Level 1:** Layman's terms with real-life examples.
  - **Level 2:** Technical examples for intermediate learners.
  - **Level 3:** Advanced technical content.

## Prerequisites

- Python 3.9 (or above)
- Virtual Environment (optional but recommended)
- Bhashini API credentials
- Azure OpenAI credentials

## Installation
To get started with Shiksha Sampadan, follow the steps below:
1. **Clone the Repository:**
    ```bash
    git clone <repository_url>
    ```
2. **Create a Python Virtual Environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
 #### 1. LLM Configuration:
 **Update the `.env` File:**
     - Navigate to the `chatbot` directory.
     - Update the `.env` file with your Azure OpenAI credentials. Obtain these credentials from [here](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal).
  
 Example configuration for `.env`:
  ```env
  OPENAI_API_KEY=<your_azure_openai_api_key>
  OPENAI_API_TYPE=<your_azure_openai_type e.g azure>
  OPENAI_API_VERSION=<your_azure_openai_version>
  OPENAI_ENDPOINT=<your_azure_openai_endpoint>
  
  ```
    
 #### 2. Bhashini Configuration:
 **Update the `config.py` File:**
     - Navigate to the `bhashini_utils` directory.
     - Update the `config.py` file with your Bhashini api credentials. Obtain these credentials from [here](https://bhashini.gov.in/ulca/user/register)
     
 Example configuration for `config.py`:
  ```env
  API_ENDPOINT=<your_bhashini_api_endpoint>
  TTS_SERVICE_ID_EN=<text-to-speech_english_service_id>
  TRANSLATION_SERVICE_ID_EN_HI=<translation_english_hindi_service_id>
  
  ```    
  **Note:** The project currently supports English, Hindi, Bangla, and Kannada. You can add more languages by referring the Bhashini documentation from [here](https://bhashini.gitbook.io/bhashini-apis)


## Running the Application
**After completing the configuration, start the Streamlit application:**
```bash
streamlit run app.py
```
The Streamlit app will be accessible in your web browser, where you can select topics and languages for content generation.

**Here is a demonstration video of Shiksha Sampadan in action:**

[](https://github.com/user-attachments/assets/586d8c94-0309-48e4-98d7-d1bc23cd2afc)

## Customization
1. **Learning Levels:**
To customize the learning levels *(Level 1, Level 2, Level 3)*, navigate to `prompt.py` in the `chatbot/chatbot_utils` directory.
Modify the prompts according to your needs.

2. **UI Customization:**
UI customization options are available in the `config.toml` file located in the `.streamlit` directory.
Modify the appearance and settings of the Streamlit app as needed.

## Future Enhancements
1. **Integration with Learning Platforms:** Incorporate Shiksha Sampadan with existing learning platforms for a seamless user experience.
2. **Enhanced Multi-Lingual Support:** Extend support to additional Indian languages and dialects.
3. **AI-Powered Feedback:** Implement AI to provide personalized feedback to learners.


  



