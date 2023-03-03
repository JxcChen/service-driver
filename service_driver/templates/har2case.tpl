import requests
from jsonpath import jsonpath


class Test{{model_name}}:

    def setup_class(self):
        pass

    def test_{{case_name}}(self):
        {%- for step in testcase_steps %}
        # {{step['name']}}
        req_data = {
            "url": "{{step['request']['url']}}",
            "method": "{{step['request']['method']}}",
            {%- if step['request']['params'] %}
            'params': {{step['request']['params']}},
            {% endif %}
            {%- if step['request']['data'] %}
            'data': {{step['request']['data']}},
            {% endif %}
            {%- if step['request']['json'] %}
            'json': {{step['request']['json']}},
            {% endif %}
            {%- if step['request']['headers'] -%}
            'headers': {{step['request']['headers']}},
            {% endif %}
        }
        resp = requests.request(**req_data)
        # 断言
        {% for valid in step['validate'] %}
        {%- for key,value in valid.items() -%}
        {%- if key=='equals' -%}
        assert resp.{{value[0]}} == {{value[1]}}
        {% else %}
        assert {{value[0]}} in "{{value[1]}}"
        {% endif %}
        {%- endfor -%}
        {%- endfor -%}

        {%- if step['header_validate'] -%}
        {% for valid in step['header_validate'] %}
        {%- for key,value in valid.items() -%}
        {%- if key=='equals' -%}
        assert resp.headers['{{value[0]}}'] == "{{value[1]}}"
        {% else %}
        assert resp.headers['{{value[0]}}'] == "{{value[1]}}"
        {% endif %}
        {%- endfor -%}
        {%- endfor -%}
        {% endif %}

        {%- if step['json_validate'] -%}
        json_resp = resp.json()
        {% for valid in step['json_validate'] %}
        {%- for key,value in valid.items() -%}
        {%- if key=='equals' -%}
        assert str(jsonpath(json_resp, '$..{{value[0]}}')[0]) == "{{value[1]}}"
        {% else %}
        assert str(jsonpath(json_resp, '$..{{value[0]}}')[0]) in "{{value[1]}}"
        {% endif %}
        {%- endfor -%}
        {%- endfor -%}
        {% endif %}
        {%- endfor -%}