import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

FONT_PATH1 = 'fonts/GenShinGothic-Monospace-Regular.ttf'
FONT_PATH2 = 'fonts/RictyDiminished-Regular.ttf'


class ChartAbstract(FigureCanvas):
    def __init__(self):
        fm.fontManager.addfont(FONT_PATH1)
        font_prop = fm.FontProperties(fname=FONT_PATH1)
        plt.rcParams['font.family'] = font_prop.get_name()
        plt.rcParams['font.size'] = 14

        # fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig = Figure()

        super().__init__(self.fig)

    def clearAxes(self):
        pass

    def refreshDraw(self):
        pass


class ChartExchange(ChartAbstract):
    def __init__(self):
        super().__init__()
        fm.fontManager.addfont(FONT_PATH2)
        font_prop = fm.FontProperties(fname=FONT_PATH2)
        plt.rcParams['font.family'] = font_prop.get_name()
        plt.rcParams['font.size'] = 14
        plt.rcParams['axes.labelsize'] = 14
        plt.rcParams['xtick.labelsize'] = 10
        plt.rcParams['ytick.labelsize'] = 10
        plt.rcParams['legend.fontsize'] = 8

        self.fig.subplots_adjust(
            top=0.9,
            bottom=0.15,
            left=0.185,
            right=0.995,
            hspace=0,
        )
        self.ax = self.fig.add_subplot(111)

    def clearAxes(self):
        axs = self.fig.axes
        for ax in axs:
            ax.cla()

    def refreshDraw(self):
        self.fig.canvas.draw()

    def removeAxes(self):
        axs = self.fig.axes
        for ax in axs:
            ax.remove()
