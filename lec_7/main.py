while True:
    try:
        input_filename = input("name file ")

        try:
            with open(input_filename, 'r') as input_file:
                file_content = input_file.read()
                print(" content:")
                print(file_content)
        except FileNotFoundError:
            print(f"File '{input_filename}' not found.")
            continue

        user_choice = input(" write to the same file (Enter 's') or a new file (Enter 'n')? ").lower()

        if user_choice == 's':
            try:
                with open(input_filename, 'a') as input_file:
                    new_content = input("Enter the content  ")
                    input_file.write(new_content)
                    print("Content has been  added ")
            except Exception as e:
                print(f"{str(e)}")
        elif user_choice == 'n':
            new_filename = input(" name of the new file: ")
            try:
                with open(new_filename, 'w') as new_file:
                    new_content = input(" new content : ")
                    new_file.write(new_content)
                    print("content added")
            except FileNotFoundError:
                print(f"Error: File '{new_filename}' not found.")
            except Exception as e:
                print(f"{str(e)}")
        else:
            print(" enter 's' or 'n.")

    except ValueError:
        print(" enter a valid filename.")
    except Exception as e:
        print(f": {str(e)}")

    finally:
        print("closed")

    user_input = input("continue (y/n)? ")
    if user_input.lower() != 'y':
        break
