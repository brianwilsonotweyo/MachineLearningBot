def response(input_message):
    message = input_message.lower()

    if message == 'nice':
        return "very nice"
    elif message == 'hello':
        return "Hello there"
    else:
        return "cool!"