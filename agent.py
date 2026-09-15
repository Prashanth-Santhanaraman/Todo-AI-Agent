import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from todo_manager import (
    add_task,
    complete_task,
    get_status
)


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )


client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash"


# -----------------------------
# Tool definitions
# -----------------------------

tools = types.Tool(
    function_declarations=[

        types.FunctionDeclaration(
            name="add_task",

            description=(
                "Add a new task to the user's todo list."
            ),

            parameters=types.Schema(
                type="OBJECT",

                properties={
                    "task": types.Schema(
                        type="STRING",
                        description="The task to add."
                    )
                },

                required=["task"]
            )
        ),

        types.FunctionDeclaration(
            name="complete_task",

            description=(
                "Mark an existing pending task as completed. "
                "The task name must match an existing pending task."
            ),

            parameters=types.Schema(
                type="OBJECT",

                properties={
                    "task_name": types.Schema(
                        type="STRING",
                        description=(
                            "The exact name of the task to mark "
                            "as completed."
                        )
                    )
                },

                required=["task_name"]
            )
        ),

        types.FunctionDeclaration(
            name="get_status",

            description=(
                "Get the user's todo status, including total, "
                "completed and pending tasks."
            ),

            parameters=types.Schema(
                type="OBJECT",

                properties={}
            )
        )
    ]
)


# -----------------------------
# Agent configuration
# -----------------------------

config = types.GenerateContentConfig(

    tools=[tools],

    system_instruction="""
You are a Todo AI Agent.

Your job is to manage the user's todo list.

You have access to three tools:

1. add_task
   Use this when the user wants to add a task.

2. complete_task
   Use this when the user says they finished a task.

3. get_status
   Use this when the user asks about their todo list,
   pending work, completed work, or progress.

IMPORTANT:

When the user says they completed a task, identify the
task name from their message and call complete_task.

If the user asks about their progress, use get_status.

Never invent tasks or completion information.

When showing status, include:

Total tasks
Completed count
Completed tasks
Pending count
Pending tasks

Keep responses concise and friendly.
"""
)


# -----------------------------
# Run agent
# -----------------------------

def run_agent(user_message):

    response = client.models.generate_content(
        model=MODEL,
        contents=user_message,
        config=config
    )

    # No tool required
    if not response.function_calls:
        return response.text

    tool_results = []

    for function_call in response.function_calls:

        name = function_call.name
        args = function_call.args

        # -------------------------
        # Add task
        # -------------------------

        if name == "add_task":

            result = add_task(
                args["task"]
            )

        # -------------------------
        # Complete task
        # -------------------------

        elif name == "complete_task":

            result = complete_task(
                args["task_name"]
            )

        # -------------------------
        # Get status
        # -------------------------

        elif name == "get_status":

            result = get_status()

        else:

            result = "Unknown tool."

        tool_results.append(

            types.Part.from_function_response(
                name=name,

                response={
                    "result": result
                }
            )
        )

    # Send tool result back to Gemini
    final_response = client.models.generate_content(

        model=MODEL,

        contents=[
            user_message,
            response.candidates[0].content,
            *tool_results
        ],

        config=config
    )

    return final_response.text