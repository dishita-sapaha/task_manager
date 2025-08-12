**Task Manager**
A Python-based command-line application for creating, managing, and tracking tasks.
Supports persistent storage using a JSON file to retain tasks between sessions.

**Features**__
-Add tasks with title, description, and optional due date.

-Mark tasks as complete or incomplete.

-Remove tasks by title.

-List all tasks with creation date.

-Data persistence via tasks.json.

**Project Structure**

task_manager/
├── manager.py      # Main program
├── storage.py      # Save/load logic for tasks
├── task.py         # Task model definition
├── tasks.json      # Persistent task data
└── README.md       # Documentation

**Installation**
-Ensure you have Python 3.8+ installed on your machine.

-(Optional) Create a virtual environment:

python -m venv myenv
myenv\Scripts\activate     # Windows
source myenv/bin/activate  # Mac/Linux

**Install dependencies (if requirements.txt exists):**
pip install -r requirements.txt

**Usage**
_Run_:
python manager.py

_Example output_:

1. ❌ Buy milk - Due: None
   ⬜ Created at: 2025-08-10
2. ✔️ Wash dishes - Due: 2025-08-12
   ⬜ Created at: 2025-08-10


Thanks for reading!
