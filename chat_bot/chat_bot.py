##### 1st eg weather 

# def simple_chatbot(user_input):
#     # Convert user input to lowercase for case-insensitive matching
#     user_input = user_input.lower()

#     # Define rules and responses
#     greetings = ['hello', 'hi', 'hey', 'greetings']
#     farewell = ['bye', 'goodbye', 'see you']
#     inquire_weather = ['what is the weather', 'how is the weather', 'weather today']
#     inquire_name = ['what is your name', 'who are you']

#     # Check user input against predefined rules
#     if any(word in user_input for word in greetings):
#         return "Hello! How can I help you today?"

#     elif any(word in user_input for word in farewell):
#         return "Goodbye! Have a great day."

#     elif any(word in user_input for word in inquire_weather):
#         return "I'm sorry, I don't have real-time weather information."

#     elif any(word in user_input for word in inquire_name):
#         return "I am a simple chatbot. What can I do for you?"

#     else:
#         return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

# # Example usage
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         print("Chatbot: Goodbye!")
#         break
#     response = simple_chatbot(user_input)
#     print("Chatbot:", response)



#########  2nd Eg 

def ecommerce_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define rules and responses
    greetings = ['hello', 'hi', 'hey', 'greetings']
    farewell = ['bye', 'goodbye', 'see you']
    inquire_product = ['tell me about', 'information on', 'details about', 'product']
    order_status = ['where is my order', 'track my order', 'order status']
    return_policy = ['return policy', 'exchange policy', 'refund process']
    default_response = "I'm sorry, I didn't understand that. Please provide more details or ask another question."

    # Check user input against predefined rules
    if any(word in user_input for word in greetings):
        return "Hello! Welcome to our online store. How can I assist you today?"

    elif any(word in user_input for word in farewell):
        return "Thank you for visiting! If you have any more questions, feel free to ask. Goodbye!"

    elif any(word in user_input for word in inquire_product):
        return "Sure, I'd be happy to help with that. Can you please specify the product you're interested in?"

    elif any(word in user_input for word in order_status):
        return "To check your order status, please provide your order number, and I'll look it up for you."

    elif any(word in user_input for word in return_policy):
        return "Our return policy allows returns within 30 days of purchase. Please visit our website for more details."

    else:
        return default_response

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Thank you for chatting with us. Goodbye!")
        break
    response = ecommerce_chatbot(user_input)
    print("Chatbot:", response)
