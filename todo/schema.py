import graphene
from graphene_django import DjangoObjectType
from .models import Todo

class TodoType(DjangoObjectType):
    class Meta:
        model = Todo

class Query(graphene.ObjectType):
    todo = graphene.List(TodoType)
    def resolve_todo(self, info, **kwargs):
        return Todo.objects.all()

class CreateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)
    class Arguments:
        content = graphene.String()
        open = graphene.Boolean()
        createdOn = graphene.DateTime()

    def mutate(self, info, content, open):
        todo = Todo(content=content, open=open)
        todo.save()
        return CreateTodo(todo)

class UpdateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)
    class Arguments:
        id = graphene.ID(required=True)
        content = graphene.String()
        open = graphene.Boolean()

    def mutate(self, info, id, content, open):
        todo = Todo.objects.get(pk=id)
        todo.content = content
        todo.open = open
        todo.save()
        return UpdateTodo(todo=todo)

class DeleteTodo(graphene.Mutation):
    ok = graphene.Boolean()
    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        todo = Todo.objects.get(pk=id)
        todo.delete()
        return DeleteTodo(ok=True)

class Mutation(graphene.ObjectType):
    delete_todo = DeleteTodo.Field()
    update_todo = UpdateTodo.Field()
    create_todo = CreateTodo.Field()
