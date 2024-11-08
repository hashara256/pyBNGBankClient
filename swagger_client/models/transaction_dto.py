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


class TransactionDto(object):
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
        'transaction_id': 'str',
        'entry_reference': 'str',
        'end_to_end_id': 'str',
        'mandate_id': 'str',
        'check_id': 'str',
        'creditor_id': 'str',
        'booking_date': 'str',
        'value_date': 'str',
        'transaction_amount': 'AmountFieldDto',
        'currency_exchange': 'ReportExchangeRateDto',
        'creditor_name': 'str',
        'creditor_account': 'AccountReferenceDto',
        'ultimate_creditor': 'str',
        'debtor_name': 'str',
        'debtor_account': 'AccountReferenceDto',
        'ultimate_debtor': 'str',
        'remittance_information_unstructured': 'str',
        'remittance_information_structured': 'str',
        'purpose_code': 'str',
        'bank_transaction_code': 'str',
        'proprietary_bank_transaction_code': 'str',
        'links': 'TransactionResponseLinksDto'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'entry_reference': 'entryReference',
        'end_to_end_id': 'endToEndId',
        'mandate_id': 'mandateId',
        'check_id': 'checkId',
        'creditor_id': 'creditorId',
        'booking_date': 'bookingDate',
        'value_date': 'valueDate',
        'transaction_amount': 'transactionAmount',
        'currency_exchange': 'currencyExchange',
        'creditor_name': 'creditorName',
        'creditor_account': 'creditorAccount',
        'ultimate_creditor': 'ultimateCreditor',
        'debtor_name': 'debtorName',
        'debtor_account': 'debtorAccount',
        'ultimate_debtor': 'ultimateDebtor',
        'remittance_information_unstructured': 'remittanceInformationUnstructured',
        'remittance_information_structured': 'remittanceInformationStructured',
        'purpose_code': 'purposeCode',
        'bank_transaction_code': 'bankTransactionCode',
        'proprietary_bank_transaction_code': 'proprietaryBankTransactionCode',
        'links': '_links'
    }

    def __init__(self, transaction_id=None, entry_reference=None, end_to_end_id=None, mandate_id=None, check_id=None, creditor_id=None, booking_date=None, value_date=None, transaction_amount=None, currency_exchange=None, creditor_name=None, creditor_account=None, ultimate_creditor=None, debtor_name=None, debtor_account=None, ultimate_debtor=None, remittance_information_unstructured=None, remittance_information_structured=None, purpose_code=None, bank_transaction_code=None, proprietary_bank_transaction_code=None, links=None, _configuration=None):  # noqa: E501
        """TransactionDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transaction_id = None
        self._entry_reference = None
        self._end_to_end_id = None
        self._mandate_id = None
        self._check_id = None
        self._creditor_id = None
        self._booking_date = None
        self._value_date = None
        self._transaction_amount = None
        self._currency_exchange = None
        self._creditor_name = None
        self._creditor_account = None
        self._ultimate_creditor = None
        self._debtor_name = None
        self._debtor_account = None
        self._ultimate_debtor = None
        self._remittance_information_unstructured = None
        self._remittance_information_structured = None
        self._purpose_code = None
        self._bank_transaction_code = None
        self._proprietary_bank_transaction_code = None
        self._links = None
        self.discriminator = None

        if transaction_id is not None:
            self.transaction_id = transaction_id
        if entry_reference is not None:
            self.entry_reference = entry_reference
        if end_to_end_id is not None:
            self.end_to_end_id = end_to_end_id
        if mandate_id is not None:
            self.mandate_id = mandate_id
        if check_id is not None:
            self.check_id = check_id
        if creditor_id is not None:
            self.creditor_id = creditor_id
        if booking_date is not None:
            self.booking_date = booking_date
        if value_date is not None:
            self.value_date = value_date
        if transaction_amount is not None:
            self.transaction_amount = transaction_amount
        if currency_exchange is not None:
            self.currency_exchange = currency_exchange
        if creditor_name is not None:
            self.creditor_name = creditor_name
        if creditor_account is not None:
            self.creditor_account = creditor_account
        if ultimate_creditor is not None:
            self.ultimate_creditor = ultimate_creditor
        if debtor_name is not None:
            self.debtor_name = debtor_name
        if debtor_account is not None:
            self.debtor_account = debtor_account
        if ultimate_debtor is not None:
            self.ultimate_debtor = ultimate_debtor
        if remittance_information_unstructured is not None:
            self.remittance_information_unstructured = remittance_information_unstructured
        if remittance_information_structured is not None:
            self.remittance_information_structured = remittance_information_structured
        if purpose_code is not None:
            self.purpose_code = purpose_code
        if bank_transaction_code is not None:
            self.bank_transaction_code = bank_transaction_code
        if proprietary_bank_transaction_code is not None:
            self.proprietary_bank_transaction_code = proprietary_bank_transaction_code
        if links is not None:
            self.links = links

    @property
    def transaction_id(self):
        """Gets the transaction_id of this TransactionDto.  # noqa: E501

        This shall be filled, if addressable resource are created by the ASPSP on the /accounts endpoint.  # noqa: E501

        :return: The transaction_id of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this TransactionDto.

        This shall be filled, if addressable resource are created by the ASPSP on the /accounts endpoint.  # noqa: E501

        :param transaction_id: The transaction_id of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def entry_reference(self):
        """Gets the entry_reference of this TransactionDto.  # noqa: E501

        Is the identification of the transaction as used e.g. for reference for deltafunction on application level. The same identification as for example used within camt.05x messages.  # noqa: E501

        :return: The entry_reference of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._entry_reference

    @entry_reference.setter
    def entry_reference(self, entry_reference):
        """Sets the entry_reference of this TransactionDto.

        Is the identification of the transaction as used e.g. for reference for deltafunction on application level. The same identification as for example used within camt.05x messages.  # noqa: E501

        :param entry_reference: The entry_reference of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._entry_reference = entry_reference

    @property
    def end_to_end_id(self):
        """Gets the end_to_end_id of this TransactionDto.  # noqa: E501

        Unique end to end identity.  # noqa: E501

        :return: The end_to_end_id of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._end_to_end_id

    @end_to_end_id.setter
    def end_to_end_id(self, end_to_end_id):
        """Sets the end_to_end_id of this TransactionDto.

        Unique end to end identity.  # noqa: E501

        :param end_to_end_id: The end_to_end_id of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._end_to_end_id = end_to_end_id

    @property
    def mandate_id(self):
        """Gets the mandate_id of this TransactionDto.  # noqa: E501

        Identification of Mandates, e.g. a SEPA Mandate ID  # noqa: E501

        :return: The mandate_id of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._mandate_id

    @mandate_id.setter
    def mandate_id(self, mandate_id):
        """Sets the mandate_id of this TransactionDto.

        Identification of Mandates, e.g. a SEPA Mandate ID  # noqa: E501

        :param mandate_id: The mandate_id of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._mandate_id = mandate_id

    @property
    def check_id(self):
        """Gets the check_id of this TransactionDto.  # noqa: E501

        Identification of a Cheque  # noqa: E501

        :return: The check_id of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._check_id

    @check_id.setter
    def check_id(self, check_id):
        """Sets the check_id of this TransactionDto.

        Identification of a Cheque  # noqa: E501

        :param check_id: The check_id of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._check_id = check_id

    @property
    def creditor_id(self):
        """Gets the creditor_id of this TransactionDto.  # noqa: E501

        Identification of Creditors, e.g. a SEPA Creditor ID  # noqa: E501

        :return: The creditor_id of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._creditor_id

    @creditor_id.setter
    def creditor_id(self, creditor_id):
        """Sets the creditor_id of this TransactionDto.

        Identification of Creditors, e.g. a SEPA Creditor ID  # noqa: E501

        :param creditor_id: The creditor_id of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._creditor_id = creditor_id

    @property
    def booking_date(self):
        """Gets the booking_date of this TransactionDto.  # noqa: E501

        The Date when an entry is posted to an account on the ASPSPs books.  # noqa: E501

        :return: The booking_date of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._booking_date

    @booking_date.setter
    def booking_date(self, booking_date):
        """Sets the booking_date of this TransactionDto.

        The Date when an entry is posted to an account on the ASPSPs books.  # noqa: E501

        :param booking_date: The booking_date of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._booking_date = booking_date

    @property
    def value_date(self):
        """Gets the value_date of this TransactionDto.  # noqa: E501

        The Date at which assets become available to the account owner in case of a credit.  # noqa: E501

        :return: The value_date of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._value_date

    @value_date.setter
    def value_date(self, value_date):
        """Sets the value_date of this TransactionDto.

        The Date at which assets become available to the account owner in case of a credit.  # noqa: E501

        :param value_date: The value_date of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._value_date = value_date

    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this TransactionDto.  # noqa: E501

        The amount of the transaction as billed to the account.  # noqa: E501

        :return: The transaction_amount of this TransactionDto.  # noqa: E501
        :rtype: AmountFieldDto
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this TransactionDto.

        The amount of the transaction as billed to the account.  # noqa: E501

        :param transaction_amount: The transaction_amount of this TransactionDto.  # noqa: E501
        :type: AmountFieldDto
        """

        self._transaction_amount = transaction_amount

    @property
    def currency_exchange(self):
        """Gets the currency_exchange of this TransactionDto.  # noqa: E501


        :return: The currency_exchange of this TransactionDto.  # noqa: E501
        :rtype: ReportExchangeRateDto
        """
        return self._currency_exchange

    @currency_exchange.setter
    def currency_exchange(self, currency_exchange):
        """Sets the currency_exchange of this TransactionDto.


        :param currency_exchange: The currency_exchange of this TransactionDto.  # noqa: E501
        :type: ReportExchangeRateDto
        """

        self._currency_exchange = currency_exchange

    @property
    def creditor_name(self):
        """Gets the creditor_name of this TransactionDto.  # noqa: E501

        Name of the creditor if a \"Debited\" transaction.  # noqa: E501

        :return: The creditor_name of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._creditor_name

    @creditor_name.setter
    def creditor_name(self, creditor_name):
        """Sets the creditor_name of this TransactionDto.

        Name of the creditor if a \"Debited\" transaction.  # noqa: E501

        :param creditor_name: The creditor_name of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._creditor_name = creditor_name

    @property
    def creditor_account(self):
        """Gets the creditor_account of this TransactionDto.  # noqa: E501


        :return: The creditor_account of this TransactionDto.  # noqa: E501
        :rtype: AccountReferenceDto
        """
        return self._creditor_account

    @creditor_account.setter
    def creditor_account(self, creditor_account):
        """Sets the creditor_account of this TransactionDto.


        :param creditor_account: The creditor_account of this TransactionDto.  # noqa: E501
        :type: AccountReferenceDto
        """

        self._creditor_account = creditor_account

    @property
    def ultimate_creditor(self):
        """Gets the ultimate_creditor of this TransactionDto.  # noqa: E501


        :return: The ultimate_creditor of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._ultimate_creditor

    @ultimate_creditor.setter
    def ultimate_creditor(self, ultimate_creditor):
        """Sets the ultimate_creditor of this TransactionDto.


        :param ultimate_creditor: The ultimate_creditor of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._ultimate_creditor = ultimate_creditor

    @property
    def debtor_name(self):
        """Gets the debtor_name of this TransactionDto.  # noqa: E501

        Name of the debtor if a \"Credited\" transaction.  # noqa: E501

        :return: The debtor_name of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._debtor_name

    @debtor_name.setter
    def debtor_name(self, debtor_name):
        """Sets the debtor_name of this TransactionDto.

        Name of the debtor if a \"Credited\" transaction.  # noqa: E501

        :param debtor_name: The debtor_name of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._debtor_name = debtor_name

    @property
    def debtor_account(self):
        """Gets the debtor_account of this TransactionDto.  # noqa: E501


        :return: The debtor_account of this TransactionDto.  # noqa: E501
        :rtype: AccountReferenceDto
        """
        return self._debtor_account

    @debtor_account.setter
    def debtor_account(self, debtor_account):
        """Sets the debtor_account of this TransactionDto.


        :param debtor_account: The debtor_account of this TransactionDto.  # noqa: E501
        :type: AccountReferenceDto
        """

        self._debtor_account = debtor_account

    @property
    def ultimate_debtor(self):
        """Gets the ultimate_debtor of this TransactionDto.  # noqa: E501


        :return: The ultimate_debtor of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._ultimate_debtor

    @ultimate_debtor.setter
    def ultimate_debtor(self, ultimate_debtor):
        """Sets the ultimate_debtor of this TransactionDto.


        :param ultimate_debtor: The ultimate_debtor of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._ultimate_debtor = ultimate_debtor

    @property
    def remittance_information_unstructured(self):
        """Gets the remittance_information_unstructured of this TransactionDto.  # noqa: E501


        :return: The remittance_information_unstructured of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._remittance_information_unstructured

    @remittance_information_unstructured.setter
    def remittance_information_unstructured(self, remittance_information_unstructured):
        """Sets the remittance_information_unstructured of this TransactionDto.


        :param remittance_information_unstructured: The remittance_information_unstructured of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._remittance_information_unstructured = remittance_information_unstructured

    @property
    def remittance_information_structured(self):
        """Gets the remittance_information_structured of this TransactionDto.  # noqa: E501

        Reference as contained in the structured remittance reference structure (without the surrounding XML structure).  # noqa: E501

        :return: The remittance_information_structured of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._remittance_information_structured

    @remittance_information_structured.setter
    def remittance_information_structured(self, remittance_information_structured):
        """Sets the remittance_information_structured of this TransactionDto.

        Reference as contained in the structured remittance reference structure (without the surrounding XML structure).  # noqa: E501

        :param remittance_information_structured: The remittance_information_structured of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._remittance_information_structured = remittance_information_structured

    @property
    def purpose_code(self):
        """Gets the purpose_code of this TransactionDto.  # noqa: E501


        :return: The purpose_code of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._purpose_code

    @purpose_code.setter
    def purpose_code(self, purpose_code):
        """Sets the purpose_code of this TransactionDto.


        :param purpose_code: The purpose_code of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._purpose_code = purpose_code

    @property
    def bank_transaction_code(self):
        """Gets the bank_transaction_code of this TransactionDto.  # noqa: E501

        Bank transaction code as used by the ASPSP and using the sub elements of this structured code defined by ISO20022  # noqa: E501

        :return: The bank_transaction_code of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._bank_transaction_code

    @bank_transaction_code.setter
    def bank_transaction_code(self, bank_transaction_code):
        """Sets the bank_transaction_code of this TransactionDto.

        Bank transaction code as used by the ASPSP and using the sub elements of this structured code defined by ISO20022  # noqa: E501

        :param bank_transaction_code: The bank_transaction_code of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._bank_transaction_code = bank_transaction_code

    @property
    def proprietary_bank_transaction_code(self):
        """Gets the proprietary_bank_transaction_code of this TransactionDto.  # noqa: E501

        proprietary bank transaction code as used within a community or within an ASPSP e.g. for MT94x based transaction reports  # noqa: E501

        :return: The proprietary_bank_transaction_code of this TransactionDto.  # noqa: E501
        :rtype: str
        """
        return self._proprietary_bank_transaction_code

    @proprietary_bank_transaction_code.setter
    def proprietary_bank_transaction_code(self, proprietary_bank_transaction_code):
        """Sets the proprietary_bank_transaction_code of this TransactionDto.

        proprietary bank transaction code as used within a community or within an ASPSP e.g. for MT94x based transaction reports  # noqa: E501

        :param proprietary_bank_transaction_code: The proprietary_bank_transaction_code of this TransactionDto.  # noqa: E501
        :type: str
        """

        self._proprietary_bank_transaction_code = proprietary_bank_transaction_code

    @property
    def links(self):
        """Gets the links of this TransactionDto.  # noqa: E501

        <p>Links to transaction details, which can be directly used for retrieving transaction details.</p>  # noqa: E501

        :return: The links of this TransactionDto.  # noqa: E501
        :rtype: TransactionResponseLinksDto
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TransactionDto.

        <p>Links to transaction details, which can be directly used for retrieving transaction details.</p>  # noqa: E501

        :param links: The links of this TransactionDto.  # noqa: E501
        :type: TransactionResponseLinksDto
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
        if issubclass(TransactionDto, dict):
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
        if not isinstance(other, TransactionDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionDto):
            return True

        return self.to_dict() != other.to_dict()
