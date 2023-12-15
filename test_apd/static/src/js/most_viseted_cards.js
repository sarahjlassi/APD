odoo.define('test_apd.tmp_cards_data', function (require) {
    var publicWidget = require('web.public.widget');
    var nb_clicks = 0;

    publicWidget.registry.mostVisitedCardsWidget = publicWidget.Widget.extend({
        selector: '.website',
        events: {
            'click': '_onWebsiteClick',
        },

        _onWebsiteClick: function (ev) {
            var cardId = $(ev.currentTarget).data('card-id');
            this._rpc({
            model: 'shop.card',
            method: 'most_visited_cards',
            args: [cardId],
            }).then(function (result) {
            console.log('RPC result:', result);
    });

},
    });

    return publicWidget.registry.mostVisitedCardsWidget;
});