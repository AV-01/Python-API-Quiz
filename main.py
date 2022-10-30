from time import sleep
import random
import requests
from colorama import Fore, Back, Style

doTypingEffect = True


def typewritingEffect(phrase):
  if doTypingEffect:
    for char in phrase:
      sleep(0.005)
      print(char, end='', flush=True)
  else:
    print(phrase)


def randomGetter():
  randomList = random.choice(results)
  results.remove(randomList)
  return randomList['question'], randomList['correct_answer'], randomList[
    'incorrect_answers']


typewritingEffect(
  "\n\nHello, welcome to the epic quiz(better than Zach's quiz). You can tell that we're better because we have a cool printing thing which Zach doesn't know how to do.\n"
)


def getQuestionAmount():
  typewritingEffect("\nHow many questions do you want(limit 100): ")
  global problems
  try:
    problems = int(input())
  except:
    typewritingEffect(Fore.RED +
                      "\nPlease input a valid number. For example: 19" +
                      Fore.WHITE)
    getQuestionAmount()
  if problems > 0 and problems <= 100:
    print("\n")
  else:
    typewritingEffect(Fore.RED +
                      "Please insert a whole number between 0 and 50!" +
                      Fore.WHITE)
    getQuestionAmount()


def getDifficulty():
  global results
  typewritingEffect(
    "\nPlease select a difficulty and press enter \n1: Easy \n2: Medium\n3: Hard\n"
  )
  difficulty = input("")
  if difficulty == "1" or difficulty.lower() == "easy":
    results = requests.get("https://opentdb.com/api.php?amount=" +
                           str(problems) +
                           "&difficulty=easy&type=multiple").json()['results']
  elif difficulty == "2" or difficulty.lower() == "medium":
    results = requests.get(
      "https://opentdb.com/api.php?amount=" + str(problems) +
      "&difficulty=medium&type=multiple").json()['results']
  elif difficulty == "3" or difficulty.lower() == "hard":
    results = requests.get("https://opentdb.com/api.php?amount=" +
                           str(problems) +
                           "&difficulty=hard&type=multiple").json()['results']
  else:
    typewritingEffect(
      "Sorry, that's not a valid option. Please type a number or the difficulty\n\n"
    )
    getDifficulty()


getQuestionAmount()
getDifficulty()
questionNum = 1


def getAnswer():
  typewritingEffect("Please type the letter of the answer you want: ")
  answer = input("")
  if answer.lower() == "a" or answer.lower() == "b" or answer.lower(
  ) == "c" or answer.lower() == "d":
    return answer
  else:
    typewritingEffect(
      Fore.RED +
      "That's not a valid solution. Please input the letter that correlates with your answer!\n"
      + Fore.WHITE)
    getAnswer()


points = 0


def displayQuestions():
  global points
  global questionNum
  necessaryItems = randomGetter()
  typewritingEffect("\n\nQuestion #" + str(questionNum) + ": " +
                    necessaryItems[0].replace("&quot;", "\"").replace(
                      "&#039;", "'").replace("&amp;", ","))
  allAnswers = necessaryItems[2]
  allAnswers.append(necessaryItems[1])
  random.shuffle(allAnswers)
  typewritingEffect("\n" + Fore.RED + "A) " + allAnswers[0].replace(
    "&quot;", "\"").replace("&#039;", "'").replace("&amp;", ",") + "\n")
  typewritingEffect(Fore.GREEN + "B) " + allAnswers[1].replace(
    "&quot;", "\"").replace("&#039;", "'").replace("&amp;", ",") + "\n")
  typewritingEffect(Fore.BLUE + "C) " + allAnswers[2].replace(
    "&quot;", "\"").replace("&#039;", "'").replace("&amp;", ",") + "\n")
  typewritingEffect(Fore.CYAN + "D) " +
                    allAnswers[3].replace("&quot;", "\"").replace(
                      "&#039;", "'").replace("&amp;", ",") + "\n" + Fore.WHITE)
  answer = getAnswer()
  try:
    if allAnswers[ord(answer.lower()) - 97] == necessaryItems[1]:
      points += 1
      typewritingEffect(Fore.GREEN + "Correct! You now have " + str(points) +
                        " points\n\n" + Fore.WHITE)
    else:
      typewritingEffect(Fore.RED + "Wrong! You have " + str(points) +
                        " points. The correct answer was \"" +
                        necessaryItems[1].replace("&quot;", "\"").replace(
                          "&#039;", "'").replace("&amp;", ",") + "\"\n\n" +
                        Fore.WHITE)
  except (AttributeError):
    typewritingEffect(
      Fore.RED +
      "Sorry, there was an error in getting your answer. We'll be skipping this question since that's easier for me to program. The correct answer would've been \""
      + necessaryItems[1].replace("&quot;", "\"").replace(
        "&#039;", "'").replace("&amp;", ",") + "\"\n\n" + Fore.WHITE)
  questionNum += 1


for i in range(0, problems):
  displayQuestions()
typewritingEffect(Fore.GREEN +
                  "You have finished the quiz!!!!! All code was written by " +
                  Fore.YELLOW + "Aryavrat Mishra!" + Fore.GREEN +
                  " Special thanks to" + Fore.RED + " Zach" + Fore.GREEN +
                  " for inspiration.")
