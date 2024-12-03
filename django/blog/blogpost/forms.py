from .models import BlogPost, Category
from  django import forms


class BlogPostForm(forms.ModelForm):
    class Meta:
        model  = BlogPost
        fields = (
            'title',
            'body',
            'author',
            'category',
        )
        widgets = { 
            'title': forms.TextInput(attrs=
            { 
                'class': 'border border-gray-400 shadow appearance-none rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 
                'placeholder': 'Your Blog Title' 
            }), 
            'body': forms.Textarea(attrs=
            { 
                'class': 'border border-gray-400 shadow appearance-none rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 
                'placeholder': 'Your Blog Content', 
                'rows': 5 
                }), 
            'author': forms.TextInput(attrs=
            {
                'class': 'border border-gray-400 shadow appearance-none rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 
                'placeholder': 'Your Name'
                }),

             'Category': forms.TextInput(attrs=
            { 
                'class': 'border border-gray-400 shadow appearance-none rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 
                'placeholder': 'Category' 
            }),     
}