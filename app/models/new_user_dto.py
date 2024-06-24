class NewUserDto(object):
    def __init__(self, name: str, location: str):
        
        self.name = name
        self.location = location

        if name is None or location is None:
            raise ValueError("Name/Location required")