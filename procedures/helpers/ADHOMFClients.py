from __future__ import annotations

from omf_sample_library_preview.Models.OMFMessageAction import OMFMessageAction
from omf_sample_library_preview.Models.OMFMessageType import OMFMessageType
from omf_sample_library_preview.Client import OMFClient

from omf_sample_library_preview.Models.OMFContainer import OMFContainer
from omf_sample_library_preview.Models.OMFData import OMFData
from omf_sample_library_preview.Models.OMFLinkData import OMFLinkData
from omf_sample_library_preview.Models.OMFMessageAction import OMFMessageAction
from omf_sample_library_preview.Models.OMFMessageType import OMFMessageType
from omf_sample_library_preview.Models.OMFType import OMFType

import requests


class ADHOMFClients(object):
    """Handles communication with ADH OMF Endpoint."""

    def __init__(
        self):
        self.__adhOMFClients: list[OMFClient] = []
        

    @property
    def Clients(self) -> list[OMFClient]:
        """
        Gets the base url
        :return:
        """
        return self.__adhOMFClients

    def addClient(
        self,
        client: OMFClient,
    ) -> requests.Response:
        """
        """
        self.__adhOMFClients.append(client)
    
    
    def omfRequest(
        self,
        message_type: OMFMessageType,
        action: OMFMessageAction,
        omf_message: list[OMFType | OMFContainer | OMFData | OMFLinkData],
    ) -> requests.Response:
        """
        Base OMF request function
        :param message_type: OMF message type
        :param action: OMF action
        :param omf_message: OMF message
        :return: Http response
        """
        for client in self.__adhOMFClients:
            client.omfRequest
    
