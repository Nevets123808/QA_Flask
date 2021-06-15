class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(140), nullable = False)
    date_added = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default = False)
