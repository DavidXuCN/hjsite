from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from .models import IMG
import markdown2
# 分页模块
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 图片


# Create your views here.

def index(request):
	return render(request, 'website/index.html') 

def about(request):
	return render(request, 'website/about.html')

def contact(request):
	return render(request, 'website/contact.html')

def category(request):
	return render(request, 'website/category.html')

def blog(request):	
	post_list = Post.objects.all().order_by('-publish_date')	
	# 分页
	paginator = Paginator(post_list,4)
	page = request.GET.get('page')	

	try:
		post_list = paginator.page(page)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except EmptyPage:
		post_list = paginator.page(paginator.num_pages)	

	return render(request, 'website/blog.html', {'post_list':post_list})	
	# return render(request, 'website/blog.html', {'post_list':post_list})

# def blog_post(request):
# 	return render(request, 'website/blog_post.html')

def blog_postB(request):	
	img = IMG.objects.all()	
	return render(request, 'website/blog_postB.html',{'img':img})

def blog_post(request, blog_link):	
	post = get_object_or_404(Post, link=blog_link)
	post.content = markdown2.markdown(post.content)		
	return render(request, 'website/blog_post.html', {'post':post})

# placemat classified style path
def placemat(request):
	return render(request, 'website/placemat.html')

def classified_style_1(request):
	return render(request, 'website/vinyl_woven_placemat/classified_style_1.html')

def classified_style_2(request):
	return render(request, 'website/vinyl_woven_placemat/classified_style_2.html')

def classified_style_3(request):
	return render(request, 'website/vinyl_woven_placemat/classified_style_3.html')

def classified_style_4(request):
	return render(request, 'website/vinyl_woven_placemat/classified_style_4.html')

def classified_style_5(request):
	return render(request, 'website/vinyl_woven_placemat/classified_style_5.html')

def classified_style_6(request):
	return render(request, 'website/vinyl_woven_placemat/classified_style_6.html')

def classified_style_7(request):
	return render(request, 'website/vinyl_woven_placemat/classified_style_7.html')

def classified_style_8(request):
	return render(request, 'website/vinyl_woven_placemat/classified_style_8.html')

def classified_style_9(request):
	return render(request, 'website/vinyl_woven_placemat/classified_style_9.html')

def classified_style_10(request):
	return render(request, 'website/vinyl_woven_placemat/classified_style_10.html')

def classified_style_11(request):
	return render(request, 'website/vinyl_woven_placemat/classified_style_11.html')

def classified_style_try(request):
	return render(request, 'website/vinyl_woven_placemat/classified_style_try.html')

def design(request):
	return render(request, 'website/design.html')

# placemat regular pattern path
def regular_pattern_1(request):
	return render(request, 'website/vinyl_woven_placemat/regular_pattern_1.html')

def regular_pattern_2(request):
	return render(request, 'website/vinyl_woven_placemat/regular_pattern_2.html')

def regular_pattern_3(request):
	return render(request, 'website/vinyl_woven_placemat/regular_pattern_3.html')

def placemat_profile(request):
	return render(request, 'website/vinyl_woven_placemat/placemat_profile.html')


# vinyl_woven_placemat path
def vinyl_woven_table_runner_1(request):
	return render(request, 'website/vinyl_woven_table_runner/vinyl_woven_table_runner_1.html')

# def vinyl_woven_table_runner_2(request):
# 	return render(request, 'website/vinyl_woven_table_runner/vinyl_woven_table_runner_2.html')

# car carpet path
def car_carpet_1(request):
	return render(request, 'website/car_carpet/car_carpet_1.html')

# vinyl tufted doormat
def vinyl_tufted_doormat_1(request):
	return render(request, 'website/vinyl_tufted_doormat/vinyl_tufted_doormat_1.html')

def vinyl_tufted_doormat_2(request):
	return render(request, 'website/vinyl_tufted_doormat/vinyl_tufted_doormat_2.html')

def vinyl_tufted_doormat_3(request):
	return render(request, 'website/vinyl_tufted_doormat/vinyl_tufted_doormat_3.html')

# plastic extrusion machinery
def machine_profile(request):
	return render(request, 'website/plastic_extrusion_machinery/machine_profile.html')

def machine_profile_2(request):
	return render(request, 'website/plastic_extrusion_machinery/machine_profile_2.html')

def eletronic_wire_equipment(request):
	return render(request, 'website/plastic_extrusion_machinery/eletronic_wire_equipment.html')

def wire_cable_sheath_line_equipment(request):
	return render(request, 'website/plastic_extrusion_machinery/wire_cable_sheath_line_equipment.html')

def pet_wiredrawing_machine_equipment(request):
	return render(request, 'website/plastic_extrusion_machinery/pet_wiredrawing_machine_equipment.html')

def pp_brush_wiredrawing_machine_equipment(request):
	return render(request, 'website/plastic_extrusion_machinery/pp_brush_wiredrawing_machine_equipment.html')

def plastic_round_monofilament_silk_wiredrawing_machine(request):
	return render(request, 'website/plastic_extrusion_machinery/plastic_round_monofilament_silk_wiredrawing_machine.html')

def manager_lin_coating_unit(request):
	return render(request, 'website/plastic_extrusion_machinery/manager_lin_coating_unit.html')

def plastic_seat_tube_equipment(request):
	return render(request, 'website/plastic_extrusion_machinery/plastic_seat_tube_equipment.html')

def plastic_sealing_equipment(request):
	return render(request, 'website/plastic_extrusion_machinery/plastic_sealing_equipment.html')

def hot_melt_glue_equipment(request):
	return render(request, 'website/plastic_extrusion_machinery/hot_melt_glue_equipment.html')

def squeeze_film_line_equipment(request):
	return render(request, 'website/plastic_extrusion_machinery/squeeze_film_line_equipment.html')

def indexcn(request):
	return render(request, 'websitecn/indexcn.html') 
