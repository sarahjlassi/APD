odoo.define('ejad_backend_theme-mewa.ListView', function(require) {
    "use strict";

    var ListView = require('web.ListView');

    ListView.include({
        init: function(viewInfo, params) {
            this._super.apply(this, arguments);
            this.loadParams.attachmentsData = [];
            this.loadParams.resDomain = params.domain;
        },
    });
    return ListView;

});