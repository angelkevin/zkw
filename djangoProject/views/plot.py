from django.shortcuts import render
from django.http import HttpResponse

# from views.show import bar_plot, map_plot, change_page


# def bar_show(request):
#     return render(request, 'bar.html', {'bar_plot_html': bar_plot().render_embed()})
#

# def map_show(request):
#     return render(request, 'map.html', {'world_map_html': map_plot().render_embed()})


def all_show(request):
    return render(request, 'all.html')


# context = {'bar_plot_html': bar_plot, 'world_map_html': map_plot()}
