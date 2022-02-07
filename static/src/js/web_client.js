odoo.define("web_notify.WebClient", function(require) {
    "use strict";

    var WebClient = require("web.WebClient");
    var session = require("web.session");
    require("bus.BusService");

    WebClient.include({
        show_application: function() {
            var res = this._super();
            this.start_polling();
            return res;
        },
        start_polling: function() {
            this.ikn_channel = "ikn_notify_4user_" + session.uid;
            // We may add support for several channels
            this.polled_channels = [
                this.ikn_channel,
            ];
            this.call("bus_service", "startPolling");

            if (this.call("bus_service", "isMasterTab")) {
                this.call("bus_service", "addChannel", this.ikn_channel);
            }
            this.call("bus_service", "on", "notification", this, this.ikn_bus_notification);
        },

        ikn_bus_notification: function(notifications) {
            var self = this;
            _.each(notifications, function(notification) {
                var channel = notification[0];
                var message = notification[1];
                if (self.polled_channels && self.polled_channels.indexOf(channel) > -1) {
                    self.on_ikn_message(message);
                }
            });
        },
        on_ikn_message: function(message) {
            return this.call("notification", "notify", {
                type: message.type,
                title: message.title,
                message: message.message,
                sticky: message.sticky,
                className: message.className,
                icon: message.icon,
                force_icon: message.force_icon,
            });
        },
    });
});
