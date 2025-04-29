import pandas as pd
import os
import openai
from openai import OpenAI
import re
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load your dataset
df = pd.read_csv("data/financial_data.csv")

# Make sure columns are cleaned
df.columns = df.columns.str.strip()

def extract_company_and_year(query):
    companies = df["Company"].unique()
    year_match = re.search(r"\b(2022|2023|2024)\b", query)
    company_match = next((c for c in companies if c.lower() in query.lower()), None)
    year = int(year_match.group()) if year_match else None
    return company_match, year

def get_financial_response(query):
    company, year = extract_company_and_year(query)

    if not company or not year:
        return None  # Fall back to GPT

    data_row = df[(df["Company"] == company) & (df["Fiscal Year"] == year)]

    if data_row.empty:
        return "Sorry, I couldn't find data for that company and year."

    row = data_row.iloc[0]

    if "total revenue" in query.lower():
        return f"{company}'s total revenue in {year} was {row['Total Revenue (in millions)']} million USD."
    elif "net income" in query.lower():
        return f"{company}'s net income in {year} was {row['Net Income (in millions)']} million USD."
    elif "assets" in query.lower():
        return f"{company}'s total assets in {year} were {row['Total Assets (in millions)']} million USD."
    elif "liabilities" in query.lower():
        return f"{company}'s total liabilities in {year} were {row['Total Liabilities (in millions)']} million USD."
    elif "cash flow" in query.lower():
        return f"{company}'s cash flow from operating activities in {year} was {row['Cash Flow from Operating Activities (in millions)']} million USD."
    elif "summary" in query.lower():
        return (
            f"Summary for {company} in {year}:\n"
            f"- Revenue: {row['Total Revenue (in millions)']}M\n"
            f"- Net Income: {row['Net Income (in millions)']}M\n"
            f"- Assets: {row['Total Assets (in millions)']}\n"
            f"- Liabilities: {row['Total Liabilities (in millions)']}\n"
            f"- Cash Flow: {row['Cash Flow from Operating Activities (in millions)']}M"
        )

    return None  # If no match found


def ask_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error communicating with OpenAI: {e}"

# Main chatbot loop
def run_chatbot():
    print("Welcome to the Financial Chatbot! Type 'help' to see options or 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        elif user_input.lower() == "help":
            print("Bot: You can ask things like:")
            print("- What is the total revenue for Microsoft in 2024?")
            print("- How has net income changed for Apple in 2023?")
            print("- What are the assets of Tesla in 2024?")
            print("- Give me a financial summary of Apple in 2023.")
        else:
            response = get_financial_response(user_input)
            if response:
                print(f"Bot: {response}")
            else:
                print("Bot (GPT):", ask_openai(user_input))

if __name__ == "__main__":
    run_chatbot()
