from . import utils
from ._amortizedlda import AmortizedLDA
from ._autozi import AUTOZI
from ._condscvi import CondSCVI
from ._destvi import DestVI
from ._jaxscvi import JaxSCVI
from ._linear_scvi import LinearSCVI
from ._multivi import MULTIVI
from ._peakvi import PEAKVI
from ._scanvi import SCANVI
from ._scvi import SCVI, CustomBatchSCVI
from ._totalvi import TOTALVI
from ._utils import get_max_epochs_heuristic

__all__ = [
    "SCVI",
    "TOTALVI",
    "LinearSCVI",
    "AUTOZI",
    "SCANVI",
    "PEAKVI",
    "CondSCVI",
    "DestVI",
    "MULTIVI",
    "AmortizedLDA",
    "utils",
    "JaxSCVI",
]
