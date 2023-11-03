   def setUpClass(cls):
        cls.app = create_app()
        cls.test_client = cls.app.test_client()
        ctx = cls.app.app_context()
        ctx.push()


class DBTest(BaseTest):
@@ -21,13 +23,16 @@ class DBTest(BaseTest):
    def setUpClass(cls):
        super().setUpClass()
        cls.db = db

    @classmethod
    def tearDown(cls):
        cls.db.session.rollback()
        cls.db.session.remove()
        cls.db.drop_all()
        cls.db.create_all()

    def save(self, model, payload):
        model = model(**payload)
        self.db.session.add(model)
        self.db.session.commit()
        return model