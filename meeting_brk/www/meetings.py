import frappe


def get_context(context):
	context.planned_meetings = get_meetings("Planned")
 		# fields=["name", "title", "date", "from_time", "to_time", "page_name"],
 		# filters={"status": "Planned", "show_in_website":1},
 		# order_by="date desc")

	context.past_meetings = get_meetings("Completed", limit_page_length=20)

def get_meetings(status, **kwargs):
	return frappe.get_all("Meeting Brk",
		fields=["name", "title", "date", "from_time", "to_time", "page_name"],
		filters={"status": status, "show_in_website": 1},
		order_by="date desc", **kwargs)


	# context.past_meetings = frappe.get_all("Meeting Brk",
 # 		fields=["name", "title", "date", "from_time", "to_time", "page_name"],
 # 		filters={"status": "Completed", "show_in_website":1},
 # 		order_by="date desc",
 # 		limit_page_length=20)


	# context.planned_meetings = get_meetings("Planned")

	# # show only 20 past meetings
	# context.past_meetings = get_meetings("Completed", limit_page_length=20)

