from __future__ import annotations
import strawberry

@strawberry.type
class lista:
    sum: int 
    positions: list

@strawberry.type
class Mutation:
    @strawberry.field
    def maxsum(self) -> lista:
        
