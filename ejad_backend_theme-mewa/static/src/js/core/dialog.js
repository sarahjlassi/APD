odoo.define('ejad_backend_theme-mewa.view_dialogs', function(require) {
    "use strict";

    var config = require('web.config');
    if (!config.device.isMobile) {
        return;
    }

    var dialogs = require('web.view_dialogs');

    dialogs.SelectCreateDialog.include({
        init: function() {
            this._super.apply(this, arguments);
            this.viewType = 'kanban';
            this.options.selectionMode = true;
        },
    });

});