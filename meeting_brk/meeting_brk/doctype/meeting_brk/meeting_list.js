frappe.listview_settings['Meeting Brk'] = {
	add_fields: ["status"],
	get_indicator: function(doc) {
		var colors = {
			"Planned": "orange",
			"Invitation Sent": "red",
			"In Progress": "orange",
			"Completed": "green",
			"Cancelled": "dark grey"
		}
		return [__(doc.status), colors[doc.status], "status,=," + doc.status];
	}

};
// 	get_indicator: function(doc) {
// 		return [__(doc.status), {
// 			"Planned": "#00CC00",
// 			"Invitation Sent": "orange",
// 			"In Progress": "green",
// 			"Completed": "red",
// 			"Cancelled": "darkgrey"
// 		}[doc.status], "status,=," + doc.status];
// 	}
// };