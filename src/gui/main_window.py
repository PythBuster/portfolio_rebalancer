import asyncio

import pandas as pd
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow
from qasync import asyncSlot

from src.custom_types import PandasModel
from src.db.db_manager import DBManager
from src.gui.pie_chart import PieChartWidget
from src.gui.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    sig_update_pie_chart = Signal()  # Define the Qt signal

    def __init__(
            self,
            db_manager: DBManager,
    ):
        self.db_manager = db_manager
        self.portfolio_model = None

        super().__init__()
        self.setupUi(self)

        # connections
        self.sig_update_pie_chart.connect(self.on_update_pie_chart)

        # load data from database & load data into UI
        self.__portfolio_allocation_data = None

        self.background_tasks = set()

        loop = asyncio.get_event_loop()

        # load portfolio data
        task_1 = loop.create_task(self.load_portfolio_data())
        task_1.add_done_callback(self.background_tasks.discard)
        self.background_tasks.add(task_1)

        # load pie chart
        task_2 = loop.create_task(self.update_pie_chart())
        task_2.add_done_callback(self.background_tasks.discard)
        self.background_tasks.add(task_2)

        self.pushButton_save_portfolio_data.setEnabled(False)
        self.pushButton_save_portfolio_data.clicked.connect(self.on_click_save_portfolio_data)

    @asyncSlot()
    async def on_click_save_portfolio_data(self):
        print("Save to database")
        self.pushButton_save_portfolio_data.setEnabled(False)


    @asyncSlot()
    async def on_update_pie_chart(self):
        await self.update_pie_chart()

    @asyncSlot()
    async def on_pandas_model_update(self):
        total_allocation = sum(self.portfolio_model.data_df["Verteilung (in %)"])

        if total_allocation != 100:
            print("Can't save data, total allocation is not 100%!")
            self.pushButton_save_portfolio_data.setEnabled(False)
            return

        print("Modified data in portfolio data, need to save portfolio data to database!")
        self.pushButton_save_portfolio_data.setEnabled(True)


    async def load_portfolio_data(self):
        portfolio_data = await self.db_manager.get_portfolio()

        # DataFrame
        portfolio_data_df = pd.DataFrame.from_dict(portfolio_data, orient="index")

        # Column names
        portfolio_data_df.reset_index(inplace=True)
        portfolio_data_df.columns = ["Position Name", "Verteilung (in %)"]  # Neue Spaltenüberschriften

        self.portfolio_model = PandasModel(data_df=portfolio_data_df)
        self.tableView_portfolio_data.setModel(self.portfolio_model)
        self.tableView_portfolio_data.resizeColumnsToContents()

        # connection
        self.portfolio_model.dataUpdated.connect(self.on_pandas_model_update)

    async def update_pie_chart(self):
        portfolio_data = await self.db_manager.get_portfolio()

        pie_chart_widget = PieChartWidget(
            self,
            data=portfolio_data
        )
        parent_layout = self.frame_canvas.parentWidget().layout()
        parent_layout.replaceWidget(self.frame_canvas, pie_chart_widget)

        self.frame_canvas.deleteLater()  # delete old widget or initial QFrame placeholder
        self.frame_canvas = pie_chart_widget  # replace it with new one
