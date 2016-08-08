// Copyright (c) 2016, bhamesh kore and contributors
// For license information, please see license.txt

frappe.ui.form.on('Meeting Brk', {
	refresh: function(frm) {

	},
	send_email:function(frm)
	{
		if (frm.doc.status == "Planned") {
			frappe.call({
				method: "meeting_brk.api.send_invitation_email",
				args: {
					"meeting": frm.doc.name
				},
				callback: function(r)
				{

				}
			});
		}
	},
	attendee:function (frm,cdt,cdn) {
		var attendee=frappe.model.get_doc(cdt,cdn);
		if(attendee.attendee)
		{
			//if attendee ,get full name
			frappe.call({
				method:"meeting_brk.meeting_brk.doctype.meeting_brk.meeting_brk.get_full_name",
				args:{

					"attendee":attendee.attendee
				},
				callback:function(r)
				{
					frappe.model.set_value(cdt,cdn,"full_name",r.message);
				}
			});
		}
		else
		{
			//if no attendee, clear full name
			frappe.model.set_value(cdt,cdn,"full_name",null);

		}
		// body...
	}
});
