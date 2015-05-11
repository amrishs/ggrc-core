__author__ = 'Ambarish Sakhare'

import json
from tests.ggrc import TestCase
from tests.ggrc.api_helper import Api
import string
import random
from faker import Factory
from tests.api_framework.object_creation import ObjectCreation



class TestObjectCreation(TestCase):

    def title_generator(self):
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

    def faker(self):
        return Factory.create()


    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_create_program(self):
        create = ObjectCreation()
        json_response, parsed_response = create.ProgramObject(host="http://localhost:8080")
        print json_response

    def test_create_workflow(self):
        create = ObjectCreation()
        json_response, parsed_response = create.WorkflowObject(host="http://localhost:8080")
        print json_response

    def test_create_policy(self):
        create = ObjectCreation()
        json_response1, json_response2, parsed_response1, parsed_response2 = create.PolicyObject(host="http://localhost:8080")
        print json_response1, "/n", json_response2

    def testGetTasksPage(self):
        create = ObjectCreation()
        json_response, parsed_response = create.GetTasks(host="http://localhost:8080")
        print json_response