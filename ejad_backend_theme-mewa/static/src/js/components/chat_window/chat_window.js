/** @odoo-module **/
import { ChatWindow } from "@mail/components/chat_window/chat_window";
const { patch } = require('web.utils');

patch(ChatWindow.prototype, '@ejad_backend_theme-mewa/static/src/js/components/chat_window/chat_window.js', {
    mounted() {
        if (!this.env.device.isMobile) {
            document.body.classList.add('ad-chat-window');
        }
        this._super(...arguments);
    },

    willUnmount() {
        if (!this.env.device.isMobile &&
            (document.querySelectorAll('.o_ChatWindow').length - 1) === 0) {
            document.body.classList.remove('ad-chat-window');
        };
        this._super(...arguments);
    },
});