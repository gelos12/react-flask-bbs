from runserver import Resource


class MainIndex(Resource):
    def get(self):
        return "MainIndex Page"