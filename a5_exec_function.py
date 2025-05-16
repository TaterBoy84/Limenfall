
"""
a5_exec_function.py - Offers support for step-based task processing
"""

class ExecutiveFunctionHelper:
    def __init__(self):
        self.last_steps = []

    def provide_steps(self, task_name, steps):
        self.last_steps = steps
        return f"Steps for {task_name}:
" + "\n".join(f"{i+1}. {step}" for i, step in enumerate(steps))

    def recall_steps(self):
        return self.last_steps
