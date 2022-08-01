def handle_uploaded_file(filename):
    with open('app1/static/uploads/'+filename.name, 'wb+') as destination:
        for chunk in filename.chunks():
            destination.write(chunk)