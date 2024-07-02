while True:
    print("Next message:")
    try:
        message = input().strip()
    except (EOFError, KeyboardInterrupt):
        print("Wrapping up command line chat...")
        break
    print(message)