from jinja2 import Environment, FileSystemLoader
import test_data
import sys

def render_template(template_name, **kwargs):
	template = env.get_template(template_name)
	td = test_data.get_test_data(template_name)
	print(template.render(td))


template_name = sys.argv[1]
env = Environment(loader=FileSystemLoader('templates'), extensions=['jinja2.ext.with_'])
render_template(template_name)

exit(0)
