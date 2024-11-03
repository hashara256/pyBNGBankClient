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


class CrossBorderPaymentDto(object):
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
        'end_to_end_identification': 'str',
        'debtor_account': 'AccountReferenceDto',
        'instructed_amount': 'AmountFieldDto',
        'creditor_account': 'CrossBorderAccountReferenceDto',
        'creditor_agent': 'str',
        'creditor_name': 'str',
        'creditor_address': 'AddressDto',
        'charge_bearer': 'str',
        'remittance_information_unstructured': 'str',
        'requested_execution_date': 'str',
        'bankcode': 'str',
        'contra_bank_name': 'str',
        'contra_bank_city': 'str',
        'contra_bank_country_code': 'str',
        'urgent': 'bool'
    }

    attribute_map = {
        'end_to_end_identification': 'endToEndIdentification',
        'debtor_account': 'debtorAccount',
        'instructed_amount': 'instructedAmount',
        'creditor_account': 'creditorAccount',
        'creditor_agent': 'creditorAgent',
        'creditor_name': 'creditorName',
        'creditor_address': 'creditorAddress',
        'charge_bearer': 'chargeBearer',
        'remittance_information_unstructured': 'remittanceInformationUnstructured',
        'requested_execution_date': 'requestedExecutionDate',
        'bankcode': 'bankcode',
        'contra_bank_name': 'contraBankName',
        'contra_bank_city': 'contraBankCity',
        'contra_bank_country_code': 'contraBankCountryCode',
        'urgent': 'urgent'
    }

    def __init__(self, end_to_end_identification=None, debtor_account=None, instructed_amount=None, creditor_account=None, creditor_agent=None, creditor_name=None, creditor_address=None, charge_bearer=None, remittance_information_unstructured=None, requested_execution_date=None, bankcode=None, contra_bank_name=None, contra_bank_city=None, contra_bank_country_code=None, urgent=None, _configuration=None):  # noqa: E501
        """CrossBorderPaymentDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_to_end_identification = None
        self._debtor_account = None
        self._instructed_amount = None
        self._creditor_account = None
        self._creditor_agent = None
        self._creditor_name = None
        self._creditor_address = None
        self._charge_bearer = None
        self._remittance_information_unstructured = None
        self._requested_execution_date = None
        self._bankcode = None
        self._contra_bank_name = None
        self._contra_bank_city = None
        self._contra_bank_country_code = None
        self._urgent = None
        self.discriminator = None

        if end_to_end_identification is not None:
            self.end_to_end_identification = end_to_end_identification
        self.debtor_account = debtor_account
        self.instructed_amount = instructed_amount
        self.creditor_account = creditor_account
        if creditor_agent is not None:
            self.creditor_agent = creditor_agent
        self.creditor_name = creditor_name
        self.creditor_address = creditor_address
        self.charge_bearer = charge_bearer
        if remittance_information_unstructured is not None:
            self.remittance_information_unstructured = remittance_information_unstructured
        self.requested_execution_date = requested_execution_date
        if bankcode is not None:
            self.bankcode = bankcode
        self.contra_bank_name = contra_bank_name
        self.contra_bank_city = contra_bank_city
        self.contra_bank_country_code = contra_bank_country_code
        self.urgent = urgent

    @property
    def end_to_end_identification(self):
        """Gets the end_to_end_identification of this CrossBorderPaymentDto.  # noqa: E501


        :return: The end_to_end_identification of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: str
        """
        return self._end_to_end_identification

    @end_to_end_identification.setter
    def end_to_end_identification(self, end_to_end_identification):
        """Sets the end_to_end_identification of this CrossBorderPaymentDto.


        :param end_to_end_identification: The end_to_end_identification of this CrossBorderPaymentDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                end_to_end_identification is not None and len(end_to_end_identification) > 35):
            raise ValueError("Invalid value for `end_to_end_identification`, length must be less than or equal to `35`")  # noqa: E501

        self._end_to_end_identification = end_to_end_identification

    @property
    def debtor_account(self):
        """Gets the debtor_account of this CrossBorderPaymentDto.  # noqa: E501


        :return: The debtor_account of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: AccountReferenceDto
        """
        return self._debtor_account

    @debtor_account.setter
    def debtor_account(self, debtor_account):
        """Sets the debtor_account of this CrossBorderPaymentDto.


        :param debtor_account: The debtor_account of this CrossBorderPaymentDto.  # noqa: E501
        :type: AccountReferenceDto
        """
        if self._configuration.client_side_validation and debtor_account is None:
            raise ValueError("Invalid value for `debtor_account`, must not be `None`")  # noqa: E501

        self._debtor_account = debtor_account

    @property
    def instructed_amount(self):
        """Gets the instructed_amount of this CrossBorderPaymentDto.  # noqa: E501


        :return: The instructed_amount of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: AmountFieldDto
        """
        return self._instructed_amount

    @instructed_amount.setter
    def instructed_amount(self, instructed_amount):
        """Sets the instructed_amount of this CrossBorderPaymentDto.


        :param instructed_amount: The instructed_amount of this CrossBorderPaymentDto.  # noqa: E501
        :type: AmountFieldDto
        """
        if self._configuration.client_side_validation and instructed_amount is None:
            raise ValueError("Invalid value for `instructed_amount`, must not be `None`")  # noqa: E501

        self._instructed_amount = instructed_amount

    @property
    def creditor_account(self):
        """Gets the creditor_account of this CrossBorderPaymentDto.  # noqa: E501


        :return: The creditor_account of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: CrossBorderAccountReferenceDto
        """
        return self._creditor_account

    @creditor_account.setter
    def creditor_account(self, creditor_account):
        """Sets the creditor_account of this CrossBorderPaymentDto.


        :param creditor_account: The creditor_account of this CrossBorderPaymentDto.  # noqa: E501
        :type: CrossBorderAccountReferenceDto
        """
        if self._configuration.client_side_validation and creditor_account is None:
            raise ValueError("Invalid value for `creditor_account`, must not be `None`")  # noqa: E501

        self._creditor_account = creditor_account

    @property
    def creditor_agent(self):
        """Gets the creditor_agent of this CrossBorderPaymentDto.  # noqa: E501

        BICFI required if no bankcode  # noqa: E501

        :return: The creditor_agent of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: str
        """
        return self._creditor_agent

    @creditor_agent.setter
    def creditor_agent(self, creditor_agent):
        """Sets the creditor_agent of this CrossBorderPaymentDto.

        BICFI required if no bankcode  # noqa: E501

        :param creditor_agent: The creditor_agent of this CrossBorderPaymentDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                creditor_agent is not None and len(creditor_agent) > 11):
            raise ValueError("Invalid value for `creditor_agent`, length must be less than or equal to `11`")  # noqa: E501

        self._creditor_agent = creditor_agent

    @property
    def creditor_name(self):
        """Gets the creditor_name of this CrossBorderPaymentDto.  # noqa: E501

        Creditor Name  # noqa: E501

        :return: The creditor_name of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: str
        """
        return self._creditor_name

    @creditor_name.setter
    def creditor_name(self, creditor_name):
        """Sets the creditor_name of this CrossBorderPaymentDto.

        Creditor Name  # noqa: E501

        :param creditor_name: The creditor_name of this CrossBorderPaymentDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and creditor_name is None:
            raise ValueError("Invalid value for `creditor_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                creditor_name is not None and len(creditor_name) > 140):
            raise ValueError("Invalid value for `creditor_name`, length must be less than or equal to `140`")  # noqa: E501

        self._creditor_name = creditor_name

    @property
    def creditor_address(self):
        """Gets the creditor_address of this CrossBorderPaymentDto.  # noqa: E501


        :return: The creditor_address of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: AddressDto
        """
        return self._creditor_address

    @creditor_address.setter
    def creditor_address(self, creditor_address):
        """Sets the creditor_address of this CrossBorderPaymentDto.


        :param creditor_address: The creditor_address of this CrossBorderPaymentDto.  # noqa: E501
        :type: AddressDto
        """
        if self._configuration.client_side_validation and creditor_address is None:
            raise ValueError("Invalid value for `creditor_address`, must not be `None`")  # noqa: E501

        self._creditor_address = creditor_address

    @property
    def charge_bearer(self):
        """Gets the charge_bearer of this CrossBorderPaymentDto.  # noqa: E501

        The charge bearer of the payment transaction (for this environment not all charge bearer types might be enabled).  Supported values are:<ul><li>DEBT, CRED, SHAR and SLEV</li></ul>  # noqa: E501

        :return: The charge_bearer of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: str
        """
        return self._charge_bearer

    @charge_bearer.setter
    def charge_bearer(self, charge_bearer):
        """Sets the charge_bearer of this CrossBorderPaymentDto.

        The charge bearer of the payment transaction (for this environment not all charge bearer types might be enabled).  Supported values are:<ul><li>DEBT, CRED, SHAR and SLEV</li></ul>  # noqa: E501

        :param charge_bearer: The charge_bearer of this CrossBorderPaymentDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and charge_bearer is None:
            raise ValueError("Invalid value for `charge_bearer`, must not be `None`")  # noqa: E501

        self._charge_bearer = charge_bearer

    @property
    def remittance_information_unstructured(self):
        """Gets the remittance_information_unstructured of this CrossBorderPaymentDto.  # noqa: E501

        Unstructured remittance information, the description. For urgent Cross-Border payments, the max length is 128  # noqa: E501

        :return: The remittance_information_unstructured of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: str
        """
        return self._remittance_information_unstructured

    @remittance_information_unstructured.setter
    def remittance_information_unstructured(self, remittance_information_unstructured):
        """Sets the remittance_information_unstructured of this CrossBorderPaymentDto.

        Unstructured remittance information, the description. For urgent Cross-Border payments, the max length is 128  # noqa: E501

        :param remittance_information_unstructured: The remittance_information_unstructured of this CrossBorderPaymentDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                remittance_information_unstructured is not None and len(remittance_information_unstructured) > 140):
            raise ValueError("Invalid value for `remittance_information_unstructured`, length must be less than or equal to `140`")  # noqa: E501

        self._remittance_information_unstructured = remittance_information_unstructured

    @property
    def requested_execution_date(self):
        """Gets the requested_execution_date of this CrossBorderPaymentDto.  # noqa: E501

        ISO Date yyyy-MM-dd, Business day, not-holiday.  # noqa: E501

        :return: The requested_execution_date of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: str
        """
        return self._requested_execution_date

    @requested_execution_date.setter
    def requested_execution_date(self, requested_execution_date):
        """Sets the requested_execution_date of this CrossBorderPaymentDto.

        ISO Date yyyy-MM-dd, Business day, not-holiday.  # noqa: E501

        :param requested_execution_date: The requested_execution_date of this CrossBorderPaymentDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and requested_execution_date is None:
            raise ValueError("Invalid value for `requested_execution_date`, must not be `None`")  # noqa: E501

        self._requested_execution_date = requested_execution_date

    @property
    def bankcode(self):
        """Gets the bankcode of this CrossBorderPaymentDto.  # noqa: E501

        Bankcode required if no creditorAgent (BICFI)  # noqa: E501

        :return: The bankcode of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: str
        """
        return self._bankcode

    @bankcode.setter
    def bankcode(self, bankcode):
        """Sets the bankcode of this CrossBorderPaymentDto.

        Bankcode required if no creditorAgent (BICFI)  # noqa: E501

        :param bankcode: The bankcode of this CrossBorderPaymentDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                bankcode is not None and len(bankcode) > 20):
            raise ValueError("Invalid value for `bankcode`, length must be less than or equal to `20`")  # noqa: E501

        self._bankcode = bankcode

    @property
    def contra_bank_name(self):
        """Gets the contra_bank_name of this CrossBorderPaymentDto.  # noqa: E501


        :return: The contra_bank_name of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: str
        """
        return self._contra_bank_name

    @contra_bank_name.setter
    def contra_bank_name(self, contra_bank_name):
        """Sets the contra_bank_name of this CrossBorderPaymentDto.


        :param contra_bank_name: The contra_bank_name of this CrossBorderPaymentDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and contra_bank_name is None:
            raise ValueError("Invalid value for `contra_bank_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                contra_bank_name is not None and len(contra_bank_name) > 70):
            raise ValueError("Invalid value for `contra_bank_name`, length must be less than or equal to `70`")  # noqa: E501

        self._contra_bank_name = contra_bank_name

    @property
    def contra_bank_city(self):
        """Gets the contra_bank_city of this CrossBorderPaymentDto.  # noqa: E501


        :return: The contra_bank_city of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: str
        """
        return self._contra_bank_city

    @contra_bank_city.setter
    def contra_bank_city(self, contra_bank_city):
        """Sets the contra_bank_city of this CrossBorderPaymentDto.


        :param contra_bank_city: The contra_bank_city of this CrossBorderPaymentDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and contra_bank_city is None:
            raise ValueError("Invalid value for `contra_bank_city`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                contra_bank_city is not None and len(contra_bank_city) > 70):
            raise ValueError("Invalid value for `contra_bank_city`, length must be less than or equal to `70`")  # noqa: E501

        self._contra_bank_city = contra_bank_city

    @property
    def contra_bank_country_code(self):
        """Gets the contra_bank_country_code of this CrossBorderPaymentDto.  # noqa: E501

        ContraBankCountryCode required and a valid country  # noqa: E501

        :return: The contra_bank_country_code of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: str
        """
        return self._contra_bank_country_code

    @contra_bank_country_code.setter
    def contra_bank_country_code(self, contra_bank_country_code):
        """Sets the contra_bank_country_code of this CrossBorderPaymentDto.

        ContraBankCountryCode required and a valid country  # noqa: E501

        :param contra_bank_country_code: The contra_bank_country_code of this CrossBorderPaymentDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and contra_bank_country_code is None:
            raise ValueError("Invalid value for `contra_bank_country_code`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                contra_bank_country_code is not None and len(contra_bank_country_code) > 2):
            raise ValueError("Invalid value for `contra_bank_country_code`, length must be less than or equal to `2`")  # noqa: E501

        self._contra_bank_country_code = contra_bank_country_code

    @property
    def urgent(self):
        """Gets the urgent of this CrossBorderPaymentDto.  # noqa: E501


        :return: The urgent of this CrossBorderPaymentDto.  # noqa: E501
        :rtype: bool
        """
        return self._urgent

    @urgent.setter
    def urgent(self, urgent):
        """Sets the urgent of this CrossBorderPaymentDto.


        :param urgent: The urgent of this CrossBorderPaymentDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and urgent is None:
            raise ValueError("Invalid value for `urgent`, must not be `None`")  # noqa: E501

        self._urgent = urgent

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
        if issubclass(CrossBorderPaymentDto, dict):
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
        if not isinstance(other, CrossBorderPaymentDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossBorderPaymentDto):
            return True

        return self.to_dict() != other.to_dict()