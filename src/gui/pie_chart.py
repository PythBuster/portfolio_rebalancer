from typing import Any

from PySide6.QtWidgets import QVBoxLayout, QWidget
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from src.utils import generate_colors, rgb_to_hex


class PieChartWidget(QWidget):
    def __init__(self, parent: QWidget, data: dict[str, Any]):
        super().__init__(parent)

        # Create Matplotlib figure and canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.__data = data

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # Initial Plot
        self.plot_pie_chart()

    def plot_pie_chart(self, labels=None, sizes=None):
        """Plots a pie chart with given labels and sizes"""

        if labels is None:
            labels = list(self.__data.keys())
        if sizes is None:
            sizes = list(self.__data.values())

        colors = rgb_to_hex(generate_colors(len(self.__data)))

        self.ax.clear()

        autopct = "%d%%"
        # autopct = "%1.1f%%"

        self.ax.pie(sizes, labels=labels, autopct=autopct, colors=colors, startangle=140)
        self.ax.set_title("Portfolio Allocation")

        self.canvas.draw()
