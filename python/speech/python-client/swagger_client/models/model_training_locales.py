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


class ModelTrainingLocales(object):
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
        '_none': 'list[str]',
        'acoustic': 'list[str]',
        'language': 'list[str]',
        'acoustic_and_language': 'list[str]',
        'custom_voice': 'list[str]',
        'sentiment': 'list[str]',
        'language_identification': 'list[str]',
        'diarization': 'list[str]',
        'keyword': 'list[str]'
    }

    attribute_map = {
        '_none': 'None',
        'acoustic': 'Acoustic',
        'language': 'Language',
        'acoustic_and_language': 'AcousticAndLanguage',
        'custom_voice': 'CustomVoice',
        'sentiment': 'Sentiment',
        'language_identification': 'LanguageIdentification',
        'diarization': 'Diarization',
        'keyword': 'Keyword'
    }

    def __init__(self, _none=None, acoustic=None, language=None, acoustic_and_language=None, custom_voice=None, sentiment=None, language_identification=None, diarization=None, keyword=None):  # noqa: E501
        """ModelTrainingLocales - a model defined in Swagger"""  # noqa: E501

        self.__none = None
        self._acoustic = None
        self._language = None
        self._acoustic_and_language = None
        self._custom_voice = None
        self._sentiment = None
        self._language_identification = None
        self._diarization = None
        self._keyword = None
        self.discriminator = None

        if _none is not None:
            self._none = _none
        if acoustic is not None:
            self.acoustic = acoustic
        if language is not None:
            self.language = language
        if acoustic_and_language is not None:
            self.acoustic_and_language = acoustic_and_language
        if custom_voice is not None:
            self.custom_voice = custom_voice
        if sentiment is not None:
            self.sentiment = sentiment
        if language_identification is not None:
            self.language_identification = language_identification
        if diarization is not None:
            self.diarization = diarization
        if keyword is not None:
            self.keyword = keyword

    @property
    def _none(self):
        """Gets the _none of this ModelTrainingLocales.  # noqa: E501


        :return: The _none of this ModelTrainingLocales.  # noqa: E501
        :rtype: list[str]
        """
        return self.__none

    @_none.setter
    def _none(self, _none):
        """Sets the _none of this ModelTrainingLocales.


        :param _none: The _none of this ModelTrainingLocales.  # noqa: E501
        :type: list[str]
        """

        self.__none = _none

    @property
    def acoustic(self):
        """Gets the acoustic of this ModelTrainingLocales.  # noqa: E501


        :return: The acoustic of this ModelTrainingLocales.  # noqa: E501
        :rtype: list[str]
        """
        return self._acoustic

    @acoustic.setter
    def acoustic(self, acoustic):
        """Sets the acoustic of this ModelTrainingLocales.


        :param acoustic: The acoustic of this ModelTrainingLocales.  # noqa: E501
        :type: list[str]
        """

        self._acoustic = acoustic

    @property
    def language(self):
        """Gets the language of this ModelTrainingLocales.  # noqa: E501


        :return: The language of this ModelTrainingLocales.  # noqa: E501
        :rtype: list[str]
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ModelTrainingLocales.


        :param language: The language of this ModelTrainingLocales.  # noqa: E501
        :type: list[str]
        """

        self._language = language

    @property
    def acoustic_and_language(self):
        """Gets the acoustic_and_language of this ModelTrainingLocales.  # noqa: E501


        :return: The acoustic_and_language of this ModelTrainingLocales.  # noqa: E501
        :rtype: list[str]
        """
        return self._acoustic_and_language

    @acoustic_and_language.setter
    def acoustic_and_language(self, acoustic_and_language):
        """Sets the acoustic_and_language of this ModelTrainingLocales.


        :param acoustic_and_language: The acoustic_and_language of this ModelTrainingLocales.  # noqa: E501
        :type: list[str]
        """

        self._acoustic_and_language = acoustic_and_language

    @property
    def custom_voice(self):
        """Gets the custom_voice of this ModelTrainingLocales.  # noqa: E501


        :return: The custom_voice of this ModelTrainingLocales.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_voice

    @custom_voice.setter
    def custom_voice(self, custom_voice):
        """Sets the custom_voice of this ModelTrainingLocales.


        :param custom_voice: The custom_voice of this ModelTrainingLocales.  # noqa: E501
        :type: list[str]
        """

        self._custom_voice = custom_voice

    @property
    def sentiment(self):
        """Gets the sentiment of this ModelTrainingLocales.  # noqa: E501


        :return: The sentiment of this ModelTrainingLocales.  # noqa: E501
        :rtype: list[str]
        """
        return self._sentiment

    @sentiment.setter
    def sentiment(self, sentiment):
        """Sets the sentiment of this ModelTrainingLocales.


        :param sentiment: The sentiment of this ModelTrainingLocales.  # noqa: E501
        :type: list[str]
        """

        self._sentiment = sentiment

    @property
    def language_identification(self):
        """Gets the language_identification of this ModelTrainingLocales.  # noqa: E501


        :return: The language_identification of this ModelTrainingLocales.  # noqa: E501
        :rtype: list[str]
        """
        return self._language_identification

    @language_identification.setter
    def language_identification(self, language_identification):
        """Sets the language_identification of this ModelTrainingLocales.


        :param language_identification: The language_identification of this ModelTrainingLocales.  # noqa: E501
        :type: list[str]
        """

        self._language_identification = language_identification

    @property
    def diarization(self):
        """Gets the diarization of this ModelTrainingLocales.  # noqa: E501


        :return: The diarization of this ModelTrainingLocales.  # noqa: E501
        :rtype: list[str]
        """
        return self._diarization

    @diarization.setter
    def diarization(self, diarization):
        """Sets the diarization of this ModelTrainingLocales.


        :param diarization: The diarization of this ModelTrainingLocales.  # noqa: E501
        :type: list[str]
        """

        self._diarization = diarization

    @property
    def keyword(self):
        """Gets the keyword of this ModelTrainingLocales.  # noqa: E501


        :return: The keyword of this ModelTrainingLocales.  # noqa: E501
        :rtype: list[str]
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this ModelTrainingLocales.


        :param keyword: The keyword of this ModelTrainingLocales.  # noqa: E501
        :type: list[str]
        """

        self._keyword = keyword

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
        if issubclass(ModelTrainingLocales, dict):
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
        if not isinstance(other, ModelTrainingLocales):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
