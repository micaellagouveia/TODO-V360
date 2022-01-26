from django.utils import timezone
from django.test import TestCase
from todo_list.models import ToDoList, ToDoTask
from django.urls import reverse


class ToDoListIndexViewTests(TestCase):
    
    def test_without_list(self):
        response = self.client.get(reverse('todo_list:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Não há listas cadastradas :(")
        self.assertContains(response, "Criar Nova Lista")
        self.assertQuerysetEqual(response.context['todos'], [])
    
    def test_index_page_with_list(self):
        time = timezone.now()
        name = "Lista Teste"
        todo_list = ToDoList.objects.create(name=name, description="teste",due_date=time)

        response = self.client.get(reverse('todo_list:index'))
        self.assertQuerysetEqual(
            response.context['todos'],
            [todo_list],
        )
        self.assertContains(response, "Criar Nova Lista")
        self.assertContains(response, name)
    
class ToDoListDetailViewTests(TestCase):
    
    def test_not_exists_list(self):
        response = self.client.get(reverse('todo_list:detail', kwargs={'pk': 4}))
        self.assertEqual(response.status_code, 404)

    def test_list_without_task(self):
        time = timezone.now()
        name = "Lista Teste"
        todo_list = ToDoList.objects.create(name=name, description="teste",due_date=time)
        response = self.client.get(reverse('todo_list:detail', kwargs={'pk': todo_list.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Esta lista não possui tasks!")
        self.assertContains(response, "Criar Nova task")

    def test_list_with_tasks(self):
        time = timezone.now()
        name = "Lista Teste"
        todo_list = ToDoList.objects.create(name=name, description="teste",due_date=time)
        todo_task = ToDoTask.objects.create(description="item teste",done=False, todo_list=todo_list)
        response = self.client.get(reverse('todo_list:detail', kwargs={'pk': todo_list.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual( response.context['todo'], todo_list )
        self.assertContains(response, "Editar task")
        self.assertContains(response, "Deletar task")
        self.assertNotContains(response, "Esta lista não possui tasks!")
        self.assertContains(response, "item teste")
        self.assertContains(response, "Criar Nova task")
    
class ToDoListDeleteViewTests(TestCase):
    def test_delete_list(self):
        time = timezone.now()
        name = "Lista Teste"
        todo_list = ToDoList.objects.create(name=name, description="teste",due_date=time)

        response = self.client.get(reverse('todo_list:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['todos'],
            [todo_list],
        )
        self.assertContains(response, name)

        response = self.client.post(reverse('todo_list:delete', kwargs={'pk': todo_list.id}))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('todo_list:index'))
        self.assertContains(response, "Não há listas cadastradas :(")
        self.assertContains(response, "Criar Nova Lista")
        self.assertQuerysetEqual(response.context['todos'], [])

class ToDoListUpdateViewTests(TestCase):
    def test_update_list(self):
        time = timezone.now()
        name = "Lista Teste"
        name2 = "Lista Teste 2"
        todo_list = ToDoList.objects.create(name=name, description="teste",due_date=time)

        response = self.client.get(reverse('todo_list:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['todos'],
            [todo_list],
        )
        self.assertContains(response, name)

        response = self.client.post(
            reverse('todo_list:update',
            kwargs={'pk': todo_list.id}),
            {'name': name2, "description":"teste", "due_date": '2022-12-01'},
        )
        self.assertEqual(response.status_code, 302)
        todo_list = ToDoList.objects.last()
        self.assertEqual(todo_list.name, name2)
        