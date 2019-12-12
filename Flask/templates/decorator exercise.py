

def restrict_access(func):
    def wrapper(*args, **kwargs):
        name = args[0]
        if name.startswith("T"):
            result = "Access Denied"
        else:
            result = func(*args, **kwargs)
        return result
    return wrapper #ohne Klammern - wir geben die Funktion zurück und nicht den Funktionswert

@restrict_access
def treasurebox(username):
    return f"Granted Access to {username}"

@restrict_access
def bank_safe(username):
    return f"GrantedAccess to rich bank safe to {username}"

if __name__ == '__main__':
    print(treasurebox("Anna"))
    print(bank_safe("Tamara"))
