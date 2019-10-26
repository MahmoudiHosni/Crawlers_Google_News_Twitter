from mongoengine import connect


class mongoConnection:
    def __init__(self, config):
        self.config = config

    def __enter__(self):
        self.connection = connect(db='ScreeningReview', host='mongodb://system:sysEqua1i0sDev@ubsdev.equalios.com:22018/?authSource=admin')

        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
