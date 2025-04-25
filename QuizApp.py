#Quiz Introduction
def display_introduction():
    print("Welcome to my quiz!\n all answers have to be typed in lowercase")
    name = input("\n Enter your name then press enter to begin\n")
    print(f"Hello {name}\nlet's begin: \n")
    return name

#Questions
q_num = 0
QUESTIONS = [
    (f" What is 5+5", "10","Other numbers that add to 10 in 1 step include 1+9, 2+8, 3+7 and 6+4"),
    (f" What gets bigger the more you take away from it" , "hole" , "This one is from my favourite game") ,
    (f" What year is it" , "2025" , "That was an easy one... You're welcome!"),
    (f" Which of the following are not vowels: \n a,e,i,s," , "s" , "The letter S is a consonant "),
    (f" What company created the Playstation", "sony", "Call me a AAA studio because I'm running out of ideas"),

]

def ask_question(question_data, question_number):
    question, correct_answer, explanation = question_data
    print(f"Question {question_number}: {question}")
    user_answer = input()
    is_correct = user_answer == correct_answer
    return is_correct, correct_answer, explanation, user_answer

def handle_correct_answer(explanation, current_correct_answers):
    print("\nCorrect!")
    print(explanation)
    print("")
    if current_correct_answers == 3:
        print(f"Wooo! You're on a roll, you have got {current_correct_answers} answers right!")
        print("")
    return 10  # Points

def handle_incorrect_answer(correct_answer):
    print(f"\nIncorrect. The answer was {correct_answer}\n")
    return 0  # No points

def display_results(player_name, final_score, correct_count, high_score):
    print(f"{player_name} You answered {correct_count} out of {len(QUESTIONS)} questions correctly.")
    print(f"Your score was {final_score} which was {high_score - final_score} points away from the highest score")
    if final_score <= 20:
        print("Unlucky you failed")
    elif final_score == 30:
        print("You Passed")
    elif final_score >= high_score:
        print("GREAT JOB!!")


#scores and question
name = display_introduction()
num_correct = 0
score = 0
highscore = 40

for question_data in QUESTIONS:
    q_num += 1
    is_correct, correct_answer, explanation, player_answer = ask_question(question_data, q_num)
    if is_correct:
        num_correct += 1
        score += handle_correct_answer(explanation,num_correct)

    else:
        handle_incorrect_answer(correct_answer)

#Results

display_results(name, score, num_correct, highscore)