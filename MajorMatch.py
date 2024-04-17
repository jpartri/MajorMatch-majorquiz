def take_major_match_test():
    print("Welcome to the MajorMatch Aptitude Test!")
    print("Please answer the following questions to discover your strengths and interests.\n")

    questions = [
        "How do you approach solving complex problems?",
        "How do you express your creativity?",
        "How do you analyze information to make decisions?",
        "How do you communicate your ideas to others?",
        "How do you contribute to a team environment?",
        "What type of work environment do you thrive in?",
        "How do you handle challenges and setbacks?",
        "What motivates you to excel?",
        "What are your long-term career goals?"
    ]
#some option choices would show up on the wrong question- I forgot commas, brackets, and quotations on some option choices.
    options = [
        ["Break them down into smaller components", "Look for patterns and similarities in previous solutions",
         "Collaborate with others to brainstorm solutions", "Trust your intuition and make quick decisions"],
        ["Through art, music, or writing", "Through designing and building things",
         "Through finding unique solutions to challenges", "Through exploring new ideas and concepts"],
        ["Use data and statistics to inform decisions", "Consider multiple perspectives and viewpoints",
         "Break down complex problems into smaller parts", "Trust your instincts and intuition"],
        ["Clearly and concisely, using precise language", "Through visual aids and presentations",
         "Through persuasive arguments and storytelling", "By listening actively and empathizing with others"],
        ["Take on leadership roles and delegate tasks", "Collaborate with others to achieve common goals",
         "Support and motivate team members", "Challenge ideas and push for innovation"],
        ["Structured and organized", "Dynamic and fast-paced", "Creative and open", "Supportive and collaborative"],
        ["Learn from them and adapt your approach", "Persist until you find a solution", "Seek help and advice from others",
         "Rethink your strategy and try a different approach"],
        ["Recognition and praise from others", "Opportunities for growth and advancement", "A sense of purpose and fulfillment",
         "Financial rewards and incentives"],
        ["To make a positive impact on others and society", "To continuously learn and grow professionally",
         "To achieve personal fulfillment and happiness", "To attain financial stability and success"]
    ]

    answers = []
    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question}")
        for j, option in enumerate(options[i]):
            print(f"{chr(65 + j)}. {option}")
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        answers.append(answer)

    print("\nThank you for completing the MajorMatch Aptitude Test!") #decided to add an indent using '\n function
    print("Your answers:")
    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question}")
        print(f"Your answer: {answers[i]}")

    # Recommend major based on answers
    recommend_major(answers)

#ran into  a problem here, turns out def 'recommend_major' was not indented (which makes it a separate function)
def recommend_major(answers):
    print("\nBased on your responses, we recommend considering the following majors:")

    # Analyze answers and provide recommendations
    
    if "A" in answers[0]:
        print("- Business Administration") #business administration would not print when tested, added parentheses. 
    if "B" in answers[1]:
        print("- Fine Arts or Industrial Design")
    if "C" in answers[2]:
        print("- Economics or Statistics")
    if "D" in answers[3]:
        print("- Communication or Marketing")
    if "A" in answers[4]:
        print("- Management or Entrepreneurship") # selecting 'A' would print both 'business administration' and 'management or entrepreneurship' at the same time, I did not define which question in brackets
    if "B" in answers[5]:
        print("- Civil Engineering or Architecture") 
    if "C" in answers[6]:
        print("- Psychology or Counseling")
    if "D" in answers[7]:
        print("- Sales or Human Resources")
  


# Main function
def main():
  
    print("Welcome to MajorMatch!")
    print("Discover your ideal college major with our comprehensive assessment.\n")


    take_major_match_test()



if __name__ == "__main__":
    main()
