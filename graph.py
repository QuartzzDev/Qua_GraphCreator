################################
# QuartzzDev <3    quartzz.dll #
################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import pyqtgraph as pg

class GraphApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Qua Graph')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        # Input for adding values
        self.input_value = QLineEdit(self)
        self.input_value.setPlaceholderText('Değer Girin .. / Enter Value ..')
        self.input_value.returnPressed.connect(self.add_value)
        self.layout.addWidget(self.input_value)

        # Button to add value
        self.add_button = QPushButton('Ekle / Add', self)
        self.add_button.clicked.connect(self.add_value)
        self.layout.addWidget(self.add_button)

        # Table to display values
        self.table = QTableWidget(self)
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(['Değerler / Values'])
        self.layout.addWidget(self.table)

        # Graph plot
        self.plot_widget = pg.PlotWidget(self)
        self.layout.addWidget(self.plot_widget)

        self.setLayout(self.layout)

        # List to store values
        self.values = []

    # Add Value
    def add_value(self):
        value_text = self.input_value.text()
        if value_text:
            self.values.append(float(value_text))
            self.update_table()
            self.input_value.clear()

    # Update Table
    def update_table(self):
        self.table.setRowCount(len(self.values))
        for i, value in enumerate(self.values):
            item = QTableWidgetItem(str(value))
            self.table.setItem(i, 0, item)

        self.plot_graph()

    # Plot Graph
    def plot_graph(self):
        self.plot_widget.clear()
        x_values = list(range(1, len(self.values) + 1))
        self.plot_widget.plot(x_values, self.values, pen='b')

    # Press Key Event
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.delete_value()

    # Delete Value
    def delete_value(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0 and selected_row < len(self.values):
            del self.values[selected_row]
            self.update_table()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GraphApp()
    window.show()
    sys.exit(app.exec_())
