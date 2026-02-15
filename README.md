🕒 Digital Clock — Python Mini Project

📌 Overview

The Digital Clock is a simple desktop application built using Python and the Tkinter GUI library.
It displays the current system time in real-time and updates automatically every second.

This project is designed for beginners to understand GUI programming, event loops, and real-time updates in Python.

---

🎯 Objectives

- Learn basic GUI development using Tkinter
- Understand real-time updates using "after()" method
- Work with Python’s built-in "time" module
- Create a clean and responsive interface

---

🛠️ Technologies Used

- Python 3
- Tkinter — GUI Library (built-in)
- time module — To fetch current system time

---

📂 Project Structure

digital-clock/
│── digital_clock.py
│── README.md

---

⚙️ How It Works

1. The Tkinter window is created.
2. The program fetches the system time using "strftime()".
3. The label displaying the time updates every 1 second using "after(1000, function)".
4. The loop continues while the application window is open.

---

▶️ How to Run the Project

Step 1 — Install Python

Make sure Python 3 is installed
Check using:

python --version

Step 2 — Download Project

Clone or download the repository

Step 3 — Run Program

Navigate to project folder and run:

python digital_clock.py

---

💡 Features

- Real-time digital clock
- Auto refresh every second
- Simple and lightweight
- No external libraries required
- Beginner friendly project

---

🧠 Concepts Covered

- GUI programming
- Event driven programming
- Infinite loop handling using "after()"
- Working with system time

---

📷 Expected Output

A window opens showing current time in format:

HH : MM : SS AM/PM

Example:

10 : 45 : 12 PM

---

🔮 Future Enhancements

- Add current date display
- Add alarm functionality
- Add theme switch (Dark / Light mode)
- Add 12/24 hour toggle
- Add stopwatch feature

---

🤝 Contribution

This project is open for improvements.
Feel free to fork and enhance it.

---

📄 License

This project is for educational purposes and free to use.
