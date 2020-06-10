from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'website_index'),
	path('about', views.about, name = 'website_about'),
	path('contact', views.contact, name = 'website_contact'),
	path('category', views.category, name = 'website_category'),
	path('blog', views.blog, name = 'website_blog'),
	# path('blog_post', views.blog_post, name = 'website_blog_post'),
	path('blog_postB', views.blog_postB, name = 'website_blog_postB'),	
	path('website/<slug:blog_link>', views.blog_post, name='website_blog_post'),
	# placemat classified style path
	path('placemat', views.placemat, name = 'website_placemat'),
	path('vinyl_woven_placemat/classified_style_1', views.classified_style_1, name = 'website_classified_style_1'),
	path('vinyl_woven_placemat/classified_style_2', views.classified_style_2, name = 'website_classified_style_2'),
	path('vinyl_woven_placemat/classified_style_3', views.classified_style_3, name = 'website_classified_style_3'),
	path('vinyl_woven_placemat/classified_style_4', views.classified_style_4, name = 'website_classified_style_4'),
	path('vinyl_woven_placemat/classified_style_5', views.classified_style_5, name = 'website_classified_style_5'),
	path('vinyl_woven_placemat/classified_style_6', views.classified_style_6, name = 'website_classified_style_6'),
	path('vinyl_woven_placemat/classified_style_7', views.classified_style_7, name = 'website_classified_style_7'),
	path('vinyl_woven_placemat/classified_style_8', views.classified_style_8, name = 'website_classified_style_8'),
	path('vinyl_woven_placemat/classified_style_9', views.classified_style_9, name = 'website_classified_style_9'),
	path('vinyl_woven_placemat/classified_style_10', views.classified_style_10, name = 'website_classified_style_10'),
	path('vinyl_woven_placemat/classified_style_11', views.classified_style_11, name = 'website_classified_style_11'),	
	path('vinyl_woven_placemat/classified_style_try', views.classified_style_try, name = 'website_classified_style_try'),
	path('design', views.design, name = 'website_design'),
	# placemat regular_pattern path
	path('vinyl_woven_placemat/regular_pattern_1', views.regular_pattern_1, name = 'website_regular_pattern_1'),
	path('vinyl_woven_placemat/regular_pattern_2', views.regular_pattern_2, name = 'website_regular_pattern_2'),
	path('vinyl_woven_placemat/regular_pattern_3', views.regular_pattern_3, name = 'website_regular_pattern_3'),
	path('vinyl_woven_placemat/placemat_profile', views.placemat_profile, name = 'website_placemat_profile'),
	# vinyl_woven_placemat path
	path('vinyl_woven_table_runner/vinyl_woven_table_runner_1', views.vinyl_woven_table_runner_1, name = 'website_vinyl_woven_table_runner_1'),
	# path('vinyl_woven_table_runner/vinyl_woven_table_runner_2', views.vinyl_woven_table_runner_2, name = 'website_vinyl_woven_table_runner_2')
	# car carpet path
	path('car_carpet/car_carpet_1', views.car_carpet_1, name = 'website_car_carpet_1'),
	# vinyl_tufted doormat
	path('vinyl_tufted_doormat/vinyl_tufted_doormat_1', views.vinyl_tufted_doormat_1, name = 'website_vinyl_tufted_doormat_1'),
	path('vinyl_tufted_doormat/vinyl_tufted_doormat_2', views.vinyl_tufted_doormat_2, name = 'website_vinyl_tufted_doormat_2'),
	path('vinyl_tufted_doormat/vinyl_tufted_doormat_3', views.vinyl_tufted_doormat_3, name = 'website_vinyl_tufted_doormat_3'),
    #plastic extrusion machinery
    path('plastic_extrusion_machinery/machine_profile', views.machine_profile, name = 'website_machine_profile'),
    path('plastic_extrusion_machinery/machine_profile_2', views.machine_profile_2, name = 'website_machine_profile_2'),
    path('plastic_extrusion_machinery/eletronic_wire_equipment', views.eletronic_wire_equipment, name = 'website_eletronic_wire_equipment'),
    path('plastic_extrusion_machinery/wire_cable_sheath_line_equipment', views.wire_cable_sheath_line_equipment, name = 'website_wire_cable_sheath_line_equipment'),
    path('plastic_extrusion_machinery/pet_wiredrawing_machine_equipment', views.pet_wiredrawing_machine_equipment, name = 'website_pet_wiredrawing_machine_equipment'),
    path('plastic_extrusion_machinery/pp_brush_wiredrawing_machine_equipment', views.pp_brush_wiredrawing_machine_equipment, name = 'website_pp_brush_wiredrawing_machine_equipment'),
    path('plastic_extrusion_machinery/plastic_round_monofilament_silk_wiredrawing_machine', views.plastic_round_monofilament_silk_wiredrawing_machine, name = 'website_plastic_round_monofilament_silk_wiredrawing_machine'),
    path('plastic_extrusion_machinery/manager_lin_coating_unit', views.manager_lin_coating_unit, name = 'website_manager_lin_coating_unit'),
    path('plastic_extrusion_machinery/plastic_seat_tube_equipment', views.plastic_seat_tube_equipment, name = 'website_plastic_seat_tube_equipment'),
    path('plastic_extrusion_machinery/plastic_sealing_equipment', views.plastic_sealing_equipment, name = 'website_plastic_sealing_equipment'),
    path('plastic_extrusion_machinery/hot_melt_glue_equipment', views.hot_melt_glue_equipment, name = 'website_hot_melt_glue_equipment'),
    path('plastic_extrusion_machinery/squeeze_film_line_equipment', views.squeeze_film_line_equipment, name = 'website_squeeze_film_line_equipment'),
    #中文版
	path('indexcn', views.indexcn, name = 'websitecn_indexcn'),
    path('app_guide_page', views.app_guide_page, name = 'websitecn_app_guide_page'),
]
    
	
