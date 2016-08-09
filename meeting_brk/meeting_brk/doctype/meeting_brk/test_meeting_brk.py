# -*- coding: utf-8 -*-
# Copyright (c) 2015, bhamesh kore and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

# test_records = frappe.get_test_records('Meeting Brk')

class TestMeetingBrk(unittest.TestCase):
	def test_sync_todos_add(self):
		meeting = make_meeting()
		todos = get_todos(meeting)

		self.assertEqual(todos[0].name, meeting.minutes[0].todo)
		self.assertEqual(todos[0].description,
			meeting.minutes[0].description)		


	def test_sync_todos_remove(self):
		meeting = make_meeting()
		meeting.minutes[0].status = "Closed"
		meeting.save()
		todos = get_todos(meeting)
		self.assertEquals(len(todos), 0)

	def test_sync_todos_on_close_todo(self):
		meeting = make_meeting()
		todos = get_todos(meeting)
		todo = frappe.get_doc("ToDo", todos[0].name)
		todo.status = "Closed"
		todo.save()

		meeting.reload()
		self.assertEqual(meeting.minutes[0].status, "Closed")
		self.assertEqual(meeting.minutes[0].todo, "Closed")


	def test_sync_todos_on_delete_todo(self):
		meeting = make_meeting()
		todos = get_todos(meeting)
		todo = frappe.get_doc("ToDo", todos[0].name)
		todo.delete()

		meeting.reload()
		self.assertEqual(meeting.minutes[0].status, "Closed")
		self.assertEqual(meeting.minutes[0].todo, "Closed")	


	def make_meeting():
		meeting = frappe.get_doc({
			"doctype": "Meeting Brk",
			"title": "test_meeting",
			"status": "Planned",
			"date": "2015-01-01",
			"from_time": "09:00",
			"to_time": "11:00",
			"minutes": [
				{
					"description": "Test Meeting 1",
					"status": "Open",
					"assigned_to": "bhams91.kore@gmail.com"
				}
			]
		})
		meeting.insert()
		return meeting

	def get_todos(meeting):
		return frappe.get_all("ToDo", 
			filter = {
				"reference_type":meeting.doctype,
				"reference_name":meeting.name,
				"owner":"bhams91.kore@gmail.com"
			},
			fields=["name","description"])