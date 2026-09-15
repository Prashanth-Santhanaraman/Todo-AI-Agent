# Todo AI Agent

A lightweight AI-powered Todo Agent built with **Python and Google Gemini** that allows users to manage their tasks using natural language.

Instead of using traditional commands, you can simply tell the agent what you want to do. The agent decides which tool to use and updates a local `todos.txt` file.

## Features

*  Add new tasks using natural language
*  Mark tasks as completed
*  View pending and completed tasks
*  Get a summary of task progress
*  Store tasks locally in a TXT file
*  Gemini-powered tool calling
*  Natural-language interaction through the command line

## Architecture

```text
                    User
                     │
                     ▼
              ┌─────────────┐
              │  Gemini AI  │
              │    Agent    │
              └──────┬──────┘
                     │
              Decides which
                 tool to use
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      Add Task   Complete Task  Get Status
          │          │          │
          └──────────┼──────────┘
                     ▼
                todos.txt
```

## Tech Stack

* **Python**
* **Google Gemini API**
* **Google GenAI SDK**
* **python-dotenv**
* **Local TXT file storage**

## Project Structure

```text
todo-ai-agent/
│
├── main.py              # Command-line interface
├── agent.py             # Gemini agent and tool calling
├── todo_manager.py      # Todo file management
├── todos.txt            # Local task storage
├── requirements.txt     # Python dependencies
├── .env                 # Gemini API key
└── .gitignore           # Ignored files
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/todo-ai-agent.git
cd todo-ai-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Do not commit the `.env` file to GitHub.

### 4. Run the agent

```bash
python main.py
```

##  Example Usage

### Add a task

```text
You: Add learn LangGraph

Agent: Task added: "learn LangGraph"
```

<img width="997" height="232" alt="image" src="https://github.com/user-attachments/assets/a145a83b-561c-4efd-88bf-ab578c25e9d0" />


### Complete a task

```text
You: I finished learning LangGraph

Agent: Task completed: "learn LangGraph"
```

<img width="797" height="121" alt="image" src="https://github.com/user-attachments/assets/6f4c531c-fac2-4141-975e-89a8773c2e22" />


### Check remaining work

```text
You: How much work is remaining?

Agent:

You have 2 pending tasks:

1. Complete my portfolio
2. Prepare for interview

Completed: 1

1. Learn LangGraph

Total: 3
```

<img width="1125" height="100" alt="image" src="https://github.com/user-attachments/assets/844146b9-6985-4a23-944b-a46b5b5e9c8d" />


##  How the Agent Works

The project uses **Gemini function/tool calling**.

The agent has three main tools:

### `add_task()`

Adds a new task to the local todo file.

### `complete_task()`

Marks an existing task as completed.

### `get_status()`

Retrieves the current task information, including:

* Total tasks
* Completed tasks
* Pending tasks

Gemini analyzes the user's natural-language request and decides which tool should be executed.

For example:

```text
"I finished my Python project"
              │
              ▼
          Gemini Agent
              │
              ▼
      Identify the task
              │
              ▼
      complete_task()
              │
              ▼
         todos.txt
```

## Data Format

Tasks are stored locally in `todos.txt`.

Example:

```text
[✓] Learn Python
[ ] Complete portfolio
[ ] Prepare for interview
```

`[✓]` represents a completed task.

`[ ]` represents a pending task.

Output:

<img width="426" height="61" alt="image" src="https://github.com/user-attachments/assets/721d4f3b-6c04-46d8-a904-0cee14b45278" />


## Purpose

This project was built as a small practical implementation of an **AI Agent** to understand:

* LLM-based decision making
* Function/tool calling
* Agent-tool interaction
* Natural-language task management
* Local data persistence

