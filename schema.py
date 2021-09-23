from __future__ import annotations
import typing
import strawberry
from test import *

s=0
p=[]

@strawberry.type
class list:
    sum:int
    positions:typing.List[int]
    
@strawberry.type
class Query:
    lista: typing.List[list]

@strawberry.type
class Mutation:
    @strawberry.field
    def maxsum(self,lista:typing.List[int]) -> list:
        p.append(position(list))
        return list(sum=max_sum(list), positions=p)

@strawberry.type
class Query:
    @strawberry.field
    def res(self) -> list:
        return list(sum,positions)


schema = strawberry.Schema(Query)
schema = strawberry.Schema(Mutation)