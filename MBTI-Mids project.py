<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox

# -------------------- QUESTIONS (12 QUESTIONS) --------------------
questions = [
    {"question": "At a party, you:", "a": ("Enjoy meeting many people", "E"), "b": ("Prefer a few close friends", "I")},
    {"question": "You trust more:", "a": ("Facts and experience", "S"), "b": ("Ideas and imagination", "N")},
    {"question": "Decisions are based on:", "a": ("Logic", "T"), "b": ("Feelings", "F")},
    {"question": "Your lifestyle is:", "a": ("Planned and structured", "J"), "b": ("Flexible and spontaneous", "P")},
    {"question": "Free time you prefer:", "a": ("Going out", "E"), "b": ("Staying home", "I")},
    {"question": "You focus on:", "a": ("Reality", "S"), "b": ("Possibilities", "N")},
    {"question": "You are more:", "a": ("Objective", "T"), "b": ("Empathetic", "F")},
    {"question": "Work style:", "a": ("Organized", "J"), "b": ("Adaptive", "P")},
    {"question": "In groups you:", "a": ("Lead conversation", "E"), "b": ("Listen more", "I")},
    {"question": "You prefer knowledge that is:", "a": ("Practical", "S"), "b": ("Theoretical", "N")},
    {"question": "Conflict handling:", "a": ("Logical solution", "T"), "b": ("Emotional understanding", "F")},
    {"question": "Deadlines make you:", "a": ("Strict and focused", "J"), "b": ("Relaxed and flexible", "P")}
]

# -------------------- PERSONALITY DATA --------------------
personality_data = {
    "INTJ": {
        "desc": "A strategic thinker who builds systems and long-term visions.",
        "story": "You are someone who often sees the world like a giant puzzle, always trying to improve and optimize everything around you.",
        "career": "Engineer, Scientist, Software Developer, Architect"
    },
    "INFP": {
        "desc": "A deeply emotional and imaginative idealist.",
        "story": "You live in a world filled with meaning, emotions, and possibilities, often guided by your inner values.",
        "career": "Writer, Artist, Psychologist, Designer"
    },
    "ENTJ": {
        "desc": "A powerful and confident natural leader.",
        "story": "You are driven by ambition and clarity, always ready to take charge and lead others toward success.",
        "career": "CEO, Entrepreneur, Manager, Consultant"
    },
    "ENFP": {
        "desc": "An energetic explorer of ideas and possibilities.",
        "story": "Your mind is like a fireworks display of ideas, creativity, and excitement for new experiences.",
        "career": "Teacher, Marketer, Journalist, Speaker"
    }
}

# -------------------- TRAIT DATA --------------------
trait_labels = {
    "E": "Extraversion",
    "I": "Introversion",
    "S": "Sensing",
    "N": "Intuition",
    "T": "Thinking",
    "F": "Feeling",
    "J": "Judging",
    "P": "Perceiving"
}

# -------------------- GLOBAL VARIABLES --------------------
scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
current_question = 0
history_db = []

# -------------------- GUI --------------------
root = tk.Tk()
root.title("MBTI Personality Test (Advanced)")
root.geometry("800x600")

# -------------------- WELCOME --------------------
welcome = tk.Frame(root)

tk.Label(welcome, text="MBTI Personality Test", font=("Arial", 24, "bold")).pack(pady=20)
tk.Label(welcome, text="Enter your name:", font=("Arial", 12)).pack()

name_entry = tk.Entry(welcome, font=("Arial", 12))
name_entry.pack(pady=10)

# -------------------- QUIZ --------------------
quiz = tk.Frame(root)

progress = tk.Label(quiz, font=("Arial", 12, "bold"))
progress.pack(pady=10)

question_lbl = tk.Label(quiz, font=("Arial", 14), wraplength=700)
question_lbl.pack(pady=20)

answer = tk.StringVar()

opt1 = tk.Radiobutton(quiz, variable=answer, value="a", font=("Arial", 12))
opt1.pack(anchor="w", padx=100)

opt2 = tk.Radiobutton(quiz, variable=answer, value="b", font=("Arial", 12))
opt2.pack(anchor="w", padx=100)

