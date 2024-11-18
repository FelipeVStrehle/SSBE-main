from kivy import *
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.garden.graph import Graph, MeshLinePlot



class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__()
        Window.maximize()

        plot1 = MeshLinePlot(color=[1, 0, 0, 1])
        plot1.points = [(x, x**0.5) for x in range(100)]
        self.ids.grafico1.add_plot(plot1)

        # Plot para o gráfico 2
        plot2 = MeshLinePlot(color=[0, 1, 0, 1])
        plot2.points = [(x, x**0.3) for x in range(100)]
        self.ids.grafico2.add_plot(plot2)

        # Plot para o gráfico 3
        plot3 = MeshLinePlot(color=[0, 0, 1, 1])
        plot3.points = [(x, x**0.2) for x in range(100)]
        self.ids.grafico3.add_plot(plot3)