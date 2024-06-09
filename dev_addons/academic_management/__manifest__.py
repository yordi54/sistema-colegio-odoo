# -*- coding: utf-8 -*-
{
    'name': "Gestion Academica",

    'summary': 'Módulo personalizado para gestion academica de un colegio',
    'description': 'Este módulo extiende de algunos modelos y crea nuevos modelos  para gestionar información específica para la gestion academica de un colegio.',

    'author': "Yordi Condori Escalera | Juan Andres Román Yáñez",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/school_views.xml',
        'views/job_type_academic_views.xml',
        'views/employee_academic_views.xml',
        'views/department_academic_views.xml',
        'views/student_views.xml',
        'views/management_views.xml',
        'views/period_views.xml',
        'views/cycle_views.xml',
        'views/parallel_views.xml',
        'views/grade_views.xml',
        'views/subject_views.xml',
        'views/management_views.xml',
        'views/period_views.xml',
        'views/guardian_views.xml',
        'views/enrollment_views.xml',
        'views/license_views.xml',
        'views/classroom_views.xml',
        'views/schedule_views.xml',
        'views/register_attendance_views.xml',
        'views/grade_book_views.xml',
        'views/mark_views.xml',
        'views/report_card_views.xml',
        'views/announcement_views.xml',

        'views/academic_management_views.xml',
        'data/ir_module_category_data.xml',
    ],

    #actions button
    'qweb': {
        #css personalizado a mi proyecto web.assets
        'web.assets_backend': [
            'my_addon/static/src/js/**/*',
        ],
    },

    
  
    #icono
    'images': ['static/description/icon.png'],

    'installable': True,
    'application': True,

}

