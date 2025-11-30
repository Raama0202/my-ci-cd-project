from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory "database" for the to-do items
tasks = []


@app.route("/")
def index():
    """Render the main page with the to-do list."""
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    """Add a new task to the list."""
    task_text = request.form.get("task")
    if task_text:
        tasks.append({"text": task_text, "done": False})
    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    """Toggle the 'done' status of a task."""
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = not tasks[task_id]["done"]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
