from django.shortcuts import render
from django.views.generic import TemplateView
from services.emoji import predict #import the specific function from the specified program 
# Create your views here.
class Index(TemplateView):
    template_name='index.html'
    def post(self, request):
        content = request.POST['text']
        #emojize it
        sentences = content.split('.')
        emojis = list(map(predict, sentences))
        emojized_content=' '
        for sentence, emoji in zip(sentences, emojis): # zip combines parallel array
            emojized_content +=sentence + emoji + "."
        context={
            "emojized_content":emojized_content
        }
        return render(request, self.template_name,context)