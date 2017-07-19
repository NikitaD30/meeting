import frappe

@frappe.whitelist()
def send_invitation_emails(meeting):
	print "inside sent Invitation***********************\n\n\n"
	meeting=frappe.get_doc("Meeting",meeting)
	meeting.check_permission("email")


	if meeting.status == "Planned":
	 	frappe.sendmail(
	 		recipients=[d.attendee for d in meeting.attendees],
	 		sender=frappe.session.user,
	 		subject=meeting.title,	
	 		message=meeting.invitation_message,
	 		reference_doctype=meeting.doctype,
	 		reference_name=meeting.name
	 	)
	 	meeting.status= (_("Invitation sent!"))
	 	meeting.save()
	else:
	 	frappe.msgprint(_("Meeting status must be 'Planned'"))
@frappe.whitelist()
def get_meetings(from_date, to_date):
	pass