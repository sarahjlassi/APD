/** @odoo-module **/

import SystrayMenu from 'web.SystrayMenu';
import Widget from 'web.Widget';

var HelperMenu = Widget.extend({
    name: 'helper_menu',
    template: 'ejad_backend_theme-mewa.SystrayHepler',
});

SystrayMenu.Items.push(HelperMenu);
export default HelperMenu;