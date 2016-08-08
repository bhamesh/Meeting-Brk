import frappe	
import frappe import _
from frappe.utils import nowdate, add_days

@frappe.whitelist()
def send_invitation_email(meeting):
	meeting = frappe.get_doc("Meeting Brk", meeting)
	meeting.check_permission("email")


	if meeting.status == "Planned":
		frappe.sendmail(
			recipients = [d.attendee for d in meeting.attendees],
			sender = frappe.session.user,
			subject = meeting.title,
			message = meeting.invitation_message,
			reference_doctype = meeting.doctype,
			reference_name = meeting.name
		)

		meeting.status = "Invitation Sent"
		meeting.save()
		frappe.msgprint(_("Invitation Sent"))

	else:
		frappe.msgprint(_("Meeting status must be 'planned'"))

@frappe.whitelist(
def get_meeting(start, end):
	if not frappe.has_permission("Meeting Brk", "read"):
		raise frappe.PermissionError

	return frappe.db.sql("""select 
		timestamp('date',from_time) as start,
		timestamp('date',to_time ) as end,
		name,
		title,
		status,
		0 as all_day	
	from 'tabMeeting Brk'
	where 'date' between %(start)s and %(end)s""",{
		"start": start,
		"end": end
	}, as_dict=True)
		
def make_orientation_meeting(doc, method):
	#create an Orientation meeting when a new user is added
	meeting = frappe.get_doc({
		"doctype": "Meeting Brk",
		"title": "Orientation for {0}".format(doc.first_name),
		"date": add_days(nowdate(), 1),
		"from_time": "09:00",
		"to_time": "11.00",
		"status": "Planned",
		"attendees": [{
			"attendee": doc.name
		}]

	})
	#the System Manager might not have permission to create a Meeting 
	meeting.flags.ignore_permission = True
	meeting.insert()
	frappe.msgprint(_("Orientation meeting created"))
