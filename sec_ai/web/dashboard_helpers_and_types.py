from __future__ import annotations


class DemoOption:
    @classmethod
    def get_names(cls, demo_options: dict[str, DemoOption]) -> list[str]:
        return [demo.name for demo in demo_options.values()]

    @classmethod
    def get_icons(cls, demo_options: dict[str, DemoOption]) -> list[str]:
        return [demo.icon for demo in demo_options.values()]

    @classmethod
    def get_by_name(
        cls,
        demo_options: dict[str, DemoOption],
        name: str | None,
    ) -> DemoOption:
        if name is None:
            msg = "Name cannot be None."
            raise ValueError(msg)
        return next(v for _, v in demo_options.items() if v.name == name)

    def __init__(self, icon: str, name: str) -> None:
        self.icon = icon
        self.name = name
