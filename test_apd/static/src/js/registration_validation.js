odoo.define('test_apd.tmp_registration', function (require) {
    'use strict';
    var publicWidget = require("web.public.widget");


    publicWidget.registry.RegistrationValidation = publicWidget.Widget.extend({
        selector: '.validation',
        events: {
            'click': '_onSubmitButton',
        },

        _onSubmitButton: function (evt) {

            console.log('hiiiiiiiiiiii');
//            var email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
//            var shop_name = this.$("input[name='name']").val();
//            var $shopType = this.$("select[name='type']").val();
//            var shop_type = ($shop_type.val() || '0');
//            if (!shop_name){
//                $(#client_side_validation).html('! حقل اسم المتجر حقل اجباري ');
//                $(#client_side_validation).show();
//                evt.preventDefault();
//            }
//            if (!shop_type){
//                $(#client_side_validation).html('! حقل هل انت  حقل اجباري ');
//                $(#client_side_validation).show();
//                evt.preventDefault();
//            }
//
//            if (!shop_name.match(email_regex)){
//                $(#client_side_validation).html('! الرجاء التحقق من بريدك الاكتروني ');
//                $(#client_side_validation).show();
//                evt.preventDefault();
//            }
//
//            alert('hi !!!');
//            console.log('hiiiiiiiiiiii');
//
    });

},
    });

    return publicWidget.registry.RegistrationValidation;
});