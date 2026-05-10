import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from source.main import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.root.mainloop()