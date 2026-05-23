DOCUMENTATION = r"""
name: render_jinja
short_description: Render a Jinja2 template string stored in a variable
description:
  - Takes a string containing Jinja2 template syntax and renders it
    using the provided variable context.
  - Useful when a file is loaded with lookup('file', ...) and the
    content contains Jinja2 that needs to be expanded.
options:
  value:
    description: The Jinja2 template string to render.
    required: true
  variables:
    description:
      - Dictionary of variables to use during rendering.
      - Pass hostvars[inventory_hostname] to get full Ansible variable scope.
    required: false
    default: {}
"""

EXAMPLES = r"""
- name: Render Jinja2 string with full host scope
  set_fact:
    rendered: "{{ my_jinja_string | my_namespace.jinja_utils.render_jinja(hostvars[inventory_hostname]) }}"

- name: Render with explicit variables
  set_fact:
    rendered: "{{ my_jinja_string | my_namespace.jinja_utils.render_jinja({'name': 'world'}) }}"
"""

RETURN = r"""
_value:
  description: The rendered string.
  type: str
"""

from jinja2 import Environment, StrictUndefined, TemplateSyntaxError, UndefinedError


class FilterModule:
    def filters(self):
        return {
            "render_jinja": render_jinja,
        }


def render_jinja(value, variables=None):
    if variables is None:
        variables = {}

    ctx = {k: v for k, v in variables.items()}
    raw = str(value)

    env = Environment(undefined=StrictUndefined)

    try:
        template = env.from_string(raw)
        return template.render(ctx)
    except TemplateSyntaxError:
        return raw
    except UndefinedError as e:
        raise ValueError(f"render_jinja: {e}") from e
