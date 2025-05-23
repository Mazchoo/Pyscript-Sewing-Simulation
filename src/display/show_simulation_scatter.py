""" Play a 3d animation just with the points of different objects """
import plotly.graph_objects as go

from src.utils.read_obj import parse_obj
from src.utils.file_io import read_json
from src.simulation.setup.extract_clothing_vertex_data import extract_all_piece_vertices
from src.simulation.simulation import FabricSimulation

from src.parameters import AVATAR_SCALING, NR_STEPS


def show_3d_scatter_simulation(simulation: FabricSimulation):
    """ Create scatter plot animation from saved frames of a simulation """

    frames = [simulation.get_scatter_at_frame(i) for i in range(simulation.nr_frames)]

    # Figure layout with buttons and slider
    fig = go.Figure(
        data=frames[0].data,
        layout=go.Layout(
            scene=dict(aspectmode='cube',
                       xaxis=dict(nticks=4, range=[-0.8, 0.8], autorange=False),
                       yaxis=dict(nticks=4, range=[-0.8, 0.8], autorange=False),
                       zaxis=dict(nticks=4, range=[0, 2.4], autorange=False)),
            updatemenus=[{
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [None, {
                            "frame": {"duration": 50, "redraw": True},
                            "fromcurrent": True,
                            "transition": {"duration": 25}
                        }]
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [[None], {
                            "frame": {"duration": 0},
                            "mode": "immediate",
                            "transition": {"duration": 0}
                        }]
                    }
                ]
            }],
            sliders=[{
                "steps": [
                    {
                        "args": [
                            [str(k)],
                            {"frame": {"duration": 0},
                             "mode": "immediate"}
                        ],
                        "label": str(k),
                        "method": "animate"
                    } for k in range(simulation.nr_frames)
                ],
                "active": 0
            }]
        ),
        frames=frames
    )

    fig.show()


if __name__ == '__main__':
    avatar_mesh = parse_obj('./assets/BodyMesh.obj', './assets/BodyAnnotations.json')
    avatar_mesh.scale_vertices(AVATAR_SCALING)

    clothing_data = read_json('./assets/sewing_shirt.json')
    all_pieces, sewing = extract_all_piece_vertices(clothing_data, avatar_mesh)

    simulation = FabricSimulation(avatar_mesh, all_pieces, sewing)
    simulation.step(NR_STEPS)

    show_3d_scatter_simulation(simulation)
