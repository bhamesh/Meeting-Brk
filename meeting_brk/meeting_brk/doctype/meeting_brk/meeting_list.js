from frappe import __
frappe.listview_settings['Meeting Brk'] = {
	get_indicator: function(doc) {
		return [__(doc.status),{
			"Planned": "blue",
			"Invitation Sent": "orange",
			"In Progress": "red",
			"Completed": "green",
			"Cancelled": "darkgrey",
		}[doc.status], "status,=," + doc.status];
				
	}
};
