import numpy as np
from napari.layers import Shapes, Points

from peepingtom.datablocks import LineBlock
from peepingtom.depictors import LineDepictor


def test_line_depictor():
    lineblock = LineBlock(np.random.rand(5, 3))
    line_depictor = LineDepictor(lineblock)
    assert line_depictor.datablock is lineblock
    assert len(line_depictor.layers) == 2
    assert isinstance(line_depictor.points, Points)
    assert isinstance(line_depictor.backbone, Shapes)
