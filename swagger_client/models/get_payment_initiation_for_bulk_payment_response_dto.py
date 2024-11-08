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


class GetPaymentInitiationForBulkPaymentResponseDto(object):
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
        'account_number': 'str',
        'payment_information_id': 'str',
        'payment_method': 'str',
        'batch_booking': 'bool',
        'number_of_transactions': 'int',
        'total_amount': 'float',
        'requested_execution_date': 'str',
        'local_instrument': 'str',
        'service_level_code': 'str',
        'instruction_priority': 'str',
        'category_purpose_code': 'str'
    }

    attribute_map = {
        'transaction_status': 'transactionStatus',
        'account_number': 'accountNumber',
        'payment_information_id': 'paymentInformationId',
        'payment_method': 'paymentMethod',
        'batch_booking': 'batchBooking',
        'number_of_transactions': 'numberOfTransactions',
        'total_amount': 'totalAmount',
        'requested_execution_date': 'requestedExecutionDate',
        'local_instrument': 'localInstrument',
        'service_level_code': 'serviceLevelCode',
        'instruction_priority': 'instructionPriority',
        'category_purpose_code': 'categoryPurposeCode'
    }

    def __init__(self, transaction_status=None, account_number=None, payment_information_id=None, payment_method=None, batch_booking=None, number_of_transactions=None, total_amount=None, requested_execution_date=None, local_instrument=None, service_level_code=None, instruction_priority=None, category_purpose_code=None, _configuration=None):  # noqa: E501
        """GetPaymentInitiationForBulkPaymentResponseDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transaction_status = None
        self._account_number = None
        self._payment_information_id = None
        self._payment_method = None
        self._batch_booking = None
        self._number_of_transactions = None
        self._total_amount = None
        self._requested_execution_date = None
        self._local_instrument = None
        self._service_level_code = None
        self._instruction_priority = None
        self._category_purpose_code = None
        self.discriminator = None

        if transaction_status is not None:
            self.transaction_status = transaction_status
        if account_number is not None:
            self.account_number = account_number
        if payment_information_id is not None:
            self.payment_information_id = payment_information_id
        if payment_method is not None:
            self.payment_method = payment_method
        if batch_booking is not None:
            self.batch_booking = batch_booking
        if number_of_transactions is not None:
            self.number_of_transactions = number_of_transactions
        if total_amount is not None:
            self.total_amount = total_amount
        if requested_execution_date is not None:
            self.requested_execution_date = requested_execution_date
        if local_instrument is not None:
            self.local_instrument = local_instrument
        if service_level_code is not None:
            self.service_level_code = service_level_code
        if instruction_priority is not None:
            self.instruction_priority = instruction_priority
        if category_purpose_code is not None:
            self.category_purpose_code = category_purpose_code

    @property
    def transaction_status(self):
        """Gets the transaction_status of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501

        The transaction status of the payment initiation.  # noqa: E501

        :return: The transaction_status of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status):
        """Sets the transaction_status of this GetPaymentInitiationForBulkPaymentResponseDto.

        The transaction status of the payment initiation.  # noqa: E501

        :param transaction_status: The transaction_status of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
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
    def account_number(self):
        """Gets the account_number of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501


        :return: The account_number of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this GetPaymentInitiationForBulkPaymentResponseDto.


        :param account_number: The account_number of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def payment_information_id(self):
        """Gets the payment_information_id of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501


        :return: The payment_information_id of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._payment_information_id

    @payment_information_id.setter
    def payment_information_id(self, payment_information_id):
        """Sets the payment_information_id of this GetPaymentInitiationForBulkPaymentResponseDto.


        :param payment_information_id: The payment_information_id of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :type: str
        """

        self._payment_information_id = payment_information_id

    @property
    def payment_method(self):
        """Gets the payment_method of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501


        :return: The payment_method of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this GetPaymentInitiationForBulkPaymentResponseDto.


        :param payment_method: The payment_method of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def batch_booking(self):
        """Gets the batch_booking of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501


        :return: The batch_booking of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :rtype: bool
        """
        return self._batch_booking

    @batch_booking.setter
    def batch_booking(self, batch_booking):
        """Sets the batch_booking of this GetPaymentInitiationForBulkPaymentResponseDto.


        :param batch_booking: The batch_booking of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :type: bool
        """

        self._batch_booking = batch_booking

    @property
    def number_of_transactions(self):
        """Gets the number_of_transactions of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501


        :return: The number_of_transactions of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :rtype: int
        """
        return self._number_of_transactions

    @number_of_transactions.setter
    def number_of_transactions(self, number_of_transactions):
        """Sets the number_of_transactions of this GetPaymentInitiationForBulkPaymentResponseDto.


        :param number_of_transactions: The number_of_transactions of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :type: int
        """

        self._number_of_transactions = number_of_transactions

    @property
    def total_amount(self):
        """Gets the total_amount of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501


        :return: The total_amount of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this GetPaymentInitiationForBulkPaymentResponseDto.


        :param total_amount: The total_amount of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def requested_execution_date(self):
        """Gets the requested_execution_date of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501


        :return: The requested_execution_date of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._requested_execution_date

    @requested_execution_date.setter
    def requested_execution_date(self, requested_execution_date):
        """Sets the requested_execution_date of this GetPaymentInitiationForBulkPaymentResponseDto.


        :param requested_execution_date: The requested_execution_date of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :type: str
        """

        self._requested_execution_date = requested_execution_date

    @property
    def local_instrument(self):
        """Gets the local_instrument of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501


        :return: The local_instrument of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._local_instrument

    @local_instrument.setter
    def local_instrument(self, local_instrument):
        """Sets the local_instrument of this GetPaymentInitiationForBulkPaymentResponseDto.


        :param local_instrument: The local_instrument of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :type: str
        """

        self._local_instrument = local_instrument

    @property
    def service_level_code(self):
        """Gets the service_level_code of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501


        :return: The service_level_code of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._service_level_code

    @service_level_code.setter
    def service_level_code(self, service_level_code):
        """Sets the service_level_code of this GetPaymentInitiationForBulkPaymentResponseDto.


        :param service_level_code: The service_level_code of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :type: str
        """

        self._service_level_code = service_level_code

    @property
    def instruction_priority(self):
        """Gets the instruction_priority of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501


        :return: The instruction_priority of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._instruction_priority

    @instruction_priority.setter
    def instruction_priority(self, instruction_priority):
        """Sets the instruction_priority of this GetPaymentInitiationForBulkPaymentResponseDto.


        :param instruction_priority: The instruction_priority of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :type: str
        """

        self._instruction_priority = instruction_priority

    @property
    def category_purpose_code(self):
        """Gets the category_purpose_code of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501


        :return: The category_purpose_code of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._category_purpose_code

    @category_purpose_code.setter
    def category_purpose_code(self, category_purpose_code):
        """Sets the category_purpose_code of this GetPaymentInitiationForBulkPaymentResponseDto.


        :param category_purpose_code: The category_purpose_code of this GetPaymentInitiationForBulkPaymentResponseDto.  # noqa: E501
        :type: str
        """

        self._category_purpose_code = category_purpose_code

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
        if issubclass(GetPaymentInitiationForBulkPaymentResponseDto, dict):
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
        if not isinstance(other, GetPaymentInitiationForBulkPaymentResponseDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetPaymentInitiationForBulkPaymentResponseDto):
            return True

        return self.to_dict() != other.to_dict()
