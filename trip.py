class Trip:
    def __init__(self, start_address, end_address):
        self.start_address = start_address
        self.end_address = end_address
    
    def __str__(self):
        return f"{self.start_address} manzilidan {self.end_address} manziliga sayohat"