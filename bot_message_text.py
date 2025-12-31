
# Write a function is_greeting(message) that returns True if the message text contains a greeting
# (e.g., "hi", "hello", "hey" — case-insensitive), and False otherwise.
# Write Pytest tests for at least 5 different inputs.
# Make sure it works with mixed-case input (e.g., "HeLLo").

GREETING = ["hi", "hello", "hey"]
def is_greeting(message: str):
    message = message.lower().split()
    if any(word in message for word in GREETING):
        return True
    else:
        return False

def test_message(greetings_check):
    assert is_greeting(greetings_check["normal"]) == True
    assert is_greeting(greetings_check["caps"]) == True
    assert is_greeting(greetings_check["incorrect"]) == False
    assert is_greeting(greetings_check["correct"]) == True
    assert is_greeting(greetings_check["caps_1"]) == True