# Import necessary modules
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListView
from PySide6.QtCore import QStringListModel

# Define a class for the Todo List App
class TodoListApp(QMainWindow):
    # Initialize the Todo List App
    def __init__(self):
        # Call the parent class's constructor
        super().__init__()
        
        # Set the window title and geometry
        self.setWindowTitle("Todo List App")
        self.setGeometry(100, 100, 400, 300)

        # Initialize an empty list to store tasks
        self.tasks = []

        # Create a central widget to hold the layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a vertical layout to arrange widgets
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create a list view to display tasks
        self.task_list = QListView()
        # Disable editing of tasks in the list view
        self.task_list.setEditTriggers(QListView.NoEditTriggers)
        # Allow single selection of tasks in the list view
        self.task_list.setSelectionMode(QListView.SingleSelection)
        self.layout.addWidget(self.task_list)

        # Create a label to prompt the user to enter a task
        self.label = QLabel("Enter a task:")
        self.layout.addWidget(self.label)

        # Create a line edit to input tasks
        self.task_input = QLineEdit()
        self.layout.addWidget(self.task_input)

        # Create a button to add tasks to the list
        self.add_button = QPushButton("Add")
        # Connect the button's clicked signal to the add_task method
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        # Create a button to remove tasks from the list
        self.remove_button = QPushButton("Remove")
        # Connect the button's clicked signal to the remove_task method
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)

        # Update the task list to display any initial tasks
        self.update_task_list()

    # Method to add a task to the list
    def add_task(self):
        # Get the text from the task input line edit
        task = self.task_input.text()
        # Check if the task is not empty
        if task:
            # Add the task to the list of tasks
            self.tasks.append(task)
            # Clear the task input line edit
            self.task_input.clear()
            # Update the task list to display the new task
            self.update_task_list()

    # Method to remove a task from the list
    def remove_task(self):
        # Get the index of the currently selected task
        selected_index = self.task_list.currentIndex()
        # Check if a task is selected
        if selected_index.isValid():
            # Get the task at the selected index
            task = self.tasks[selected_index.row()]
            # Remove the task from the list of tasks
            self.tasks.remove(task)
            # Update the task list to reflect the removed task
            self.update_task_list()

    # Method to update the task list
    def update_task_list(self):
        # Create a string list model from the list of tasks
        self.task_list.setModel(QStringListModel(self.tasks))

# Check if the script is being run directly (not being imported)
if __name__ == "__main__":
    # Create a Qt application
    app = QApplication(sys.argv)
    # Create an instance of the Todo List App
    window = TodoListApp()
    # Show the Todo List App window
    window.show()
    # Start the Qt application's event loop
    sys.exit(app.exec())
