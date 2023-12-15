odoo.define('shortcuts.raccourci', function (require) {
    'use strict';

    var ajax = require('web.ajax');
    console.log('shortcuts start')

    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.altKey && e.key === 'h') {
            console.log('go to home');
            window.location.href = '/';
        } else if (e.ctrlKey && e.altKey && e.key === 'b') {
            window.location.href = '/my/home';
        } else if (e.ctrlKey && e.altKey && e.key === 'n') {
            window.location.href = '/blog/news-2';
        } else if (e.ctrlKey && e.altKey && e.key === 'e') {
            window.location.href = '/event';
        } else if (e.ctrlKey && e.altKey && e.key === 'c') {
            window.location.href = '/contact-us';
        } else if (e.ctrlKey && e.altKey && e.key === 'g') {
            window.location.href = '/sources';
        } else if (e.ctrlKey && e.altKey && e.key === 'p') {
            window.location.href = '/e-participation';
        }
    });
});
