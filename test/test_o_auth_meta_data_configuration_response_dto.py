# coding: utf-8

"""
    BNG Bank - XS2A Interface 1.0

    <h1>Summary</h1>  <p>The <strong>BNG Bank - XS2A Interface</strong> <em>API</em>. This API enables European banking customers to benefit from innovative products and services ('Banking as a Service') by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data.</p>  <p>The possible Approaches are:</p>  <ul>     <li>Redirect SCA OAuth Approach</li>  </ul>  <h2>Some General Remarks Related to this version of the specification:</h2>  <ul>     <li>        <p><strong>This API definition is based on the Implementation Guidelines of the Berlin Group PSD2 API.</strong>It is not an replacement in any sense. The main specification is (at the moment) always the Implementation Guidelines of the Berlin Group PSD2 API.</p>     </li>     <li>        <p><strong>This API definition contains the REST-API for requests from the TPP to the ASPSP.</strong></p>     </li>  </ul>  <h2>General Remarks on Data Types</h2>  <p>The Berlin Group definition of UTF-8 strings in context of the PSD2 API have to support at least the following characters</p>  <p>a b c d e f g h i j k l m n o p q r s t u v w x y z</p>  <p>A B C D E F G H I J K L M N O P Q R S T U V W X Y Z</p>  <p>0 1 2 3 4 5 6 7 8 9</p>  <p>/ - ? : ( ) . , ' +</p>  <p>Space</p>  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.o_auth_meta_data_configuration_response_dto import OAuthMetaDataConfigurationResponseDto  # noqa: E501
from swagger_client.rest import ApiException


class TestOAuthMetaDataConfigurationResponseDto(unittest.TestCase):
    """OAuthMetaDataConfigurationResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOAuthMetaDataConfigurationResponseDto(self):
        """Test OAuthMetaDataConfigurationResponseDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.o_auth_meta_data_configuration_response_dto.OAuthMetaDataConfigurationResponseDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
