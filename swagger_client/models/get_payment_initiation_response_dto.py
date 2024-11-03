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


class GetPaymentInitiationResponseDto(object):
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
        'transaction_status': 'str',
        'end_to_end_identification': 'str',
        'debtor_account': 'AccountReferenceDto',
        'instructed_amount': 'EuroAmountFieldDto',
        'creditor_account': 'AccountReferenceDto',
        'creditor_agent': 'str',
        'creditor_name': 'str',
        'creditor_address': 'AddressDto',
        'remittance_information_unstructured': 'str',
        'remittance_information_structured': 'RemittanceDto',
        'urgent': 'bool',
        'requested_execution_date': 'str',
        'frequency': 'str',
        'start_date': 'str',
        'end_date': 'str'
    }

    attribute_map = {
        'transaction_status': 'transactionStatus',
        'end_to_end_identification': 'endToEndIdentification',
        'debtor_account': 'debtorAccount',
        'instructed_amount': 'instructedAmount',
        'creditor_account': 'creditorAccount',
        'creditor_agent': 'creditorAgent',
        'creditor_name': 'creditorName',
        'creditor_address': 'creditorAddress',
        'remittance_information_unstructured': 'remittanceInformationUnstructured',
        'remittance_information_structured': 'remittanceInformationStructured',
        'urgent': 'urgent',
        'requested_execution_date': 'requestedExecutionDate',
        'frequency': 'frequency',
        'start_date': 'startDate',
        'end_date': 'endDate'
    }

    def __init__(self, transaction_status=None, end_to_end_identification=None, debtor_account=None, instructed_amount=None, creditor_account=None, creditor_agent=None, creditor_name=None, creditor_address=None, remittance_information_unstructured=None, remittance_information_structured=None, urgent=None, requested_execution_date=None, frequency=None, start_date=None, end_date=None, _configuration=None):  # noqa: E501
        """GetPaymentInitiationResponseDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transaction_status = None
        self._end_to_end_identification = None
        self._debtor_account = None
        self._instructed_amount = None
        self._creditor_account = None
        self._creditor_agent = None
        self._creditor_name = None
        self._creditor_address = None
        self._remittance_information_unstructured = None
        self._remittance_information_structured = None
        self._urgent = None
        self._requested_execution_date = None
        self._frequency = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if transaction_status is not None:
            self.transaction_status = transaction_status
        if end_to_end_identification is not None:
            self.end_to_end_identification = end_to_end_identification
        self.debtor_account = debtor_account
        self.instructed_amount = instructed_amount
        self.creditor_account = creditor_account
        if creditor_agent is not None:
            self.creditor_agent = creditor_agent
        self.creditor_name = creditor_name
        if creditor_address is not None:
            self.creditor_address = creditor_address
        if remittance_information_unstructured is not None:
            self.remittance_information_unstructured = remittance_information_unstructured
        if remittance_information_structured is not None:
            self.remittance_information_structured = remittance_information_structured
        if urgent is not None:
            self.urgent = urgent
        if requested_execution_date is not None:
            self.requested_execution_date = requested_execution_date
        if frequency is not None:
            self.frequency = frequency
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def transaction_status(self):
        """Gets the transaction_status of this GetPaymentInitiationResponseDto.  # noqa: E501

        The transaction status of the payment initiation.  # noqa: E501

        :return: The transaction_status of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status):
        """Sets the transaction_status of this GetPaymentInitiationResponseDto.

        The transaction status of the payment initiation.  # noqa: E501

        :param transaction_status: The transaction_status of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["PDNG", "RCVD", "PATC", "ACTC", "ACWC", "CANC", "RJCT", "PCAN"]  # noqa: E501
        if (self._configuration.client_side_validation and
                transaction_status not in allowed_values):
            raise ValueError(
                "Invalid value for `transaction_status` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_status, allowed_values)
            )

        self._transaction_status = transaction_status

    @property
    def end_to_end_identification(self):
        """Gets the end_to_end_identification of this GetPaymentInitiationResponseDto.  # noqa: E501


        :return: The end_to_end_identification of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._end_to_end_identification

    @end_to_end_identification.setter
    def end_to_end_identification(self, end_to_end_identification):
        """Sets the end_to_end_identification of this GetPaymentInitiationResponseDto.


        :param end_to_end_identification: The end_to_end_identification of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                end_to_end_identification is not None and len(end_to_end_identification) > 35):
            raise ValueError("Invalid value for `end_to_end_identification`, length must be less than or equal to `35`")  # noqa: E501

        self._end_to_end_identification = end_to_end_identification

    @property
    def debtor_account(self):
        """Gets the debtor_account of this GetPaymentInitiationResponseDto.  # noqa: E501


        :return: The debtor_account of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: AccountReferenceDto
        """
        return self._debtor_account

    @debtor_account.setter
    def debtor_account(self, debtor_account):
        """Sets the debtor_account of this GetPaymentInitiationResponseDto.


        :param debtor_account: The debtor_account of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: AccountReferenceDto
        """
        if self._configuration.client_side_validation and debtor_account is None:
            raise ValueError("Invalid value for `debtor_account`, must not be `None`")  # noqa: E501

        self._debtor_account = debtor_account

    @property
    def instructed_amount(self):
        """Gets the instructed_amount of this GetPaymentInitiationResponseDto.  # noqa: E501


        :return: The instructed_amount of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: EuroAmountFieldDto
        """
        return self._instructed_amount

    @instructed_amount.setter
    def instructed_amount(self, instructed_amount):
        """Sets the instructed_amount of this GetPaymentInitiationResponseDto.


        :param instructed_amount: The instructed_amount of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: EuroAmountFieldDto
        """
        if self._configuration.client_side_validation and instructed_amount is None:
            raise ValueError("Invalid value for `instructed_amount`, must not be `None`")  # noqa: E501

        self._instructed_amount = instructed_amount

    @property
    def creditor_account(self):
        """Gets the creditor_account of this GetPaymentInitiationResponseDto.  # noqa: E501


        :return: The creditor_account of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: AccountReferenceDto
        """
        return self._creditor_account

    @creditor_account.setter
    def creditor_account(self, creditor_account):
        """Sets the creditor_account of this GetPaymentInitiationResponseDto.


        :param creditor_account: The creditor_account of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: AccountReferenceDto
        """
        if self._configuration.client_side_validation and creditor_account is None:
            raise ValueError("Invalid value for `creditor_account`, must not be `None`")  # noqa: E501

        self._creditor_account = creditor_account

    @property
    def creditor_agent(self):
        """Gets the creditor_agent of this GetPaymentInitiationResponseDto.  # noqa: E501

        BICFI  # noqa: E501

        :return: The creditor_agent of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._creditor_agent

    @creditor_agent.setter
    def creditor_agent(self, creditor_agent):
        """Sets the creditor_agent of this GetPaymentInitiationResponseDto.

        BICFI  # noqa: E501

        :param creditor_agent: The creditor_agent of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: str
        """

        self._creditor_agent = creditor_agent

    @property
    def creditor_name(self):
        """Gets the creditor_name of this GetPaymentInitiationResponseDto.  # noqa: E501

        Creditor Name  # noqa: E501

        :return: The creditor_name of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._creditor_name

    @creditor_name.setter
    def creditor_name(self, creditor_name):
        """Sets the creditor_name of this GetPaymentInitiationResponseDto.

        Creditor Name  # noqa: E501

        :param creditor_name: The creditor_name of this GetPaymentInitiationResponseDto.  # noqa: E501
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
        """Gets the creditor_address of this GetPaymentInitiationResponseDto.  # noqa: E501


        :return: The creditor_address of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: AddressDto
        """
        return self._creditor_address

    @creditor_address.setter
    def creditor_address(self, creditor_address):
        """Sets the creditor_address of this GetPaymentInitiationResponseDto.


        :param creditor_address: The creditor_address of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: AddressDto
        """

        self._creditor_address = creditor_address

    @property
    def remittance_information_unstructured(self):
        """Gets the remittance_information_unstructured of this GetPaymentInitiationResponseDto.  # noqa: E501

        Unstructured remittance information  # noqa: E501

        :return: The remittance_information_unstructured of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._remittance_information_unstructured

    @remittance_information_unstructured.setter
    def remittance_information_unstructured(self, remittance_information_unstructured):
        """Sets the remittance_information_unstructured of this GetPaymentInitiationResponseDto.

        Unstructured remittance information  # noqa: E501

        :param remittance_information_unstructured: The remittance_information_unstructured of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                remittance_information_unstructured is not None and len(remittance_information_unstructured) > 140):
            raise ValueError("Invalid value for `remittance_information_unstructured`, length must be less than or equal to `140`")  # noqa: E501

        self._remittance_information_unstructured = remittance_information_unstructured

    @property
    def remittance_information_structured(self):
        """Gets the remittance_information_structured of this GetPaymentInitiationResponseDto.  # noqa: E501

        Not allowed for urgent payments  # noqa: E501

        :return: The remittance_information_structured of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: RemittanceDto
        """
        return self._remittance_information_structured

    @remittance_information_structured.setter
    def remittance_information_structured(self, remittance_information_structured):
        """Sets the remittance_information_structured of this GetPaymentInitiationResponseDto.

        Not allowed for urgent payments  # noqa: E501

        :param remittance_information_structured: The remittance_information_structured of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: RemittanceDto
        """

        self._remittance_information_structured = remittance_information_structured

    @property
    def urgent(self):
        """Gets the urgent of this GetPaymentInitiationResponseDto.  # noqa: E501

        Can not be used when creating a recurring payment  # noqa: E501

        :return: The urgent of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: bool
        """
        return self._urgent

    @urgent.setter
    def urgent(self, urgent):
        """Sets the urgent of this GetPaymentInitiationResponseDto.

        Can not be used when creating a recurring payment  # noqa: E501

        :param urgent: The urgent of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: bool
        """

        self._urgent = urgent

    @property
    def requested_execution_date(self):
        """Gets the requested_execution_date of this GetPaymentInitiationResponseDto.  # noqa: E501

        ISO Date yyyy-MM-dd, Business day, not-holiday. Required for non-periodic payments. Not allowed for periodic payments  # noqa: E501

        :return: The requested_execution_date of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._requested_execution_date

    @requested_execution_date.setter
    def requested_execution_date(self, requested_execution_date):
        """Sets the requested_execution_date of this GetPaymentInitiationResponseDto.

        ISO Date yyyy-MM-dd, Business day, not-holiday. Required for non-periodic payments. Not allowed for periodic payments  # noqa: E501

        :param requested_execution_date: The requested_execution_date of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: str
        """

        self._requested_execution_date = requested_execution_date

    @property
    def frequency(self):
        """Gets the frequency of this GetPaymentInitiationResponseDto.  # noqa: E501

        Required for periodic payments, not allowed for other payments  # noqa: E501

        :return: The frequency of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this GetPaymentInitiationResponseDto.

        Required for periodic payments, not allowed for other payments  # noqa: E501

        :param frequency: The frequency of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: str
        """

        self._frequency = frequency

    @property
    def start_date(self):
        """Gets the start_date of this GetPaymentInitiationResponseDto.  # noqa: E501

        Required for periodic payments, not allowed for other payments  # noqa: E501

        :return: The start_date of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this GetPaymentInitiationResponseDto.

        Required for periodic payments, not allowed for other payments  # noqa: E501

        :param start_date: The start_date of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this GetPaymentInitiationResponseDto.  # noqa: E501

        Optional for periodic payments, not allowed for other payments  # noqa: E501

        :return: The end_date of this GetPaymentInitiationResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this GetPaymentInitiationResponseDto.

        Optional for periodic payments, not allowed for other payments  # noqa: E501

        :param end_date: The end_date of this GetPaymentInitiationResponseDto.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

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
        if issubclass(GetPaymentInitiationResponseDto, dict):
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
        if not isinstance(other, GetPaymentInitiationResponseDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetPaymentInitiationResponseDto):
            return True

        return self.to_dict() != other.to_dict()
