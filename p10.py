def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you?")

        elif "how are you" in user_input:
            print("Chatbot: I'm just code, but I'm doing great!")

        elif "your name" in user_input:
            print("Chatbot: I'm a simple Python chatbot.")

        elif "help" in user_input:
            print("Chatbot: You can greet me, ask my name, or say bye.")

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()