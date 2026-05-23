[![CI](https://github.com/de-it-krachten/ansible-collection-utils/workflows/CI/badge.svg?event=push)](https://github.com/de-it-krachten/ansible-collection-utils/actions?query=workflow%3ACI)


# deitkrachten.utils

Set of custom roles and filters

## Installation

```bash
ansible-galaxy collection install deitkrachten.utils-1.0.0.tar.gz
```

Or from Galaxy (once published):

```bash
ansible-galaxy collection install deitkrachten.utils
```

## Filters

### `render_jinja`

Renders a Jinja2 template string that is stored in a variable.

**Usage:**

```yaml
- set_fact:
    rendered: "{{ my_jinja_string | deitkrachten.utils.render_jinja(hostvars[inventory_hostname]) }}"
```

**Arguments:**

| Argument    | Required | Description |
|-------------|----------|-------------|
| `value`     | yes      | The Jinja2 template string to render |
| `variables` | no       | Dict of variables for rendering context. Use `hostvars[inventory_hostname]` for full scope. |

## Example Playbook

```yaml
- hosts: localhost
  gather_facts: false
  vars:
    template_string: "{{ lookup('file', 'my_template.txt') }}"

  tasks:
    - set_fact:
        rendered: "{{ template_string | deitkrachten.utils.render_jinja(hostvars[inventory_hostname]) }}"

    - debug:
        var: rendered
```


## Dependencies

## Other documentation
