odoo.define('apd_ticket_portal.new_fetures', function (require) {
'use strict';
var core = require('web.core');
var ajax = require('web.ajax');
var qweb = core.qweb;
ajax.loadXML('/apd_ticket_portal/static/src/xml/potal_template.xml', qweb);
});