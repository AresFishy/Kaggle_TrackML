from trackml.dataset import load_event
from trackml.randomize import shuffle_hits
from trackml.score import score_event

import numpy as np
import pandas as pd

# TODO: Turn this into a proper function
traces = []
cnt = 0
for ind in np.unique(truth["particle_id"]):
    if cnt < 30 and ind != 0:
        x,y = (truth[truth["particle_id"]==ind].tx,
        truth[truth["particle_id"]==ind].ty)
        z = truth[truth["particle_id"]==ind].tz
#         ax.scatter(z, x, y, s=14)
        traces.append(plotly_trace(x,y,z))
        cnt += 1
