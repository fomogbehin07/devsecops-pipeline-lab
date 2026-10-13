def greet(name):
    if not name:
        raise ValueError("Name is required")
    return f"Hi, {name}!"

if __name__ == "__main__":
    print(greet("DevSecOps"))
