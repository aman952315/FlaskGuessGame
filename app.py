from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Initialize game state
random_number = random.randint(1, 1000)
count = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global random_number, count
    message = None

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            count += 1

            if guess > random_number:
                message = "Enter a lower number!"
            elif guess < random_number:
                message = "Enter a higher number!"
            else:
                message = f"🎉 Congratulations! Correct number in {count} tries."
                random_number = random.randint(1, 1000)
                count = 0
        except ValueError:
            message = "Please enter a valid number."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
