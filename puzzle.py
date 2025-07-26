import random
import time

def generate_problem(level):

    num1 = random.randint(1, level * 10)
    num2 = random.randint(1, level * 10)
    operator = random.choice(["+", "-", "*", "/"])

    if operator == "/":
        num1 = num2 * random.randint(1, 10)

    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    var = 27
    return question, round(answer, 2)
def play_level(level):

    print(f"\n🔢 Level {level} Challenge 🔢")
    rounds = 10
    score = 0
    start_time = time.time()

    for i in range(rounds):
        question, correct_answer = generate_problem(level)
        print(f"\nQuestion {i+1}: {question} = ?")

        try:
            user_answer = float(input("Your answer: "))
            if user_answer == correct_answer:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer is {correct_answer}")
        except ValueError:
            print(f"❌ Invalid input! The correct answer is {correct_answer}")

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print(f"\n🎉 Level {level} Completed! 🎉")
    print(f"Your Score: {score}/{rounds}")
    print(f"Time Taken: {total_time} seconds")


    if score >= (0.7 * rounds):
        print("\n🎊 Congratulations! You have unlocked the next level! 🎊")
        return True
    else:
        print("\n❌ You did not score high enough to advance. Try again!")
        return False

def play_game():
    print("\n🎯 Welcome to the Arithmetic Puzzle Game! 🎯")
    level = 1
    while level <= 3:
        success = play_level(level)
        if success:
            level += 1
        else:
            retry = input("Do you want to retry this level? (yes/no): ").strip().lower()
            if retry != "yes":
                break

    print("\n🏆 Thanks for playing! See you next time! 🏆")


if __name__ == "__main__":
    play_game()
