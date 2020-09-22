from django.shortcuts import render

details = [
    {
        'Name': 'Biraj Subedi',
        'Designation': 'TA',
        'Study': 'BE in Computer Engineering'
    },
    {
        'Name' : 'Vibek Subedi',
        'Designation' : 'Site Engineer',
        'Study' : 'BE in Electrical Engineering'
    },
    {
        'Name' : 'Mahendra Rana',
        'Designation' : 'Secondary Teacher',
        'Study' : 'BSc'
    }
]

def home(request):
    info ={
        'details' : details
    }
    return render(request, 'blog/Home.html',info)

def about(request):
    return render(request,'blog/About.html')
