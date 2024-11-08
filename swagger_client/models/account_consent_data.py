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


class AccountConsentData(object):
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
        'access': 'AccountConsentAccess',
        'combined_service_indicator': 'bool',
        'recurring_indicator': 'bool',
        'valid_until': 'str',
        'frequency_per_day': 'int'
    }

    attribute_map = {
        'access': 'access',
        'combined_service_indicator': 'combinedServiceIndicator',
        'recurring_indicator': 'recurringIndicator',
        'valid_until': 'validUntil',
        'frequency_per_day': 'frequencyPerDay'
    }

    def __init__(self, access=None, combined_service_indicator=None, recurring_indicator=None, valid_until=None, frequency_per_day=None, _configuration=None):  # noqa: E501
        """AccountConsentData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access = None
        self._combined_service_indicator = None
        self._recurring_indicator = None
        self._valid_until = None
        self._frequency_per_day = None
        self.discriminator = None

        self.access = access
        self.combined_service_indicator = combined_service_indicator
        self.recurring_indicator = recurring_indicator
        self.valid_until = valid_until
        self.frequency_per_day = frequency_per_day

    @property
    def access(self):
        """Gets the access of this AccountConsentData.  # noqa: E501

        Requested access services for a consent.  # noqa: E501

        :return: The access of this AccountConsentData.  # noqa: E501
        :rtype: AccountConsentAccess
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this AccountConsentData.

        Requested access services for a consent.  # noqa: E501

        :param access: The access of this AccountConsentData.  # noqa: E501
        :type: AccountConsentAccess
        """
        if self._configuration.client_side_validation and access is None:
            raise ValueError("Invalid value for `access`, must not be `None`")  # noqa: E501

        self._access = access

    @property
    def combined_service_indicator(self):
        """Gets the combined_service_indicator of this AccountConsentData.  # noqa: E501

        If \"true\" indicates that a payment initiation service will be addressed in the same \"session\".  # noqa: E501

        :return: The combined_service_indicator of this AccountConsentData.  # noqa: E501
        :rtype: bool
        """
        return self._combined_service_indicator

    @combined_service_indicator.setter
    def combined_service_indicator(self, combined_service_indicator):
        """Sets the combined_service_indicator of this AccountConsentData.

        If \"true\" indicates that a payment initiation service will be addressed in the same \"session\".  # noqa: E501

        :param combined_service_indicator: The combined_service_indicator of this AccountConsentData.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and combined_service_indicator is None:
            raise ValueError("Invalid value for `combined_service_indicator`, must not be `None`")  # noqa: E501

        self._combined_service_indicator = combined_service_indicator

    @property
    def recurring_indicator(self):
        """Gets the recurring_indicator of this AccountConsentData.  # noqa: E501

        \"true\", if the consent is for recurring access to the account data.<br />\"false\", if the consent is for one access to the account data.  # noqa: E501

        :return: The recurring_indicator of this AccountConsentData.  # noqa: E501
        :rtype: bool
        """
        return self._recurring_indicator

    @recurring_indicator.setter
    def recurring_indicator(self, recurring_indicator):
        """Sets the recurring_indicator of this AccountConsentData.

        \"true\", if the consent is for recurring access to the account data.<br />\"false\", if the consent is for one access to the account data.  # noqa: E501

        :param recurring_indicator: The recurring_indicator of this AccountConsentData.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and recurring_indicator is None:
            raise ValueError("Invalid value for `recurring_indicator`, must not be `None`")  # noqa: E501

        self._recurring_indicator = recurring_indicator

    @property
    def valid_until(self):
        """Gets the valid_until of this AccountConsentData.  # noqa: E501

        <p>This parameter is requesting a valid until date for the requested consent.<br />The content is the local ASPSP date in ISO-Date Format, e.g. 2017-10-30.</p>  <p>Future dates might get adjusted by ASPSP.</p>  <p>If a maximal available date is requested, a date in far future is to be used: \"9999-12-31\".</p>  <p>In both cases the consent object to be retrieved by the GET Consent Request will contain the adjusted date.</p>  # noqa: E501

        :return: The valid_until of this AccountConsentData.  # noqa: E501
        :rtype: str
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this AccountConsentData.

        <p>This parameter is requesting a valid until date for the requested consent.<br />The content is the local ASPSP date in ISO-Date Format, e.g. 2017-10-30.</p>  <p>Future dates might get adjusted by ASPSP.</p>  <p>If a maximal available date is requested, a date in far future is to be used: \"9999-12-31\".</p>  <p>In both cases the consent object to be retrieved by the GET Consent Request will contain the adjusted date.</p>  # noqa: E501

        :param valid_until: The valid_until of this AccountConsentData.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and valid_until is None:
            raise ValueError("Invalid value for `valid_until`, must not be `None`")  # noqa: E501

        self._valid_until = valid_until

    @property
    def frequency_per_day(self):
        """Gets the frequency_per_day of this AccountConsentData.  # noqa: E501

        <p>This field indicates the requested maximum frequency for an access without PSU involvement per day.<br />For a one-off access, this attribute is set to \"1\".</p>  <p>The frequency needs to be greater equal to one.</p>  # noqa: E501

        :return: The frequency_per_day of this AccountConsentData.  # noqa: E501
        :rtype: int
        """
        return self._frequency_per_day

    @frequency_per_day.setter
    def frequency_per_day(self, frequency_per_day):
        """Sets the frequency_per_day of this AccountConsentData.

        <p>This field indicates the requested maximum frequency for an access without PSU involvement per day.<br />For a one-off access, this attribute is set to \"1\".</p>  <p>The frequency needs to be greater equal to one.</p>  # noqa: E501

        :param frequency_per_day: The frequency_per_day of this AccountConsentData.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and frequency_per_day is None:
            raise ValueError("Invalid value for `frequency_per_day`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                frequency_per_day is not None and frequency_per_day > 4):  # noqa: E501
            raise ValueError("Invalid value for `frequency_per_day`, must be a value less than or equal to `4`")  # noqa: E501
        if (self._configuration.client_side_validation and
                frequency_per_day is not None and frequency_per_day < 1):  # noqa: E501
            raise ValueError("Invalid value for `frequency_per_day`, must be a value greater than or equal to `1`")  # noqa: E501

        self._frequency_per_day = frequency_per_day

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
        if issubclass(AccountConsentData, dict):
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
        if not isinstance(other, AccountConsentData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountConsentData):
            return True

        return self.to_dict() != other.to_dict()
