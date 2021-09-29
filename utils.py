# the sequence for exiting a program
def input_error_seq(error_message, action):
    print(error_message)
    input("Press ENTER to exit app...")
    print("\n----------------------------\n")
    action()

# todo
# convert to JSON
# save JSON to file
# check if filename exist in directory
# check if directory exist
