
msg = """Hello World
herinein
hierbe"""

print(len(msg))
print(msg[6])
print(msg[0:6])
print(msg[6:])
print(msg.lower())
print(msg.upper())
print(msg.count("Hello"))
print(msg.count("l"))
print(msg.find("World"))
new_msg = msg.replace("World", "Universe")
print(new_msg)
greeting = "Hello"
name = "Michael"
message = f"{greeting}, {name}. Welcome!"
print(message)