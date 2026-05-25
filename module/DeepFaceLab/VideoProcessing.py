import multiprocessing
import os
import subprocess
from pathlib import Path

from module.DeepFaceLab.core.leras import nn
from module.DeepFaceLab.mainscripts import VideoEd, Merger, Extractor
# nn.initialize_main_env()
# multiprocessing.set_start_method("spawn")

class VideoProcessing:
    def __init__(self):
        self.input_file = 'workspace/data_src/source.*'
        self.reference_file = 'workspace/data_src/source.*'
        pass

    def Cut(self):
        VideoEd.extract_video(input_file = self.input_file, output_dir="workspace/data_dst",output_ext=None, fps = 0)
    def MergeVedio(self):
        VideoEd.video_from_sequence(input_dir="workspace/data_dst/merged",
                                    output_file="workspace/result.mp4",
                                    reference_file=self.reference_file,
                                    ext='png',
                                    fps=None,
                                    bitrate=None,
                                    include_audio=True,
                                    lossless=False)
        VideoEd.video_from_sequence(input_dir="workspace/data_dst/merged",
                                    output_file="workspace/result.mp4",
                                    reference_file=self.reference_file,
                                    ext='png',
                                    fps=None,
                                    bitrate=None,
                                    include_audio=False,
                                    lossless=True)
    def MergeSADE(self):
        nn.initialize_main_env()
        Merger.main(model_class_name='SAEHD',
                    saved_models_path=Path("workspace/model"),
                    force_model_name="new",
                    input_path=Path("workspace/data_dst"),
                    output_path=Path("workspace/data_dst/merged"),
                    output_mask_path=Path("workspace/data_dst/merged_mask"),
                    aligned_path=Path("workspace/data_dst/aligned"),
                    force_gpu_idxs=None,
                    cpu_only=False)
    def ExtractFace(self):
        nn.initialize_main_env()
        Extractor.main(detector='s3fd',
                       input_path=Path("workspace/data_dst"),
                       output_path=Path("workspace/data_dst/aligned"),
                       output_debug=None,
                       manual_fix=False,
                       manual_output_debug_fix=False,
                       manual_window_size=1368,
                       face_type='full_face',
                       max_faces_from_image=0,
                       image_size=None,
                       jpeg_quality=None,
                       cpu_only=False,
                       force_gpu_idxs=None
                       )


