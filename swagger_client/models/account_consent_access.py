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


class AccountConsentAccess(object):
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
        'accounts': 'list[AccountAccess]',
        'balances': 'list[AccountAccess]',
        'transactions': 'list[AccountAccess]',
        'available_accounts': 'str',
        'available_accounts_with_balances': 'str',
        'all_psd2': 'str'
    }

    attribute_map = {
        'accounts': 'accounts',
        'balances': 'balances',
        'transactions': 'transactions',
        'available_accounts': 'availableAccounts',
        'available_accounts_with_balances': 'availableAccountsWithBalances',
        'all_psd2': 'allPsd2'
    }

    def __init__(self, accounts=None, balances=None, transactions=None, available_accounts=None, available_accounts_with_balances=None, all_psd2=None, _configuration=None):  # noqa: E501
        """AccountConsentAccess - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accounts = None
        self._balances = None
        self._transactions = None
        self._available_accounts = None
        self._available_accounts_with_balances = None
        self._all_psd2 = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if balances is not None:
            self.balances = balances
        if transactions is not None:
            self.transactions = transactions
        if available_accounts is not None:
            self.available_accounts = available_accounts
        if available_accounts_with_balances is not None:
            self.available_accounts_with_balances = available_accounts_with_balances
        if all_psd2 is not None:
            self.all_psd2 = all_psd2

    @property
    def accounts(self):
        """Gets the accounts of this AccountConsentAccess.  # noqa: E501

        <p>Is asking for detailed account information.</p>  <p>If the array is empty, the TPP is asking for an accessible account list.<br />This may be restricted in a PSU/ASPSP authorization dialogue.<br />If the array is empty, also the arrays for balances or transactions shall be empty, if used.</p>  # noqa: E501

        :return: The accounts of this AccountConsentAccess.  # noqa: E501
        :rtype: list[AccountAccess]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this AccountConsentAccess.

        <p>Is asking for detailed account information.</p>  <p>If the array is empty, the TPP is asking for an accessible account list.<br />This may be restricted in a PSU/ASPSP authorization dialogue.<br />If the array is empty, also the arrays for balances or transactions shall be empty, if used.</p>  # noqa: E501

        :param accounts: The accounts of this AccountConsentAccess.  # noqa: E501
        :type: list[AccountAccess]
        """

        self._accounts = accounts

    @property
    def balances(self):
        """Gets the balances of this AccountConsentAccess.  # noqa: E501

        <p>Is asking for balances of the addressed accounts.</p>  <p>If the array is empty, the TPP is asking for the balances of all accessible account lists.<br />This may be restricted in a PSU/ASPSP authorization dialogue.<br />If the array is empty, also the arrays for accounts or transactions shall be empty, if used.</p>  # noqa: E501

        :return: The balances of this AccountConsentAccess.  # noqa: E501
        :rtype: list[AccountAccess]
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this AccountConsentAccess.

        <p>Is asking for balances of the addressed accounts.</p>  <p>If the array is empty, the TPP is asking for the balances of all accessible account lists.<br />This may be restricted in a PSU/ASPSP authorization dialogue.<br />If the array is empty, also the arrays for accounts or transactions shall be empty, if used.</p>  # noqa: E501

        :param balances: The balances of this AccountConsentAccess.  # noqa: E501
        :type: list[AccountAccess]
        """

        self._balances = balances

    @property
    def transactions(self):
        """Gets the transactions of this AccountConsentAccess.  # noqa: E501

        <p>Is asking for transactions of the addressed accounts.</p>  <p>If the array is empty, the TPP is asking for the transactions of all accessible account lists.<br />This may be restricted in a PSU/ASPSP authorization dialogue.<br />If the array is empty, also the arrays for accounts or balances shall be empty, if used.</p>  # noqa: E501

        :return: The transactions of this AccountConsentAccess.  # noqa: E501
        :rtype: list[AccountAccess]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this AccountConsentAccess.

        <p>Is asking for transactions of the addressed accounts.</p>  <p>If the array is empty, the TPP is asking for the transactions of all accessible account lists.<br />This may be restricted in a PSU/ASPSP authorization dialogue.<br />If the array is empty, also the arrays for accounts or balances shall be empty, if used.</p>  # noqa: E501

        :param transactions: The transactions of this AccountConsentAccess.  # noqa: E501
        :type: list[AccountAccess]
        """

        self._transactions = transactions

    @property
    def available_accounts(self):
        """Gets the available_accounts of this AccountConsentAccess.  # noqa: E501

        <p>Only the value \"allAccounts\" is admitted.</p>  # noqa: E501

        :return: The available_accounts of this AccountConsentAccess.  # noqa: E501
        :rtype: str
        """
        return self._available_accounts

    @available_accounts.setter
    def available_accounts(self, available_accounts):
        """Sets the available_accounts of this AccountConsentAccess.

        <p>Only the value \"allAccounts\" is admitted.</p>  # noqa: E501

        :param available_accounts: The available_accounts of this AccountConsentAccess.  # noqa: E501
        :type: str
        """

        self._available_accounts = available_accounts

    @property
    def available_accounts_with_balances(self):
        """Gets the available_accounts_with_balances of this AccountConsentAccess.  # noqa: E501

        <p>Only the value \"allAccounts\" is admitted.</p>  # noqa: E501

        :return: The available_accounts_with_balances of this AccountConsentAccess.  # noqa: E501
        :rtype: str
        """
        return self._available_accounts_with_balances

    @available_accounts_with_balances.setter
    def available_accounts_with_balances(self, available_accounts_with_balances):
        """Sets the available_accounts_with_balances of this AccountConsentAccess.

        <p>Only the value \"allAccounts\" is admitted.</p>  # noqa: E501

        :param available_accounts_with_balances: The available_accounts_with_balances of this AccountConsentAccess.  # noqa: E501
        :type: str
        """

        self._available_accounts_with_balances = available_accounts_with_balances

    @property
    def all_psd2(self):
        """Gets the all_psd2 of this AccountConsentAccess.  # noqa: E501

        <p>Only the value \"allAccounts\" is admitted.</p>  # noqa: E501

        :return: The all_psd2 of this AccountConsentAccess.  # noqa: E501
        :rtype: str
        """
        return self._all_psd2

    @all_psd2.setter
    def all_psd2(self, all_psd2):
        """Sets the all_psd2 of this AccountConsentAccess.

        <p>Only the value \"allAccounts\" is admitted.</p>  # noqa: E501

        :param all_psd2: The all_psd2 of this AccountConsentAccess.  # noqa: E501
        :type: str
        """

        self._all_psd2 = all_psd2

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
        if issubclass(AccountConsentAccess, dict):
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
        if not isinstance(other, AccountConsentAccess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountConsentAccess):
            return True

        return self.to_dict() != other.to_dict()
