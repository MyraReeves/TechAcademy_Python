# Example from w3Schools.com

try:
    f = open("demofile.txt")
    try:
        f.write("Lorem ipsum")

    # This next block will run if there is failure to write to the file:
    except:
        print("Something went wrong when writing to the file")
    finally:
        print("Closing program...")
        f.close()

# This block will run if an error is thrown when attempting to open the file:
except:
    print("Something went wrong when opening the file")