Here’s a clean, well-formatted version of your README content suitable for a Markdown file:

````markdown
# AI-Focused Newsletter Automation

This project automates the creation of an AI-focused newsletter using a team of autonomous AI agents built with the **CrewAI** framework.

---

## Overview

The system works as a hierarchical team of agents, each with a specialized role:

- **Editor**: Oversees the entire newsletter creation process, ensuring quality and coherence.
- **News Fetcher**: Scours the internet for the latest and most relevant AI news stories.
- **News Analyzer**: Analyzes each story, providing a detailed summary, key bullet points, and an explanation of why the news is important.
- **Newsletter Compiler**: Takes the analyzed stories and compiles them into a well-formatted markdown newsletter.

The process is managed by a lead agent (`manager_llm`) that delegates tasks to the specialized agents. The final output is saved as a date-stamped markdown file, ready for distribution.

---

## Key Technologies

- **[CrewAI](https://docs.crewai.com/)**: For building and managing the AI agent crew.
- **[LangChain OpenAI](https://www.langchain.com/)**: To interact with OpenAI's language models (like `gpt-4o-mini`).
- **[python-decouple](https://pypi.org/project/python-decouple/)** and **[python-dotenv](https://pypi.org/project/python-dotenv/)**: For managing API keys and environment variables.
- **Custom `SearchInternetTool`**: Uses the Serper API for real-time news searches.

---

## Workflow

1. **Fetch News**: `News Fetcher` agent collects the latest AI news from the internet.
2. **Analyze News**: `News Analyzer` agent generates summaries, bullet points, and insights.
3. **Compile Newsletter**: `Newsletter Compiler` agent formats the analyzed content into a markdown newsletter.
4. **Review & Quality Control**: `Editor` ensures consistency, clarity, and engagement.
5. **Output**: The final newsletter is saved as a date-stamped `.md` file for distribution.

---

## Setup

1. Clone the repository.
2. Create a virtual environment:
  ```bash
   python -m venv venv
   ```
   


3. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Add your API keys to a `.env` file:

   ```env
   GOOGLE_API_KEY=your_openai_api_key
   SERPER_API_KEY=your_serper_api_key
   ```
5. Run the main script:

   ```bash
   python main.py
   ```

---
