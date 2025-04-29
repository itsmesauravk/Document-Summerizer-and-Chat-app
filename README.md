# ChatWRP - Chat with Research Papers

ChatWRP is a tool that allows users to upload research papers and chat with them. The tool extracts content from PDF research papers, generates a summary, and allows users to ask questions about the paper's content.

## Features

- Upload PDF research papers
- Generate paper summaries
- Chat with papers using natural language
- Get accurate responses based on the paper's content

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/itsmesauravk/Document-Summerizer-and-Chat-app.git
   cd Document-Summerizer-and-Chat-app
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage

Run the application:

```
streamlit run app.py
```

Then follow the UI instructions to upload a paper and chat with it.

## Project Structure

- `app.py`: Main Streamlit application
- `src/`: Source code for the application
- `uploads/`: Uploaded papers are stored here
- `utils/`: Utility functions

## License

MIT
