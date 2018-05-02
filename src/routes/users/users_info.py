from src.instance.flask_app import api
from flask_restplus import Resource
from src.misc.service_logger import serviceLogger as logger
from src.namespace import user_api

@user_api.route("/UserInfo")
class UsersInfo(Resource):
    def get(self):
        """
        GET request endpoint of UsersInfo
        :return:

            "Hello world, from Users!"
        """
        logger.info("testing accessibility of users endpoint")
        return "Hello world, from Users!"

    @user_api.doc(False)
    def post(self):
        """
        POST request endpoint of UsersInfo
        """
        api.abbort(403)

    @user_api.doc(False)
    def put(self):
        """
        PUT request endpoint of UsersInfo
        """
        api.abbort(403)

    @user_api.doc(False)
    def delete(self):
        """
        DELETE request endpoint of UsersInfo
        """
        api.abbort(403)