# getdata.py

class GetData:
    def __init__(self):
        self.scene = 0
        self.q_list = [None] * 5
        self.music = None

    def get_scene(self):
        return self.scene

    def set_scene(self, scene):
        self.scene = scene
