"""
    py-ISPyB

    FastAPI Prototype  # noqa: E501

    The version of the OpenAPI document: 0.1alpha
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from mxcubecore.utils import pyispyb_clientfrom mxcubecore.utils.pyispyb_client.model.data_collection import DataCollection
from mxcubecore.utils.pyispyb_client.model.data_collection_meta_data import DataCollectionMetaData
from mxcubecore.utils.pyispyb_client.model.pyispyb_core_schemas_events_data_collection_group import PyispybCoreSchemasEventsDataCollectionGroup
from mxcubecore.utils.pyispyb_client.model.robot_action import RobotAction
globals()['DataCollection'] = DataCollection
globals()['DataCollectionMetaData'] = DataCollectionMetaData
globals()['PyispybCoreSchemasEventsDataCollectionGroup'] = PyispybCoreSchemasEventsDataCollectionGroup
globals()['RobotAction'] = RobotAction
from mxcubecore.utils.pyispyb_client.model.item import Item


class TestItem(unittest.TestCase):
    """Item unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testItem(self):
        """Test Item"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Item()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()