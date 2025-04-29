# Financial Chatbot

## Overview

This project is a Financial Chatbot that integrates AI and financial data analysis to provide insightful responses to financial queries. The chatbot is powered by OpenAI's GPT models and leverages data from a CSV file containing financial data for Microsoft, Apple, and Tesla for the years 2022 to 2024. 

The primary functionality of this chatbot is to provide users with financial insights such as total revenue, net income, and year-over-year changes in these financial metrics.

## Features

- Predefined financial queries (e.g., "What is the total revenue?", "How has net income changed over the last year?").
- AI-powered responses via OpenAI's GPT model for dynamic conversations.
- Data from an Excel file containing financial details about Microsoft, Apple, and Tesla.
- Simple Flask-based web application interface for easy interaction.

## Requirements

- Python 3.7 or higher
- Virtual environment (optional but recommended)

## Setup Instructions

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/financial-chatbot.git
cd financial-chatbot
```

### 2. Set up the virtual environment (optional but recommended):

- Install `virtualenv` if you don't have it installed:
  
  ```bash
  pip install virtualenv
  ```

- Create a virtual environment:

  ```bash
  python -m venv venv
  ```

- Activate the virtual environment:

  - **Windows**:
  
    ```bash
    venv\Scripts\activate
    ```

  - **MacOS/Linux**:
  
    ```bash
    source venv/bin/activate
    ```

### 3. Install dependencies:

Run the following command to install all the required Python libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Obtain an OpenAI API key:

1. Go to [OpenAI](https://beta.openai.com/signup/).
2. Sign up or log in.
3. Navigate to the [API section](https://beta.openai.com/account/api-keys).
4. Copy your API key.

### 5. Set up environment variables:

Create a `.env` file in the root of the project and add the following line, replacing `your-api-key` with the key you obtained from OpenAI:

```
OPENAI_API_KEY=your-api-key
```

### 6. Place your financial data:

Ensure that your financial data file `financial_data.csv` is in the `data/` folder. The CSV file should contain the following columns: `Company`, `Fiscal Year`, `Total Revenue (in millions)`, `Net Income (in millions)`, `Total Assets (in millions)`, `Total Liabilities (in millions)`, `Cash Flow from Operating Activities (in millions)`.

Example data for `financial_data.csv`:

```
Company,Fiscal Year,Total Revenue (in millions),Net Income (in millions),Total Assets (in millions),Total Liabilities (in millions),Cash Flow from Operating Activities (in millions)
Microsoft,2024,245.122,88.136,512.163,243.686,118.548
Microsoft,2023,211.915,72.361,411.976,205.753,87.582
Apple,2024,391.035,93.736,364.98,308.03,118.254
Apple,2023,383.285,96.995,352.583,290.437,110.543
Tesla,2024,97.69,7.153,122.07,48.39,14.923
Tesla,2023,96.773,14.974,106.618,43.009,13.256
```

### 7. Running the chatbot:

To run the chatbot locally, execute the following command:

```bash
python financial_chatbot.py
```

Alternatively, if you’ve set up a Flask web app, you can start the Flask server by running:

```bash
python app.py
```

### 8. Interacting with the chatbot:

Once the program is running, interact with the chatbot through the terminal (if using the command-line interface) or through the web interface (if using Flask). The chatbot will respond to predefined queries like:

- "What is the total revenue for Microsoft in 2024?"
- "How has net income changed for Apple in 2023?"

### Example Query:

```bash
What is the total revenue for Microsoft in 2024?
```

The chatbot will return something like:

```bash
The total revenue for Microsoft in 2024 is $245.122 million.
```

## How the Chatbot Works

1. **Data Loading:** The financial data is loaded from the CSV file into a pandas DataFrame.
2. **Data Analysis:** The chatbot processes the data to calculate year-over-year growth for each financial metric.
3. **User Input:** The user inputs a query (e.g., "What is the total revenue?") and the chatbot provides a response based on the data.
4. **OpenAI Integration:** If more advanced conversational capabilities are needed, the chatbot can use OpenAI’s GPT models for natural language understanding and dynamic responses.

## Notes

- The chatbot is currently limited to responding to predefined queries.
- For more advanced features, the chatbot can be extended to handle natural language queries using OpenAI's API or other NLP tools.
- Ensure your OpenAI API key is set correctly in the `.env` file.
## Notes on OpenAI Integration

This chatbot uses OpenAI's GPT model (gpt-3.5-turbo) to answer natural language questions that can't be answered directly from the dataset.

However, to use GPT responses:

- You must provide your own OpenAI API key in a `.env` file:


## Troubleshooting


- **API Key Issues:** If the chatbot isn't working properly with OpenAI, double-check that your API key is valid and set correctly in the `.env` file.

---

### Final Notes

This project serves as an initial step toward developing a more advanced financial chatbot using AI. You can expand it by integrating more advanced NLP capabilities, such as natural language understanding, to allow for more dynamic conversations.
