import asyncio
import sys

from PySide6.QtWidgets import QApplication
from qasync import QEventLoop

from src.db.db_manager import DBManager
from src.gui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    event_loop = QEventLoop(app)
    asyncio.set_event_loop(event_loop)

    app_close_event = asyncio.Event()
    app.aboutToQuit.connect(app_close_event.set)

    db_manager = DBManager()
    main_window = MainWindow(db_manager=db_manager)
    main_window.show()

    with event_loop:
        event_loop.run_until_complete(app_close_event.wait())