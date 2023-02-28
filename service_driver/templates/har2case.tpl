class Test{{case_name}}:

    def setup_class(self):
        pass

    def test_{{case_name}}:
        {%- for step in path["test_steps"] %}
        req_data = {
            "url": {% if step["url_param"] %}f"{{path["url"]}}/{ {{path["url_param"]}} }"{% else %}f"{{key}}"{% endif %},
            "params": {
                {%- for param in path["parameters"] %}
                "{{param["name"]}}": {{param["name"]}}{%- if not loop.last %},{% else %}
                {% endif %}
                {%- endfor -%}
            },
            "json": {
                {%- for param_name in path["json"] %}
                "{{param_name}}": {{param_name}}{%- if not loop.last %},{% else %}
                {% endif %}
                {%- endfor -%}
            },
            "files": {
                {%- for file_name in path["files"] %}
                "{{file_name}}": open({{file_name}}, "rb"),{%- if not loop.last %},{% else %}
                {% endif %}
                {%- endfor -%}
            }
        }
        resp = self.req(method="{{path["method"]}}", **req_data)
        {%- for param_name in path["json"] %}
        :param {{param_name}}:
        {%- if loop.last %}
        {% endif %}
        {%- endfor -%}