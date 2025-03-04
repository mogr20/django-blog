from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'a',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
        
    def test_form_name_is_invalid(self):
        """ Test for name field"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
            })
        self.assertFalse(form.is_valid(), msg="Name was not provided, but the form is valid")
        
    def test_form_email_is_invalid(self):
        """ Test for name field"""
        form = CollaborateForm({
            'name': 'Roger',
            'email': '',
            'message': 'Hello!'
            })
        self.assertFalse(form.is_valid(), msg="Email was not provided, but the form is valid")
        
    def test_form_message_is_invalid(self):
        """ Test for name field"""
        form = CollaborateForm({
            'name': 'Roger',
            'email': 'test@test.com',
            'message': ''
            })
        self.assertFalse(form.is_valid(), msg="Message was not provided, but the form is valid")