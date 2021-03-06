frappe.views.calendar["Meeting"] = {
	field_map: {
		"start": "from_date",
		"end": "to_date",
		"id": "name",
		"title": "title",
		"status": "status",
		"color": "color"
	},
	options: {
		header:{
			left:'prev,next today',
			center: 'title',
			right:'month'
		}
	},
	get_events_method: "meeting.api.get_meetings"
}