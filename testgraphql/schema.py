import graphene

import links.schema
import todo.schema


class Query(todo.schema.Query, links.schema.Query, graphene.ObjectType):
    pass

class Mutation(todo.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)