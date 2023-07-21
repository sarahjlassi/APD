# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'MEWA Backend Theme (For Community Edition)',
    'category': "Themes/Backend",
    'version': '1.0',
    'license': 'OPL-1',
    'summary': 'Flexible, Powerful and Fully Responsive Customized Backend Theme with many features(Favorite Bar, Vertical Horizontal Menu Bar, Night Mode, Tree view of Menu and Sub menu, Fuzzy search for apps, Display density) in Community Edition.',
    'description': """ Flexible, Powerful and Fully Responsive Customized Backend Theme with many features(Favorite Bar,
    Vertical Horizontal Menu Bar, Night Mode, Tree view of Menu and Sub menu, Fuzzy search for apps, Display density).

    MEWA backend theme
Backend
backend theme
responsive backend theme
responsive frontend theme
responsive web theme
responsive website theme
responsive ecommerce theme

global search
fully responsive
User Interface
Odoo ERP
submenu
main menu[

toggle
ui ux
ui & ux
bootstrap
Customized Layouts
Menu bar
Submenu bar
Control Panel
List view
Search option layout
Form view action buttons
Dashboard
Kanban View
List View Form View
Graph View Pivot View
General View
Calendar View
Planner view Chat Panel
variations
color palette
default color panel
color scheme
colour palette
default colour panel
colour scheme
Dynamic Graph view
desktop layout
tablet layout
mobile layout
desktop view
tablet view
mobile view
favourite bar
full width
horizontal tab
vertical tab
normal view
light view
night view
customized icons
2d icon
3d icon
isometric icon
base icon
dynamic color palette
dynamic colour palette
display density
horizontal menu
vertical menu
full screen
default form view
comfortable
compact
ejad
flexible
fuzzy search
theme color
theme colour
app icon
without global search


    """,
    'author': 'Synconics Technologies Pvt. Ltd.',
    'depends': ['web', 'web_editor', 'mail'],
    'website': 'www.synconics.com',
    'data': [
        'data/theme_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/res_users_views.xml',
        'views/web_layout_custom.xml',
        'views/ir_module_views.xml',
        'views/ir_ui_menu.xml',
        'views/ir_ui_menu_category.xml',

    ],
    'images': [
        'static/description/main_screen.png',
        'static/description/ejad_screenshot.png',
    ],
     'assets': {
        'web.assets_common':[
            '/ejad_backend_theme-mewa/static/src/js/freamwork/config.js',
        ],
        'web._assets_primary_variables' :    [
            # <!-- link scss variables-->
            "ejad_backend_theme-mewa/static/src/scss/variables.scss",
            "ejad_backend_theme-mewa/static/src/scss/other_variable.scss",
            "ejad_backend_theme-mewa/static/src/scss/night_mode/ni_variables.scss",
        ],
        'web.assets_backend': [
            # <!-- Layout File - Start-->
            "/ejad_backend_theme-mewa/static/src/lib/minicolors/jquery.minicolors.css",
            "/ejad_backend_theme-mewa/static/src/scss/animation.scss",
            "/ejad_backend_theme-mewa/static/src/scss/fonts.scss",
            "/ejad_backend_theme-mewa/static/src/scss/light_mode/light_mode.scss",
            # Home Menu
            "/ejad_backend_theme-mewa/static/src/scss/layout/home_menu/home_menu.scss",
            # Left panel
            "/ejad_backend_theme-mewa/static/src/scss/layout/left_panel/left_menu_horizontal.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/left_panel/left_menu_vertical.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/left_panel/left_menu.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/left_panel/theme_customize_model.scss",
            #control panel
            "/ejad_backend_theme-mewa/static/src/scss/layout/control_panel/control_panel_search.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/control_panel/control_search_options.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/control_panel/control_action_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/control_panel/control_panel_top.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/control_panel/control_panel_bottom.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/control_panel/control_panel_model.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/control_panel/control_panel.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/control_panel/search_panel.scss",
            # kanban view
            "/ejad_backend_theme-mewa/static/src/scss/layout/kanban/group_kanban.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/kanban/ungroup_kanban.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/kanban/kanban_model.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/kanban/kanban_view.scss",
            #List View
            "/ejad_backend_theme-mewa/static/src/scss/layout/list/list_view.scss",
            #calendar view
            "/ejad_backend_theme-mewa/static/src/scss/layout/calendar/calendar_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/calendar/web_calender.scss",
            # activity view
            "/ejad_backend_theme-mewa/static/src/scss/layout/activity/activity_view.scss",
            # pivot view
            "/ejad_backend_theme-mewa/static/src/scss/layout/pivot/pivot_view.scss",
            #discuss
            "/ejad_backend_theme-mewa/static/src/scss/layout/discuss/composer_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/discuss/message_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/discuss/video_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/discuss/mailbox_mail.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/discuss/chat_view.scss",
            # Form view
            "/ejad_backend_theme-mewa/static/src/scss/layout/form/form_statusbar.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/form/button_box.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/form/notbook_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/form/form_view_mixin.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/form/form_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/form/form_model.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/form/setting_view.scss",
            # Graph view
            "/ejad_backend_theme-mewa/static/src/scss/layout/graph/graph_view.scss",
            # Import view
            "/ejad_backend_theme-mewa/static/src/scss/layout/import/import_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/import/select_drop.scss",
            #App
            "/ejad_backend_theme-mewa/static/src/scss/layout/app/expense_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/app/hr_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/app/lunch_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/app/purchase_view.scss",
            #core
            "/ejad_backend_theme-mewa/static/src/scss/layout/core/loading.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/core/error_message_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/core/nocontent_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/core/signout_layout.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/core/effects.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/web_client.scss",
            "/ejad_backend_theme-mewa/static/src/scss/layout/layout.scss",
            # <!-- Responsive -->
            #left_panel
            "/ejad_backend_theme-mewa/static/src/scss/responsive/left_panel/left_menu.scss",
            #app
            "/ejad_backend_theme-mewa/static/src/scss/responsive/app/r_hr_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/responsive/home_menu.scss",
            "/ejad_backend_theme-mewa/static/src/scss/responsive/chat_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/responsive/control_panel_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/responsive/kanban_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/responsive/list_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/responsive/form_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/responsive/configration.scss",
            "/ejad_backend_theme-mewa/static/src/scss/responsive/mail_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/responsive/pivot_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/responsive/base_settings.scss",
            "/ejad_backend_theme-mewa/static/src/scss/responsive/responsive_xs.scss",
            # <!-- Rtl -->
            "/ejad_backend_theme-mewa/static/src/scss/rtl/rtl.scss",
            # <!-- Lib -->
            "/ejad_backend_theme-mewa/static/src/lib/custom_radiobutton.scss",
            "/ejad_backend_theme-mewa/static/src/lib/custom_checkbox.scss",
            # <!-- NI mode -->
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/freamwork/ni_control_panel.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/freamwork/ni_header_layout.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_home_menu.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_kanban_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_list_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_graph_layout.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_activity_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_barcode_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_pivot_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_calander_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_mail_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_gernal_setting_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_dashboards_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_form_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_model_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_import_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_window_chnage_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_attendance_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_lunch_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/views/ni_purchase_view.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/ni_common_layout.scss",
            "/ejad_backend_theme-mewa/static/src/scss/night_mode/ni_layout.scss",
            "/ejad_backend_theme-mewa/static/src/scss/all.css",
            "/ejad_backend_theme-mewa/static/src/scss/custom.scss",
            "/ejad_backend_theme-mewa/static/src/scss/media.scss",
            # <!-- Main Menu Category -->
            "/ejad_backend_theme-mewa/static/src/less/menu_category.less",


            # <!-- JS Path - start -->
            "/ejad_backend_theme-mewa/static/src/js/ejad_web_themes.js",
            "/ejad_backend_theme-mewa/static/src/lib/minicolors/jquery.minicolors.min.js",
            "/ejad_backend_theme-mewa/static/src/js/main_view.js",
            "/ejad_backend_theme-mewa/static/src/js/views/res_config_settings.js",
            "/ejad_backend_theme-mewa/static/src/js/views/menu.js",
            "/ejad_backend_theme-mewa/static/src/js/chrome/error_handlers.js",
            "/ejad_backend_theme-mewa/static/src/js/components/chat_window/chat_window.js",
            "/ejad_backend_theme-mewa/static/src/js/components/action_menus.js",
            "/ejad_backend_theme-mewa/static/src/js/components/dropdown_navigation_hook.js",
            "/ejad_backend_theme-mewa/static/src/js/components/dropdown_menu.js",
            "/ejad_backend_theme-mewa/static/src/js/components/dropdown.js",
            "/ejad_backend_theme-mewa/static/src/js/views/control_panel/control_panel.js",
            "/ejad_backend_theme-mewa/static/src/js/views/control_panel/control_panel_ext.js",
            "/ejad_backend_theme-mewa/static/src/js/views/control_panel/search_bar.js",
            "/ejad_backend_theme-mewa/static/src/js/search/search_panel.js",
            "/ejad_backend_theme-mewa/static/src/js/search/search_bar/search_bar.js",
            "/ejad_backend_theme-mewa/static/src/js/webclient/navbar/navbar.js",
            "/ejad_backend_theme-mewa/static/src/js/webclient/navbar/systray_activity_menu.js",
            "/ejad_backend_theme-mewa/static/src/js/webclient/menubar.js",
            "/ejad_backend_theme-mewa/static/src/js/webclient/favorite_menu_view.js",
            "/ejad_backend_theme-mewa/static/src/js/webclient/action_service.js",
            "/ejad_backend_theme-mewa/static/src/js/webclient/webclient.js",
            "/ejad_backend_theme-mewa/static/src/js/webclient/custom_menu/custom_menu.js",
            "/ejad_backend_theme-mewa/static/src/js/webclient/custom_menu/menus/menu_helpers.js",
            "/ejad_backend_theme-mewa/static/src/js/services/systray_hepler.js",
            "/ejad_backend_theme-mewa/static/src/js/views/search_panel_mobile.js",
            "/ejad_backend_theme-mewa/static/src/js/views/form/form_renderer.js",
            "/ejad_backend_theme-mewa/static/src/js/views/list/list_model.js",
            "/ejad_backend_theme-mewa/static/src/js/views/list/list_controller.js",
            "/ejad_backend_theme-mewa/static/src/js/views/list/list_renderer.js",
            "/ejad_backend_theme-mewa/static/src/js/views/list/list_view.js",
            "/ejad_backend_theme-mewa/static/src/js/views/kanban/kanban_column_quick_create_mobile.js",
            "/ejad_backend_theme-mewa/static/src/js/views/kanban/kanban_controller.js",
            "/ejad_backend_theme-mewa/static/src/js/views/kanban/kanban_renderer_mobile.js",
            "/ejad_backend_theme-mewa/static/src/js/views/kanban/kanban_view.js",
            "/ejad_backend_theme-mewa/static/src/js/views/graph/color.js",
            "/ejad_backend_theme-mewa/static/src/js/views/graph/graph_renderer.js",
            "/ejad_backend_theme-mewa/static/src/js/freamwork/dashboard.js",
            "/ejad_backend_theme-mewa/static/src/js/views/import_action.js",
            "/ejad_backend_theme-mewa/static/src/js/core/dialog.js",
            "/ejad_backend_theme-mewa/static/src/js/core/block_ui.js",
            "/ejad_backend_theme-mewa/static/src/js/fields/relational_fields.js",
            "/ejad_backend_theme-mewa/static/src/js/fields/basic_fields.js",
            "/ejad_backend_theme-mewa/static/src/js/responsive/breadcrumb.js",
            "/ejad_backend_theme-mewa/static/src/js/plugins.js",
        ],
        'web.assets_backend_prod_only': [
            ('replace', 'web/static/src/main.js', '/ejad_backend_theme-mewa/static/src/js/main.js'),
        ],
        'web.assets_qweb': [
            'ejad_backend_theme-mewa/static/src/xml/*.xml',
            'ejad_backend_theme-mewa/static/src/xml/**/*.xml',
        ],
    },
    'post_init_hook': 'post_init_check',
    'uninstall_hook': 'uninstall_hook',
    'price': 400.0,
    'currency': 'USD',
    'installable': True,
    'auto_install': False,
    'bootstrap': True,
}