import re
import json
import subprocess


class VideoProber:

    def __init__(self):
        self.fp = None
        self._video_info = []

    def probe(self, filename):
        res = re.match(r'file:///', filename)
        if res:
            if res.group():
                res = re.split(r'file:///', filename)[1]
            self.fp = res
        else: self.fp = filename
        try:
            res = subprocess.check_output(
                ['ffprobe', '-i', self.fp, '-print_format', 'json', '-show_format', '-show_streams', '-v',
                 'quiet'])
            res = res.decode('utf8')

            self._video_info = json.loads(res)
            # print('_video_info ',self._video_info)
        except Exception as e:
            print(e)
            raise Exception('获取视频信息失败')

    def get_video_width_height(self):
        streams = self._video_info['streams'][0]
        return streams['height'], streams['width']

    def get_video_file_size(self):
        video_format = self._video_info['format']
        size = int(video_format['size'])
        kb = 1024
        mb = kb * 1024
        gb = mb * 1024

        if size >= gb:
            return "%.1f GB" % float(size / gb)
        elif size >= mb:
            return "%.1f MB" % float(size / mb)
        elif size >= kb:
            return "%.1f KB" % float(size / kb)

    def get_video_frame_rate(self):
        streams = self._video_info['streams'][0]

        res = re.split(r'/',streams['avg_frame_rate'])
        return '%.1f' % (float(res[0]) / float(res[1]))
    def get_video_info(self):
        return {
            'path': self.fp,
            'file_size': self.get_video_file_size(),
            'height_width': self.get_video_width_height(),
            'frame_rate': self.get_video_frame_rate()
        }


if __name__ == '__main__':
    v = VideoProber()
    v.probe(r'file:///D:/Py program/CultScreenTest/3.mp4')
    print(v.get_video_info())
