# A "try" block lets you test a block of code for errors.  The "except" block lets you handle any errors.



# An "else" block lets you execute code when no error occurs

# Example in which no error will occur:
try: print("Hello there!")
except: print("Something went wrong causing you to lose this light saber battle")
else: print("I am Obi-wan Kenobi and I have the high ground!")




print("-------------------------")




# A "finally" block lets you execute code, regardless of success/failure results of a try/except block.

# Example from w3Schools.com:
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

# This block will run if an error is thrown when attempting to open the file, which is what will happen since there is no "demofile.txt" file here:
except:
    print("Something went wrong when opening the file")