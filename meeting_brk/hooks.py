# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "meeting_brk"
app_title = "Meeting Brk"
app_publisher = "bhamesh kore"
app_description = "Prepare agenda, send email to user and record minutes of meeting"
app_icon = "octicon octicon-file-directory"
app_color = "yellow"
app_email = "bhams91.kore@gmail.com"
app_license = "GPL v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/meeting_brk/css/meeting_brk.css"
# app_include_js = "/assets/meeting_brk/js/meeting_brk.js"

# include js, css files in header of web template
# web_include_css = "/assets/meeting_brk/css/meeting_brk.css"
# web_include_js = "/assets/meeting_brk/js/meeting_brk.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "meeting_brk.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype


website_generators = ["Meeting Brk"]
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "meeting_brk.install.before_install"
# after_install = "meeting_brk.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "meeting_brk.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events
doc_events = {
	"User": {
		"after_insert": "meeting_brk.api.make_orientation_meeting"
	},
	"ToDo":{
		"on_update": "meeting_brk.api.update_minute_status",
		"on_trash": "meeting_brk.api.update_minute_status"
	}
}



# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"meeting_brk.tasks.all"
# 	],
# 	"daily": [
# 		"meeting_brk.tasks.daily"
# 	],
# 	"hourly": [
# 		"meeting_brk.tasks.hourly"
# 	],
# 	"weekly": [
# 		"meeting_brk.tasks.weekly"
# 	]
# 	"monthly": [
# 		"meeting_brk.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "meeting_brk.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "meeting_brk.event.get_events"
# }