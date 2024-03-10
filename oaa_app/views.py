from django.shortcuts import render
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import nbformat
from nbconvert import HTMLExporter
import nbformat
import os
from django.conf import settings

def home_view(request):
    return render(request, 'oaa_app/home.html')

def data_view(request):
    data_path = os.path.join('C:\\Users\\rutva', 'oaa_data_analysis.ipynb')

    with open(data_path, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)

    # Create HTMLExporter instance with exclude_code option
    html_exporter = HTMLExporter()
    #html_exporter.exclude_code = True

    #Convert notebook to HTML
    body, _ = html_exporter.from_notebook_node(notebook_content)

    
    # Pass data and plot path to the template
    context = {
        'data': body,
    }

    return render(request, 'oaa_app/data.html', context )

def data_visualization_view(request):
    return render(request, 'oaa_app/data_visualization.html')
