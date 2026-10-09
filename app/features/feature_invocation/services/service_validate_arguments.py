# Validates the tool name and JSON arguments against discovered schemas.
# A model recommendation is untrusted until this check finishes.
from jsonschema import validate, ValidationError

def service_validate_arguments(name: str, arguments: dict, tools: list[dict]) -> None:
    match = next((tool for tool in tools if tool["name"] == name), None)
    if match is None:
        raise ValueError(f"Unknown MCP tool: {name}")
    if not isinstance(arguments, dict):
        raise ValueError("MCP tool arguments must be a JSON object")
    try:
        validate(instance=arguments, schema=match["input_schema"])
    except ValidationError as exc:
        raise ValueError(f"Invalid {name} arguments") from exc
