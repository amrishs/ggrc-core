__author__ = 'Ambarish Sakhare'


import json
import requests
from tests.ggrc import TestCase
from tests.ggrc.api_helper import Api
import string
import random
from faker import Factory

class ObjectCreation(TestCase):

    def __init__(self):
        self.api = Api()

    def title_generator(self):
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

    def faker(self):
        return Factory.create()

    def ProgramObject(self, payload=None, headers=None, host=None, custom_attribute_definitions=[], custom_attributes={}, _transient={}, contact=None, title=None, private=False, description='', secondary_contact=None, notes='', url='', reference_url='', slug='', start_date='', end_date='', status='Draft',context=None, provisional_id='provisional_2961500', **kwargs):

        #self.api.set_user(name='David Graham', email='david.graham@test.com') # sets the given user  otherwise default user is used

        request_url= "/api/programs"

        if host:
            request_url = host+request_url
            my_request = requests
        else:
            my_request = self.api.tc # this refers to the current instance of test client

        if not title:
            title = self.title_generator()

        #get the current user id and send it via contact field below

        if not contact:
            contact = {"id":358,"href":"/api/people/758","type":"Person"}

        if not headers:
            headers={'Accept':'application/json', "X-Requested-By": "gGRC", 'Content-type': 'application/json'}

        if not payload:
            payload = {"program":{"custom_attributes":custom_attributes,"_transient":_transient,"contact":contact,"kind":"Directive","_transient:title":None,"title":title,"private":private,"description":description,"secondary_contact":None,"notes":notes,"url":url,"reference_url":reference_url,"slug":slug,"start_date":start_date,"end_date":end_date,"status":status,"context":context,"provisional_id":provisional_id}}

        response = my_request.post(request_url, data=json.dumps(payload), headers=headers)

        if host:
            assert response.status_code == 200
            parsed_data = json.loads(response.content)
            json_data = response.content

        else:
            assert response.status_code == 201
            parsed_data = json.loads(response.data)
            json_data = response.data
            print json_data

        return json_data, parsed_data


    def WorkflowObject(self, payload=None, headers=None, host=None, **kwargs):
        title = self.title_generator()
        my_request = self.api.tc # this refers to the current instance of test client
        request_url= "/api/workflows"
        if host:
            request_url = host+request_url
            my_request = requests
        if not payload:
            payload = {"workflow":{"custom_attribute_definitions":[],"custom_attributes":{},"_transient":{},"title":title,"description":"","frequency":"one_time","notify_on_change":False,"task_group_title":"Task Group 1","notify_custom_message":"","owners":None,"context":None,"provisional_id":"provisional_9186593"}}
        if not headers:
            headers= {'Accept':'application/json', "X-Requested-By": "gGRC", 'Content-type': 'application/json'}
        response = my_request.post(request_url, data=json.dumps(payload), headers=headers)
        if host:
            assert response.status_code == 200
            parsed_data = json.loads(response.content)
            json_data = response.content
        else:
            assert response.status_code == 201
            parsed_data = json.loads(response.data)
            json_data = response.data

        return json_data, parsed_data

    def PolicyObject(self, payload=None, headers=None, host=None, **kwargs):
        title = self.title_generator()
        my_request = self.api.tc # this refers to the current instance of test client
        request_url_policies= "/api/policies"
        user_id = '358'
        if host:
            request_url_policies = host+request_url_policies
            my_request = requests
        if not payload:
            payload = {"policy":{"kind":"","owners":[],"custom_attribute_definitions":[],"custom_attributes":{},"_transient":{},"contact":{"id":user_id,"href":"/api/people/"+user_id,"type":"Person"},"_transient:title":None,"title":title,"description":"","secondary_contact":None,"notes":"","url":"","reference_url":"","slug":"","start_date":"","end_date":"","status":"Draft","context":None,"provisional_id":"provisional_4595116"}}
        if not headers:
            headers={'Accept':'application/json', "X-Requested-By": "gGRC", 'Content-type': 'application/json'}
        response1 = my_request.post(request_url_policies, data=json.dumps(payload), headers=headers)
        if host:
            assert response1.status_code == 200
            parsed_data1 = json.loads(response1.content)
            json_data1 = response1.content
        else:
            assert response1.status_code == 201
            parsed_data1 = json.loads(response1.data)
            json_data1 = response1.data
            print json_data1

        ''' Call sequence: Object owner   '''

        policy_id =parsed_data1['policy']['id']
        user_id= parsed_data1['policy']['modified_by']['id']
        request_url_objectowners= "/api/object_owners"
        if host:
            request_url = host+request_url_objectowners
        payload2 = {"object_owner":{"context":None,"ownable":{"id":policy_id,"href":"/api/policies/"+str(policy_id),"type":"Policy"},"person":{"id":user_id,"href":"/api/people/"+str(user_id),"type":"Person"},"provisional_id":"provisional_3386275"}}
        response2 = my_request.post(request_url_objectowners, data=json.dumps(payload2), headers=headers)
        if host:
            assert response2.status_code == 200
            parsed_data2 = json.loads(response1.content)
            json_data2 = response1.content
        else:
            assert response1.status_code == 201
            parsed_data2 = json.loads(response1.data)
            json_data2 = response1.data
            print json_data2

        return json_data1, parsed_data1, json_data2, parsed_data2

    def GetTasks(self, payload=None, headers=None, host=None, **kwargs):
        my_request = self.api.tc
        request_url= "/api/cycle_task_group_object_tasks"
        if host:
            request_url = host+request_url
            my_request = requests
        if not headers:
            headers={'Accept':'application/json', "X-Requested-By": "gGRC", 'Content-type': 'application/json'}
        response = my_request.get(request_url, headers=headers)
        if host:
            assert response.status_code == 200
            parsed_data = json.loads(response.content)
            json_data = response.content

        else:
            assert response.status_code == 201
            parsed_data = json.loads(response.data)
            json_data = response.data

        return json_data, parsed_data

    def GetProgramObject(self, id=id, payload=None, headers=None, host=None, **kwargs):
        my_request = self.api.tc
        request_url= "/api/programs"
        if host:
            request_url = host+request_url+"/"+str(id)
            my_request = requests
        else:
            request_url = request_url+"/"+str(id)
        if not headers:
            headers={'Accept':'application/json', "X-Requested-By": "gGRC", 'Content-type': 'application/json'}
        response = my_request.get(request_url, headers=headers)
        if host:
            assert response.status_code == 200
            parsed_data = json.loads(response.content)
            json_data = response.content
            headers = response.headers

        else:
            assert response.status_code == 200
            parsed_data = json.loads(response.data)
            json_data = response.data
            headers = response.headers

        return json_data, parsed_data, headers

    def MapProgramPolicy(self, payload=None, headers=None, host=None, **kwargs):

        if host:
            json_response, parsed_response = self.ProgramObject(host="http://localhost:8080")
        else:
            json_response, parsed_response = self.ProgramObject()

        program_id = parsed_response['program']['id']

        if host:
            json_response1, parsed_response1, json_response2, parsed_response2 = self.PolicyObject(host="http://localhost:8080")
        else:
            json_response1, parsed_response1, json_response2, parsed_response2 = self.PolicyObject()

        policy_id = parsed_response1['policy']['id']

        my_request = self.api.tc
        request_url="/api/program_directives"
        if host:
            request_url = host+request_url
            my_request = requests
        if not payload:
            payload = {"program_directive":{"directive":{"id":policy_id,"href":"/api/policies/"+str(policy_id),"type":"Policy"},"program":{"id":program_id,"href":"/api/programs/"+str(program_id),"type":"Program"},"context":{},"provisional_id":"provisional_8890298"}}
        if not headers:
            headers={'Accept':'application/json', "X-Requested-By": "gGRC", 'Content-type': 'application/json'}
        response = my_request.post(request_url, data=json.dumps(payload), headers=headers)
        if host:
            assert response.status_code == 200
            parsed_data = json.loads(response.content)
            json_data = response.content
        else:
            assert response.status_code == 201
            parsed_data = json.loads(response.data)
            json_data = response.data

        ''' Call sequence: Object owner   '''

        return json_data, parsed_data

    def UserObject(self, payload=None, headers=None, host=None, **kwargs):
        title = self.title_generator()
        email = self.faker().email()
        name = self.faker().name()
        my_request = self.api.tc # this refers to the current instance of test client
        request_url= "/api/people"
        if host:
            request_url = host+request_url
            my_request = requests
        if not payload:
            payload = {"person":{"name":title,"email":email,"contact":None,"owners":None,"custom_attribute_definitions":[],"custom_attributes":{},"_transient":{},"is_enabled":True,"company":"","context":None,"provisional_id":"provisional_5325266"}}
        if not headers:
            headers= {'Accept':'application/json', "X-Requested-By": "gGRC", 'Content-type': 'application/json'}
        response = my_request.post(request_url, data=json.dumps(payload), headers=headers)
        if host:
            assert response.status_code == 200
            parsed_data = json.loads(response.content)
            json_data = response.content
        else:
            assert response.status_code == 201
            parsed_data = json.loads(response.data)
            json_data = response.data

        person_id =parsed_data['person']['id']
        person_email =parsed_data['person']['email']
        person_name =parsed_data['person']['name']

        if not host:
            self.api.set_user(name=name, email=email)
        else:
            pass

        return person_id, person_name, person_email

    def EditProgramObject(self, id=None, payload=None, headers=None, host=None, custom_attributes=None, contact=None, title=None, private=None, description=None, secondary_contact=None, notes=None, url=None, reference_url=None, slug=None, start_date=None, end_date=None, status=None, **kwargs):

        if not id:
            print "Program id is not given for editing the program. Quitting..... "
            return

        json_data, parsed_data, headers = self.GetProgramObject(id=id)

        print headers

        custom_attributes = {} if (custom_attributes is None and 'custom_attributes' not in parsed_data.get('program', {})) else parsed_data['program']['custom_attributes']
        contact= {} if (contact is None and 'contact' not in parsed_data.get('contact', {})) else parsed_data['program']['contact']
        title= '' if (not title and not parsed_data['program']['title']) else parsed_data['program']['title']
        private= False if (not private and not parsed_data['program']['private']) else parsed_data['program']['private']
        description = '' if (not description and not parsed_data['program']['description']) else parsed_data['program']['description']
        secondary_contact= '' if (not secondary_contact and not parsed_data['program']['secondary_contact']) else parsed_data['program']['secondary_contact']
        notes= '' if (not notes and not parsed_data['program']['notes']) else parsed_data['program']['notes']
        url= '' if (not url and not parsed_data['program']['url']) else parsed_data['program']['url']
        reference_url= '' if (not reference_url and not parsed_data['program']['reference_url']) else parsed_data['program']['reference_url']
        slug= '' if (not slug and not parsed_data['program']['slug']) else parsed_data['program']['slug']
        start_date= '' if (not start_date and not parsed_data['program']['start_date']) else parsed_data['program']['start_date']
        end_date= '' if (not end_date and not parsed_data['program']['end_date']) else parsed_data['program']['end_date']
        status= 'Draft' if (not status and not parsed_data['program']['status']) else parsed_data['program']['status']

        request_url= "/api/programs/"+str(id)

        if host:
            request_url = host+request_url
            my_request = requests
        else:
            my_request = self.api.tc # this refers to the current instance of test client

        if not headers:
            headers={'Accept':'application/json', "X-Requested-By": "gGRC", 'Content-type': 'application/json', 'If-Match': headers['Etag'], 'If-Unmodified-Since': headers['Last-Modified']}

        if not payload:
            payload = {"program":{"custom_attributes":custom_attributes, "contact":contact, "title":title, "private":private, "description":description, "secondary_contact":secondary_contact,"notes":notes,"url":url,"reference_url":reference_url,"slug":slug,"start_date":start_date,"end_date":end_date,"status":status}}

            print payload

        response = my_request.put(request_url, data=json.dumps(payload), headers=headers)


        if host:
            #assert response.status_code == 200
            parsed_data = json.loads(response.content)
            json_data = response.content

        else:
            print response.status_code
            #assert response.status_code == 201
            parsed_data = json.loads(response.data)
            json_data = response.data
            print json_data

        return json_data, parsed_data





