odoo.define("inouk_notifications.Notification", function(require) {
    "use strict";

    var Notification = require("web.Notification");

    Notification.include({
        icon_types_mapper: {
            danger: "fa-exclamation-circle",
            warning: "fa-exclamation",
            success: "fa-check",
            info: "fa-info",
        },
        init: function() {
            this._super.apply(this, arguments);
            if(arguments[1] && arguments[1].force_icon) {
                this.icon = arguments[1].force_icon;
            } else {
                this.icon = this.icon_types_mapper[this.type] || this.icon_types_mapper.default;
            }
            this.className += ' ikn_'+this.type;
        }
    });
});
