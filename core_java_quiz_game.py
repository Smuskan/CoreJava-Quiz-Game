import os

# ==============================
#   Author: Muskan Shaikh :)
#   Welcome to the Quiz Game    
# ==============================

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome_message():
    """Displays a welcome message."""
    print('==============================')
    print('   Welcome to the Quiz Game    ')
    print('==============================')


def choose_level():
    """Asks the player to choose a difficulty level."""
    print("Please choose your level:")
    print("1. Easy")
    print("2. Intermediate")
    print("3. Hard")

    while True:
        level = input("Enter the number of your choice (1-3): ")
        if level in ['1', '2', '3']:
            return level
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def ask_questions(level):
    """Asks questions based on the chosen difficulty level."""
    questions = {
        '1': [
            (
                "Question 1: What is the keyword used to define a class in Java?\n(a) class\n(b) def\n(c) function\n(d) method",
                "a"),
            (
                "Question 2: Which of the following is a valid declaration of a boolean variable?\n(a) boolean b = 1\n(b) boolean b = true\n(c) boolean b = 'true'\n(d) boolean b = 0",
                "b"),
            (
                "Question 3: What is the default value of a boolean variable in Java?\n(a) true\n(b) false\n(c) 0\n(d) null",
                "b"),
            (
                "Question 4: Which of the following is a valid comment in Java?\n(a) // This is a comment\n(b) /* This is a comment */\n(c) Both a and b\n(d) None of the above",
                "c"),
            (
                "Question 5: In Java, which operator is used to assign a value to a variable?\n(a) ==\n(b) =\n(c) ===\n(d) !=",
                "b"),
            (
                "Question 6: What is the size of an int variable in Java?\n(a) 16 bit\n(b) 32 bit\n(c) 64 bit\n(d) 8 bit",
                "b"),
            (
                "Question 7: Which method is used to start a thread in Java?\n(a) start()\n(b) run()\n(c) init()\n(d) execute()",
                "a"),
            (
                "Question 8: Which keyword is used to inherit a class in Java?\n(a) implements\n(b) extends\n(c) inherits\n(d) uses",
                "b"),
            (
                "Question 9: Which of these is not a Java keyword?\n(a) class\n(b) interface\n(c) string\n(d) public", "c"),
            (
                "Question 10: What is the correct way to create an array in Java?\n(a) int[] arr = new int[5];\n(b) int arr[] = new int[5];\n(c) Both a and b\n(d) None of the above",
                "c")
        ],
        '2': [
            (
                "Question 1: What is the output of the following code? System.out.println(1 + 2 + '3');\n(a) 33\n(b) 6\n(c) 123\n(d) 15",
                "a"),
            (
                "Question 2: Which of the following is true about constructors in Java?\n(a) They can return values\n(b) They can be overloaded\n(c) They cannot have parameters\n(d) They are called automatically when a class is instantiated",
                "b"),
            ("Question 3: What is the superclass of all classes in Java?\n(a) Object\n(b) Class\n(c) Super\n(d) Base",
             "a"),
            (
                "Question 4: Which of the following is not an access modifier?\n(a) public\n(b) private\n(c) protected\n(d) static",
                "d"),
            ("Question 5: What is the result of the expression 10 + 20 + '30'?\n(a) 102030\n(b) 60\n(c) 1030\n(d) 30",
             "c"),
            (
                "Question 6: Which of the following is a valid way to declare a multi-dimensional array?\n(a) int arr[][];\n(b) int[] arr[];\n(c) Both a and b\n(d) None of the above",
                "c"),
            (
                "Question 7: Which of the following methods can be used to find the length of an array?\n(a) length()\n(b) size()\n(c) length\n(d) getSize()",
                "c"),
            (
                "Question 8: What does the 'final' keyword signify in Java?\n(a) It can be overridden\n(b) It cannot be inherited\n(c) It cannot be changed\n(d) None of the above",
                "c"),
            (
                "Question 9: Which of these statements is true?\n(a) A constructor can be private\n(b) A class can have multiple constructors with the same name\n(c) Both a and b\n(d) None of the above",
                "c"),
            (
                "Question 10: What is the purpose of the 'this' keyword in Java?\n(a) Refers to the current object\n(b) Refers to the superclass\n(c) Refers to the parent class\n(d) Refers to the calling class",
                "a")
        ],
        '3': [
            (
                "Question 1: Which of the following statements is true?\n(a) In Java, a class can inherit from multiple classes\n(b) In Java, a class can implement multiple interfaces\n(c) Both a and b\n(d) None of the above",
                "b"),
            (
                "Question 2: What is the output of the following code? System.out.println(2 == 2 ? 'Yes' : 'No');\n(a) Yes\n(b) No\n(c) 2\n(d) Error",
                "a"),
            (
                "Question 3: Which of the following is a feature of OOP?\n(a) Encapsulation\n(b) Inheritance\n(c) Polymorphism\n(d) All of the above",
                "d"),
            (
                "Question 4: Which of the following is true about the String class?\n(a) Strings are mutable\n(b) Strings are immutable\n(c) String class does not provide any methods\n(d) None of the above",
                "b"),
            (
                "Question 5: What is the difference between == and equals() in Java?\n(a) == checks for reference equality, equals() checks for value equality\n(b) Both check for the same equality\n(c) equals() checks for reference equality, == checks for value equality\n(d) None of the above",
                "a"),
            (
                "Question 6: Which exception is thrown when a program attempts to divide by zero?\n(a) NullPointerException\n(b) ArithmeticException\n(c) ArrayIndexOutOfBoundsException\n(d) ClassCastException",
                "b"),
            ("Question 7: What is the result of the following expression?\n(a) 1\n(b) 0\n(c) Exception\n(d) 2", "b"),
            (
                "Question 8: Which of the following is true about the 'super' keyword?\n(a) It is used to call the constructor of the parent class\n(b) It cannot be used in static methods\n(c) Both a and b\n(d) None of the above",
                "c"),
            (
                "Question 9: Which of the following statements is true about interfaces?\n(a) An interface can have method bodies\n(b) An interface can extend multiple interfaces\n(c) An interface can implement other interfaces\n(d) None of the above",
                "b"),
            (
                "Question 10: What does the keyword 'volatile' indicate in Java?\n(a) A variable can be accessed by multiple threads\n(b) A variable is subject to change\n(c) Both a and b\n(d) None of the above",
                "c")
        ]
    }

    score = 0
    total_questions = 10

    for index, (question, correct_answer) in enumerate(questions[level], 1):
        print(f"\n{question}")
        print(f"Your answer (a/b/c/d): ", end='')
        answer = input().lower()
        if answer == correct_answer:
            score += 1
            print('Correct!')
        else:
            print('Wrong Answer :(')

    return score, total_questions


def calculate_grade(score, total_questions):
    """Calculates the grade based on the score."""
    percentage = (score / total_questions) * 100
    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'D'


def main():
    clear_screen()
    welcome_message()
    answer = input('Are you ready to play the Quiz? (yes/no): ').lower()

    if answer == 'yes':
        level = choose_level()
        if level == '1':
            print("\nYou are at Easy level.")
        elif level == '2':
            print("\nYou are at Intermediate level.")
        else:
            print("\nYou are at Hard level.")

        score, total_questions = ask_questions(level)
        grade = calculate_grade(score, total_questions)

        print(f"\nYour Score: {score}/{total_questions}")
        print(f"Your Grade: {grade}")
        print('Thank you for playing!')

    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
