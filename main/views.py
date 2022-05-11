from django.shortcuts import render


# Create your views here.
def homeView(request):
    # gets the file and verifies if it's a .txt file; if so, procede.
    if request.method == 'POST':
        file = request.FILES['document']
        if file.content_type == 'text/plain':
            # creates an instance using each line; it ignores the first one.
            for n, line in enumerate(file):
                if n == 0:
                    continue

                # decodes and creates a list with the data information
                instance_list = str(line.decode('latin-1')).split('\t')

    return render(request, 'main/base.html', {})