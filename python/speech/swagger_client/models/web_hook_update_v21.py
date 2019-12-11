# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: crservice@microsoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WebHookUpdateV21(object):
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
        'configuration': 'WebHookConfiguration',
        'active': 'bool',
        'events': 'list[str]',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'configuration': 'configuration',
        'active': 'active',
        'events': 'events',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, configuration=None, active=None, events=None, name=None, description=None):  # noqa: E501
        """WebHookUpdateV21 - a model defined in Swagger"""  # noqa: E501

        self._configuration = None
        self._active = None
        self._events = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.configuration = configuration
        self.active = active
        self.events = events
        self.name = name
        if description is not None:
            self.description = description

    @property
    def configuration(self):
        """Gets the configuration of this WebHookUpdateV21.  # noqa: E501

        The configuration of the web hook registration.                If the property secret is omitted or contains an empty string in a POST or PATCH request,  no signature hash will be calculated.                When retrieving web hook registration information from the service, the secret is always omitted  # noqa: E501

        :return: The configuration of this WebHookUpdateV21.  # noqa: E501
        :rtype: WebHookConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this WebHookUpdateV21.

        The configuration of the web hook registration.                If the property secret is omitted or contains an empty string in a POST or PATCH request,  no signature hash will be calculated.                When retrieving web hook registration information from the service, the secret is always omitted  # noqa: E501

        :param configuration: The configuration of this WebHookUpdateV21.  # noqa: E501
        :type: WebHookConfiguration
        """
        if configuration is None:
            raise ValueError("Invalid value for `configuration`, must not be `None`")  # noqa: E501

        self._configuration = configuration

    @property
    def active(self):
        """Gets the active of this WebHookUpdateV21.  # noqa: E501

        A value indicating whether callbacks to the registered URL are made or not  # noqa: E501

        :return: The active of this WebHookUpdateV21.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this WebHookUpdateV21.

        A value indicating whether callbacks to the registered URL are made or not  # noqa: E501

        :param active: The active of this WebHookUpdateV21.  # noqa: E501
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def events(self):
        """Gets the events of this WebHookUpdateV21.  # noqa: E501

        A value indicating the webhook event kinds  # noqa: E501

        :return: The events of this WebHookUpdateV21.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this WebHookUpdateV21.

        A value indicating the webhook event kinds  # noqa: E501

        :param events: The events of this WebHookUpdateV21.  # noqa: E501
        :type: list[str]
        """
        if events is None:
            raise ValueError("Invalid value for `events`, must not be `None`")  # noqa: E501
        allowed_values = ["DatasetCreation", "DatasetImportStart", "DatasetImportCompletion", "DatasetDeletion", "ModelCreation", "ModelStart", "ModelCompletion", "ModelDeletion", "AccuracyTestCreation", "AccuracyTestStart", "AccuracyTestCompletion", "AccuracyTestDeletion", "TranscriptionCreation", "TranscriptionStart", "TranscriptionCompletion", "TranscriptionDeletion", "EndpointCreation", "EndpointReplacement", "EndpointDeploymentStart", "EndpointDeploymentCompletion", "EndpointDeletion", "DataCollectionCreation", "DataCollectionStart", "DataCollectionCompletion", "DataCollectionDeletion", "DataCollectionAudioLogsDeletion", "Ping"]  # noqa: E501
        if not set(events).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `events` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(events) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._events = events

    @property
    def name(self):
        """Gets the name of this WebHookUpdateV21.  # noqa: E501

        The name of the object  # noqa: E501

        :return: The name of this WebHookUpdateV21.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebHookUpdateV21.

        The name of the object  # noqa: E501

        :param name: The name of this WebHookUpdateV21.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this WebHookUpdateV21.  # noqa: E501

        The description of the object  # noqa: E501

        :return: The description of this WebHookUpdateV21.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WebHookUpdateV21.

        The description of the object  # noqa: E501

        :param description: The description of this WebHookUpdateV21.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(WebHookUpdateV21, dict):
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
        if not isinstance(other, WebHookUpdateV21):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
