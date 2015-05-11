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
        self.api = Api()

    def tearDown(self):
        self.api.tc.get("/logout")

    def test_smoke(self): # used as a simple smoke test for debugging code
        email = self.faker().email()
        print email
        name = self.faker().name()
        print name
        print 'success'

    def test_create_program(self):
        create = ObjectCreation()
        json_response, parsed_response = create.ProgramObject()
        print json_response

    def test_create_workflow(self):
        create = ObjectCreation()
        json_response, parsed_response = create.WorkflowObject()
        print json_response

    def test_create_policy(self):
        create = ObjectCreation()
        json_response1, json_response2, parsed_response1, parsed_response2 = create.PolicyObject()
        print json_response1, "/n", json_response2

    def test_get_tasks_page(self):
        create = ObjectCreation()
        json_response, parsed_response = create.GetTasks()
        print json_response

    def test_mapping(self):
        create = ObjectCreation()
        json_response, parsed_response = create.MapProgramPolicy()
        print json_response

    def test_create_user(self):
        create = ObjectCreation()
        id, name, emails = create.UserObject()
        print id, name, emails

    def test_get_program(self):
        create = ObjectCreation()
        json_response, parsed_response, headers = create.GetProgramObject(id=45)
        print json_response

    def test_jira_core_1744(self):
        create = ObjectCreation()
        #json_response, parsed_response = create.CreateProgramObject()
        #program_id = parsed_response['program']['id']
        json_response, parsed_response = create.EditProgramObject(id=45, private=True)



