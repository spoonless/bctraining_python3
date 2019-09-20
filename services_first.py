import hug

@hug.get("/hello")
def say_hello():
    return "hello world"

@hug.get("/who")
def say_hello_to(nom, age: hug.types.number):
    return f"Hello {nom}, tu as {age} ans"

