
frappe.views.calendar["Meeting Brk"] = {
	field_map: {
		"start": "start",
		"end": "end",
		"id": "name",
		"title": "title",
		"status": "status",
	},
	get_events_method: "meeting_brk.api.get_meeting"
}