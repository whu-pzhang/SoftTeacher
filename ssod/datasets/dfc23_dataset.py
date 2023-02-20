from mmdet.datasets import CocoDataset
from mmdet.datasets.builder import DATASETS


@DATASETS.register_module()
class DFC23Track1Dataset(CocoDataset):
    CLASSES = ("flat_roof", "gable_roof", "gambrel_roof", "row_roof",
               "multiple_eave_roof", "hipped_roof_v1", "hipped_roof_v2",
               "mansard_roof", "pyramid_roof", "arched_roof", "revolved",
               "other")

    PALETTE = [(220, 20, 60), (119, 11, 32), (0, 0, 142), (0, 0, 230),
               (106, 0, 228), (0, 60, 100), (0, 80, 100), (0, 0, 70),
               (0, 0, 192), (250, 170, 30), (100, 170, 30), (220, 220, 0)]
