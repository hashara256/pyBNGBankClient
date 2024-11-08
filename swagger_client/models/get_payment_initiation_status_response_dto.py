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


class GetPaymentInitiationStatusResponseDto(object):
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
        'transaction_status': 'str'
    }

    attribute_map = {
        'transaction_status': 'transactionStatus'
    }

    def __init__(self, transaction_status=None, _configuration=None):  # noqa: E501
        """GetPaymentInitiationStatusResponseDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transaction_status = None
        self.discriminator = None

        if transaction_status is not None:
            self.transaction_status = transaction_status

    @property
    def transaction_status(self):
        """Gets the transaction_status of this GetPaymentInitiationStatusResponseDto.  # noqa: E501

        <p>The transaction status is filled with codes of the ISO 20022 data table:</p>  <ul>    <li>      <p>'ACCC': 'AcceptedSettlementCompleted' -Settlement on the creditor's account has been completed.</p>    </li>    <li>      <p>'ACCP': 'AcceptedCustomerProfile' -Preceding check of technical validation was successful.Customer profile check was also successful.</p>    </li>    <li>      <p>'ACSC': 'AcceptedSettlementCompleted' -Settlement on the debtor�s account has been completed.</p>      <p>        <strong>Usage:</strong> this can be used by the first agent to report to the debtor that the transaction has been completed.</p>      <p>        <strong>Warning:</strong> this status is provided for transaction status reasons, not for financial information.It can only be used after bilateral agreement.</p>    </li>    <li>      <p>'ACSP': 'AcceptedSettlementInProcess' -All preceding checks such as technical validation and customer profile were successful and therefore the payment initiation has been accepted for execution.</p>    </li>    <li>      <p>'ACTC': 'AcceptedTechnicalValidation' -Authentication and syntactical and semantical validation are successful.</p>    </li>    <li>      <p>'ACWC': 'AcceptedWithChange' -Instruction is accepted but a change will be made, such as date or remittance not sent.</p>    </li>    <li>      <p>'ACWP': 'AcceptedWithoutPosting' -Payment instruction included in the credit transfer is accepted without being posted to the creditor customer�s account.</p>    </li>    <li>      <p>'RCVD': 'Received' -Payment initiation has been received by the receiving agent.</p>    </li>    <li>      <p>'PDNG': 'Pending' -Payment initiation or individual transaction included in the payment initiation is pending.Further checks and status update will be performed.</p>    </li>    <li>      <p>'RJCT': 'Rejected' -Payment initiation or individual transaction included in the payment initiation has been rejected.</p>    </li>    <li>      <p>'CANC': 'Cancelled'Payment initiation has been cancelled before executionRemark: This code is still requested from ISO20022.</p>    </li>    <li>      <p>'ACFC': 'AcceptedFundsChecked' -Preceeding check of technical validation and customer profile was successful and an automatic funds check was positive .Remark: This code is still requested from ISO20022.</p>    </li>    <li>      <p>'PATC': 'PartiallyAcceptedTechnical'Correct The payment initiation needs multiple authentications, where some but not yet all have been performed. Syntactical and semantical validations are successful.Remark: This code is still requested from ISO20022.</p>    </li>  </ul>  # noqa: E501

        :return: The transaction_status of this GetPaymentInitiationStatusResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status):
        """Sets the transaction_status of this GetPaymentInitiationStatusResponseDto.

        <p>The transaction status is filled with codes of the ISO 20022 data table:</p>  <ul>    <li>      <p>'ACCC': 'AcceptedSettlementCompleted' -Settlement on the creditor's account has been completed.</p>    </li>    <li>      <p>'ACCP': 'AcceptedCustomerProfile' -Preceding check of technical validation was successful.Customer profile check was also successful.</p>    </li>    <li>      <p>'ACSC': 'AcceptedSettlementCompleted' -Settlement on the debtor�s account has been completed.</p>      <p>        <strong>Usage:</strong> this can be used by the first agent to report to the debtor that the transaction has been completed.</p>      <p>        <strong>Warning:</strong> this status is provided for transaction status reasons, not for financial information.It can only be used after bilateral agreement.</p>    </li>    <li>      <p>'ACSP': 'AcceptedSettlementInProcess' -All preceding checks such as technical validation and customer profile were successful and therefore the payment initiation has been accepted for execution.</p>    </li>    <li>      <p>'ACTC': 'AcceptedTechnicalValidation' -Authentication and syntactical and semantical validation are successful.</p>    </li>    <li>      <p>'ACWC': 'AcceptedWithChange' -Instruction is accepted but a change will be made, such as date or remittance not sent.</p>    </li>    <li>      <p>'ACWP': 'AcceptedWithoutPosting' -Payment instruction included in the credit transfer is accepted without being posted to the creditor customer�s account.</p>    </li>    <li>      <p>'RCVD': 'Received' -Payment initiation has been received by the receiving agent.</p>    </li>    <li>      <p>'PDNG': 'Pending' -Payment initiation or individual transaction included in the payment initiation is pending.Further checks and status update will be performed.</p>    </li>    <li>      <p>'RJCT': 'Rejected' -Payment initiation or individual transaction included in the payment initiation has been rejected.</p>    </li>    <li>      <p>'CANC': 'Cancelled'Payment initiation has been cancelled before executionRemark: This code is still requested from ISO20022.</p>    </li>    <li>      <p>'ACFC': 'AcceptedFundsChecked' -Preceeding check of technical validation and customer profile was successful and an automatic funds check was positive .Remark: This code is still requested from ISO20022.</p>    </li>    <li>      <p>'PATC': 'PartiallyAcceptedTechnical'Correct The payment initiation needs multiple authentications, where some but not yet all have been performed. Syntactical and semantical validations are successful.Remark: This code is still requested from ISO20022.</p>    </li>  </ul>  # noqa: E501

        :param transaction_status: The transaction_status of this GetPaymentInitiationStatusResponseDto.  # noqa: E501
        :type: str
        """

        self._transaction_status = transaction_status

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
        if issubclass(GetPaymentInitiationStatusResponseDto, dict):
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
        if not isinstance(other, GetPaymentInitiationStatusResponseDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetPaymentInitiationStatusResponseDto):
            return True

        return self.to_dict() != other.to_dict()
