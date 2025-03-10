"""All custom types are located here."""
import pandas as pd
from PySide6 import QtCore
from PySide6.QtCore import Qt, Signal, QAbstractTableModel
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class AppEnvVariables(BaseSettings):
    """The app env vars, with all settings/credentials for:
    - database
    """

    # DATABASE
    db_driver: str
    """Database driver."""

    db_name: str
    """Database name."""

    model_config = ConfigDict(extra="forbid")
    """Model config."""


class PandasModel(QAbstractTableModel):
    """
    Klasse zum Darstellen eines Pandas-DataFrame in einer QTableView mit editierbarer 2. Spalte
    """
    # **Neues Signal, das ausgelöst wird, wenn Daten geändert wurden**
    dataUpdated = Signal()

    def __init__(self, data_df=pd.DataFrame(), parent=None):
        super().__init__(parent)
        self.data_df = data_df

    def rowCount(self, parent=None):
        return len(self.data_df)

    def columnCount(self, parent=None):
        return self.data_df.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        # **Rechtsbündige Ausrichtung für die zweite Spalte ("Allocation")**
        if role == Qt.TextAlignmentRole:
            if index.column() == 1:  # 2. Spalte (0-basiert)
                return Qt.AlignRight | Qt.AlignVCenter  # Rechts + vertikal zentriert

        if role == Qt.DisplayRole or role == Qt.EditRole:  # Anzeige- und Bearbeitungsmodus
            return str(self.data_df.iloc[index.row(), index.column()])

        return None

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            try:
                if index.column() == 1:  # **Nur Spalte 2 editierbar**
                    self.data_df.iloc[index.row(), index.column()] = float(value) if value else 0.0
                    self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole])  # UI aktualisieren

                    self.dataUpdated.emit()  # **Signal nach Update auslösen**

                    return True
            except ValueError:
                return False  # Falls die Eingabe kein Float ist, nichts ändern

        return False

    def flags(self, index):
        flags = super().flags(index)
        if index.column() == 1:  # **Nur Spalte 2 editierbar**
            return flags | Qt.ItemIsEditable
        return flags

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.data_df.columns[col]
        return None
