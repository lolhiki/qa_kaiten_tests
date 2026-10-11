def get_access_level(role: str):
    match role:
        case "admin":
            return "full"
        case "manager":
            return "edit"
        case "user":
            return "read"
        case _:
            return "none"

if __name__ == "__main__":
    tests = ["admin", "manager", "user", "guest"]
    for t in tests:
        print(t, "->", get_access_level(t))