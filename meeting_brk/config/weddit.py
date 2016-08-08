# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{	
			"label": _("Tools"),
			"icon": "octicon octicon-briefcase",
			"item":[
				{
					"type": "doctype",
					"name": "Meeting Brk",
					"label": _("Meeting Brk"),
					"description": _("Prepare agenda, send mail and record minutes"),
				},
			]
		}
	]
