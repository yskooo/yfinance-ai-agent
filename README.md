# Create an AI Finance Agent Using Python  

Unlock the power of AI to streamline financial insights and web searches! This guide shows you how to create an AI Finance Agent in Python using **Groq** and **Phidata**. With this setup, you can retrieve detailed financial data, perform web searches, and combine agents for more robust applications.  

---

## 🚀 Features  

### 🌟 Finance Agent  
- Fetch real-time stock prices.  
- Access stock fundamentals and analyst recommendations.  
- Retrieve company news and comprehensive information.  
- Organize data into clean, easy-to-read tables.  

### 🌟 Web Search Agent  
- Search the web for relevant information.  
- Provide summarized results with proper source citations.  

### 🌟 Multi-Agent System  
- Combine multiple agents for versatile and enhanced functionalities.  

### 🌟 Advanced AI Models  
- Leverage Groq's powerful models like `llama3-groq-70b` for sophisticated tasks.  

### 🌟 Phidata Framework  
- Utilize Phidata for building and orchestrating multi-modal agents and workflows.  

---

## 🛠 Prerequisites  

- Python 3.8 or above.  
- API keys for **PHI_API_KEY** and **GROQ_API_KEY**.  

---

## 📥 Installation  

1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/ai-finance-agent.git  
   cd ai-finance-agent  
   ```  

2. Create a virtual environment:  
   ```bash
   python -m venv env  
   source env/bin/activate  # For Linux/MacOS  
   env\Scripts\activate     # For Windows  
   ```  

3. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt  
   ```  

4. Set up environment variables:  
   Create a `.env` file in the root directory and include your API keys:  
   ```env  
   PHI_API_KEY=<your_phi_api_key>  
   GROQ_API_KEY=<your_groq_api_key>  
   ```  

---

## 🏃‍♂️ Run the Application  

Run the script using the following command:  
```bash  
python finance-agent.py  
```  

---

## 📋 Requirements  

Ensure your `requirements.txt` contains the following packages:  
```txt  
openai  
phidata  
python-dotenv  
yfinance  
packaging  
duckduckgo-search  
fastapi  
uvicorn  
groq  
```  

---

## 🌐 Usage  

- Use the **Finance Agent** to gather financial insights like stock prices and news.  
- Use the **Web Search Agent** to search the web and retrieve results with references.  
- Combine agents with **Groq** models for a more powerful multi-agent system.  

---

## 📚 Example Output  

1. **Finance Agent**:  
   - Displays stock prices and fundamentals in table format.  
   - Retrieves news articles with clear sources.  

2. **Web Search Agent**:  
   - Searches for specific queries and returns concise summaries with links.  

3. **Multi-Agent System**:  
   - Handles complex queries like “Summarize analyst recommendations and share the latest news for Meta.”  

---

## 🌟 Contributing  

We welcome contributions! Feel free to fork this repository, create a branch, and submit a pull request for improvements or new features.  

---

## 💡 Tips  

- Replace `<your_phi_api_key>` and `<your_groq_api_key>` with your actual API keys in the `.env` file.  
- Ensure a stable internet connection for fetching financial data and performing web searches.  

---
