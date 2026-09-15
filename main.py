from agent import run_agent


def main():

    print("=" * 50)
    print("           TODO AI AGENT")
    print("=" * 50)

    print("Type 'exit' to quit.")
    print()

    while True:

        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit"]:

            print("Agent: Goodbye! 👋")
            break

        try:

            response = run_agent(user_input)

            print()
            print("Agent:", response)
            print()

        except Exception as e:

            print()
            print("Agent: Something went wrong.")
            print("Error:", e)
            print()


if __name__ == "__main__":
    main()