# -------------------- FUNCTIONS --------------------
def reset_test():
    global scores, current_question
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    current_question = 0

def show_question():
    global current_question
    q = questions[current_question]

    progress.config(text=f"Question {current_question+1}/{len(questions)}")
    question_lbl.config(text=q["question"])

    opt1.config(text=q["a"][0])
    opt2.config(text=q["b"][0])

    answer.set("")

def draw_trait_chart(parent):
    frame = tk.LabelFrame(parent, text="Personality Trait Comparison", padx=10, pady=10)
    frame.pack(fill="both", padx=10, pady=10)

    traits = [("E","I"), ("S","N"), ("T","F"), ("J","P")]

    for a, b in traits:
        a_val = scores[a]
        b_val = scores[b]

        tk.Label(frame, text=f"{trait_labels[a]} vs {trait_labels[b]}").pack()

        bar = tk.Canvas(frame, height=20, width=400)
        bar.pack(pady=5)

        total = a_val + b_val if (a_val + b_val) != 0 else 1
        a_width = (a_val / total) * 400

        bar.create_rectangle(0, 0, a_width, 20, fill="blue")
        bar.create_rectangle(a_width, 0, 400, 20, fill="red")

def show_result():
    mbti = ""
    mbti += "E" if scores["E"] >= scores["I"] else "I"
    mbti += "S" if scores["S"] >= scores["N"] else "N"
    mbti += "T" if scores["T"] >= scores["F"] else "F"
    mbti += "J" if scores["J"] >= scores["P"] else "P"

    data = personality_data.get(mbti, {
        "desc": "Unique personality type.",
        "story": "Your personality is complex and unique...",
        "career": "Multiple careers suit you."
    })

    history_db.append({
        "type": mbti,
        "scores": scores.copy(),
        "name": name_entry.get(),
        "data": data
    })

    win = tk.Toplevel(root)
    win.title("Your Personality Result")
    win.geometry("800x700")

    tk.Label(win, text=f"Your Type: {mbti}", font=("Arial", 18, "bold")).pack(pady=10)

    tk.Label(win, text="Description", font=("Arial", 14, "bold")).pack()
    tk.Label(win, text=data["desc"], wraplength=700).pack(pady=5)

    tk.Label(win, text="Story", font=("Arial", 14, "bold")).pack()
    tk.Label(win, text=data["story"], wraplength=700).pack(pady=5)

    tk.Label(win, text="Career", font=("Arial", 14, "bold")).pack()
    tk.Label(win, text=data["career"], wraplength=700).pack(pady=5)

    draw_trait_chart(win)

    tk.Button(win, text="Finish & Restart", command=restart_app).pack(pady=10)

def restart_app():
    reset_test()
    quiz.pack_forget()
    welcome.pack(fill="both", expand=True)

def show_history():
    hist = tk.Toplevel(root)
    hist.title("History")
    hist.geometry("500x400")

    tk.Label(hist, text="Saved Results", font=("Arial", 16, "bold")).pack()

    for i, item in enumerate(history_db):
        tk.Label(hist, text=f"{i+1}. {item['name']} - {item['type']}").pack(anchor="w")

def next_q():
    global current_question

    if answer.get() == "":
        messagebox.showwarning("Warning", "Select an answer")
        return

    letter = questions[current_question][answer.get()][1]
    scores[letter] += 1

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        show_result()

def start():
    if name_entry.get() == "":
        messagebox.showwarning("Warning", "Enter name")
        return

    welcome.pack_forget()
    quiz.pack(fill="both", expand=True)
    show_question()

# -------------------- BUTTONS --------------------
tk.Button(welcome, text="Start Test", command=start, bg="lightgreen", width=20).pack(pady=20)
tk.Button(welcome, text="View History", command=show_history, bg="orange", width=20).pack(pady=10)
tk.Button(quiz, text="Next", command=next_q, bg="lightblue", width=20).pack(pady=20)

# -------------------- RUN --------------------
welcome.pack(fill="both", expand=True)
root.mainloop()

=======
import tkinter as tk
from tkinter import messagebox

