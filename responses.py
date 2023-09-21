
def get_response(message: str) -> str:


    message = message.lower()
    
    if message =="hello":
        return "hello"
    
    if message.__contains__("dylan"):
        return "dylan roast"
    
    return "default message"