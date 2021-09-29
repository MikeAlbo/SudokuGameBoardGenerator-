# the sequence for exiting a program
def input_error_seq(error_message, action):
    print(error_message)
    input("Press ENTER to exit app...")
    print("\n----------------------------\n")
    action()
