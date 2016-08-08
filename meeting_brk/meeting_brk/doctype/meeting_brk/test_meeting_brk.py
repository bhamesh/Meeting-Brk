# -*- coding: utf-8 -*-
# Copyright (c) 2015, bhamesh kore and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

# test_records = frappe.get_test_records('Meeting Brk')

class TestMeetingBrk(unittest.TestCase):
	def test_sync_todos(self):
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

		todo = frappe.get_all("ToDo", filter = {
			"reference_type":meeting.doctype,
			"reference_name":meeting.name,
			"owner":"bhams91.kore@gmail.com"
		})

		self.assertEqual(todo[0].name, meeting.minutes[0].todo)
		self.assertEqual(todo[0].description,
			meeting.minutes[0].description)		
