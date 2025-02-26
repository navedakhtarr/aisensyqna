# Web Content Q&A Tool

This project is a web-based application that allows users to input URLs, extract textual content from those web pages, and pose questions related to the extracted content. The application processes the content and provides answers to the user's questions.

## Features

- **Content Extraction**: Fetches and extracts text from user-provided URLs.
- **Question Answering**: Utilizes Natural Language Processing (NLP) techniques to answer questions based on the extracted content.
- **Web Interface**: Provides an interactive web interface using Streamlit for user interaction.


## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/navedakhtarr/aisensyqna.git
cd aisensyqna
```


#### Using VS Code 


#### Manual Setup


1. **Activate the Virtual Environment**:

   - On Windows:

     ```bash
     qna_env\Scripts\activate.bat
     ```

   - On macOS/Linux:

     ```bash
     source qna_env/bin/activate
     ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   ```bash
   streamlit run app.py
   ```

   This will start the Streamlit server, and you can access the application in your web browser at `http://localhost:8501`.

## Project Structure

- `app.py`: The main application script that sets up the Streamlit web interface.
- `scraper.py`: Contains the `extract_text_from_url` function to fetch and extract text from web pages.
- `qa.py`: Defines the `QASystem` class that processes the extracted text and answers user questions using NLP techniques.
- `requirements.txt`: Lists all the Python dependencies required for the project.

## Usage

1. **Ingest Content**:
   - Enter one or more URLs (each on a new line) into the "Enter URLs" text area.
   - Click the "Ingest Content" button to fetch and process the content from the provided URLs.

2. **Ask Questions**:
   - After successfully ingesting content, enter your question into the "Ask a question" input field.
   - Click the "Get Answer" button to receive an answer based on the ingested content.

## Notes

- Ensure that the URLs provided are accessible and contain textual content for accurate extraction and processing.
- The application relies on the BeautifulSoup library for web scraping and NLTK along with scikit-learn for NLP tasks.

