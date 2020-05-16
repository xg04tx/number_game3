from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/game', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('game.html')
    else:
        return render_template('guess.html')
        NumOfTry = 10
        LimitLow = 1
        LimitHigh = 1000
        NumToGuess = 500
        while NumOfTry != 0:
            try:
                print("I try: ", NumToGuess)
                print("Please type: 1 for my try is too high")
                print("             2 for my try is too low")
                print("             3 I guessed your number")
                Answer = int(input("So did I guess right?"))
                if 1 < Answer > 3:
                    print("Please enter a valid answer. 1, 2 and 3 are the valid choice")
                    NumOfTry = NumOfTry + 1
                if Answer == 1:
                    LimitHigh = NumToGuess
                    print("Hmm, so your number is between ", LimitLow, "and ", LimitHigh)
                    NumOfTry = NumOfTry - 1
                    print(NumOfTry, "attempts left")
                    NumToGuess = int(((LimitHigh - LimitLow) / 2) + LimitLow)
                    if NumToGuess <= LimitLow:
                        NumToGuess = NumToGuess + 1
                    if LimitHigh - LimitLow == 2:
                        NumToGuess = LimitLow + 1
                elif Answer == 2:
                    LimitLow = NumToGuess
                    print("Hmm, so your number is between ", LimitLow, "and ", LimitHigh)
                    NumOfTry = NumOfTry - 1
                    print(NumOfTry, "attempts left")
                    NumToGuess = int(((LimitHigh - LimitLow) / 2) + LimitLow)
                    if NumToGuess <= LimitLow:
                        NumToGuess = NumToGuess + 1
                    if LimitHigh - LimitLow == 2:
                        NumToGuess = LimitLow + 1
                elif num == NumToGuess:
                    print("Don't cheat")
                    NumOfTry = NumOfTry + 1
                elif Answer == 3:
                    print("I won!!!!")
                    NumOfTry = 0
            except:
                return render_template('game.html')


if __name__ == '__main__':
    app.run(debug=True)
