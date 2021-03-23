class Component:
    def operation(self) -> str:
        # this operation can be altered by decorators
        pass


class ConcreteComponent(Component):
    def operation(self) -> str:
        return "This is a concrete component"


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component) -> None:
    print(f"Result : {component.operation()}")
    print("\n")


if __name__ == "__main__":
    simple = ConcreteComponent()
    print("Client : I have a simple component-")
    client_code(simple)

    print("\n")
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client : I now have decorated component-")
    client_code(decorator2)
