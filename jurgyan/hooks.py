# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "jurgyan"
app_title = "Jurgyan"
app_publisher = "Epoch"
app_description = "Jurgyan Industries"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "umag@epochconsulting.in"
app_license = "MIT"
fixtures = ["Custom Field",
"Property Setter",
"Custom Script",
"Report",
"Print Format"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jurgyan/css/jurgyan.css"
# app_include_js = "/assets/jurgyan/js/jurgyan.js"

# include js, css files in header of web template
# web_include_css = "/assets/jurgyan/css/jurgyan.css"
# web_include_js = "/assets/jurgyan/js/jurgyan.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "jurgyan.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "jurgyan.install.before_install"
# after_install = "jurgyan.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jurgyan.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
       "Sales Invoice": {
                "validate": "jurgyan.api.set_total_in_words"
             }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"jurgyan.tasks.all"
# 	],
# 	"daily": [
# 		"jurgyan.tasks.daily"
# 	],
# 	"hourly": [
# 		"jurgyan.tasks.hourly"
# 	],
# 	"weekly": [
# 		"jurgyan.tasks.weekly"
# 	]
# 	"monthly": [
# 		"jurgyan.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "jurgyan.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "jurgyan.event.get_events"
# }

