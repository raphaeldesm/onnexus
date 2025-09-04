from django.shortcuts import render

def messages(request):
    contacts = [
        {'name': 'Juliana Paes', 'avatar_id': 'juliana'},
        {'name': 'Ricardo Alves', 'avatar_id': 'ricardo'},
        {'name': 'Mariana Costa', 'avatar_id': 'mariana'},
        {'name': 'Lucas Martins', 'avatar_id': 'lucas'},
        {'name': 'Beatriz Santos', 'avatar_id': 'beatriz'},
    ]
    context = {
        'contacts': contacts,
        'selected_contact': contacts[0]
    }
    return render(request, 'messaging/messages.html', context)
