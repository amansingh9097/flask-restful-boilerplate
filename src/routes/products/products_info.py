import json
from flask import request
from src.core.models import Products
import src.misc.constants as cn
from src.instance.flask_app import api
from flask_restplus import Resource, fields
from src.misc.response_generator import response_generator
from src.misc.service_logger import serviceLogger as logger
from src.namespace import prod_api
from src.misc.db_misc_functions import db_save

product_display_model = api.model("products",
                                   {
                                     "product_name": fields.String(
                                         required=True,
                                         description="product name"
                                     ),
                                     "product_type": fields.String(
                                         required=True,
                                         description="product type"
                                     )
                                   })

parser = api.parser()
products_post = parser.copy()

products_post.add_argument('product_name', type=str, required=True, help='product name', location='json')
products_post.add_argument('product_type', type=str, required=True, help='product type', location='json')



@prod_api.route("/ProductInfo")
class ProductsInfo(Resource):
    def get(self):
        """
        GET request endpoint of ProductsInfo
        :return:

            "Hello world, from Products!"
        """
        logger.info("testing accessibility of products endpoint")
        return "Hello world, from Products!"

    @prod_api.expect(product_display_model, validate=True)
    def post(self):
        """
        add products and product details.
        :return:

            {"payload" : "Product details added successfully."}
        """
        try:
            data = request.data
            if type(data) == bytes:
                data = data.decode('utf-8')

            data = json.loads(data)

            product_name = str(data['product_name'])
            product_type = float(data['product_type'])

            new_product = Products(product_name=product_name, product_type=product_type)

            db_save(new_product)
            logger.info(cn.PRODUCT_ADDED_SUCC)
            return response_generator(cn.PRODUCT_ADDED_SUCC, status=201)

        except Exception as e:
            logger.error(cn.INTERNAL_SERV_ERR, exc_info=True)
            return response_generator(cn.INTERNAL_SERV_ERR, status=500)

    @prod_api.doc(False)
    def put(self):
        """
        PUT request endpoint of ProductsInfo
        """
        api.abbort(403)

    @prod_api.doc(False)
    def delete(self):
        """
        DELETE request endpoint of ProductsInfo
        """
        api.abbort(403)

