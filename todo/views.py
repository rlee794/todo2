from django.shortcuts import render, redirect

from django.views import View

from todo.forms import TaskForm, CommentForm
from todo.models import Task, Comment

# Create your views here.

class TodoListView(View):
    def get(self, request):
        '''GET the todo list homepage, listing all tasks in reverse order that they were created'''
        tasks = Task.objects.all().order_by('-id')
        task_form = TaskForm()

        return render(
            request=request,
            template_name='list.html',
            context={'task_list': tasks, 'task_form': task_form},
        )

    def post(self, request):
        '''POST the data in the form submitted by the user, creating a new task in the todo list'''
        form = TaskForm(request.POST)
        form.save()

        # "redirect" to the todo homepage
        return redirect('todo_list')


class TodoDetailView(View):
    def get(self, request, task_id):
        '''GET the detail view of a single task on the todo list'''
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(instance=task)

        comment_form = CommentForm(task=task)
        comments = Comment.objects.filter(task=task).order_by('created_at')
        print(comments)

        return render(
            request=request,
            template_name='detail.html',
            context={'task_form': task_form, 'id': task_id, 'comments': comments, 'comment_form': comment_form}
        )

    def post(self, request, task_id):
        '''Update or delete the specific task based on what the user submitted in the form'''
        task = Task.objects.get(id=task_id)

        # comment = Comment.objects.get(id=comment_id)

        if 'save' in request.POST:
            task_form = TaskForm(request.POST, instance=task)
            task_form.save()

        elif 'delete' in request.POST:
            task.delete()
        
        elif 'add' in request.POST:
            # form = CommentForm(request.POST)
            form = CommentForm(request.POST, task=task)
            form.save()
            # APOLOGIES FOR THESE COMMENTS - I TRIED TO APPROACH THIS A DIFFERENT WAY WITH A TA AND WANTED TO KEEP THESE NOTES FOR MYSELF
            # if form.is_valid():
            #     comment_description = form.cleaned_data['comment']
            #     id_description = form.cleaned_data['task_id']
            #     print(id_description)
            #     Comment.objects.create(comment=comment_description, task=id_description)


            # comment.objects.create(comment=form['comment'])
            # comment_form = CommentForm(request.POST, instance=task)
            # comment_form.save()

            # note_description = form.cleaned_data['description']
            # Note.objects.create(text=note_description)
            # form = TaskForm(request.POST)
            # if form.is_valid():
            #     task_description = form.cleaned_data['description']
            #     task.update(description=task_description)


        # "redirect" to the todo homepage
        return redirect('todo_list')
