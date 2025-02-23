"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subjects()
    display_subjects(subjects)



def load_subjects():
    """Load data from file formatted like: code,lecturer,number_of_students."""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        subject.append(parts)
    input_file.close()
    return subject

def display_subjects(subjects):
    """Display data properly."""
    for subject in subjects:
        print("{} is taught by {:12} and has {:3} students".format(*subject))



main()