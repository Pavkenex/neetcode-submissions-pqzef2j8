class TimeMap:

    def __init__(self):
        self.objects=dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.objects:
            self.objects[key] = {}
        self.objects[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.objects:
            return ""

        valid_timestamps = [t for t in self.objects[key] if t <= timestamp]
        if not valid_timestamps:
            return ""

        latest = max(valid_timestamps)
        return self.objects[key][latest]
        
        
