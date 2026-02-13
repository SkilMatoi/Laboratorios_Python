from dataclasses import dataclass, field

from pydantic import BaseModel, EmailStr


class OrderIn(BaseModel):
    id: int
    cliente: str
    email: EmailStr
    producto: str
    totalsinIVA: float


@dataclass
class Order:
    total: float = field(init=False)
    totalsinIVA: float
    id: int
    cliente: str

    def __post_init__(self):

        self.total = round(self.totalsinIVA * 1.16, 2)

    def __str__(self):
        return f"\nOrden numero: {self.id} \nDel cliente: {self.cliente} \nCon un total (IVA incluido): ${self.total}"


def procesarCompra(**kwargs):

    orden = OrderIn(**kwargs)

    return Order(id=orden.id, cliente=orden.cliente, totalsinIVA=orden.totalsinIVA)


orden = procesarCompra(
    id=2,
    cliente="Saul",
    email="Layna@gmail.com",
    producto="Teclado",
    total_sinIVA=200.0,
)
print(orden)
