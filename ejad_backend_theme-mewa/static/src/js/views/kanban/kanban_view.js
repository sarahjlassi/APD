odoo.define('ejad_backend_theme-mewa.KanbanView', function(require) {
    "use strict";

    var KanbanView = require('web.KanbanView');
    const config = require('web.config');

    KanbanView.include({
        /**
         * @override
         */
        init: function(viewInfo, params) {
            this._super.apply(this, arguments);
            if (config.device.isMobile) {
                this.jsLibs.push('/ejad_backend_theme-mewa/static/src/lib/jquery.touchSwipe/jquery.touchSwipe.js');
            };
        },
    });

});