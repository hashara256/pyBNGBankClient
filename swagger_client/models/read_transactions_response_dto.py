# coding: utf-8

"""
    BNG Bank - XS2A Interface 1.0

    <h1>Summary</h1>  <p>The <strong>BNG Bank - XS2A Interface</strong> <em>API</em>. This API enables European banking customers to benefit from innovative products and services ('Banking as a Service') by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data.</p>  <p>The possible Approaches are:</p>  <ul>     <li>Redirect SCA OAuth Approach</li>  </ul>  <h2>Some General Remarks Related to this version of the specification:</h2>  <ul>     <li>        <p><strong>This API definition is based on the Implementation Guidelines of the Berlin Group PSD2 API.</strong>It is not an replacement in any sense. The main specification is (at the moment) always the Implementation Guidelines of the Berlin Group PSD2 API.</p>     </li>     <li>        <p><strong>This API definition contains the REST-API for requests from the TPP to the ASPSP.</strong></p>     </li>  </ul>  <h2>General Remarks on Data Types</h2>  <p>The Berlin Group definition of UTF-8 strings in context of the PSD2 API have to support at least the following characters</p>  <p>a b c d e f g h i j k l m n o p q r s t u v w x y z</p>  <p>A B C D E F G H I J K L M N O P Q R S T U V W X Y Z</p>  <p>0 1 2 3 4 5 6 7 8 9</p>  <p>/ - ? : ( ) . , ' +</p>  <p>Space</p>  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ReadTransactionsResponseDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account': 'AccountReferenceDto',
        'transactions': 'AccountReportDto',
        'balances': 'list[BalanceDto]',
        'links': 'ReadTransactionsResponseLinksDto'
    }

    attribute_map = {
        'account': 'account',
        'transactions': 'transactions',
        'balances': 'balances',
        'links': '_links'
    }

    def __init__(self, account=None, transactions=None, balances=None, links=None, _configuration=None):  # noqa: E501
        """ReadTransactionsResponseDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account = None
        self._transactions = None
        self._balances = None
        self._links = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if transactions is not None:
            self.transactions = transactions
        if balances is not None:
            self.balances = balances
        if links is not None:
            self.links = links

    @property
    def account(self):
        """Gets the account of this ReadTransactionsResponseDto.  # noqa: E501

        Account reference.  # noqa: E501

        :return: The account of this ReadTransactionsResponseDto.  # noqa: E501
        :rtype: AccountReferenceDto
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ReadTransactionsResponseDto.

        Account reference.  # noqa: E501

        :param account: The account of this ReadTransactionsResponseDto.  # noqa: E501
        :type: AccountReferenceDto
        """

        self._account = account

    @property
    def transactions(self):
        """Gets the transactions of this ReadTransactionsResponseDto.  # noqa: E501

        JSON based account report.  # noqa: E501

        :return: The transactions of this ReadTransactionsResponseDto.  # noqa: E501
        :rtype: AccountReportDto
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this ReadTransactionsResponseDto.

        JSON based account report.  # noqa: E501

        :param transactions: The transactions of this ReadTransactionsResponseDto.  # noqa: E501
        :type: AccountReportDto
        """

        self._transactions = transactions

    @property
    def balances(self):
        """Gets the balances of this ReadTransactionsResponseDto.  # noqa: E501

        A list of balances regarding this account, e.g. the current balance, the last booked balance.  # noqa: E501

        :return: The balances of this ReadTransactionsResponseDto.  # noqa: E501
        :rtype: list[BalanceDto]
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this ReadTransactionsResponseDto.

        A list of balances regarding this account, e.g. the current balance, the last booked balance.  # noqa: E501

        :param balances: The balances of this ReadTransactionsResponseDto.  # noqa: E501
        :type: list[BalanceDto]
        """

        self._balances = balances

    @property
    def links(self):
        """Gets the links of this ReadTransactionsResponseDto.  # noqa: E501

        <p>Links to the read transactions response.</p>  # noqa: E501

        :return: The links of this ReadTransactionsResponseDto.  # noqa: E501
        :rtype: ReadTransactionsResponseLinksDto
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ReadTransactionsResponseDto.

        <p>Links to the read transactions response.</p>  # noqa: E501

        :param links: The links of this ReadTransactionsResponseDto.  # noqa: E501
        :type: ReadTransactionsResponseLinksDto
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ReadTransactionsResponseDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReadTransactionsResponseDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReadTransactionsResponseDto):
            return True

        return self.to_dict() != other.to_dict()