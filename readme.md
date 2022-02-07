# Inouk Notifications

Send Odoo standard notifications to users.

This addon allows to send notification messages using Odoo internal message bus.
This addons runs only when Odoo is launched in multiprocessing mode (--workers=...)
By itself this module does nothing. You must use it's features in your own code using it's dead simple API.

## Installation

Just install the addon.


## Usage instructions

The addon adds one method to `res.users`:

```
    def ik_notify(self, message_type, message_title, message, force_icon=None, sticky=False):
        """ Send a notification. 
        param message_type: "danger", "warning", "success" or "info". This defines the overall aspect of the notification.
        param message_title: The title of the notification
        param message: The message text. HTML content is supported.
        param force_icon: A Font-Awesome class that will be diplayed in the title bar (eg. fa-paw).
        param sticky: When set the notification must be explicitly closed by the user.        
        """
````

Call it and the user will receive the notification.

The addon adds a button in the User to generate a set of sample notifications.


## Licence

This addon and all the files that compose it are licensed under LGPL-3.0.

## Bugs

Use github issues


## Credits

This addon has been inspired by the OCA web_notify addon.

