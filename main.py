
from fastapi import FastAPI
import random

app = FastAPI()


# we will be build two simple endpoints
# 1. /sidehustles
# 2. /moneyQuotes

side_hustles = [
"Freelance Web Development – Build websites using Django or Flask.",
"Automating Tasks – Write scripts to automate repetitive business processes.",
"Data Analysis & Visualization – Analyze data and create visualizations with Pandas and Matplotlib.",
"Stock Market Analysis – Use Python to track and analyze stock trends with yfinance.",
"API Development – Develop REST APIs with FastAPI or Flask.",
"Web Scraping – Extract and collect data from websites using BeautifulSoup or Scrapy.",
"Chatbot Development – Build AI-powered chatbots with Python and NLP libraries.",
"Cybersecurity & Ethical Hacking – Use Python for penetration testing and security analysis.",
"Selling Python Scripts – Develop and sell useful automation scripts online.",
"Teaching Python – Offer coding lessons through online platforms or courses.",
"Building SaaS Products – Create and sell cloud-based software solutions.",
"Game Development – Design and develop simple games using Pygame.",
"AI & Machine Learning Projects – Work on ML models using TensorFlow and Scikit-Learn.",
"Discord & Telegram Bots – Develop bots to automate tasks for communities.",
"Writing Technical Blogs – Share Python knowledge and monetize through blogs.",
]

money_quotes = [
"“The best way to predict the future is to create it.” – Peter Drucker",
"“Money is a terrible master but an excellent servant.” – P.T. Barnum",
"“The more you learn, the more you earn.” – Warren Buffett",
"“The only limit to our realization of tomorrow will be our doubts of today.” – Franklin D. Roosevelt",
"“The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.” – Jordan Belfort",
"“The best investment you can make is in yourself.” – Warren Buffett",
"“The only thing that overcomes hard luck is hard work.” – Harry Golden",
"“The only way to do great work is to love what you do.” – Steve Jobs",
"“The only place where success comes before work is in the dictionary.” – Vidal Sassoon",
"“The only thing that will stop you from fulfilling your dreams is you.” – Tom Bradley",
"“The only thing that will make you happy is being happy with who you are.” – Goldie Hawn",
]

@app.get("/side_hustles")
def get_side_hustles():
    """"Return a Random side hustle idea"""
    return {"side_hustles": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():
    """ Return a Random Money Quotes """
    return {"money_quotes": random.choice(money_quotes)}