# -------------------- QUESTIONS (12 QUESTIONS) --------------------
questions = [
    {"question": "At a party, you:", "a": ("Enjoy meeting many people", "E"), "b": ("Prefer a few close friends", "I")},
    {"question": "You trust more:", "a": ("Facts and experience", "S"), "b": ("Ideas and imagination", "N")},
    {"question": "Decisions are based on:", "a": ("Logic", "T"), "b": ("Feelings", "F")},
    {"question": "Your lifestyle is:", "a": ("Planned and structured", "J"), "b": ("Flexible and spontaneous", "P")},
    {"question": "Free time you prefer:", "a": ("Going out", "E"), "b": ("Staying home", "I")},
    {"question": "You focus on:", "a": ("Reality", "S"), "b": ("Possibilities", "N")},
    {"question": "You are more:", "a": ("Objective", "T"), "b": ("Empathetic", "F")},
    {"question": "Work style:", "a": ("Organized", "J"), "b": ("Adaptive", "P")},
    {"question": "In groups you:", "a": ("Lead conversation", "E"), "b": ("Listen more", "I")},
    {"question": "You prefer knowledge that is:", "a": ("Practical", "S"), "b": ("Theoretical", "N")},
    {"question": "Conflict handling:", "a": ("Logical solution", "T"), "b": ("Emotional understanding", "F")},
    {"question": "Deadlines make you:", "a": ("Strict and focused", "J"), "b": ("Relaxed and flexible", "P")}
]

# -------------------- PERSONALITY DATA --------------------
personality_data = {
    "INTJ": {
        "desc": "A strategic thinker who builds systems and long-term visions.",
        "story": "You are someone who often sees the world like a giant puzzle, always trying to improve and optimize everything around you.",
        "career": "Engineer, Scientist, Software Developer, Architect"
    },
    "INFP": {
        "desc": "A deeply emotional and imaginative idealist.",
        "story": "You live in a world filled with meaning, emotions, and possibilities, often guided by your inner values.",
        "career": "Writer, Artist, Psychologist, Designer"
    },
    "ENTJ": {
        "desc": "A powerful and confident natural leader.",
        "story": "You are driven by ambition and clarity, always ready to take charge and lead others toward success.",
        "career": "CEO, Entrepreneur, Manager, Consultant"
    },
    "ENFP": {
        "desc": "An energetic explorer of ideas and possibilities.",
        "story": "Your mind is like a fireworks display of ideas, creativity, and excitement for new experiences.",
        "career": "Teacher, Marketer, Journalist, Speaker"
    }
}

# -------------------- TRAIT DATA --------------------
trait_labels = {
    "E": "Extraversion",
    "I": "Introversion",
    "S": "Sensing",
    "N": "Intuition",
    "T": "Thinking",
    "F": "Feeling",
    "J": "Judging",
    "P": "Perceiving"
}

# -------------------- GLOBAL VARIABLES --------------------
scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
current_question = 0
history_db = []

# -------------------- GUI --------------------
root = tk.Tk()
root.title("MBTI Personality Test (Advanced)")
root.geometry("800x600")

# -------------------- WELCOME --------------------
welcome = tk.Frame(root)

tk.Label(welcome, text="MBTI Personality Test", font=("Arial", 24, "bold")).pack(pady=20)
tk.Label(welcome, text="Enter your name:", font=("Arial", 12)).pack()

name_entry = tk.Entry(welcome, font=("Arial", 12))
name_entry.pack(pady=10)

# -------------------- QUIZ --------------------
quiz = tk.Frame(root)

progress = tk.Label(quiz, font=("Arial", 12, "bold"))
progress.pack(pady=10)

question_lbl = tk.Label(quiz, font=("Arial", 14), wraplength=700)
question_lbl.pack(pady=20)

answer = tk.StringVar()

opt1 = tk.Radiobutton(quiz, variable=answer, value="a", font=("Arial", 12))
opt1.pack(anchor="w", padx=100)

opt2 = tk.Radiobutton(quiz, variable=answer, value="b", font=("Arial", 12))
opt2.pack(anchor="w", padx=100)

