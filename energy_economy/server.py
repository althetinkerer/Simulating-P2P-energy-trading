from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer

from energy_economy.model import ForestFire


def energy_economy_portrayal(tree):
    if tree is None:
        return
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
    (x, y) = tree.get_pos()
    portrayal["x"] = x
    portrayal["y"] = y
    colors = {"Unelectrified": "#663300",
              "Transition": "#ffcc00",
              "Electrified": "#5cd65c"}
    portrayal["Color"] = colors[tree.condition]
    return portrayal

canvas_element = CanvasGrid(energy_economy_portrayal, 100, 100, 600, 600)
tree_chart = ChartModule([{"Label": "Unelectrified", "Color": "brown"},
                          {"Label": "Transition", "Color": "orange"},
                          {"Label": "Electrified", "Color": "green"}],
                          canvas_height=300, canvas_width=650)

server = ModularServer(ForestFire, [canvas_element, tree_chart], "Prava: Peer-to-Peer Energy Marketplace",
                       100, 100, 0.50)
