from app.commands import handle_command

def main():
    print("Todo CLI started. Type 'help' for commands.")
    while True:
        cmd = input("> ").strip()
        if cmd in ["exit", "quit"]:
            break
        handle_command(cmd)

if __name__ == "__main__":
    main()
