from odoo import api, fields, models, exceptions
from odoo.exceptions import UserError


MESSAGE_TYPES = [
    "danger",
    "warning",
    "success",
    "info",
]


class IKNResUsers(models.Model):
    _inherit = "res.users"

    def ik_notify(self, message_type, message_title, message, force_icon=None, sticky=False):
        """ Send a notification. 
        param message_type: "danger", "warning", "success" or "info". This defines the overall aspect of the notification.
        param message_title: The title of the notification
        param message: The message text. HTML content is supported.
        param force_icon: A Font-Awesome class that will be diplayed in the title bar (eg. fa-paw).
        param sticky: When set the notification must be explicitly closed by the user.        
        """
        if message_type not in MESSAGE_TYPES:
            raise UserError(
                "Unsupported message_type:'%s'. Allowed values are %s." % (
                    message_type,
                    ', '.join(MESSAGE_TYPES),
                )
            )

        if not self.env.user._is_admin():
            raise exceptions.UserError(
                "Only administrators are allowed to send notifications"
            )

        _message = {
            "type": message_type,
            "message": message,
            "title": message_title,
            "sticky": sticky,
            "force_icon": force_icon,
        }
        _notifications = [
            ("ikn_notify_4user_%s" % record.id, _message) for record in self
        ]
        self.env["bus.bus"].sendmany(_notifications)

    def btn_test_ik_notifications(self):
        self.ensure_one()
        self.ik_notify(
            'danger',
            'Oups !',
            "This is an Inouk Notification of type Danger!. These notifications must be closed explicitly.", 
            sticky=True
        )
        self.ik_notify(
            'warning',
            'Be careful !',
            "This is an Inouk Notification of type Warning!",
            sticky=False
        )
        self.ik_notify(
            'success',
            'Yeah',
            "This is an Inouk Notification of type Success!", 
            sticky=False
        )
        self.ik_notify(
            'info',
            'Notice',
            "This is an Inouk Notification of type Info!", 
            sticky=False
        )