# -------------------- FUNCTIONS --------------------
def reset_test():
    global scores, current_question
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    current_question = 0

def show_question():
    global current_question
    q = questions[current_question]

    progress.config(text=f"Question {current_question+1}/{len(questions)}")
    question_lbl.config(text=q["question"])

    opt1.config(text=q["a"][0])
    opt2.config(text=q["b"][0])

    answer.set("")

def draw_trait_chart(parent):
    frame = tk.LabelFrame(parent, text="Personality Trait Comparison", padx=10, pady=10)
    frame.pack(fill="both", padx=10, pady=10)

    traits = [("E","I"), ("S","N"), ("T","F"), ("J","P")]

    for a, b in traits:
        a_val = scores[a]
        b_val = scores[b]

        tk.Label(frame, text=f"{trait_labels[a]} vs {trait_labels[b]}").pack()

        bar = tk.Canvas(frame, height=20, width=400)
        bar.pack(pady=5)

        total = a_val + b_val if (a_val + b_val) != 0 else 1
        a_width = (a_val / total) * 400

        bar.create_rectangle(0, 0, a_width, 20, fill="blue")
        bar.create_rectangle(a_width, 0, 400, 20, fill="red")

def show_result():
    mbti = ""
    mbti += "E" if scores["E"] >= scores["I"] else "I"
    mbti += "S" if scores["S"] >= scores["N"] else "N"
    mbti += "T" if scores["T"] >= scores["F"] else "F"
    mbti += "J" if scores["J"] >= scores["P"] else "P"

    data = personality_data.get(mbti, {
        "desc": "Unique personality type.",
        "story": "Your personality is complex and unique...",
        "career": "Multiple careers suit you."
    })

    history_db.append({
        "type": mbti,
        "scores": scores.copy(),
        "name": name_entry.get(),
        "data": data
    })

    win = tk.Toplevel(root)
    win.title("Your Personality Result")
    win.geometry("800x700")

    tk.Label(win, text=f"Your Type: {mbti}", font=("Arial", 18, "bold")).pack(pady=10)

    tk.Label(win, text="Description", font=("Arial", 14, "bold")).pack()
    tk.Label(win, text=data["desc"], wraplength=700).pack(pady=5)

    tk.Label(win, text="Story", font=("Arial", 14, "bold")).pack()
    tk.Label(win, text=data["story"], wraplength=700).pack(pady=5)

    tk.Label(win, text="Career", font=("Arial", 14, "bold")).pack()
    tk.Label(win, text=data["career"], wraplength=700).pack(pady=5)

    draw_trait_chart(win)

    tk.Button(win, text="Finish & Restart", command=restart_app).pack(pady=10)

def restart_app():
    reset_test()
    quiz.pack_forget()
    welcome.pack(fill="both", expand=True)

def show_history():
    hist = tk.Toplevel(root)
    hist.title("History")
    hist.geometry("500x400")

    tk.Label(hist, text="Saved Results", font=("Arial", 16, "bold")).pack()

    for i, item in enumerate(history_db):
        tk.Label(hist, text=f"{i+1}. {item['name']} - {item['type']}").pack(anchor="w")

def next_q():
    global current_question

    if answer.get() == "":
        messagebox.showwarning("Warning", "Select an answer")
        return

    letter = questions[current_question][answer.get()][1]
    scores[letter] += 1

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        show_result()

def start():
    if name_entry.get() == "":
        messagebox.showwarning("Warning", "Enter name")
        return

    welcome.pack_forget()
    quiz.pack(fill="both", expand=True)
    show_question()

# -------------------- BUTTONS --------------------
tk.Button(welcome, text="Start Test", command=start, bg="lightgreen", width=20).pack(pady=20)
tk.Button(welcome, text="View History", command=show_history, bg="orange", width=20).pack(pady=10)
tk.Button(quiz, text="Next", command=next_q, bg="lightblue", width=20).pack(pady=20)

# -------------------- RUN --------------------
welcome.pack(fill="both", expand=True)
root.mainloop()

>>>>>>> 0c397287bc919e0e4f7eaf88d5ea557055305f64
