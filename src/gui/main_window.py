import asyncio

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QWidget
from qasync import asyncSlot

from src.gui.pie_chart import PieChartWidget
from src.gui.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    sig_update_pie_chart = Signal()  # Define the Qt signal

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setupUi(self)

        # connections
        self.sig_update_pie_chart.connect(self.on_update_pie_chart)

        # load data from database & load data into UI
        self.__portfolio_allocation_data = {
            "MSCI ACWI IMI": 46,
            "MSCI World Inf. Techn.": 14,
            "MSCI EM": 11,
            "Core Stoxx Europe 600": 9,
            "MSCI World Momentum": 8,
            "MSCI Health Care": 6,
            "MSCI World Energy": 2,
            "Physical Gold": 2,
        }

        self.sig_update_pie_chart.emit()

    @asyncSlot()
    async def on_update_pie_chart(self):
        await self.update_pie_chart()

    async def update_pie_chart(self):
        pie_chart_widget = PieChartWidget(
            self,
            data=self.__portfolio_allocation_data
        )
        parent_layout = self.frame_canvas.parentWidget().layout()
        parent_layout.replaceWidget(self.frame_canvas, pie_chart_widget)

        self.frame_canvas.deleteLater()  # delete old widget or initial QFrame placeholder
        self.frame_canvas = pie_chart_widget  # replace it with new one
