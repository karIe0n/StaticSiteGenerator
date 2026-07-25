class HTMLNode:
    def __init__(self, tag: str | None, value: str | None, props: dict[str, str] | None, children: list ["HTMLNode"] | None):
        self.tag = tag
        self.value = value
        self.props = props if props is not None else {}
        self.children = children if children is not None else []

    def to_html(self):
        raise NotImplementedError("Subclasses must implement the to_html method.")
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return f" {props_str}"

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props}, children={self.children})"
    